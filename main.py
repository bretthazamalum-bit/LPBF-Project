# Root controller for the LPBF orientation sweep.
# This file owns the list of test rotations, runs the SolidWorks STEP export,
# then passes each generated STEP into Ansys for stress evaluation.
from __future__ import annotations

import argparse
import json
import csv
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SOLIDWORKS_DIR = PROJECT_ROOT / "Solidworks"
ANSYS_DIR = PROJECT_ROOT / "ANSYS"
PROJECT_PYTHON = (
    PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
    if (PROJECT_ROOT / ".venv" / "Scripts" / "python.exe").exists()
    else Path(sys.executable)
)

PART_FILE = SOLIDWORKS_DIR / "Part1.SLDPRT"
STEP_OUTPUT_DIR = PROJECT_ROOT / "generated_steps"
RESULTS_DIR = PROJECT_ROOT / "results"
ORIENTATION_RESULTS_CSV = RESULTS_DIR / "orientation_results.csv"
Z_CLEARANCE_STEP_MM = 0.25
Z_CLEARANCE_MAX_STEPS = 400

ANSYS_ENABLED = True


@dataclass(frozen=True)
class OrientationPoint:
    name: str
    rot_x: float
    rot_y: float
    rot_z: float


STARTER_POINTS = [
    OrientationPoint("point_01_baseline", 0.0, 0.0, 0.0),
    OrientationPoint("point_02_x45", 45.0, 0.0, 0.0),
    OrientationPoint("point_03_y45", 0.0, 45.0, 0.0),
    OrientationPoint("point_04_z45", 0.0, 0.0, 45.0),
]


def format_angle(value: float) -> str:
    text = f"{value:g}"
    return text.replace("-", "neg").replace(".", "p")


def step_path_for(point: OrientationPoint) -> Path:
    filename = (
        f"{point.name}_"
        f"Rx{format_angle(point.rot_x)}_"
        f"Ry{format_angle(point.rot_y)}_"
        f"Rz{format_angle(point.rot_z)}.step"
    )
    return STEP_OUTPUT_DIR / filename


def result_path_for(point: OrientationPoint) -> Path:
    return RESULTS_DIR / f"{point.name}_results.json"


def next_optimizer_run_number() -> int:
    """Return the next unique bo_NNN id across prior optimizer runs."""
    if not ORIENTATION_RESULTS_CSV.exists():
        return 1
    highest = 0
    with ORIENTATION_RESULTS_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            match = re.fullmatch(r"bo_(\d+)", row.get("run_id", ""))
            if match:
                highest = max(highest, int(match.group(1)))
    return highest + 1


def run_command(command: list[str], cwd: Path, dry_run: bool) -> None:
    printable = " ".join(command)
    print(f"\nWorking folder: {cwd}")
    print(f"Command: {printable}")

    if dry_run:
        return

    subprocess.run(command, cwd=str(cwd), check=True)


def run_solidworks_export(point: OrientationPoint, step_file: Path, dry_run: bool) -> None:
    print(f"\n--- SolidWorks export for {point.name} ---")
    print(
        "Rotation passed to SolidWorks: "
        f"X={point.rot_x} deg, Y={point.rot_y} deg, Z={point.rot_z} deg"
    )
    print(
        "Collision resolver passed to SolidWorks: "
        f"part='part', base='base', z_step={Z_CLEARANCE_STEP_MM} mm, "
        f"max_steps={Z_CLEARANCE_MAX_STEPS}"
    )
    print(f"STEP output path passed to SolidWorks exporter: {step_file}")

    run_command(
        [
            str(PROJECT_PYTHON),
            str(PROJECT_ROOT / "solidworks_workflow.py"),
            "--part-file",
            str(PART_FILE),
            "--step-file",
            str(step_file),
            "--rot-x",
            str(point.rot_x),
            "--rot-y",
            str(point.rot_y),
            "--rot-z",
            str(point.rot_z),
            "--z-step-mm",
            str(Z_CLEARANCE_STEP_MM),
            "--z-max-steps",
            str(Z_CLEARANCE_MAX_STEPS),
        ],
        PROJECT_ROOT,
        dry_run,
    )


def run_ansys_analysis(point: OrientationPoint, step_file: Path, dry_run: bool) -> None:
    print(f"\n--- Ansys analysis for {point.name} ---")
    print(f"STEP input passed to Ansys: {step_file}")
    print(
        "Rotation metadata passed to Ansys: "
        f"X={point.rot_x} deg, Y={point.rot_y} deg, Z={point.rot_z} deg"
    )


def run_orientation(point: OrientationPoint, dry_run: bool, skip_ansys: bool) -> None:
    """Run the complete CAD export and optional Ansys analysis for one point."""
    step_file = step_path_for(point)
    run_solidworks_export(point, step_file, dry_run)

    if skip_ansys:
        print(
            "Ansys skipped by --skip-ansys. Would pass STEP and rotation metadata: "
            f"step_file={step_file}, run_id={point.name}, "
            f"rot_x={point.rot_x}, rot_y={point.rot_y}, rot_z={point.rot_z}"
        )
    else:
        run_ansys_analysis(point, step_file, dry_run)

    result_file = result_path_for(point)
    run_command(
        [
            str(PROJECT_PYTHON),
            "run_lpbf_simulation.py",
            "--step-file",
            str(step_file),
            "--run-id",
            point.name,
            "--rot-x",
            str(point.rot_x),
            "--rot-y",
            str(point.rot_y),
            "--rot-z",
            str(point.rot_z),
            "--result-file",
            str(result_file),
        ],
        ANSYS_DIR,
        dry_run,
    )


def read_result_summary(point: OrientationPoint) -> dict:
    result_file = result_path_for(point)
    if not result_file.exists():
        return {"run_id": point.name, "status": "missing_result_file"}

    try:
        return json.loads(result_file.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "run_id": point.name,
            "status": "result_file_read_failed",
            "error": str(exc),
            "result_file": str(result_file),
        }


def write_run_manifest(points: list[OrientationPoint], dry_run: bool) -> None:
    manifest = {
        "project_root": str(PROJECT_ROOT),
        "solidworks_dir": str(SOLIDWORKS_DIR),
        "ansys_dir": str(ANSYS_DIR),
        "ansys_enabled": ANSYS_ENABLED,
        "z_clearance_step_mm": Z_CLEARANCE_STEP_MM,
        "z_clearance_max_steps": Z_CLEARANCE_MAX_STEPS,
        "part_file": str(PART_FILE),
        "step_output_dir": str(STEP_OUTPUT_DIR),
        "results_dir": str(RESULTS_DIR),
        "points": [
            {
                **asdict(point),
                "step_file": str(step_path_for(point)),
                "result_file": str(result_path_for(point)),
                "result_summary": read_result_summary(point) if ANSYS_ENABLED and not dry_run else None,
            }
            for point in points
        ],
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    manifest_path = RESULTS_DIR / "run_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    if dry_run:
        print(f"\nDry-run manifest written to: {manifest_path}")
    else:
        print(f"\nRun manifest written to: {manifest_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rotate the LPBF part in SolidWorks, export STEP files, and run "
            "Ansys stress results for the four starter orientations."
        )
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print and record the commands without launching SolidWorks or Ansys.",
    )
    parser.add_argument(
        "--skip-ansys",
        action="store_true",
        help="Only generate STEP files and skip the Ansys analysis stage.",
    )
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Use adaptive optimization to select orientations from the CSV history.",
    )
    parser.add_argument(
        "--contour-map",
        action="store_true",
        help="Use local adaptive contour mapping instead of global Bayesian search.",
    )
    parser.add_argument(
        "--optimization-iterations",
        type=int,
        default=10,
        help="Number of additional Bayesian orientations to evaluate (default: 10).",
    )
    parser.add_argument(
        "--optimization-min-angle",
        type=float,
        default=0.0,
        help="Minimum angle for each rotation axis (default: 0 degrees).",
    )
    parser.add_argument(
        "--optimization-max-angle",
        type=float,
        default=90.0,
        help="Maximum angle for each rotation axis (default: 90 degrees).",
    )
    parser.add_argument(
        "--optimization-grid-step",
        type=float,
        default=15.0,
        help="Candidate grid spacing in degrees (default: 15 degrees).",
    )
    parser.add_argument(
        "--contour-step",
        type=float,
        default=15.0,
        help="Initial local contour spacing in degrees (default: 15 degrees).",
    )
    parser.add_argument(
        "--stop-improvement",
        type=float,
        default=0.05,
        help="Stop threshold for relative stress improvement (default: 0.05).",
    )
    parser.add_argument(
        "--stop-patience",
        type=int,
        default=3,
        help="Consecutive below-threshold runs before stopping (default: 3).",
    )
    parser.add_argument(
        "--minimum-optimization-iterations",
        type=int,
        default=5,
        help="Minimum evaluations before convergence stopping is allowed (default: 5).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not PART_FILE.exists():
        raise FileNotFoundError(f"SolidWorks part file not found: {PART_FILE}")

    STEP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.optimize or args.contour_map:
        if args.optimization_iterations <= 0:
            raise ValueError("--optimization-iterations must be positive")

        from optimize_orientation import load_successful_results, next_contour_orientation, next_orientation

        optimization_points = []
        stalled_iterations = 0
        next_run_number = next_optimizer_run_number()
        for iteration in range(1, args.optimization_iterations + 1):
            previous_observations = load_successful_results(ORIENTATION_RESULTS_CSV)
            previous_best = min((value for _, value in previous_observations), default=None)
            if args.contour_map:
                candidate, diagnostics = next_contour_orientation(
                    ORIENTATION_RESULTS_CSV,
                    min_angle=args.optimization_min_angle,
                    max_angle=args.optimization_max_angle,
                    contour_step=args.contour_step,
                )
            else:
                candidate, diagnostics = next_orientation(
                    ORIENTATION_RESULTS_CSV,
                    min_angle=args.optimization_min_angle,
                    max_angle=args.optimization_max_angle,
                    grid_step=args.optimization_grid_step,
                )
            if candidate is None:
                print(f"Bayesian optimization stopped: {diagnostics['reason']}")
                break

            point = OrientationPoint(
                name=f"bo_{next_run_number:03d}",
                rot_x=candidate.rot_x,
                rot_y=candidate.rot_y,
                rot_z=candidate.rot_z,
            )
            next_run_number += 1
            print(f"\n=== Bayesian orientation {iteration}/{args.optimization_iterations} ===")
            print(json.dumps(diagnostics, indent=2))
            print(
                "Selected orientation: "
                f"X={point.rot_x}, Y={point.rot_y}, Z={point.rot_z} degrees"
            )
            run_orientation(point, args.dry_run, args.skip_ansys)
            optimization_points.append(point)

            if args.dry_run:
                print("Dry-run optimization stopped after one candidate; no CSV observation was created.")
                break

            current_observations = load_successful_results(ORIENTATION_RESULTS_CSV)
            current_best = min((value for _, value in current_observations), default=None)
            if previous_best is not None and current_best is not None:
                relative_improvement = (previous_best - current_best) / previous_best
                if relative_improvement < args.stop_improvement:
                    stalled_iterations += 1
                else:
                    stalled_iterations = 0
                print(
                    f"Relative best-stress improvement: {relative_improvement:.2%}; "
                    f"below-threshold streak: {stalled_iterations}"
                )
                if (
                    iteration >= args.minimum_optimization_iterations
                    and stalled_iterations >= args.stop_patience
                ):
                    print(
                        "Optimization stopped: the best average stress improved by "
                        f"less than {args.stop_improvement:.1%} for "
                        f"{args.stop_patience} consecutive evaluations."
                    )
                    break

        write_run_manifest(optimization_points, args.dry_run)
        return 0

    for point in STARTER_POINTS:
        run_orientation(point, args.dry_run, args.skip_ansys)

    write_run_manifest(STARTER_POINTS, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
