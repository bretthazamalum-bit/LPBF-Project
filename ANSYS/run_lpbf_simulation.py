"""Run one disposable ANSYS Mechanical analysis and collect its results.

The runner owns orchestration and file/CSV output; Mechanical API operations
live in ``ANSYS/mechanical_scripts`` so they can be inspected independently.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from lpbf.config import (
    ANSYS_DIR,
    DEFAULT_BASE_MESH_SIZE_MM,
    DEFAULT_GEOMETRY_FILE,
    DEFAULT_PART_MESH_SIZE_MM,
    DEFAULT_RESULTS_CSV,
    RUN_WORK_DIR,
    TEMPLATE_FILE,
    WORKSPACE_DIR,
)
from lpbf.script_loader import (
    DELETE_GEOMETRY_SCRIPT,
    RESULTS_SCRIPT,
    import_geometry_script,
    mesh_script,
    solve_script,
)
from lpbf.material_config import load_material_config
from lpbf.process_config import load_process_config
from lpbf.session import (
    MECHANICAL_EXECUTABLE,
    MECHANICAL_VERSION,
    close_open_ansys_guis,
    launch_mechanical,
)


def prepare_template_copy(run_id: str) -> Path:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template Mechanical database not found: {TEMPLATE_FILE}")

    RUN_WORK_DIR.mkdir(parents=True, exist_ok=True)
    safe_run_id = "".join(char if char.isalnum() or char in "-_" else "_" for char in run_id)
    run_template = RUN_WORK_DIR / f"{safe_run_id}.mechdb"
    # Mechanical stores project state beside the database. Remove only the
    # disposable sidecar for this run so a prior interrupted session cannot
    # force the newly copied database into read-only mode.
    stale_sidecar = RUN_WORK_DIR / f"{safe_run_id}_Mech_Files"
    if stale_sidecar.exists():
        shutil.rmtree(stale_sidecar)

    for lock_file in RUN_WORK_DIR.glob(f"{safe_run_id}*.lock"):
        try:
            lock_file.unlink()
        except OSError:
            pass

    shutil.copy2(TEMPLATE_FILE, run_template)
    return run_template


def execute_writable_script(mechanical_session, script: str):
    """Execute in Mechanical's full scripting context, not light/read-only mode."""
    public_runner = getattr(mechanical_session, "run_python_script", None)
    if callable(public_runner):
        # Visible PyMechanical sessions expose the public remote scripting API
        # but do not necessarily expose the embedded script_engine attribute.
        return public_runner(script)

    scope_name = "lpbf-workflow"
    if not hasattr(mechanical_session, "script_engine"):
        import clr

        clr.AddReference("Ansys.Mechanical.Scripting")
        import Ansys

        script_engine = Ansys.Mechanical.Scripting.EngineFactory.CreateEngine()
        script_engine.CreateScope(scope_name, False, False)
        mechanical_session.script_engine = script_engine

    result = mechanical_session.script_engine.ExecuteCode(
        script,
        scope_name,
        False,
        None,
        None,
    )
    if result is None:
        raise RuntimeError("Mechanical returned no script result.")
    if result.Error is not None:
        raise RuntimeError(f"Mechanical script failed: {result.Error.Message}")
    return result.Value


def run_stage(mechanical_session, stage_name: str, script: str):
    print(stage_name)
    result = execute_writable_script(mechanical_session, script)
    if result:
        print(result)
    return result


def close_mechanical(mechanical_session) -> None:
    try:
        mechanical_session.exit(force=True)
        return
    except TypeError:
        pass
    except Exception:
        pass

    for method_name in ("exit", "close"):
        method = getattr(mechanical_session, method_name, None)
        if callable(method):
            try:
                method()
                return
            except Exception:
                pass


def parse_result(raw_result: str) -> dict:
    if isinstance(raw_result, dict):
        return raw_result
    if isinstance(raw_result, bytes):
        raw_result = raw_result.decode("utf-8", errors="replace")
    try:
        parsed = json.loads(raw_result)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass
    return {"raw_result": raw_result}


def numeric_result(value):
    """Convert Mechanical's formatted result strings to numeric values."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        import re

        match = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", str(value))
        return float(match.group(0)) if match else None


def stress_result_status(stress_results: dict) -> tuple[str, str]:
    average = numeric_result(stress_results.get("average_stress"))
    maximum = numeric_result(stress_results.get("max_stress"))
    if average is None or maximum is None:
        return "invalid", "Stress result did not contain numeric average and maximum values."
    if average <= 0.0 or maximum <= 0.0:
        return "invalid", "Stress result was non-positive; excluding it from optimization."
    return "success", ""


def write_orientation_csv(
    args: argparse.Namespace,
    stress_results: dict | None,
    *,
    status: str,
    error: str = "",
    started_at: str | None = None,
) -> None:
    """Append one flat, optimizer-friendly record for this simulation."""
    csv_file = Path(args.results_csv)
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    stress_results = stress_results or {}
    fieldnames = [
        "run_id", "material_id", "status", "rot_x_deg", "rot_y_deg", "rot_z_deg",
        "average_stress_pa", "max_stress_pa", "min_stress_pa", "stress_units",
        "step_file", "result_file", "started_at_utc", "completed_at_utc", "error",
    ]
    row = {
        "run_id": args.run_id,
        "material_id": args.material_config_data["id"],
        "status": status,
        "rot_x_deg": args.rot_x,
        "rot_y_deg": args.rot_y,
        "rot_z_deg": args.rot_z,
        "average_stress_pa": numeric_result(stress_results.get("average_stress")),
        "max_stress_pa": numeric_result(stress_results.get("max_stress")),
        "min_stress_pa": numeric_result(stress_results.get("min_stress")),
        "stress_units": "Pa",
        "step_file": str(Path(args.step_file).resolve()),
        "result_file": str(Path(args.result_file).resolve()) if args.result_file else "",
        "started_at_utc": started_at or "",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "error": error,
    }
    file_exists = csv_file.exists() and csv_file.stat().st_size > 0
    with csv_file.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print(f"Orientation record appended: {csv_file}")


def write_result_file(args: argparse.Namespace, stress_results: dict, *, status: str = "success", error: str = "") -> None:
    if not args.result_file:
        return

    result_file = Path(args.result_file)
    result_file.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": args.run_id,
        "material": {
            "id": args.material_config_data["id"],
            "display_name": args.material_config_data["display_name"],
            "ansys_part_material": args.material_config_data["ansys_part_material"],
            "ansys_base_material": args.material_config_data["ansys_base_material"],
            "config_path": args.material_config_data["config_path"],
        },
        "process": args.process_config_data,
        "status": status,
        "step_file": str(Path(args.step_file).resolve()),
        "rotation_degrees": {
            "rot_x": args.rot_x,
            "rot_y": args.rot_y,
            "rot_z": args.rot_z,
        },
        "stress_results": stress_results,
    }
    if error:
        payload["error"] = error
    result_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Result file written: {result_file}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one LPBF Ansys simulation from a STEP file.")
    parser.add_argument("--step-file", default=str(DEFAULT_GEOMETRY_FILE))
    parser.add_argument("--run-id", default="manual_run")
    parser.add_argument("--rot-x", type=float, default=0.0)
    parser.add_argument("--rot-y", type=float, default=0.0)
    parser.add_argument("--rot-z", type=float, default=0.0)
    parser.add_argument(
        "--part-mesh-size-mm",
        type=float,
        default=DEFAULT_PART_MESH_SIZE_MM,
        help="Part mesh element size in millimeters.",
    )
    parser.add_argument(
        "--base-mesh-size-mm",
        type=float,
        default=DEFAULT_BASE_MESH_SIZE_MM,
        help="Base mesh element size in millimeters.",
    )
    parser.add_argument("--result-file")
    parser.add_argument(
        "--material-config",
        default=None,
        help="JSON material configuration; defaults to materials/inconel_718.json.",
    )
    parser.add_argument(
        "--process-config",
        default=None,
        help="CSV process settings; defaults to process_settings.csv.",
    )
    parser.add_argument(
        "--screenshot-file",
        help="PNG path for the equivalent-stress viewport image.",
    )
    parser.add_argument(
        "--results-csv",
        default=str(DEFAULT_RESULTS_CSV),
        help="CSV file to which one optimizer record is appended per run.",
    )
    parser.add_argument(
        "--pause-before-close",
        action="store_true",
        help="Wait for Enter before closing Mechanical.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.material_config_data = load_material_config(args.material_config)
    args.process_config_data = load_process_config(args.process_config)
    step_file = Path(args.step_file).resolve()
    started_at = datetime.now(timezone.utc).isoformat()

    if not step_file.exists():
        raise FileNotFoundError(f"STEP file not found: {step_file}")
    if args.part_mesh_size_mm <= 0 or args.base_mesh_size_mm <= 0:
        raise ValueError("Mesh sizes must be greater than zero millimeters.")

    run_template = prepare_template_copy(args.run_id)
    screenshot_file = None
    if args.screenshot_file:
        screenshot_file = Path(args.screenshot_file).resolve()
    elif args.result_file:
        result_path = Path(args.result_file).resolve()
        screenshot_file = result_path.with_name(
            f"{args.run_id}_equivalent_stress.png"
        )
    if screenshot_file is not None:
        screenshot_file.parent.mkdir(parents=True, exist_ok=True)

    close_open_ansys_guis()

    # Launch the visible Mechanical desktop first, using the same direct
    # Use the direct PyMechanical GUI launch path.
    mechanical_session = launch_mechanical(
        exec_file=str(MECHANICAL_EXECUTABLE),
        version=MECHANICAL_VERSION,
        batch=False,
        cleanup_on_exit=False,
    )

    try:
        print("Mechanical GUI launched and connected; opening template...")
        mechanical_session.run_python_script(
            f"ExtAPI.DataModel.Project.Open(r'{run_template}')"
        )
        # The visible remote Mechanical API owns the active license internally;
        # editability is validated by the first model mutation below.

        print("mechopen")
        print(f"run_id={args.run_id}")
        print(f"step_file={step_file}")
        print(f"template_copy={run_template}")
        print(f"rotation_degrees=({args.rot_x}, {args.rot_y}, {args.rot_z})")
        print(
            "material="
            f"{args.material_config_data['display_name']} "
            f"(part={args.material_config_data['ansys_part_material']}, "
            f"base={args.material_config_data['ansys_base_material']})"
        )
        print(
            "process="
            f"{args.process_config_data['config_name']} "
            f"(scan={args.process_config_data['scan_speed_mm_s']} mm/s, "
            f"layer={args.process_config_data['deposition_thickness_mm']} mm, "
            f"hatch={args.process_config_data['hatch_spacing_mm']} mm, "
            f"preheat={args.process_config_data['preheat_temperature_c']} C)"
        )

        print("template opened in visible Mechanical GUI")
        # Do not issue a separate Project.Save() here.  In the visible
        # PyMechanical session that call can wait indefinitely on Mechanical's
        # UI even though the remote scripting channel is healthy.  The
        # mutation stages below validate writability and the run copy is
        # disposable; save only through the stage scripts when needed.
        run_stage(mechanical_session, "deleting old geometry", DELETE_GEOMETRY_SCRIPT)
        run_stage(mechanical_session, "importing geometry", import_geometry_script(step_file))
        run_stage(
            mechanical_session,
            "meshing geometry",
            mesh_script(
                args.part_mesh_size_mm,
                args.base_mesh_size_mm,
                args.material_config_data["ansys_part_material"],
                args.material_config_data["ansys_base_material"],
            ),
        )
        run_stage(mechanical_session, "solving analyses", solve_script(args.process_config_data))

        screenshot_literal = repr(str(screenshot_file)) if screenshot_file else "None"
        raw_result = execute_writable_script(
            mechanical_session,
            RESULTS_SCRIPT.replace("__SCREENSHOT_FILE__", screenshot_literal),
        )
        stress_results = parse_result(raw_result)
        print(json.dumps(stress_results, indent=2))
        result_status, result_error = stress_result_status(stress_results)
        write_result_file(args, stress_results, status=result_status, error=result_error)
        write_orientation_csv(
            args,
            stress_results,
            status=result_status,
            error=result_error,
            started_at=started_at,
        )

        if args.pause_before_close:
            input("Press Enter to close Mechanical...")
    except Exception as error:
        error_text = f"{type(error).__name__}: {error}"
        write_result_file(args, {}, status="failed", error=error_text)
        write_orientation_csv(
            args,
            {},
            status="failed",
            error=error_text,
            started_at=started_at,
        )
        raise
    finally:
        close_mechanical(mechanical_session)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
