"""Mechanical executable discovery and PyMechanical session helpers."""

from __future__ import annotations

import os
import subprocess
import time
from pathlib import Path

from ansys.mechanical.core import launch_mechanical


def close_open_ansys_guis() -> None:
    """Release seats held by already-open Ansys GUI processes."""
    if os.name != "nt":
        return
    for image_name in ("AnsysWBU.exe", "RunWB2.exe"):
        subprocess.run(
            ["taskkill", "/F", "/T", "/IM", image_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    time.sleep(2)


def find_mechanical_executable() -> Path:
    configured_path = os.environ.get("ANSYS_MECHANICAL_EXECUTABLE")
    if configured_path:
        executable = Path(configured_path).expanduser().resolve()
        if not executable.is_file():
            raise FileNotFoundError(
                "ANSYS_MECHANICAL_EXECUTABLE does not point to a file: "
                f"{executable}"
            )
        return executable

    candidates = []
    for environment_name, environment_value in os.environ.items():
        if not environment_name.startswith("AWP_ROOT") or not environment_value:
            continue
        ansys_root = Path(environment_value).expanduser()
        if ansys_root.name.casefold() == "ansys":
            ansys_root = ansys_root.parent
        candidates.append(ansys_root / "aisol" / "bin" / "winx64" / "AnsysWBU.exe")

    install_root = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "ANSYS Inc"
    candidates.extend(install_root.glob(r"v*\aisol\bin\winx64\AnsysWBU.exe"))
    candidates = sorted(
        {candidate.resolve() for candidate in candidates if candidate.is_file()},
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError(
            "Could not find Ansys Mechanical. Set ANSYS_MECHANICAL_EXECUTABLE "
            "to the full path of AnsysWBU.exe."
        )
    return candidates[0]


def mechanical_version_from_executable(executable: Path) -> int:
    for parent in executable.parents:
        if parent.name.startswith("v") and parent.name[1:].isdigit():
            return int(parent.name[1:])
    raise ValueError(f"Could not determine Ansys version from: {executable}")


MECHANICAL_EXECUTABLE = find_mechanical_executable()
MECHANICAL_VERSION = mechanical_version_from_executable(MECHANICAL_EXECUTABLE)
