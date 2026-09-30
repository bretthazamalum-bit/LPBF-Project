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
from html import escape
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

DEFAULT_PART_FILE = SOLIDWORKS_DIR / "Part1.SLDPRT"
DEFAULT_PART_MESH_SIZE_MM = 0.1
DEFAULT_BASE_MESH_SIZE_MM = 0.5
STEP_OUTPUT_DIR = PROJECT_ROOT / "generated_steps"
RESULTS_DIR = PROJECT_ROOT / "results"
ORIENTATION_RESULTS_CSV = RESULTS_DIR / "orientation_results.csv"
PROGRESS_GRAPH_FILE = RESULTS_DIR / "stress_progress.svg"
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


def update_progress_graph() -> None:
    """Write a dependency-free live SVG graph from the orientation CSV."""
    if not ORIENTATION_RESULTS_CSV.exists():
        return

    rows = []
    with ORIENTATION_RESULTS_CSV.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            try:
                average_pa = float(row.get("average_stress_pa", ""))
            except (TypeError, ValueError):
                continue
            if average_pa > 0:
                rows.append((len(rows) + 1, average_pa, row.get("run_id", "")))

    if not rows:
        return

    width, height = 1000, 620
    left, right, top, bottom = 90, 30, 70, 80
    plot_width = width - left - right
    plot_height = height - top - bottom
    x_max = max(1, len(rows))
    y_max = max(value for _, value, _ in rows) * 1.1
    if y_max <= 0:
        y_max = 1.0

    def x_position(index: int) -> float:
        return left if x_max == 1 else left + (index - 1) * plot_width / (x_max - 1)

    def y_position(value: float) -> float:
        return top + plot_height - value * plot_height / y_max

    path_points = " ".join(
        f"{x_position(index):.1f},{y_position(value):.1f}"
        for index, value, _ in rows
    )
    best_so_far = []
    current_best = None
    for index, value, _ in rows:
        current_best = value if current_best is None else min(current_best, value)
        best_so_far.append((index, current_best))
    best_path = " ".join(
        f"{x_position(index):.1f},{y_position(value):.1f}"
        for index, value in best_so_far
    )

    grid = []
    for step in range(6):
        value = y_max * step / 5
        y = y_position(value)
        grid.append(
            f'<line x1="{left}" y1="{y:.1f}" x2="{width-right}" y2="{y:.1f}" '
            'stroke="#d9d9d9"/><text x="10" y="{:.1f}" font-size="12">{:.1f} MPa</text>'.format(
                y + 4, value / 1e6
            )
        )

    circles = []
    labels = []
    for index, value, run_id in rows:
        x, y = x_position(index), y_position(value)
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#1769aa"/>')
        if len(rows) <= 12 or index == len(rows):
            labels.append(
                f'<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle" '
                f'font-size="11">{escape(run_id)} {value/1e6:.1f}</text>'
            )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white"/>
<text x="{width/2:.1f}" y="30" text-anchor="middle" font-size="20" font-family="Arial">Average Stress by Orientation Evaluation</text>
{''.join(grid)}
<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="black"/>
<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="black"/>
<polyline points="{path_points}" fill="none" stroke="#1769aa" stroke-width="2"/>
<polyline points="{best_path}" fill="none" stroke="#d1495b" stroke-width="2" stroke-dasharray="7 5"/>
{''.join(circles)}
{''.join(labels)}
<text x="{width/2:.1f}" y="{height-20}" text-anchor="middle" font-size="14" font-family="Arial">Evaluation number</text>
<text x="18" y="{height/2:.1f}" text-anchor="middle" font-size="14" font-family="Arial" transform="rotate(-90 18 {height/2:.1f})">Average equivalent stress (MPa)</text>
<text x="{width-250}" y="{height-42}" font-size="12" fill="#1769aa">blue: measured</text>
<text x="{width-120}" y="{height-42}" font-size="12" fill="#d1495b">red: best</text>
</svg>
'''
    PROGRESS_GRAPH_FILE.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_GRAPH_FILE.write_text(svg, encoding="utf-8")


def print_progress_summary(label: str, iteration: int, total: int | None) -> None:
    """Print a concise progress line after each completed orientation."""
    rows = []
    if ORIENTATION_RESULTS_CSV.exists():
        with ORIENTATION_RESULTS_CSV.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
    valid = []
    for row in rows:
        try:
            value = float(row.get("average_stress_pa", ""))
            if row.get("status") == "success" and value > 0:
                valid.append(value)
        except (TypeError, ValueError):
            pass
    if not valid:
        print(f"Progress: completed {label}; no valid stress result yet.")
        return
    suffix = f"/{total}" if total is not None else ""
    print(
        f"Progress: iteration {iteration}{suffix} complete; "
        f"average stress={valid[-1] / 1e6:.3f} MPa; "
        f"best={min(valid) / 1e6:.3f} MPa; "
        f"live graph={PROGRESS_GRAPH_FILE}"
    )


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


def choose_part_file() -> Path:
    """Show a Windows file picker and return the selected SolidWorks part."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as error:
        raise RuntimeError(
            "The part picker requires tkinter. Use --part-file to select a part "
            "from a command line instead."
        ) from error

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        selected_file = filedialog.askopenfilename(
            title="Select SolidWorks part to analyze",
            initialdir=str(DEFAULT_PART_FILE.parent),
            filetypes=[
                ("SolidWorks part files", "*.SLDPRT"),
                ("All files", "*.*"),
            ],
        )
    finally:
        root.destroy()

    if not selected_file:
        raise SystemExit("No SolidWorks part selected; exiting without a run.")

    return Path(selected_file).resolve()


def choose_mesh_sizes(
    part_default: float = DEFAULT_PART_MESH_SIZE_MM,
    base_default: float = DEFAULT_BASE_MESH_SIZE_MM,
) -> tuple[float, float]:
    """Ask for the part and base mesh sizes in millimeters."""
    try:
        import tkinter as tk
        from tkinter import simpledialog
    except ImportError as error:
        raise RuntimeError(
            "The mesh-size dialogs require tkinter. Use --part-mesh-size-mm "
            "and --base-mesh-size-mm from a command line instead."
        ) from error

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        part_mesh_size = simpledialog.askfloat(
            "Part mesh size",
            "Part mesh element size (mm):",
            initialvalue=part_default,
            minvalue=0.000001,
            parent=root,
        )
        if part_mesh_size is None:
            raise SystemExit("Part mesh size was cancelled; exiting without a run.")

        base_mesh_size = simpledialog.askfloat(
            "Base mesh size",
            "Base mesh element size (mm):",
            initialvalue=base_default,
            minvalue=0.000001,
            parent=root,
        )
        if base_mesh_size is None:
            raise SystemExit("Base mesh size was cancelled; exiting without a run.")
    finally:
        root.destroy()

    return part_mesh_size, base_mesh_size


def run_solidworks_export(
    point: OrientationPoint,
    step_file: Path,
    part_file: Path,
    dry_run: bool,
) -> None:
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
            str(part_file),
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


def run_ansys_analysis(
    point: OrientationPoint,
    step_file: Path,
    part_mesh_size_mm: float,
    base_mesh_size_mm: float,
    dry_run: bool,
) -> None:
    print(f"\n--- Ansys analysis for {point.name} ---")
    print(f"STEP input passed to Ansys: {step_file}")
    print(
        "Rotation metadata passed to Ansys: "
        f"X={point.rot_x} deg, Y={point.rot_y} deg, Z={point.rot_z} deg"
    )
    print(
        "Mesh sizes passed to Ansys: "
        f"part={part_mesh_size_mm} mm, base={base_mesh_size_mm} mm"
    )


def run_orientation(
    point: OrientationPoint,
    part_file: Path,
    part_mesh_size_mm: float,
    base_mesh_size_mm: float,
    dry_run: bool,
    skip_ansys: bool,
) -> None:
    """Run the complete CAD export and optional Ansys analysis for one point."""
    step_file = step_path_for(point)
    run_solidworks_export(point, step_file, part_file, dry_run)

    if skip_ansys:
        print(
            "Ansys skipped by --skip-ansys. Would pass STEP and rotation metadata: "
            f"step_file={step_file}, run_id={point.name}, "
            f"rot_x={point.rot_x}, rot_y={point.rot_y}, rot_z={point.rot_z}"
        )
    else:
        run_ansys_analysis(
            point,
            step_file,
            part_mesh_size_mm,
            base_mesh_size_mm,
            dry_run,
        )

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
            "--part-mesh-size-mm",
            str(part_mesh_size_mm),
            "--base-mesh-size-mm",
            str(base_mesh_size_mm),
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


def write_run_manifest(
    points: list[OrientationPoint],
    part_file: Path,
    part_mesh_size_mm: float,
    base_mesh_size_mm: float,
    dry_run: bool,
) -> None:
    manifest = {
        "project_root": str(PROJECT_ROOT),
        "solidworks_dir": str(SOLIDWORKS_DIR),
        "ansys_dir": str(ANSYS_DIR),
        "ansys_enabled": ANSYS_ENABLED,
        "z_clearance_step_mm": Z_CLEARANCE_STEP_MM,
        "z_clearance_max_steps": Z_CLEARANCE_MAX_STEPS,
        "part_file": str(part_file),
        "part_mesh_size_mm": part_mesh_size_mm,
        "base_mesh_size_mm": base_mesh_size_mm,
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
        "--part-file",
        help=(
            "SolidWorks .SLDPRT to analyze. If omitted, a file-selection popup "
            "opens when the program starts."
        ),
    )
    parser.add_argument(
        "--part-mesh-size-mm",
        type=float,
        help="Part mesh element size in millimeters; otherwise ask in a popup.",
    )
    parser.add_argument(
        "--base-mesh-size-mm",
        type=float,
        help="Base mesh element size in millimeters; otherwise ask in a popup.",
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
        "--contour-min-step",
        type=float,
        default=3.75,
        help=(
            "Smallest local contour spacing allowed before convergence stopping "
            "(default: 3.75 degrees)."
        ),
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

    part_file = (
        Path(args.part_file).expanduser().resolve()
        if args.part_file
        else choose_part_file()
    )
    if not part_file.exists():
        raise FileNotFoundError(f"SolidWorks part file not found: {part_file}")
    if part_file.suffix.casefold() != ".sldprt":
        raise ValueError(f"Selected file is not a SolidWorks part: {part_file}")

    print(f"Selected SolidWorks part: {part_file}")

    part_mesh_size_mm = args.part_mesh_size_mm
    base_mesh_size_mm = args.base_mesh_size_mm
    if part_mesh_size_mm is None or base_mesh_size_mm is None:
        selected_part_default = (
            part_mesh_size_mm
            if part_mesh_size_mm is not None
            else DEFAULT_PART_MESH_SIZE_MM
        )
        selected_base_default = (
            base_mesh_size_mm
            if base_mesh_size_mm is not None
            else DEFAULT_BASE_MESH_SIZE_MM
        )
        part_mesh_size_mm, base_mesh_size_mm = choose_mesh_sizes(
            selected_part_default,
            selected_base_default,
        )
    if part_mesh_size_mm <= 0 or base_mesh_size_mm <= 0:
        raise ValueError("Mesh sizes must be greater than zero millimeters.")
    print(
        "Selected mesh sizes: "
        f"part={part_mesh_size_mm} mm, base={base_mesh_size_mm} mm"
    )

    STEP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.optimize or args.contour_map:
        if args.optimization_iterations <= 0:
            raise ValueError("--optimization-iterations must be positive")
        if args.contour_map and args.contour_min_step <= 0:
            raise ValueError("--contour-min-step must be positive")
        if args.contour_map and args.contour_min_step > args.contour_step:
            raise ValueError("--contour-min-step cannot exceed --contour-step")

        from optimize_orientation import load_successful_results, next_contour_orientation, next_orientation

        optimization_points = []
        stalled_iterations = 0
        contour_step = args.contour_step
        next_run_number = next_optimizer_run_number()
        for iteration in range(1, args.optimization_iterations + 1):
            previous_observations = load_successful_results(ORIENTATION_RESULTS_CSV)
            previous_best = min((value for _, value in previous_observations), default=None)
            if args.contour_map:
                candidate, diagnostics = next_contour_orientation(
                    ORIENTATION_RESULTS_CSV,
                    min_angle=args.optimization_min_angle,
                    max_angle=args.optimization_max_angle,
                    contour_step=contour_step,
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
            run_orientation(
                point,
                part_file,
                part_mesh_size_mm,
                base_mesh_size_mm,
                args.dry_run,
                args.skip_ansys,
            )
            optimization_points.append(point)
            if not args.dry_run:
                update_progress_graph()
                print_progress_summary(
                    point.name,
                    iteration,
                    args.optimization_iterations,
                )

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
                    if args.contour_map and contour_step > args.contour_min_step:
                        previous_step = contour_step
                        contour_step = max(
                            args.contour_min_step,
                            contour_step / 2.0,
                        )
                        stalled_iterations = 0
                        print(
                            "No improvement at the current incumbent; refining "
                            f"the local contour step from {previous_step:g} to "
                            f"{contour_step:g} degrees and continuing."
                        )
                        continue
                    print(
                        "Optimization stopped: the best average stress improved by "
                        f"less than {args.stop_improvement:.1%} for "
                        f"{args.stop_patience} consecutive evaluations."
                    )
                    break

        write_run_manifest(
            optimization_points,
            part_file,
            part_mesh_size_mm,
            base_mesh_size_mm,
            args.dry_run,
        )
        return 0

    for iteration, point in enumerate(STARTER_POINTS, start=1):
        run_orientation(
            point,
            part_file,
            part_mesh_size_mm,
            base_mesh_size_mm,
            args.dry_run,
            args.skip_ansys,
        )
        if not args.dry_run:
            update_progress_graph()
            print_progress_summary(point.name, iteration, len(STARTER_POINTS))

    write_run_manifest(
        STARTER_POINTS,
        part_file,
        part_mesh_size_mm,
        base_mesh_size_mm,
        args.dry_run,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
