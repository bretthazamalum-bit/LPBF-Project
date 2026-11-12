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


def solve_script(process_settings: dict) -> str:
    """Load the solve stage with values from process_settings.csv."""
    replacements = {
        "__SOLVER_CORES__": str(process_settings["solver_cores"]),
        "__DEPOSITION_THICKNESS__": f'{process_settings["deposition_thickness_mm"]:.12g}',
        "__HATCH_SPACING__": f'{process_settings["hatch_spacing_mm"]:.12g}',
        "__SCAN_SPEED__": f'{process_settings["scan_speed_mm_s"]:.12g}',
        "__DWELL_TIME__": f'{process_settings["dwell_time_s"]:.12g}',
        "__PREHEAT_TEMPERATURE__": f'{process_settings["preheat_temperature_c"]:.12g}',
        "__ROOM_TEMPERATURE__": f'{process_settings["room_temperature_c"]:.12g}',
        "__BUILD_GAS_TEMPERATURE__": f'{process_settings["build_gas_temperature_c"]:.12g}',
        "__BUILD_POWDER_TEMPERATURE__": f'{process_settings["build_powder_temperature_c"]:.12g}',
        "__COOLDOWN_GAS_TEMPERATURE__": f'{process_settings["cooldown_gas_temperature_c"]:.12g}',
        "__COOLDOWN_POWDER_TEMPERATURE__": f'{process_settings["cooldown_powder_temperature_c"]:.12g}',
        "__BASE_TEMPERATURE__": f'{process_settings["base_temperature_c"]:.12g}',
        "__LAYER_ROTATION_ANGLE__": f'{process_settings["layer_rotation_angle_deg"]:.12g}',
        "__START_LAYER_ANGLE__": f'{process_settings["start_layer_angle_deg"]:.12g}',
        "__SCAN_STRIPE_WIDTH__": f'{process_settings["scan_stripe_width_mm"]:.12g}',
        "__BEAM_POWER__": f'{process_settings["beam_power_w"]:.12g}',
        "__BEAM_DIAMETER__": f'{process_settings["beam_diameter_mm"]:.12g}',
        "__ABSORPTIVITY__": f'{process_settings["absorptivity"]:.12g}',
        "__NUMBER_OF_HEAT_SOURCES__": str(process_settings["number_of_heat_sources"]),
    }
    return load_mechanical_script("solve_analyses.py", replacements)


def import_geometry_script(step_file: Path) -> str:
    return load_mechanical_script(
        "import_geometry.py",
        {"__GEOMETRY_FILE__": repr(str(step_file))},
    )


def mesh_script(
    part_mesh_size_mm: float,
    base_mesh_size_mm: float,
    part_material: str = "Inconel 718",
    base_material: str = "Inconel 718",
) -> str:
    return load_mechanical_script(
        "mesh_geometry.py",
        {
            "__PART_MESH_SIZE__": f"{part_mesh_size_mm:.12g}",
            "__BASE_MESH_SIZE__": f"{base_mesh_size_mm:.12g}",
            "__PART_MATERIAL__": repr(part_material),
            "__BASE_MATERIAL__": repr(base_material),
        },
    )
