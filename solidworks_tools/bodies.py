"""SolidWorks body lookup, selection, mass properties, and bounds."""

from __future__ import annotations

import pythoncom
from win32com.client import VARIANT


def get_bodies(model):
    bodies = model.GetBodies2(0, False)
    if not bodies:
        raise RuntimeError("No solid bodies found.")
    return bodies


def find_body(model, body_name):
    """Resolve a body by its stable internal name (normally part or base)."""
    bodies = get_bodies(model)
    for body in bodies:
        try:
            if body.Name == body_name:
                return body
        except Exception:
            pass
    names = []
    for body in bodies:
        try:
            names.append(body.Name)
        except Exception:
            names.append("<unnamed>")
    raise RuntimeError(f"Body '{body_name}' not found. Bodies present: {names}")


def select_body(model, body, body_name):
    model.ClearSelection2(True)
    if not body.Select(False, 1):
        raise RuntimeError(f"Failed to select body '{body_name}'.")


def get_body_center_of_mass(model, body, body_name):
    select_body(model, body, body_name)
    errors = []
    try:
        status = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
        values = model.Extension.GetMassProperties2(1, status, True)
    except Exception as exc:
        errors.append(f"GetMassProperties2: {exc}")
        try:
            status = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
            values = model.Extension.GetMassProperties(1, status)
        except Exception as exc:
            errors.append(f"GetMassProperties: {exc}")
            raise RuntimeError(
                f"Could not read center of mass for body '{body_name}'. "
                + " | ".join(errors)
            ) from exc

    if isinstance(values, tuple) and len(values) == 2:
        candidate = values[0]
        if hasattr(candidate, "__len__") and len(candidate) >= 3:
            values = candidate
    if values is None or len(values) < 3:
        raise RuntimeError(f"Invalid mass properties for '{body_name}': {values!r}")

    center = tuple(float(values[index]) for index in range(3))
    print(
        f"Rotation center for '{body_name}' (center of mass): "
        f"X={center[0]:g}, Y={center[1]:g}, Z={center[2]:g} m"
    )
    return center


def body_box(body):
    """Return SolidWorks' axis-aligned box in metres: min XYZ, then max XYZ."""
    box = body.GetBodyBox()
    if box is None or len(box) != 6:
        raise RuntimeError(f"Could not read bounding box for body '{body.Name}'.")
    return tuple(float(value) for value in box)

