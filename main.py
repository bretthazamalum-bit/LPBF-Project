# Root controller for the LPBF orientation sweep.
# This file owns the list of test rotations, runs the SolidWorks STEP export,
# then passes each generated STEP into Ansys for stress evaluation.
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SOLIDWORKS_DIR = PROJECT_ROOT / "Solidworks"
ANSYS_DIR = PROJECT_ROOT / "ANSYS"

PART_FILE = SOLIDWORKS_DIR / "Part1.SLDPRT"
STEP_OUTPUT_DIR = PROJECT_ROOT / "generated_steps"
RESULTS_DIR = PROJECT_ROOT / "results"
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
            sys.executable,
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

    result_file = result_path_for(point)
    run_command(
        [
            sys.executable,
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
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not PART_FILE.exists():
        raise FileNotFoundError(f"SolidWorks part file not found: {PART_FILE}")

    STEP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for point in STARTER_POINTS:
        step_file = step_path_for(point)
        run_solidworks_export(point, step_file, args.dry_run)

        if args.skip_ansys:
            print(
                "Ansys skipped by --skip-ansys. Would pass STEP and rotation metadata: "
                f"step_file={step_file}, "
                f"run_id={point.name}, "
                f"rot_x={point.rot_x}, rot_y={point.rot_y}, rot_z={point.rot_z}"
            )
        else:
            run_ansys_analysis(point, step_file, args.dry_run)

    write_run_manifest(STARTER_POINTS, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
