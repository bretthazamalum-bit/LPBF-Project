from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
ANSYS_DIR = PROJECT_ROOT / "ANSYS"
STEP_OUTPUT_DIR = PROJECT_ROOT / "generated_steps"
RESULTS_DIR = PROJECT_ROOT / "results"


ANGLE_PATTERN = re.compile(
    r"_Rx(?P<rot_x>(?:neg)?\d+(?:p\d+)?)_"
    r"Ry(?P<rot_y>(?:neg)?\d+(?:p\d+)?)_"
    r"Rz(?P<rot_z>(?:neg)?\d+(?:p\d+)?)$"
)


def parse_angle(text: str) -> float:
    return float(text.replace("neg", "-").replace("p", "."))


def rotation_from_step_name(step_file: Path) -> tuple[float, float, float]:
    match = ANGLE_PATTERN.search(step_file.stem)
    if match is None:
        return 0.0, 0.0, 0.0

    return (
        parse_angle(match.group("rot_x")),
        parse_angle(match.group("rot_y")),
        parse_angle(match.group("rot_z")),
    )


def list_step_files() -> list[Path]:
    if not STEP_OUTPUT_DIR.exists():
        return []

    return sorted(
        STEP_OUTPUT_DIR.glob("*.step"),
        key=lambda step_file: step_file.stat().st_mtime,
    )


def prompt_step_file() -> Path | None:
    step_files = list_step_files()

    print("\nAvailable STEP files:")
    if step_files:
        for index, step_file in enumerate(step_files, start=1):
            print(f"  {index}. {step_file.name}")
    else:
        print(f"  No .step files found in {STEP_OUTPUT_DIR}")

    print("\nEnter a number, paste a STEP path, or press Enter to cancel.")

    while True:
        choice = input("STEP file: ").strip().strip('"')
        if not choice:
            return None

        if choice.isdigit():
            selected_index = int(choice)
            if 1 <= selected_index <= len(step_files):
                return step_files[selected_index - 1]

            print(f"Choose a number from 1 to {len(step_files)}.")
            continue

        selected_file = Path(choice)
        if not selected_file.is_absolute():
            selected_file = (PROJECT_ROOT / selected_file).resolve()

        if selected_file.exists() and selected_file.suffix.lower() in {".step", ".stp"}:
            return selected_file

        print(f"Not a STEP file: {selected_file}")


def prompt_text(label: str, default: str) -> str:
    value = input(f"{label} [{default}]: ").strip()
    return value or default


def prompt_yes_no(label: str, default: bool) -> bool:
    default_text = "Y/n" if default else "y/N"

    while True:
        value = input(f"{label} [{default_text}]: ").strip().lower()
        if not value:
            return default
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please enter y or n.")


def safe_file_stem(text: str) -> str:
    safe_text = "".join(char if char.isalnum() or char in "-_" else "_" for char in text)
    return safe_text.strip("_") or "debug_run"


def run_ansys_debug(step_file: Path, run_id: str, pause_before_close: bool) -> None:
    rot_x, rot_y, rot_z = rotation_from_step_name(step_file)
    result_file = RESULTS_DIR / f"{safe_file_stem(run_id)}_results.json"

    command = [
        sys.executable,
        "run_lpbf_simulation.py",
        "--step-file",
        str(step_file),
        "--run-id",
        run_id,
        "--rot-x",
        str(rot_x),
        "--rot-y",
        str(rot_y),
        "--rot-z",
        str(rot_z),
        "--result-file",
        str(result_file),
    ]

    if pause_before_close:
        command.append("--pause-before-close")

    print(f"\nWorking folder: {ANSYS_DIR}")
    print("Command:")
    print(" ".join(command))
    print()

    subprocess.run(command, cwd=str(ANSYS_DIR), check=True)


def main() -> int:
    step_file = prompt_step_file()
    if step_file is None:
        print("Canceled.")
        return 0

    default_run_id = f"debug_{step_file.stem}"
    run_id = prompt_text("Run ID", default_run_id)
    pause_before_close = prompt_yes_no("Pause before closing Mechanical", True)

    run_ansys_debug(step_file.resolve(), run_id, pause_before_close)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
