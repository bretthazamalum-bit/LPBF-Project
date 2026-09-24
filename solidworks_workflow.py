# Bundled SolidWorks workflow for one orientation.
#
# This replaces the old multi-process sequence:
# openswx.py -> rotateswx.py -> resolve_collision_z.py -> swxexportstep.py
# -> closeswx.py
#
# Keeping the CAD steps in one process reduces repeated COM attach/startup
# friction and makes the variable handoff easier to inspect. The source
# .SLDPRT is still opened fresh and closed without saving after STEP export.
from __future__ import annotations

import argparse
import math
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import pythoncom
import win32com.client
from win32com.client import VARIANT


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_PART_FILE = SCRIPT_DIR / "Part1.SLDPRT"

SW_DOC_PART = 1
SW_OPEN_SILENT = 1

DEFAULT_PART_BODY = "part"
DEFAULT_BASE_BODY = "base"
DEFAULT_Z_STEP_MM = 0.25
DEFAULT_Z_MAX_STEPS = 400
M_PER_MM = 0.001
SOLIDWORKS_STARTUP_TIMEOUT_SECONDS = 120


FILE_LOAD_ERROR_FLAGS = {
    1: "generic file-load error",
    2: "file not found or referenced file suppressed",
    1024: "invalid file type",
    8192: "future-version file: saved in a newer SolidWorks version",
    65536: "a document with the same title is already open",
    131072: "file is encrypted by Liquid Machines",
    262144: "blocked because system resources are low",
    524288: "file contains no display data",
    1048576: "open operation was interrupted",
    2097152: "file requires non-critical repair",
    4194304: "file has critical data corruption",
}


@dataclass(frozen=True)
class CollisionState:
    collided: bool
    method: str
    detail: str


def describe_file_load_errors(error_value):
    descriptions = [
        description
        for flag, description in FILE_LOAD_ERROR_FLAGS.items()
        if int(error_value) & flag
    ]
    return "; ".join(descriptions) if descriptions else "no decoded file-load errors"


def deg_to_rad(deg):
    return deg * math.pi / 180.0


def make_solidworks_visible(sw):
    # Visibility is helpful when debugging, but not required for automation.
    # Some SolidWorks sessions reject these properties, so keep going.
    try:
        sw.Visible = True
    except Exception as exc:
        print(f"Could not set SolidWorks visibility; continuing. Details: {exc}")

    try:
        sw.FrameState = 1
    except Exception as exc:
        print(f"Could not set SolidWorks window state; continuing. Details: {exc}")


def get_sw():
    last_errors = []

    # A COM server can take several seconds to register after SolidWorks.exe
    # appears.  Use the standard activation path first; this is the path used
    # by the known-working VSCode launcher.  Keep DispatchEx as a fallback.
    launchers = (
        ("Dispatch", win32com.client.Dispatch),
        ("DispatchEx", win32com.client.DispatchEx),
    )
    launcher_index = 0
    deadline = time.time() + SOLIDWORKS_STARTUP_TIMEOUT_SECONDS

    while time.time() < deadline:
        try:
            sw = win32com.client.GetActiveObject("SldWorks.Application")
            print("Attached to existing SolidWorks instance.")
            make_solidworks_visible(sw)
            return sw
        except Exception as exc:
            last_errors.append(f"attach: {exc}")

        if launcher_index < len(launchers):
            launcher_name, launcher = launchers[launcher_index]
            launcher_index += 1
            try:
                sw = launcher("SldWorks.Application")
                print(f"Started new SolidWorks instance with {launcher_name}.")
                make_solidworks_visible(sw)
                return sw
            except Exception as exc:
                last_errors.append(f"{launcher_name}: {exc}")

        # Allow the interactive COM server to process startup messages before
        # trying GetActiveObject again.
        pythoncom.PumpWaitingMessages()
        time.sleep(1)

    recent_errors = "; ".join(last_errors[-4:])
    raise RuntimeError(
        "SolidWorks did not become available through COM within "
        f"{SOLIDWORKS_STARTUP_TIMEOUT_SECONDS} seconds. "
        "If a first-start, activation, license, login, or recovery dialog is "
        "visible, complete it and run the workflow again. "
        f"Recent COM errors: {recent_errors}"
    )


def get_active_model(sw):
    model = sw.ActiveDoc
    if model is None:
        raise RuntimeError("No active SolidWorks document.")
    return model


def get_model_path(model):
    try:
        path = model.GetPathName()
        return Path(path).resolve() if path else None
    except Exception:
        return None


def same_path(left: Path | None, right: Path):
    if left is None:
        return False
    return str(left).casefold() == str(right.resolve()).casefold()


def get_active_matching_document(sw, part_file: Path):
    model = sw.ActiveDoc
    if model is None:
        return None

    active_path = get_model_path(model)
    if same_path(active_path, part_file):
        return model

    if active_path is not None:
        print(f"Active SolidWorks document is not the requested part: {active_path}")

    return None


def get_com_value(obj, name, default=0):
    try:
        return getattr(obj, name)
    except Exception:
        return default


def activate_model(sw, model):
    try:
        title = model.GetTitle()
    except Exception:
        return model

    try:
        errors = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
        activated = sw.ActivateDoc3(title, False, 0, errors)
        return activated if activated is not None else model
    except Exception:
        return model


def wait_for_any_active_document(sw, timeout=30):
    start = time.time()

    while time.time() - start < timeout:
        try:
            pythoncom.PumpWaitingMessages()
            model = sw.ActiveDoc
            if model is not None:
                return model
        except Exception:
            pass

        time.sleep(0.5)

    return None


def open_with_opendoc7(sw, part_file: Path):
    spec = sw.GetOpenDocSpec(str(part_file))
    spec.DocumentType = SW_DOC_PART
    spec.Silent = True
    spec.ReadOnly = False
    spec.ConfigurationName = ""

    model = sw.OpenDoc7(spec)
    errors = get_com_value(spec, "Error")
    warnings = get_com_value(spec, "Warning")
    return model, errors, warnings


def open_with_opendoc6(sw, part_file: Path):
    errors = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    warnings = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)

    model = sw.OpenDoc6(
        str(part_file),
        SW_DOC_PART,
        SW_OPEN_SILENT,
        "",
        errors,
        warnings,
    )
    return model, errors.value, warnings.value


def open_part(sw, part_file: Path):
    if not part_file.exists():
        raise FileNotFoundError(f"Part file not found: {part_file}")

    print("SolidWorks launched.")
    model = get_active_matching_document(sw, part_file)
    errors = 0
    warnings = 0

    if model is not None:
        print(f"Using already-open part: {part_file}")
    else:
        # OpenDoc6 is the compatibility path used by the known-working
        # launcher.  OpenDoc7 can trigger an RPC failure on this SolidWorks
        # installation before the document server is fully ready.
        opendoc6_exc = None
        for attempt in range(30):
            try:
                model, errors, warnings = open_with_opendoc6(sw, part_file)
                print("Opened part with OpenDoc6.")
                break
            except Exception as exc:
                opendoc6_exc = exc
                pythoncom.PumpWaitingMessages()
                time.sleep(1)
        else:
            raise RuntimeError(
                "SolidWorks failed while opening the part after 30 seconds. "
                "Try opening the part manually in SolidWorks first, then rerun. "
                f"OpenDoc6 details: {opendoc6_exc!r}"
            ) from opendoc6_exc

    if model is None:
        raise RuntimeError(
            "Failed to open part. "
            f"errors={errors} ({describe_file_load_errors(errors)}), "
            f"warnings={warnings}"
        )

    model = activate_model(sw, model)
    print(f"Opened part: {part_file}")
    print(f"errors={errors}, warnings={warnings}")

    model = wait_for_any_active_document(sw, timeout=30)
    if model is None:
        raise RuntimeError("No active document appeared in time.")

    print("A document is active and ready.")
    return model


def rebuild_model(model):
    # pywin32 can expose this COM member as either a method or a property.
    rebuild_result = model.EditRebuild3
    if callable(rebuild_result):
        return rebuild_result()
    return rebuild_result


def get_bodies(model):
    bodies = model.GetBodies2(0, False)
    if not bodies:
        raise RuntimeError("No solid bodies found.")
    return bodies


def find_body(model, body_name):
    bodies = get_bodies(model)

    for body in bodies:
        try:
            if body.Name == body_name:
                return body
        except Exception:
            pass

    names = []
    for body in bodies:
        try:
            names.append(body.Name)
        except Exception:
            names.append("<unnamed>")

    raise RuntimeError(f"Body '{body_name}' not found. Bodies present: {names}")


def select_body(model, body, body_name):
    model.ClearSelection2(True)
    selected = body.Select(False, 1)
    if not selected:
        raise RuntimeError(f"Failed to select body '{body_name}'.")


def get_body_center_of_mass(model, body, body_name):
    """Return the selected body's center of mass in model coordinates."""
    select_body(model, body, body_name)

    property_errors = []
    try:
        status = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
        mass_properties = model.Extension.GetMassProperties2(1, status, True)
    except Exception as exc:
        property_errors.append(f"GetMassProperties2: {exc}")
        try:
            # The body-level API is more consistently exposed by pywin32 and
            # returns the same first three center-of-mass coordinates.
            status = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
            mass_properties = model.Extension.GetMassProperties(1, status)
        except Exception as exc:
            property_errors.append(f"Body.GetMassProperties: {exc}")
            raise RuntimeError(
                f"Could not read center of mass for body '{body_name}'. "
                + " | ".join(property_errors)
            ) from exc

    # GetMassProperties2 returns [COM X, COM Y, COM Z, volume, ...].
    if isinstance(mass_properties, tuple) and len(mass_properties) == 2:
        # Some COM wrappers expose a (values, status) pair.
        candidate = mass_properties[0]
        if hasattr(candidate, "__len__") and len(candidate) >= 3:
            mass_properties = candidate

    if mass_properties is None or len(mass_properties) < 3:
        raise RuntimeError(
            f"SolidWorks returned invalid mass properties for body '{body_name}': "
            f"{mass_properties!r}"
        )

    center = tuple(float(mass_properties[index]) for index in range(3))
    print(
        f"Rotation center for '{body_name}' (center of mass): "
        f"X={center[0]:g}, Y={center[1]:g}, Z={center[2]:g} m"
    )
    return center


def rotate_body(model, body_name, rot_x_deg, rot_y_deg, rot_z_deg):
    body = find_body(model, body_name)
    rotation_center = get_body_center_of_mass(model, body, body_name)

    feature = model.FeatureManager.InsertMoveCopyBody2(
        0.0,
        0.0,
        0.0,
        0.0,
        rotation_center[0],
        rotation_center[1],
        rotation_center[2],
        deg_to_rad(rot_x_deg),
        deg_to_rad(rot_y_deg),
        deg_to_rad(rot_z_deg),
        False,
        1,
    )

    model.ClearSelection2(True)

    if feature is None:
        raise RuntimeError("InsertMoveCopyBody2 rotation failed.")

    rebuild_ok = rebuild_model(model)
    print("Move/Copy Body rotation feature created.")
    print(f"Body: {body_name}")
    print(f"RotX: {rot_x_deg} deg")
    print(f"RotY: {rot_y_deg} deg")
    print(f"RotZ: {rot_z_deg} deg")
    print(f"Rebuild result: {rebuild_ok}")


def body_box(body):
    box = body.GetBodyBox()
    if box is None or len(box) != 6:
        raise RuntimeError(f"Could not read bounding box for body '{body.Name}'.")
    return tuple(float(value) for value in box)


def boxes_overlap(box_a, box_b, tolerance_m):
    ax_min, ay_min, az_min, ax_max, ay_max, az_max = box_a
    bx_min, by_min, bz_min, bx_max, by_max, bz_max = box_b

    return (
        ax_min < bx_max - tolerance_m
        and ax_max > bx_min + tolerance_m
        and ay_min < by_max - tolerance_m
        and ay_max > by_min + tolerance_m
        and az_min < bz_max - tolerance_m
        and az_max > bz_min + tolerance_m
    )


def bbox_collision(part_body, base_body, tolerance_m):
    # Bounding boxes are only a fallback; exact body interference is preferred.
    part_box = body_box(part_body)
    base_box = body_box(base_body)
    collided = boxes_overlap(part_box, base_box, tolerance_m)
    return CollisionState(
        collided=collided,
        method="bounding-box",
        detail=f"part_box={part_box}, base_box={base_box}",
    )


def exact_collision(sw, part_body, base_body):
    modeler = sw.GetModeler()

    faces_1 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
    faces_2 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
    intersected_bodies = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)

    result = modeler.CheckInterferenceBetweenTwoBodies(
        part_body,
        base_body,
        False,
        faces_1,
        faces_2,
        intersected_bodies,
    )

    if isinstance(result, tuple):
        collided = bool(result[0]) if result else False
    else:
        collided = bool(result)

    return CollisionState(
        collided=collided,
        method="exact-body-interference",
        detail=f"interference_result={result}",
    )


def check_collision(sw, part_body, base_body, tolerance_m):
    try:
        return exact_collision(sw, part_body, base_body)
    except Exception as exc:
        fallback = bbox_collision(part_body, base_body, tolerance_m)
        return CollisionState(
            collided=fallback.collided,
            method="bounding-box fallback",
            detail=f"exact check failed: {exc!r}; {fallback.detail}",
        )


def move_body_z(model, body, body_name, step_m):
    select_body(model, body, body_name)

    feature = model.FeatureManager.InsertMoveCopyBody2(
        0.0,
        0.0,
        step_m,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        False,
        1,
    )

    model.ClearSelection2(True)

    if feature is None:
        raise RuntimeError(f"Move/Copy Body Z step failed for body '{body_name}'.")

    rebuild_model(model)


def resolve_collision_z(
    sw,
    model,
    part_name,
    base_name,
    step_mm,
    max_steps,
    tolerance_mm,
):
    step_m = step_mm * M_PER_MM
    tolerance_m = tolerance_mm * M_PER_MM
    total_z_m = 0.0

    if step_m <= 0:
        raise ValueError("Z step must be greater than zero.")

    for step_index in range(max_steps + 1):
        # Re-find bodies each pass because Move/Copy Body can refresh COM refs.
        part_body = find_body(model, part_name)
        base_body = find_body(model, base_name)
        state = check_collision(sw, part_body, base_body, tolerance_m)

        print(
            "Collision check "
            f"{step_index}: collided={state.collided}, method={state.method}"
        )

        if not state.collided:
            print(
                "Collision resolved: "
                f"total_z_shift_mm={total_z_m / M_PER_MM:g}, "
                f"steps={step_index}"
            )
            return total_z_m

        if step_index == max_steps:
            break

        print(f"Collision detected. Moving '{part_name}' +Z by {step_mm:g} mm.")
        move_body_z(model, part_body, part_name, step_m)
        total_z_m += step_m

    raise RuntimeError(
        f"Collision remained after {max_steps} Z steps "
        f"({total_z_m / M_PER_MM:g} mm total)."
    )


def export_step(model, output_file: Path):
    os.makedirs(output_file.parent, exist_ok=True)
    model.ClearSelection2(True)

    save_status = model.SaveAs3(str(output_file), 0, 0)

    if not output_file.exists():
        raise RuntimeError(
            f"STEP export did not create the expected file: {output_file}. "
            f"SaveAs3 status: {save_status}"
        )

    print(f"Exported to: {output_file}")
    print(f"SaveAs3 status: {save_status}")


def close_solidworks(sw):
    # Discard unsaved rotation/Z-clearance features so Part1.SLDPRT is clean
    # for the next orientation.
    sw.CloseAllDocuments(True)
    sw.ExitApp()


def run_workflow(
    part_file: Path,
    step_file: Path,
    rot_x_deg,
    rot_y_deg,
    rot_z_deg,
    part_body,
    base_body,
    z_step_mm,
    z_max_steps,
    tolerance_mm,
    keep_open=False,
):
    print(f"Part file: {part_file}")
    print(f"STEP output: {step_file}")
    print(f"Rotation: X={rot_x_deg} deg, Y={rot_y_deg} deg, Z={rot_z_deg} deg")
    print(
        "Collision resolver: "
        f"part='{part_body}', base='{base_body}', "
        f"z_step={z_step_mm} mm, max_steps={z_max_steps}"
    )

    com_initialized = False
    try:
        pythoncom.CoInitialize()
        com_initialized = True
    except pythoncom.com_error as exc:
        # The caller may already have initialized this thread in a different
        # COM apartment.  In that case, continue using the existing apartment.
        if getattr(exc, "hresult", None) != -2147417850:  # RPC_E_CHANGED_MODE
            raise

    sw = None
    model = None

    try:
        sw = get_sw()
        model = open_part(sw, part_file)
        rotate_body(model, part_body, rot_x_deg, rot_y_deg, rot_z_deg)
        resolve_collision_z(
            sw=sw,
            model=model,
            part_name=part_body,
            base_name=base_body,
            step_mm=z_step_mm,
            max_steps=z_max_steps,
            tolerance_mm=tolerance_mm,
        )
        export_step(model, step_file)
    finally:
        if sw is not None and model is not None and not keep_open:
            close_solidworks(sw)
        if com_initialized:
            pythoncom.CoUninitialize()


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Open a SolidWorks part, rotate body 'part', lift it in Z until it "
            "does not collide with body 'base', export STEP, and close unsaved."
        )
    )
    parser.add_argument("--part-file", default=str(DEFAULT_PART_FILE))
    parser.add_argument("--step-file", required=True)
    parser.add_argument("--rot-x", type=float, required=True)
    parser.add_argument("--rot-y", type=float, required=True)
    parser.add_argument("--rot-z", type=float, required=True)
    parser.add_argument("--part-body", default=DEFAULT_PART_BODY)
    parser.add_argument("--base-body", default=DEFAULT_BASE_BODY)
    parser.add_argument("--z-step-mm", type=float, default=DEFAULT_Z_STEP_MM)
    parser.add_argument("--z-max-steps", type=int, default=DEFAULT_Z_MAX_STEPS)
    parser.add_argument("--tolerance-mm", type=float, default=0.0)
    parser.add_argument(
        "--keep-open",
        action="store_true",
        help="Leave SolidWorks open after export instead of closing unsaved.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    run_workflow(
        part_file=Path(args.part_file).resolve(),
        step_file=Path(args.step_file).resolve(),
        rot_x_deg=args.rot_x,
        rot_y_deg=args.rot_y,
        rot_z_deg=args.rot_z,
        part_body=args.part_body,
        base_body=args.base_body,
        z_step_mm=args.z_step_mm,
        z_max_steps=args.z_max_steps,
        tolerance_mm=args.tolerance_mm,
        keep_open=args.keep_open,
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
