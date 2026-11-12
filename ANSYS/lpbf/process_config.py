"""Load the editable ANSYS LPBF process settings CSV."""

from __future__ import annotations

import csv
from pathlib import Path

from .config import ANSYS_DIR


PROJECT_ROOT = ANSYS_DIR.parent
DEFAULT_PROCESS_CONFIG = PROJECT_ROOT / "process_settings.csv"

_FLOAT_FIELDS = {
    "deposition_thickness_mm", "hatch_spacing_mm", "scan_speed_mm_s",
    "dwell_time_s", "preheat_temperature_c", "room_temperature_c",
    "build_gas_temperature_c", "build_powder_temperature_c",
    "cooldown_gas_temperature_c", "cooldown_powder_temperature_c",
    "base_temperature_c", "layer_rotation_angle_deg", "start_layer_angle_deg",
    "scan_stripe_width_mm", "beam_power_w", "beam_diameter_mm", "absorptivity",
}
_INT_FIELDS = {"solver_cores", "number_of_heat_sources"}


def load_process_config(config_path: str | Path | None = None) -> dict:
    path = Path(config_path) if config_path else DEFAULT_PROCESS_CONFIG
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path = path.resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Process settings CSV not found: {path}")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 1:
        raise ValueError(f"Process settings CSV must contain exactly one data row: {path}")
    row = rows[0]
    required = _FLOAT_FIELDS | _INT_FIELDS
    missing = sorted(field for field in required if not row.get(field, "").strip())
    if missing:
        raise ValueError(f"Process settings CSV is missing values: {', '.join(missing)}")
    settings = {"config_name": row.get("config_name", "default").strip(), "config_path": str(path)}
    for field in _FLOAT_FIELDS:
        settings[field] = float(row[field])
    for field in _INT_FIELDS:
        settings[field] = int(row[field])
    if not 0.0 < settings["absorptivity"] <= 1.0:
        raise ValueError("absorptivity must be greater than 0 and no greater than 1")
    if settings["solver_cores"] <= 0 or settings["number_of_heat_sources"] <= 0:
        raise ValueError("solver_cores and number_of_heat_sources must be positive")
    return settings
