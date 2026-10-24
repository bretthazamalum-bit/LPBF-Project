"""CLI orchestrator for one SolidWorks LPBF orientation."""

from __future__ import annotations

import argparse
from pathlib import Path

from solidworks_tools.com_session import (
    close_solidworks,
    get_sw,
    initialize_com,
    uninitialize_com,
)
from solidworks_tools.config import (
    DEFAULT_BASE_BODY,
    DEFAULT_PART_BODY,
    DEFAULT_PART_FILE,
    DEFAULT_PLATE_MARGIN_MM,
    DEFAULT_SUPPORT_LIFT_MM,
    DEFAULT_Z_MAX_STEPS,
    DEFAULT_Z_STEP_MM,
)
from solidworks_tools.documents import open_part
from solidworks_tools.export import export_step
from solidworks_tools.placement import ensure_support_gap, ensure_xy_containment
from solidworks_tools.transforms import rotate_body


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
    support_lift_mm,
    plate_margin_mm,
    keep_open=False,
):
    """Run one orientation in one COM session without saving the template.

    The order is deliberate: rotate around the center of mass first, then
    place the rotated body using its world-coordinate bounds, and only then
    export the disposable document to STEP.
    """
    print(f"Part file: {part_file}")
    print(f"STEP output: {step_file}")
    print(f"Rotation: X={rot_x_deg} deg, Y={rot_y_deg} deg, Z={rot_z_deg} deg")
    print(
        "Bounding-box placement: "
        f"part='{part_body}', base='{base_body}', minimum_gap={support_lift_mm:g} mm"
    )

    com_initialized = initialize_com()
    sw = None
    model = None
    try:
        sw = get_sw()
        model = open_part(sw, part_file)
        rotate_body(model, part_body, rot_x_deg, rot_y_deg, rot_z_deg)
        ensure_xy_containment(model, part_body, base_body, plate_margin_mm)
        ensure_support_gap(model, part_body, base_body, support_lift_mm)
        export_step(model, step_file)
    finally:
        if sw is not None and model is not None and not keep_open:
            close_solidworks(sw)
        uninitialize_com(com_initialized)


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Open a SolidWorks part, rotate body 'part', place it over body "
            "'base', apply an LPBF support lift, export STEP, and close unsaved."
        )
    )
    parser.add_argument("--part-file", default=str(DEFAULT_PART_FILE))
    parser.add_argument("--step-file", required=True)
    parser.add_argument("--rot-x", type=float, required=True)
    parser.add_argument("--rot-y", type=float, required=True)
    parser.add_argument("--rot-z", type=float, required=True)
    parser.add_argument("--part-body", default=DEFAULT_PART_BODY)
    parser.add_argument("--base-body", default=DEFAULT_BASE_BODY)
    # Retained so existing main.py callers remain compatible. Direct placement
    # now uses bounding boxes and does not need incremental Z settings.
    parser.add_argument("--z-step-mm", type=float, default=DEFAULT_Z_STEP_MM)
    parser.add_argument("--z-max-steps", type=int, default=DEFAULT_Z_MAX_STEPS)
    parser.add_argument("--tolerance-mm", type=float, default=0.0)
    parser.add_argument(
        "--plate-margin-mm", type=float, default=DEFAULT_PLATE_MARGIN_MM,
        help="Required XY margin from the build-plate edges in millimeters.",
    )
    parser.add_argument(
        "--support-lift-mm", type=float, default=DEFAULT_SUPPORT_LIFT_MM,
        help="Extra +Z gap above the base for LPBF supports.",
    )
    parser.add_argument(
        "--keep-open", action="store_true",
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
        support_lift_mm=args.support_lift_mm,
        plate_margin_mm=args.plate_margin_mm,
        keep_open=args.keep_open,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

