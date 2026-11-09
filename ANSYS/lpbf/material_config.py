"""Load and validate the selectable ANSYS material configurations."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MATERIALS_DIR = PROJECT_ROOT / "materials"
DEFAULT_MATERIAL_ID = "inconel_718"


def available_material_ids() -> list[str]:
    return sorted(path.stem for path in MATERIALS_DIR.glob("*.json"))


def load_material_config(config_path: str | Path | None = None) -> dict:
    if config_path:
        candidate = Path(config_path).expanduser()
        path = (
            MATERIALS_DIR / f"{candidate}.json"
            if candidate.suffix == "" and len(candidate.parts) == 1
            else candidate.resolve()
        )
    else:
        path = MATERIALS_DIR / f"{DEFAULT_MATERIAL_ID}.json"
    if not path.is_file():
        raise FileNotFoundError(f"Material configuration not found: {path}")
    config = json.loads(path.read_text(encoding="utf-8"))
    required = ("id", "display_name", "ansys_part_material", "ansys_base_material")
    missing = [key for key in required if not config.get(key)]
    if missing:
        raise ValueError(f"Material configuration is missing: {', '.join(missing)}")
    config["config_path"] = str(path)
    return config
