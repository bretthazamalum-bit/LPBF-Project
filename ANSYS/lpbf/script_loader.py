from __future__ import annotations

"""Load embedded Mechanical scripts and substitute per-run parameters."""

from pathlib import Path

from .config import ANSYS_DIR


MECHANICAL_SCRIPTS_DIR = ANSYS_DIR / "mechanical_scripts"


def load_mechanical_script(script_name: str, replacements=None) -> str:
    script_path = MECHANICAL_SCRIPTS_DIR / script_name
    if not script_path.is_file():
        raise FileNotFoundError(f"Mechanical script not found: {script_path}")
    script = script_path.read_text(encoding="utf-8")
    for token, value in (replacements or {}).items():
        script = script.replace(token, value)
    return script


DELETE_GEOMETRY_SCRIPT = load_mechanical_script("delete_geometry.py")
SOLVE_SCRIPT = load_mechanical_script("solve_analyses.py")
RESULTS_SCRIPT = load_mechanical_script("collect_results.py")


def import_geometry_script(step_file: Path) -> str:
    return load_mechanical_script(
        "import_geometry.py",
        {"__GEOMETRY_FILE__": repr(str(step_file))},
    )


def mesh_script(part_mesh_size_mm: float, base_mesh_size_mm: float) -> str:
    return load_mechanical_script(
        "mesh_geometry.py",
        {
            "__PART_MESH_SIZE__": f"{part_mesh_size_mm:.12g}",
            "__BASE_MESH_SIZE__": f"{base_mesh_size_mm:.12g}",
        },
    )
