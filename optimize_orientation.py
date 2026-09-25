"""Lightweight Bayesian optimization for LPBF part orientation.

The module deliberately uses only the Python standard library. Each call to
``next_orientation`` fits a small Gaussian-process surrogate to successful
rows in ``results/orientation_results.csv`` and selects the candidate with
the highest expected improvement for average stress.
"""
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Candidate:
    rot_x: float
    rot_y: float
    rot_z: float


def _number(value: str) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def load_successful_results(csv_file: Path) -> list[tuple[Candidate, float]]:
    if not csv_file.exists():
        return []

    observations = []
    with csv_file.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("status") != "success":
                continue
            value = _number(row.get("average_stress_pa", ""))
            x = _number(row.get("rot_x_deg", ""))
            y = _number(row.get("rot_y_deg", ""))
            z = _number(row.get("rot_z_deg", ""))
            if value is not None and x is not None and y is not None and z is not None:
                observations.append((Candidate(x, y, z), value))
    return observations


def load_attempted_orientations(csv_file: Path) -> set[Candidate]:
    """Return every orientation already attempted, including invalid runs."""
    attempted = set()
    if not csv_file.exists():
        return attempted
    with csv_file.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            x = _number(row.get("rot_x_deg", ""))
            y = _number(row.get("rot_y_deg", ""))
            z = _number(row.get("rot_z_deg", ""))
            if x is not None and y is not None and z is not None:
                attempted.add(Candidate(x, y, z))
    return attempted


def _distance(a: Candidate, b: Candidate, scale: float) -> float:
    return math.sqrt(
        ((a.rot_x - b.rot_x) / scale) ** 2
        + ((a.rot_y - b.rot_y) / scale) ** 2
        + ((a.rot_z - b.rot_z) / scale) ** 2
    )


def _kernel(a: Candidate, b: Candidate, length_scale: float) -> float:
    distance = _distance(a, b, length_scale)
    return math.exp(-0.5 * distance * distance)


def _solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Solve a small dense linear system using Gaussian elimination."""
    size = len(vector)
    augmented = [matrix[index][:] + [vector[index]] for index in range(size)]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-14:
            raise ValueError("Singular Gaussian-process covariance matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        for index in range(column, size + 1):
            augmented[column][index] /= pivot_value
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            for index in range(column, size + 1):
                augmented[row][index] -= factor * augmented[column][index]
    return [augmented[index][size] for index in range(size)]


def _predict(
    candidate: Candidate,
    observations: list[tuple[Candidate, float]],
    length_scale: float,
) -> tuple[float, float]:
    points = [point for point, _ in observations]
    values = [value for _, value in observations]
    scale = max(1.0, max(abs(value) for value in values))
    normalized_values = [value / scale for value in values]
    covariance = [
        [
            _kernel(first, second, length_scale) + (1e-8 if row == column else 0.0)
            for column, second in enumerate(points)
        ]
        for row, first in enumerate(points)
    ]
    cross = [_kernel(candidate, point, length_scale) for point in points]
    alpha = _solve(covariance, normalized_values)
    weights = _solve(covariance, cross)
    mean = sum(weight * value for weight, value in zip(cross, alpha)) * scale
    variance = max(0.0, 1.0 - sum(weight * value for weight, value in zip(cross, weights)))
    return mean, math.sqrt(variance) * scale


def _expected_improvement(mean: float, deviation: float, best: float) -> float:
    if deviation <= 1e-12:
        return max(0.0, best - mean)
    improvement = best - mean
    z_score = improvement / deviation
    cdf = 0.5 * (1.0 + math.erf(z_score / math.sqrt(2.0)))
    pdf = math.exp(-0.5 * z_score * z_score) / math.sqrt(2.0 * math.pi)
    return improvement * cdf + deviation * pdf


def candidate_grid(min_angle: float, max_angle: float, grid_step: float) -> list[Candidate]:
    if grid_step <= 0:
        raise ValueError("grid_step must be positive")
    count = int(math.floor((max_angle - min_angle) / grid_step + 1e-9))
    angles = [round(min_angle + index * grid_step, 6) for index in range(count + 1)]
    if not angles or angles[-1] < max_angle - 1e-9:
        angles.append(max_angle)
    return [Candidate(x, y, z) for x in angles for y in angles for z in angles]


def next_orientation(
    csv_file: Path,
    *,
    min_angle: float = 0.0,
    max_angle: float = 90.0,
    grid_step: float = 15.0,
    length_scale: float = 30.0,
) -> tuple[Candidate | None, dict]:
    """Return the next orientation and selection diagnostics."""
    observations = load_successful_results(csv_file)
    candidates = candidate_grid(min_angle, max_angle, grid_step)
    observed = load_attempted_orientations(csv_file)
    candidates = [candidate for candidate in candidates if candidate not in observed]
    if not candidates:
        return None, {"reason": "candidate_grid_exhausted", "observations": len(observations)}

    if len(observations) < 2:
        selected = candidates[0]
        return selected, {"method": "initial_grid", "observations": len(observations)}

    best_value = min(value for _, value in observations)
    scored = []
    for candidate in candidates:
        mean, deviation = _predict(candidate, observations, length_scale)
        score = _expected_improvement(mean, deviation, best_value)
        scored.append((score, candidate, mean, deviation))
    score, selected, predicted_mean, predicted_deviation = max(scored, key=lambda item: item[0])
    return selected, {
        "method": "gaussian_process_expected_improvement",
        "observations": len(observations),
        "best_average_stress_pa": best_value,
        "expected_improvement": score,
        "predicted_average_stress_pa": predicted_mean,
        "predicted_standard_deviation_pa": predicted_deviation,
    }


def _bounded(value: float, minimum: float, maximum: float) -> float | None:
    if value < minimum - 1e-9 or value > maximum + 1e-9:
        return None
    return round(minimum if abs(value - minimum) < 1e-9 else maximum if abs(value - maximum) < 1e-9 else value, 6)


def next_contour_orientation(
    csv_file: Path,
    *,
    min_angle: float = 0.0,
    max_angle: float = 90.0,
    contour_step: float = 15.0,
    length_scale: float = 30.0,
) -> tuple[Candidate | None, dict]:
    """Select an untested point on a local 3-D contour around the best result.

    The contour is the 3x3x3 neighborhood around the incumbent, excluding the
    center. Expected improvement ranks the contour points using all prior CSV
    observations, so the search follows measured stress contours instead of
    blindly scanning the global grid.
    """
    observations = load_successful_results(csv_file)
    if not observations:
        return Candidate(min_angle, min_angle, min_angle), {
            "method": "contour_initial_point",
            "observations": 0,
        }
    if contour_step <= 0:
        raise ValueError("contour_step must be positive")

    incumbent, best_value = min(observations, key=lambda item: item[1])
    observed = load_attempted_orientations(csv_file)
    candidates = []
    for dx in (-contour_step, 0.0, contour_step):
        for dy in (-contour_step, 0.0, contour_step):
            for dz in (-contour_step, 0.0, contour_step):
                if dx == dy == dz == 0.0:
                    continue
                x = _bounded(incumbent.rot_x + dx, min_angle, max_angle)
                y = _bounded(incumbent.rot_y + dy, min_angle, max_angle)
                z = _bounded(incumbent.rot_z + dz, min_angle, max_angle)
                if x is not None and y is not None and z is not None:
                    candidate = Candidate(x, y, z)
                    if candidate not in observed and candidate not in candidates:
                        candidates.append(candidate)

    if not candidates and contour_step > 2.0:
        return next_contour_orientation(
            csv_file,
            min_angle=min_angle,
            max_angle=max_angle,
            contour_step=contour_step / 2.0,
            length_scale=length_scale,
        )
    if not candidates:
        return None, {
            "method": "contour_exhausted",
            "observations": len(observations),
            "incumbent": incumbent.__dict__,
        }

    scored = []
    for candidate in candidates:
        mean, deviation = _predict(candidate, observations, length_scale)
        score = _expected_improvement(mean, deviation, best_value)
        scored.append((score, candidate, mean, deviation))
    score, selected, predicted_mean, predicted_deviation = max(
        scored, key=lambda item: item[0]
    )
    return selected, {
        "method": "adaptive_contour_expected_improvement",
        "observations": len(observations),
        "incumbent": incumbent.__dict__,
        "best_average_stress_pa": best_value,
        "contour_step_degrees": contour_step,
        "contour_candidates": len(candidates),
        "expected_improvement": score,
        "predicted_average_stress_pa": predicted_mean,
        "predicted_standard_deviation_pa": predicted_deviation,
    }
