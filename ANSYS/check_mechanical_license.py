"""Small GUI-first PyMechanical licensing and template-open diagnostic.

This intentionally does not modify the LPBF model. It launches the visible
Mechanical desktop, proves that the remote session accepts a script, and only
then optionally opens a template copy. Use ``--keep-open`` when inspecting the
GUI or its licensing messages.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import time
from pathlib import Path

from ansys.mechanical.core import launch_mechanical


DEFAULT_TEMPLATE = Path(__file__).resolve().parent / "lpbfsim.mechdb"


def find_mechanical_executable() -> Path:
    configured = os.environ.get("ANSYS_MECHANICAL_EXECUTABLE")
    if configured:
        executable = Path(configured).expanduser().resolve()
        if not executable.is_file():
            raise FileNotFoundError(
                f"ANSYS_MECHANICAL_EXECUTABLE is not a file: {executable}"
            )
        return executable

    # A local installation may be on a different drive than ``ProgramFiles``.
    # AWP_ROOT### is set by Ansys for each installed release and is the most
    # reliable way to find the matching installation on this machine.
    candidates = []
    for environment_name, environment_value in os.environ.items():
        if not environment_name.startswith("AWP_ROOT") or not environment_value:
            continue
        ansys_root = Path(environment_value).expanduser()
        if ansys_root.name.casefold() == "ansys":
            ansys_root = ansys_root.parent
        candidates.append(ansys_root / "aisol" / "bin" / "winx64" / "AnsysWBU.exe")

    install_root = Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
    candidates.extend(install_root.glob(r"ANSYS Inc\v*\aisol\bin\winx64\AnsysWBU.exe"))
    candidates = sorted(
        {candidate.resolve() for candidate in candidates if candidate.is_file()},
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError(
            "Mechanical executable not found. Set "
            "ANSYS_MECHANICAL_EXECUTABLE to AnsysWBU.exe."
        )
    return candidates[0]


def mechanical_version(executable: Path) -> int:
    for parent in executable.parents:
        if parent.name.startswith("v") and parent.name[1:].isdigit():
            return int(parent.name[1:])
    raise ValueError(f"Could not determine Mechanical version from {executable}")


def prepare_template(template: Path, use_original: bool) -> Path:
    if not template.is_file():
        raise FileNotFoundError(f"Template not found: {template}")

    if use_original:
        return template

    check_copy = template.with_name(f"{template.stem}_license_check.mechdb")
    shutil.copy2(template, check_copy)
    return check_copy


def run_script(session, script: str):
    """Use the public remote-session API exposed by PyMechanical."""
    method = getattr(session, "run_python_script", None)
    if not callable(method):
        raise RuntimeError("PyMechanical session has no run_python_script() method")
    return method(script)


def close_session(session) -> None:
    for method_name, kwargs in (("exit", {"force": True}), ("close", {})):
        method = getattr(session, method_name, None)
        if not callable(method):
            continue
        try:
            method(**kwargs)
            return
        except TypeError:
            try:
                method()
                return
            except Exception:
                pass
        except Exception:
            pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Launch visible Mechanical first and test its PyMechanical license session."
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help="Optional Mechanical database to open after the GUI session is ready.",
    )
    parser.add_argument(
        "--open-template",
        action="store_true",
        help="Open --template only after the visible Mechanical session responds.",
    )
    parser.add_argument(
        "--use-original",
        action="store_true",
        help="Open --template directly instead of using a disposable copy; never save it.",
    )
    parser.add_argument(
        "--wait-seconds",
        type=float,
        default=3.0,
        help="Seconds to leave the GUI visible before the probe (default: 3).",
    )
    parser.add_argument(
        "--keep-open",
        action="store_true",
        help="Keep Mechanical open when the diagnostic finishes (default).",
    )
    parser.add_argument(
        "--close",
        dest="keep_open",
        action="store_false",
        help="Close Mechanical automatically when the diagnostic finishes.",
    )
    parser.set_defaults(keep_open=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    executable = find_mechanical_executable()
    version = mechanical_version(executable)
    template = args.template.expanduser().resolve()
    open_path = prepare_template(template, args.use_original) if args.open_template else None

    print(f"Mechanical executable: {executable}")
    print(f"Mechanical version: {version}")
    print("Shared Web licensing is delegated to the local Ansys Licensing Settings client.")

    # Use the same direct PyMechanical GUI launch path as launch_mechanical_gui.py.
    session = launch_mechanical(
        exec_file=str(executable),
        version=version,
        batch=False,
        cleanup_on_exit=False,
    )

    try:
        time.sleep(max(0.0, args.wait_seconds))
        print("Mechanical GUI launched; sending license/session probe...")
        probe_result = run_script(
            session,
            "str(getattr(ExtAPI.DataModel.Project, 'IsReadOnly', 'UNAVAILABLE'))",
        )
        print("License/session probe accepted by Mechanical.")
        print(f"Initial Project.IsReadOnly response: {probe_result!r}")

        if open_path is not None:
            if args.use_original:
                print(f"Opening original template through Mechanical scripting: {open_path}")
            else:
                print(f"Opening disposable template copy through Mechanical scripting: {open_path}")
            open_result = run_script(
                session,
                f"ExtAPI.DataModel.Project.Open({json.dumps(str(open_path))})",
            )
            print("Template-open command accepted by Mechanical.")
            readonly_result = run_script(session, "str(getattr(ExtAPI.DataModel.Project, 'IsReadOnly', 'UNAVAILABLE'))")
            print(f"Project.IsReadOnly after template open: {readonly_result!r}")
            if args.use_original:
                print("Original template opened without a save attempt.")
            else:
                try:
                    save_result = run_script(session, "ExtAPI.DataModel.Project.Save()")
                    print(f"Project.Save() accepted: {save_result!r}")
                    print("WRITE_TEST=PASS (Mechanical accepted a save on the disposable copy)")
                except Exception as error:
                    print(f"Project.Save() failed: {error}")
                    print("WRITE_TEST=FAIL (Mechanical did not accept a save)")
            print(f"Template-open response: {open_result!r}")

        if args.keep_open:
            input("Mechanical is still open. Press Enter to close it... ")
    finally:
        if not args.keep_open:
            close_session(session)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
