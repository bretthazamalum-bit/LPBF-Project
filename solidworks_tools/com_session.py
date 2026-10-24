"""SolidWorks COM session lifecycle."""

from __future__ import annotations

import time

import pythoncom
import win32com.client

from .config import SOLIDWORKS_STARTUP_TIMEOUT_SECONDS


def make_solidworks_visible(sw):
    try:
        sw.Visible = True
    except Exception as exc:
        print(f"Could not set SolidWorks visibility; continuing. Details: {exc}")
    try:
        sw.FrameState = 1
    except Exception as exc:
        print(f"Could not set SolidWorks window state; continuing. Details: {exc}")


def initialize_com():
    try:
        pythoncom.CoInitialize()
        return True
    except pythoncom.com_error as exc:
        if getattr(exc, "hresult", None) != -2147417850:  # RPC_E_CHANGED_MODE
            raise
        return False


def uninitialize_com(initialized):
    if initialized:
        pythoncom.CoUninitialize()


def get_sw():
    """Attach to or start SolidWorks while keeping one COM session per run."""
    last_errors = []
    launchers = (
        ("Dispatch", win32com.client.Dispatch),
        ("DispatchEx", win32com.client.DispatchEx),
    )
    launcher_index = 0
    deadline = time.time() + SOLIDWORKS_STARTUP_TIMEOUT_SECONDS

    while time.time() < deadline:
        try:
            sw = win32com.client.GetActiveObject("SldWorks.Application")
            print("Attached to existing SolidWorks instance.")
            make_solidworks_visible(sw)
            return sw
        except Exception as exc:
            last_errors.append(f"attach: {exc}")

        if launcher_index < len(launchers):
            launcher_name, launcher = launchers[launcher_index]
            launcher_index += 1
            try:
                sw = launcher("SldWorks.Application")
                print(f"Started new SolidWorks instance with {launcher_name}.")
                make_solidworks_visible(sw)
                return sw
            except Exception as exc:
                last_errors.append(f"{launcher_name}: {exc}")

        pythoncom.PumpWaitingMessages()
        time.sleep(1)

    raise RuntimeError(
        "SolidWorks did not become available through COM within "
        f"{SOLIDWORKS_STARTUP_TIMEOUT_SECONDS} seconds. "
        "Complete any first-start, activation, license, login, or recovery "
        "dialog and run the workflow again. Recent COM errors: "
        + "; ".join(last_errors[-4:])
    )


def close_solidworks(sw):
    # Discard unsaved Move/Copy Body features so the template remains clean.
    sw.CloseAllDocuments(True)
    sw.ExitApp()

