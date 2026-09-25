"""Launch a visible local Ansys Mechanical instance through PyMechanical."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from ansys.mechanical.core import launch_mechanical


def find_executable() -> Path:
    configured = os.environ.get("ANSYS_MECHANICAL_EXECUTABLE")
    if configured:
        executable = Path(configured).expanduser().resolve()
    else:
        ansys_root = Path(
            os.environ.get("AWP_ROOT261", r"D:\Program Files\ANSYS Inc\v261")
        )
        if ansys_root.name.casefold() == "ansys":
            ansys_root = ansys_root.parent
        executable = ansys_root / "aisol" / "bin" / "winx64" / "AnsysWBU.exe"
    if not executable.is_file():
        raise FileNotFoundError(f"Mechanical executable not found: {executable}")
    return executable


def main() -> None:
    executable = find_executable()
    print(f"Python: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")
    for name in sorted(os.environ):
        if any(key in name for key in ("ANSYS", "AWP", "PYMECHANICAL")):
            print(f"{name}={os.environ[name]}")
    print(f"Launching Mechanical 2026 R1: {executable}")
    mechanical = launch_mechanical(
        exec_file=str(executable),
        version=261,
        batch=False,
        cleanup_on_exit=False,
    )
    print(mechanical)
    input("Mechanical is running. Press Enter to close it... ")
    mechanical.exit(force=True)


if __name__ == "__main__":
    main()
