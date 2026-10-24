"""SolidWorks document opening and activation helpers."""

from __future__ import annotations

import time
from pathlib import Path

import pythoncom
from win32com.client import VARIANT

from .config import SW_DOC_PART, SW_OPEN_SILENT, describe_file_load_errors


def get_active_model(sw):
    model = sw.ActiveDoc
    if model is None:
        raise RuntimeError("No active SolidWorks document.")
    return model


def get_model_path(model):
    try:
        path = model.GetPathName()
        return Path(path).resolve() if path else None
    except Exception:
        return None


def same_path(left: Path | None, right: Path):
    return left is not None and str(left).casefold() == str(right.resolve()).casefold()


def get_active_matching_document(sw, part_file: Path):
    model = sw.ActiveDoc
    if model is None:
        return None
    active_path = get_model_path(model)
    if same_path(active_path, part_file):
        return model
    if active_path is not None:
        print(f"Active SolidWorks document is not the requested part: {active_path}")
    return None


def activate_model(sw, model):
    try:
        title = model.GetTitle()
        errors = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
        activated = sw.ActivateDoc3(title, False, 0, errors)
        return activated if activated is not None else model
    except Exception:
        return model


def wait_for_any_active_document(sw, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            pythoncom.PumpWaitingMessages()
            model = sw.ActiveDoc
            if model is not None:
                return model
        except Exception:
            pass
        time.sleep(0.5)
    return None


def open_with_opendoc6(sw, part_file: Path):
    errors = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    warnings = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    model = sw.OpenDoc6(
        str(part_file), SW_DOC_PART, SW_OPEN_SILENT, "", errors, warnings
    )
    return model, errors.value, warnings.value


def open_part(sw, part_file: Path):
    """Open the requested part and wait until SolidWorks exposes an active doc."""
    if not part_file.exists():
        raise FileNotFoundError(f"Part file not found: {part_file}")

    model = get_active_matching_document(sw, part_file)
    errors = warnings = 0
    if model is not None:
        print(f"Using already-open part: {part_file}")
    else:
        opendoc6_exc = None
        for _ in range(30):
            try:
                model, errors, warnings = open_with_opendoc6(sw, part_file)
                print("Opened part with OpenDoc6.")
                break
            except Exception as exc:
                opendoc6_exc = exc
                pythoncom.PumpWaitingMessages()
                time.sleep(1)
        else:
            raise RuntimeError(
                "SolidWorks failed while opening the part after 30 seconds. "
                f"OpenDoc6 details: {opendoc6_exc!r}"
            ) from opendoc6_exc

    if model is None:
        raise RuntimeError(
            "Failed to open part. "
            f"errors={errors} ({describe_file_load_errors(errors)}), "
            f"warnings={warnings}"
        )

    model = activate_model(sw, model)
    print(f"Opened part: {part_file}")
    print(f"errors={errors}, warnings={warnings}")
    model = wait_for_any_active_document(sw, timeout=30)
    if model is None:
        raise RuntimeError("No active document appeared in time.")
    print("A document is active and ready.")
    return model


def rebuild_model(model):
    rebuild_result = model.EditRebuild3
    return rebuild_result() if callable(rebuild_result) else rebuild_result

