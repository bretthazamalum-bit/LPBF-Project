"""Deterministic post-rotation placement for LPBF export."""

from __future__ import annotations

from .bodies import body_box, find_body
from .config import M_PER_MM
from .transforms import move_body_xyz, move_body_z


def _closest_translation(low_m, high_m):
    if low_m > high_m:
        raise ValueError("No translation can satisfy the requested bounds.")
    if low_m <= 0.0 <= high_m:
        return 0.0
    return low_m if low_m > 0.0 else high_m


def ensure_xy_containment(model, part_name, base_name, margin_mm):
    """Translate the rotated part into the base XY bounding box."""
    # Each axis produces an allowed translation interval. Choosing the value
    # nearest zero preserves the original placement whenever it already fits.
    if margin_mm < 0:
        raise ValueError("Plate margin must be zero or greater.")
    part_box = body_box(find_body(model, part_name))
    base_box = body_box(find_body(model, base_name))
    margin_m = margin_mm * M_PER_MM
    x_low = base_box[0] + margin_m - part_box[0]
    x_high = base_box[3] - margin_m - part_box[3]
    y_low = base_box[1] + margin_m - part_box[1]
    y_high = base_box[4] - margin_m - part_box[4]
    if x_low > x_high or y_low > y_high:
        raise RuntimeError(
            "Rotated part cannot fit within build plate XY bounds: "
            f"part_box={part_box}, base_box={base_box}, margin={margin_mm:g} mm"
        )

    shift_x = _closest_translation(x_low, x_high)
    shift_y = _closest_translation(y_low, y_high)
    print(
        "XY containment: "
        f"required_shift=({shift_x / M_PER_MM:g}, {shift_y / M_PER_MM:g}) mm"
    )
    if shift_x != 0.0 or shift_y != 0.0:
        move_body_xyz(model, find_body(model, part_name), part_name, shift_x, shift_y, 0.0)

    final_box = body_box(find_body(model, part_name))
    tolerance_m = 1e-9
    if (
        final_box[0] < base_box[0] + margin_m - tolerance_m
        or final_box[3] > base_box[3] - margin_m + tolerance_m
        or final_box[1] < base_box[1] + margin_m - tolerance_m
        or final_box[4] > base_box[4] - margin_m + tolerance_m
    ):
        raise RuntimeError(
            "Could not place rotated part within build plate XY bounds: "
            f"final_part_box={final_box}, base_box={base_box}"
        )
    print(f"Verified XY containment: part_box={final_box}")
    return shift_x, shift_y


def ensure_support_gap(model, part_name, base_name, gap_mm):
    """Lift the part until its lowest point is gap_mm above the base."""
    # This is a single bounding-box correction, not a long sequence of small
    # interference moves; it handles upside-down orientations efficiently.
    if gap_mm < 0:
        raise ValueError("Support lift must be zero or greater.")
    part_box = body_box(find_body(model, part_name))
    base_box = body_box(find_body(model, base_name))
    target_z = base_box[5] + gap_mm * M_PER_MM
    required_lift = max(0.0, target_z - part_box[2])
    print(
        "Post-rotation Z placement: "
        f"part_min_z={part_box[2]:g} m, base_max_z={base_box[5]:g} m, "
        f"required_lift={required_lift / M_PER_MM:g} mm"
    )
    if required_lift > 0.0:
        move_body_z(model, find_body(model, part_name), part_name, required_lift)
    final_box = body_box(find_body(model, part_name))
    if final_box[2] + 1e-9 < target_z:
        raise RuntimeError(
            f"Could not establish support gap: final part_min_z={final_box[2]:g}, "
            f"target={target_z:g}"
        )
    print(f"Verified final part-to-base Z gap: {(final_box[2] - base_box[5]) / M_PER_MM:g} mm")
    return required_lift

