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
import time
from datetime import datetime, timezone
from html import escape
from dataclasses import asdict, dataclass
from pathlib import Path

from analyze_orientation_results import render_svg_png


PROJECT_ROOT = Path(__file__).resolve().parent
SOLIDWORKS_DIR = PROJECT_ROOT / "Solidworks"
ANSYS_DIR = PROJECT_ROOT / "ANSYS"
MATERIALS_DIR = PROJECT_ROOT / "materials"
PROCESS_SETTINGS_FILE = PROJECT_ROOT / "process_settings.csv"
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
PROGRESS_GRAPH_PNG_FILE = RESULTS_DIR / "stress_progress.png"
Z_CLEARANCE_STEP_MM = 0.25
Z_CLEARANCE_MAX_STEPS = 400
LPBF_SUPPORT_LIFT_MM = 2.0

ANSYS_ENABLED = True
DEFAULT_MATERIAL_ID = "inconel_718"
MATERIAL_OPTIONS = {
    "inconel_718": "Inconel 718",
    "316l_stainless_steel": "316L Stainless Steel",
    "ti_6al_4v": "Ti-6Al-4V",
}


@dataclass(frozen=True)
class OrientationPoint:
    name: str
    rot_x: float
    rot_y: float
    rot_z: float


def material_config_path(material_id: str) -> Path:
    path = MATERIALS_DIR / f"{material_id}.json"
    if not path.is_file():
        raise FileNotFoundError(f"Material configuration not found: {path}")
    return path


def load_material_config(material_id: str) -> dict:
    path = material_config_path(material_id)
    config = json.loads(path.read_text(encoding="utf-8"))
    for key in ("id", "display_name", "ansys_part_material", "ansys_base_material"):
        if not config.get(key):
            raise ValueError(f"Material configuration missing '{key}': {path}")
    config["config_path"] = str(path)
    return config


def load_optimizer_config(args: argparse.Namespace, config_path: Path | None) -> argparse.Namespace:
    """Apply one-row optimizer settings from a separate CSV file."""
    if config_path is None:
        return args
    path = config_path.expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Optimizer configuration not found: {path}")

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if len(rows) != 1:
        raise ValueError(f"Optimizer configuration must contain exactly one data row: {path}")

    row = rows[0]
    fields = {
        "sobol_initial_runs": int,
        "contour_starts": int,
        "contour_step": float,
        "contour_min_step": float,
        "stop_improvement": float,
        "stop_patience": int,
        "minimum_optimization_iterations": int,
    }
    for field, converter in fields.items():
        value = row.get(field, "").strip()
        if value == "":
            raise ValueError(f"Optimizer configuration is missing '{field}': {path}")
        setattr(args, field, converter(value))
    print(f"Loaded optimizer settings: {path}")
    return args


def format_angle(value: float) -> str:
    text = f"{value:g}"
    return text.replace("-", "neg").replace(".", "p")


def configure_output_directory(output_dir: Path | None) -> Path:
    """Redirect generated artifacts while preserving the legacy default layout."""
    global STEP_OUTPUT_DIR
    global RESULTS_DIR
    global ORIENTATION_RESULTS_CSV
    global PROGRESS_GRAPH_FILE
    global PROGRESS_GRAPH_PNG_FILE

    if output_dir is None:
        resolved = PROJECT_ROOT
    else:
        candidate = output_dir.expanduser()
        resolved = (PROJECT_ROOT / candidate).resolve() if not candidate.is_absolute() else candidate.resolve()

    if resolved == PROJECT_ROOT:
        STEP_OUTPUT_DIR = PROJECT_ROOT / "generated_steps"
        RESULTS_DIR = PROJECT_ROOT / "results"
    else:
        STEP_OUTPUT_DIR = resolved / "generated_steps"
        RESULTS_DIR = resolved / "results"

    ORIENTATION_RESULTS_CSV = RESULTS_DIR / "orientation_results.csv"
    PROGRESS_GRAPH_FILE = RESULTS_DIR / "stress_progress.svg"
    PROGRESS_GRAPH_PNG_FILE = RESULTS_DIR / "stress_progress.png"
    return resolved


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
    # Leave a dedicated lane for the Y-axis title to the left of the tick
    # values.  The old x=10 tick labels overlapped the rotated title at x=18.
    left, right, top, bottom = 110, 30, 70, 80
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
            'stroke="#d9d9d9"/><text x="90" y="{:.1f}" text-anchor="end" font-size="12">{:.1f} MPa</text>'.format(
                y + 4, value / 1e6
            )
        )

    circles = []
    label_candidates = []
    for index, value, run_id in rows:
        x, y = x_position(index), y_position(value)
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#1769aa"/>')
        if len(rows) <= 12 or index == len(rows):
            label_candidates.append((index == len(rows), x, y, f"{run_id} {value/1e6:.1f}"))

    # Keep only labels whose estimated bounding boxes do not overlap. Always
    # prioritize the newest evaluation, then place labels above/below points.
    labels = []
    occupied = []
    for _, x, y, text in sorted(label_candidates, reverse=True):
        box_width = max(34.0, len(text) * 6.2 + 8.0)
        placed = None
        for offset in (-12.0, 22.0, -30.0, 40.0):
            baseline = max(top + 13.0, min(height - bottom - 4.0, y + offset))
            box = (x - box_width / 2, baseline - 13.0, x + box_width / 2, baseline + 3.0)
            if all(
                box[2] < other[0] - 3
                or box[0] > other[2] + 3
                or box[3] < other[1] - 3
                or box[1] > other[3] + 3
                for other in occupied
            ):
                placed = (baseline, box)
                break
        if placed is None:
            continue
        baseline, box = placed
        occupied.append(box)
        labels.append(
            f'<rect x="{box[0]:.1f}" y="{box[1]:.1f}" width="{box_width:.1f}" height="16" '
            f'fill="white" fill-opacity="0.82"/>'
            f'<text x="{x:.1f}" y="{baseline:.1f}" text-anchor="middle" '
            f'font-size="11">{escape(text)}</text>'
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
    render_svg_png(PROGRESS_GRAPH_FILE, PROGRESS_GRAPH_PNG_FILE)


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


def choose_material() -> str:
    """Show a dropdown for the printable-part material configuration."""
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError as error:
        raise RuntimeError(
            "The material picker requires tkinter. Use --material from a command line instead."
        ) from error

    selected_material = {"id": None}
    root = tk.Tk()
    root.title("Select LPBF material")
    root.attributes("-topmost", True)
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=14)
    frame.grid(row=0, column=0, sticky="nsew")
    ttk.Label(frame, text="Material for the printed part:").grid(
        row=0, column=0, padx=4, pady=(0, 8), sticky="w"
    )
    labels = list(MATERIAL_OPTIONS.values())
    dropdown = ttk.Combobox(frame, values=labels, state="readonly", width=28)
    dropdown.current(labels.index(MATERIAL_OPTIONS[DEFAULT_MATERIAL_ID]))
    dropdown.grid(row=1, column=0, padx=4, pady=(0, 12), sticky="ew")

    def accept():
        selected_label = dropdown.get()
        selected_material["id"] = next(
            material_id
            for material_id, display_name in MATERIAL_OPTIONS.items()
            if display_name == selected_label
        )
        root.destroy()

    def cancel():
        root.destroy()

    buttons = ttk.Frame(frame)
    buttons.grid(row=2, column=0, sticky="e")
    ttk.Button(buttons, text="Cancel", command=cancel).grid(row=0, column=0, padx=(0, 6))
    ttk.Button(buttons, text="Continue", command=accept).grid(row=0, column=1)
    dropdown.focus_set()
    root.bind("<Return>", lambda _event: accept())
    root.bind("<Escape>", lambda _event: cancel())
    root.protocol("WM_DELETE_WINDOW", cancel)
    root.mainloop()

    if selected_material["id"] is None:
        raise SystemExit("Material selection was cancelled; exiting without a run.")
    return selected_material["id"]


def choose_sampling_symmetry() -> tuple[str, str, int]:
    """Ask how symmetry may be used to reduce only initial sampling."""
    try:
        import tkinter as tk
        from tkinter import simpledialog
    except ImportError as error:
        raise RuntimeError(
            "The symmetry dialog requires tkinter. Use --symmetry-type from a command line instead."
        ) from error

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        symmetry_type = simpledialog.askstring(
            "Initial sampling symmetry",
            "Enter symmetry type: none or cyclic",
            initialvalue="none",
            parent=root,
        )
        if symmetry_type is None:
            raise SystemExit("Symmetry selection was cancelled; exiting without a run.")
        symmetry_type = symmetry_type.strip().casefold()
        if symmetry_type not in {"none", "cyclic"}:
            raise ValueError("Symmetry type must be 'none' or 'cyclic'.")

        axis = "z"
        repeats = 1
        if symmetry_type == "cyclic":
            axis = simpledialog.askstring(
                "Cyclic symmetry axis",
                "Axis of cyclic symmetry: x, y, or z",
                initialvalue="z",
                parent=root,
            )
            if axis is None:
                raise SystemExit("Symmetry-axis selection was cancelled; exiting without a run.")
            axis = axis.strip().casefold()
            if axis not in {"x", "y", "z"}:
                raise ValueError("Cyclic symmetry axis must be x, y, or z.")
            repeats = simpledialog.askinteger(
                "Cyclic symmetry repeats",
                "Number of identical repeated sectors:",
                initialvalue=1,
                minvalue=2,
                parent=root,
            )
            if repeats is None:
                raise SystemExit("Symmetry-repeat selection was cancelled; exiting without a run.")
    finally:
        root.destroy()

    return symmetry_type, axis, repeats


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
        "Bounding-box placement passed to SolidWorks: "
        f"part='part', base='base', "
        f"minimum_gap={LPBF_SUPPORT_LIFT_MM} mm"
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
            "--support-lift-mm",
            str(LPBF_SUPPORT_LIFT_MM),
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
    material_config_file: Path,
    process_config_file: Path,
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
            "--material-config",
            str(material_config_file),
            "--process-config",
            str(process_config_file),
            "--results-csv",
            str(ORIENTATION_RESULTS_CSV),
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
    sobol_initial_runs: int = 0,
    symmetry_type: str | None = None,
    symmetry_axis: str | None = None,
    symmetry_repeats: int = 1,
    contour_starts: int = 0,
    run_metadata: dict[str, object] | None = None,
) -> None:
    manifest = {
        "project_root": str(PROJECT_ROOT),
        "solidworks_dir": str(SOLIDWORKS_DIR),
        "ansys_dir": str(ANSYS_DIR),
        "ansys_enabled": ANSYS_ENABLED,
        "z_clearance_step_mm": Z_CLEARANCE_STEP_MM,
        "z_clearance_max_steps": Z_CLEARANCE_MAX_STEPS,
        "lpbf_support_lift_mm": LPBF_SUPPORT_LIFT_MM,
        "part_file": str(part_file),
        "part_mesh_size_mm": part_mesh_size_mm,
        "base_mesh_size_mm": base_mesh_size_mm,
        "sobol_initial_runs": sobol_initial_runs,
        "initial_sampling_symmetry": {
            "type": symmetry_type,
            "axis": symmetry_axis,
            "repeats": symmetry_repeats,
        },
        "contour_starts": contour_starts,
        "step_output_dir": str(STEP_OUTPUT_DIR),
        "results_dir": str(RESULTS_DIR),
        **(run_metadata or {}),
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


def format_runtime(seconds: float) -> str:
    total = max(0, int(round(seconds)))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours} h {minutes} m {secs} s"
    if minutes:
        return f"{minutes} m {secs} s"
    return f"{secs} s"


def write_post_run_outputs(metadata: dict[str, object]) -> None:
    """Write the human summary and contour map after a completed run."""
    from analyze_orientation_results import (
        choose_slice,
        load_observations,
        write_contour_svg,
        write_summary,
    )

    observations = load_observations(RESULTS_DIR)
    selected_rz, selected = choose_slice(observations, None)
    if not selected:
        print("No successful stress results; run summary and contour map were not generated.")
        return
    contour_path = RESULTS_DIR / "orientation_contour_map.svg"
    contour_png_path = RESULTS_DIR / "orientation_contour_map.png"
    summary_path = RESULTS_DIR / "run_summary.txt"
    write_contour_svg(contour_path, selected, "average", selected_rz)
    render_svg_png(contour_path, contour_png_path)
    write_summary(summary_path, observations, "average", selected_rz, contour_path, metadata)
    print(f"Run summary written to: {summary_path}")
    print(f"Contour map written to: {contour_path}")
    if contour_png_path.exists():
        print(f"Contour map PNG written to: {contour_png_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run Sobol initialization and multi-start contour refinement for "
            "LPBF orientation optimization."
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
        "--material",
        choices=("inconel_718", "316l_stainless_steel", "ti_6al_4v"),
        default=None,
        help="Material configuration; if omitted, show the material-selection popup.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help=(
            "Directory for generated_steps, results, CSV, screenshots, maps, and summaries. "
            "If omitted, use the project folders."
        ),
    )
    parser.add_argument(
        "--process-config",
        type=Path,
        default=PROCESS_SETTINGS_FILE,
        help="CSV containing ANSYS LPBF process settings.",
    )
    parser.add_argument(
        "--optimizer-config",
        type=Path,
        help="One-row CSV containing Sobol and contour stopping settings.",
    )
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Use Bayesian expected-improvement optimization instead of contour mode.",
    )
    parser.add_argument(
        "--contour-map",
        action="store_true",
        help="Explicitly select the default Sobol plus contour workflow.",
    )
    parser.add_argument(
        "--sobol-initial-runs",
        type=int,
        default=8,
        help=(
            "Number of low-discrepancy Sobol orientations before contour "
            "refinement in contour mode (default: 8; use 0 to disable)."
        ),
    )
    parser.add_argument(
        "--symmetry-type",
        choices=("none", "cyclic"),
        help=(
            "Use symmetry only to reduce initial Sobol sampling. Cyclic symmetry "
            "also requires --symmetry-axis and --symmetry-repeats."
        ),
    )
    parser.add_argument(
        "--symmetry-axis",
        choices=("x", "y", "z"),
        default="z",
        help="Axis for cyclic sampling symmetry (default: z).",
    )
    parser.add_argument(
        "--symmetry-repeats",
        type=int,
        help="Number of identical cyclic sectors; must be at least 2.",
    )
    parser.add_argument(
        "--optimization-iterations",
        type=int,
        default=40,
        help=(
            "Maximum total evaluations for the flip, Sobol, and refinement "
            "phases (default: 40)."
        ),
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
        default=180.0,
        help="Maximum angle for each rotation axis (default: 180 degrees).",
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
        "--contour-starts",
        type=int,
        default=3,
        help=(
            "Number of lowest-stress measured orientations used as independent "
            "contour refinement starts (default: 3)."
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
    args = load_optimizer_config(args, args.optimizer_config)
    run_started_at = datetime.now(timezone.utc)
    run_timer_start = time.perf_counter()
    output_dir = configure_output_directory(args.output_dir)
    selected_material_id = args.material or choose_material()
    material_config = load_material_config(selected_material_id)
    material_config_file = Path(material_config["config_path"])
    process_config_file = args.process_config.expanduser()
    if not process_config_file.is_absolute():
        process_config_file = PROJECT_ROOT / process_config_file
    process_config_file = process_config_file.resolve()
    if not process_config_file.is_file():
        raise FileNotFoundError(f"Process settings CSV not found: {process_config_file}")

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
    print(
        "Selected material: "
        f"{material_config['display_name']} "
        f"(part={material_config['ansys_part_material']}, "
        f"base={material_config['ansys_base_material']})"
    )
    print(f"Output directory: {output_dir}")

    # Contour mode is now the normal workflow. --optimize remains available
    # for users who want the older global Bayesian expected-improvement path.
    contour_mode = not args.optimize
    if args.optimize and args.contour_map:
        raise ValueError("Use either --optimize or --contour-map, not both.")

    # Raster direction is configured independently in Ansys. Keep the part's
    # in-plane yaw fixed at zero and optimize only its X/Y build orientation.
    symmetry_type = None
    symmetry_axis = None
    symmetry_repeats = 1

    STEP_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.optimization_iterations <= 0:
        raise ValueError("--optimization-iterations must be positive")
    if contour_mode and args.contour_min_step <= 0:
        raise ValueError("--contour-min-step must be positive")
    if contour_mode and args.contour_min_step > args.contour_step:
        raise ValueError("--contour-min-step cannot exceed --contour-step")
    if contour_mode and args.sobol_initial_runs < 0:
        raise ValueError("--sobol-initial-runs cannot be negative")
    if contour_mode and args.contour_starts <= 0:
        raise ValueError("--contour-starts must be positive")

    if contour_mode or args.optimize:

        from optimize_orientation import (
            load_successful_results,
            next_contour_orientation,
            next_orientation,
            initial_orientation_anchors,
            next_sobol_orientation,
        )

        optimization_points = []
        stalled_iterations = 0
        contour_step = args.contour_step
        sobol_axis_max_angles = (
            args.optimization_max_angle,
            args.optimization_max_angle,
        )
        symmetry_anchors = initial_orientation_anchors(
            args.optimization_min_angle,
            args.optimization_max_angle,
            None,
        )
        next_run_number = next_optimizer_run_number()
        flip_anchor_count = len(symmetry_anchors) if contour_mode else 0
        sobol_end_iteration = flip_anchor_count + (
            args.sobol_initial_runs if contour_mode else 0
        )
        for iteration in range(1, args.optimization_iterations + 1):
            previous_observations = load_successful_results(ORIENTATION_RESULTS_CSV)
            previous_best = min((value for _, value in previous_observations), default=None)
            initial_design_phase = contour_mode and iteration <= sobol_end_iteration
            refinement_phase = contour_mode and iteration > sobol_end_iteration
            if initial_design_phase:
                candidate, diagnostics = next_sobol_orientation(
                    ORIENTATION_RESULTS_CSV,
                    sample_index=iteration - 1,
                    min_angle=args.optimization_min_angle,
                    max_angle=args.optimization_max_angle,
                    axis_max_angles=sobol_axis_max_angles,
                    symmetry_anchors=symmetry_anchors,
                )
            elif contour_mode:
                candidate, diagnostics = next_contour_orientation(
                    ORIENTATION_RESULTS_CSV,
                    min_angle=args.optimization_min_angle,
                    max_angle=args.optimization_max_angle,
                    contour_step=contour_step,
                    contour_starts=args.contour_starts,
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
                rot_z=0.0,
            )
            next_run_number += 1
            phase_name = (
                "flip anchor"
                if contour_mode and iteration <= flip_anchor_count
                else "Sobol"
                if initial_design_phase
                else "contour refinement"
                if refinement_phase
                else "Bayesian"
            )
            print(f"\n=== {phase_name} orientation {iteration}/{args.optimization_iterations} ===")
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
                material_config_file,
                process_config_file,
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
            if not refinement_phase:
                stalled_iterations = 0
                continue
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
                    iteration >= max(
                        args.minimum_optimization_iterations,
                        sobol_end_iteration + 1,
                    )
                    and stalled_iterations >= args.stop_patience
                ):
                    if contour_mode and contour_step > args.contour_min_step:
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

        run_completed_at = datetime.now(timezone.utc)
        total_runtime_seconds = time.perf_counter() - run_timer_start
        run_metadata = {
            "run_started_at_utc": run_started_at.isoformat(),
            "run_completed_at_utc": run_completed_at.isoformat(),
            "total_runtime_seconds": round(total_runtime_seconds, 3),
            "total_runtime": format_runtime(total_runtime_seconds),
            "part_file": str(part_file),
            "part_mesh_size_mm": part_mesh_size_mm,
            "base_mesh_size_mm": base_mesh_size_mm,
            "workflow": "Sobol initialization + multi-start contour refinement"
            if contour_mode
            else "Bayesian expected improvement",
            "maximum_evaluations": args.optimization_iterations,
            "solver_cores": 16,
            "material": {
                "id": material_config["id"],
                "display_name": material_config["display_name"],
                "ansys_part_material": material_config["ansys_part_material"],
                "ansys_base_material": material_config["ansys_base_material"],
                "config_path": str(material_config_file),
            },
        }
        write_run_manifest(
            optimization_points,
            part_file,
            part_mesh_size_mm,
            base_mesh_size_mm,
            args.dry_run,
            args.sobol_initial_runs if contour_mode else 0,
            symmetry_type if contour_mode else None,
            symmetry_axis if contour_mode else None,
            symmetry_repeats if contour_mode else 1,
            args.contour_starts if contour_mode else 0,
            run_metadata,
        )
        if not args.dry_run:
            write_post_run_outputs(run_metadata)
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
