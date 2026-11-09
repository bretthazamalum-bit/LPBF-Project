"""Run multiple LPBF cases from a CSV manifest.

Each CSV row is executed sequentially through the existing main.py workflow.
The output folder is derived from the row's run name, material, and mesh sizes
so cases using the same part at different mesh sizes cannot overwrite one
another.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
MAIN_SCRIPT = PROJECT_ROOT / "main.py"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / "runs"
DEFAULT_OPTIMIZER_CONFIG = PROJECT_ROOT / "optimizer_settings.csv"
REQUIRED_COLUMNS = {
    "run_name",
    "part_file",
    "material",
    "part_mesh_size_mm",
    "base_mesh_size_mm",
    "optimization_iterations",
}
VALID_MATERIALS = {"inconel_718", "316l_stainless_steel", "ti_6al_4v"}


def safe_component(value: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", str(value).strip())
    return text.strip("._-") or "run"


def numeric_component(value: str) -> str:
    number = float(value)
    if number <= 0:
        raise ValueError(f"Mesh size must be positive: {value}")
    return f"{number:g}".replace("-", "neg").replace(".", "p") + "mm"


def output_folder(row: dict[str, str], output_root: Path) -> Path:
    part_stem = Path(row["part_file"]).stem
    folder_name = "_".join(
        (
            safe_component(row["run_name"]),
            safe_component(part_stem),
            safe_component(row["material"]),
            numeric_component(row["part_mesh_size_mm"]),
            numeric_component(row["base_mesh_size_mm"]),
        )
    )
    return output_root / folder_name


def choose_csv_file() -> Path:
    """Show a Windows file picker for the batch CSV manifest."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as error:
        raise RuntimeError(
            "The CSV picker requires tkinter. Use --csv from a command line instead."
        ) from error

    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    try:
        selected_file = filedialog.askopenfilename(
            title="Select LPBF batch CSV",
            initialdir=str(PROJECT_ROOT),
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*"),
            ],
        )
    finally:
        root.destroy()

    if not selected_file:
        raise SystemExit("No batch CSV selected; exiting without a run.")
    return Path(selected_file).resolve()


def build_command(
    row: dict[str, str],
    output_dir: Path,
    *,
    dry_run: bool,
    optimizer_config: Path | None,
) -> list[str]:
    part_file = Path(row["part_file"]).expanduser()
    if not part_file.is_absolute():
        part_file = PROJECT_ROOT / part_file
    command = [
        sys.executable,
        str(MAIN_SCRIPT),
        "--part-file",
        str(part_file.resolve()),
        "--material",
        row["material"].strip(),
        "--part-mesh-size-mm",
        str(float(row["part_mesh_size_mm"])),
        "--base-mesh-size-mm",
        str(float(row["base_mesh_size_mm"])),
        "--optimization-iterations",
        str(int(row["optimization_iterations"])),
        "--output-dir",
        str(output_dir.resolve()),
    ]
    if optimizer_config is not None:
        command.extend(("--optimizer-config", str(optimizer_config.resolve())))
    if dry_run:
        command.append("--dry-run")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run LPBF cases from a CSV manifest.")
    parser.add_argument(
        "--csv",
        type=Path,
        help="Batch CSV manifest; if omitted, show a file-selection popup.",
    )
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument(
        "--optimizer-config",
        type=Path,
        default=DEFAULT_OPTIMIZER_CONFIG,
        help="Separate one-row CSV with Sobol/contour settings.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print/run main.py in dry-run mode.")
    parser.add_argument("--continue-on-error", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    csv_path = (args.csv or choose_csv_file()).expanduser()
    if not csv_path.is_absolute():
        csv_path = PROJECT_ROOT / csv_path
    csv_path = csv_path.resolve()
    if not csv_path.is_file():
        raise FileNotFoundError(f"Batch CSV not found: {csv_path}")

    output_root = args.output_root.expanduser()
    if not output_root.is_absolute():
        output_root = PROJECT_ROOT / output_root
    output_root = output_root.resolve()

    optimizer_config = args.optimizer_config.expanduser() if args.optimizer_config else None
    if optimizer_config is not None:
        if not optimizer_config.is_absolute():
            optimizer_config = PROJECT_ROOT / optimizer_config
        optimizer_config = optimizer_config.resolve()
        if not optimizer_config.is_file():
            raise FileNotFoundError(f"Optimizer configuration not found: {optimizer_config}")

    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            raise ValueError(f"Batch CSV is missing columns: {', '.join(sorted(missing))}")
        rows = list(reader)

    if not rows:
        raise ValueError(f"Batch CSV has no data rows: {csv_path}")

    failures = 0
    for index, row in enumerate(rows, start=1):
        material = row["material"].strip()
        if material not in VALID_MATERIALS:
            raise ValueError(f"Unsupported material on row {index}: {material}")
        output_dir = output_folder(row, output_root)
        command = build_command(
            row,
            output_dir,
            dry_run=args.dry_run,
            optimizer_config=optimizer_config,
        )
        print(f"\n=== Batch case {index}/{len(rows)}: {row['run_name']} ===")
        print(f"Output folder: {output_dir}")
        print("Command: " + " ".join(command))
        try:
            subprocess.run(command, cwd=str(PROJECT_ROOT), check=True)
        except subprocess.CalledProcessError as error:
            failures += 1
            print(f"Case failed with exit code {error.returncode}: {row['run_name']}")
            if not args.continue_on_error:
                raise

    print(f"\nBatch complete: {len(rows) - failures} succeeded, {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
