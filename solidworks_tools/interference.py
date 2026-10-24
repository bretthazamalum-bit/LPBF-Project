"""Optional exact and fallback SolidWorks interference diagnostics."""

from __future__ import annotations

from dataclasses import dataclass

import pythoncom
from win32com.client import VARIANT

from .bodies import body_box


@dataclass(frozen=True)
class CollisionState:
    collided: bool
    method: str
    detail: str


def boxes_overlap(box_a, box_b, tolerance_m):
    ax0, ay0, az0, ax1, ay1, az1 = box_a
    bx0, by0, bz0, bx1, by1, bz1 = box_b
    return (
        ax0 < bx1 - tolerance_m and ax1 > bx0 + tolerance_m
        and ay0 < by1 - tolerance_m and ay1 > by0 + tolerance_m
        and az0 < bz1 - tolerance_m and az1 > bz0 + tolerance_m
    )


def bbox_collision(part_body, base_body, tolerance_m):
    part = body_box(part_body)
    base = body_box(base_body)
    return CollisionState(
        boxes_overlap(part, base, tolerance_m),
        "bounding-box",
        f"part_box={part}, base_box={base}",
    )


def exact_collision(sw, part_body, base_body):
    modeler = sw.GetModeler()
    faces_1 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
    faces_2 = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
    intersected = VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
    result = modeler.CheckInterferenceBetweenTwoBodies(
        part_body, base_body, False, faces_1, faces_2, intersected
    )
    collided = bool(result[0]) if isinstance(result, tuple) and result else bool(result)
    return CollisionState(collided, "exact-body-interference", f"interference_result={result}")


def check_collision(sw, part_body, base_body, tolerance_m):
    try:
        return exact_collision(sw, part_body, base_body)
    except Exception as exc:
        fallback = bbox_collision(part_body, base_body, tolerance_m)
        return CollisionState(
            fallback.collided,
            "bounding-box fallback",
            f"exact check failed: {exc!r}; {fallback.detail}",
        )

