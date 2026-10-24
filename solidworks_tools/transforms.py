"""Body rotations and translations."""

from __future__ import annotations

import math

from .bodies import find_body, get_body_center_of_mass, select_body
from .documents import rebuild_model


def deg_to_rad(deg):
    return deg * math.pi / 180.0


def rotate_body(model, body_name, rot_x_deg, rot_y_deg, rot_z_deg):
    # The COM is read before creating Move/Copy Body so the rotation does not
    # translate the part away from its own physical center.
    body = find_body(model, body_name)
    center = get_body_center_of_mass(model, body, body_name)
    feature = model.FeatureManager.InsertMoveCopyBody2(
        0.0, 0.0, 0.0, 0.0,
        center[0], center[1], center[2],
        deg_to_rad(rot_x_deg), deg_to_rad(rot_y_deg), deg_to_rad(rot_z_deg),
        False, 1,
    )
    model.ClearSelection2(True)
    if feature is None:
        raise RuntimeError("InsertMoveCopyBody2 rotation failed.")
    rebuild_ok = rebuild_model(model)
    print("Move/Copy Body rotation feature created.")
    print(f"Body: {body_name}; RotX={rot_x_deg}; RotY={rot_y_deg}; RotZ={rot_z_deg} deg")
    print(f"Rebuild result: {rebuild_ok}")


def move_body_xyz(model, body, body_name, x_m, y_m, z_m):
    # Re-select the body for every feature: SolidWorks may refresh COM body
    # references after a preceding Move/Copy Body operation.
    select_body(model, body, body_name)
    feature = model.FeatureManager.InsertMoveCopyBody2(
        x_m, y_m, z_m, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 1
    )
    model.ClearSelection2(True)
    if feature is None:
        raise RuntimeError(f"Move/Copy Body translation failed for '{body_name}'.")
    rebuild_model(model)


def move_body_z(model, body, body_name, step_m):
    move_body_xyz(model, body, body_name, 0.0, 0.0, step_m)

