"""Summarize LPBF orientation results and generate a contour-style SVG map.

The script is intentionally dependency-free.  It reads the controller CSV when
available and fills any missing records from per-run JSON files.  The contour
map is a 2-D inverse-distance interpolation of average stress over Rx/Ry for
one Rz slice; measured results are drawn on top of the interpolated field.

Example:
    python analyze_orientation_results.py
    python analyze_orientation_results.py --metric max --rz 0
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import math
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_RESULTS = ROOT / "results"


def render_svg_png(svg_path: Path, png_path: Path) -> bool:
    """Render an SVG to PNG using an available local renderer.

    No renderer is required for the workflow: SVG remains the primary output.
    The fallback chain makes PNG output work on common Windows installations
    without adding a Python package to the project environment.
    """
    svg_path = svg_path.resolve()
    png_path = png_path.resolve()
    png_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=1100)
        return png_path.exists()
    except (ImportError, OSError, RuntimeError):
        pass

    converters = []
    magick = shutil.which("magick")
    if magick:
        converters.append([magick, str(svg_path), str(png_path)])
    inkscape = shutil.which("inkscape")
    if inkscape:
        converters.append([inkscape, str(svg_path), "--export-type=png", f"--export-filename={png_path}"])
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        converters.append([rsvg, "-o", str(png_path), str(svg_path)])

    edge_candidates = [
        shutil.which("msedge"),
        shutil.which("chrome"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for browser in edge_candidates:
        if browser and Path(browser).is_file():
            converters.append([
                browser,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--run-all-compositor-stages-before-draw",
                "--window-size=1100,760",
                f"--screenshot={png_path}",
                Path(svg_path).as_uri(),
            ])
            break

    for command in converters:
        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)
            if png_path.exists() and png_path.stat().st_size > 0:
                return True
        except (OSError, subprocess.SubprocessError):
            continue
    return False


@dataclass(frozen=True)
class Observation:
    run_id: str
    status: str
    rx: float
    ry: float
    rz: float
    average_pa: float | None
    maximum_pa: float | None
    minimum_pa: float | None
    units: str
    step_file: str
    result_file: str
    screenshot_file: str
    error: str

    @property
    def valid(self) -> bool:
        return self.status.lower() == "success" and self.average_pa is not None


def number(value: object) -> float | None:
    """Parse a numeric CSV/JSON value, including strings such as '12 [Pa]'."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        pass
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return float(text.split("[", 1)[0].strip())
    except ValueError:
        return None


def json_observation(path: Path) -> Observation | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    rotation = payload.get("rotation_degrees") or {}
    stress = payload.get("stress_results") or {}
    return Observation(
        run_id=str(payload.get("run_id") or path.stem.replace("_results", "")),
        status=str(payload.get("status") or "unknown"),
        rx=number(rotation.get("rot_x")) or 0.0,
        ry=number(rotation.get("rot_y")) or 0.0,
        rz=number(rotation.get("rot_z")) or 0.0,
        average_pa=number(stress.get("average_stress")),
        maximum_pa=number(stress.get("max_stress")),
        minimum_pa=number(stress.get("min_stress")),
        units=str(stress.get("stress_units") or "Pa"),
        step_file=str(payload.get("step_file") or ""),
        result_file=str(path),
        screenshot_file=str(stress.get("screenshot_file") or ""),
        error=str(payload.get("error") or ""),
    )


def csv_observations(path: Path) -> list[Observation]:
    records: list[Observation] = []
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                records.append(
                    Observation(
                        run_id=row.get("run_id", ""),
                        status=row.get("status", "unknown"),
                        rx=number(row.get("rot_x_deg")) or 0.0,
                        ry=number(row.get("rot_y_deg")) or 0.0,
                        rz=number(row.get("rot_z_deg")) or 0.0,
                        average_pa=number(row.get("average_stress_pa")),
                        maximum_pa=number(row.get("max_stress_pa")),
                        minimum_pa=number(row.get("min_stress_pa")),
                        units=row.get("stress_units") or "Pa",
                        step_file=row.get("step_file", ""),
                        result_file=row.get("result_file", ""),
                        screenshot_file="",
                        error=row.get("error", ""),
                    )
                )
    except (OSError, UnicodeError):
        return []
    return records


def load_observations(results_dir: Path) -> list[Observation]:
    csv_records = csv_observations(results_dir / "orientation_results.csv")
    json_records = {
        item.run_id: item
        for path in sorted(results_dir.glob("*_results.json"))
        if (item := json_observation(path)) is not None
    }
    merged: dict[str, Observation] = {}
    for item in csv_records:
        merged[item.run_id] = json_records.get(item.run_id, item)
    for run_id, item in json_records.items():
        merged.setdefault(run_id, item)
    return sorted(merged.values(), key=lambda item: item.run_id)


def fmt_stress(value: float | None) -> str:
    if value is None:
        return "n/a"
    if abs(value) >= 1e6:
        return f"{value / 1e6:.4f} MPa"
    if abs(value) >= 1e3:
        return f"{value / 1e3:.4f} kPa"
    return f"{value:.6g} Pa"


def metric_value(item: Observation, metric: str) -> float | None:
    return item.maximum_pa if metric == "max" else item.average_pa


def choose_slice(observations: list[Observation], rz: float | None) -> tuple[float, list[Observation]]:
    valid = [item for item in observations if item.valid]
    if rz is not None:
        selected = [item for item in valid if math.isclose(item.rz, rz, abs_tol=1e-7)]
        return rz, selected
    groups: dict[float, list[Observation]] = {}
    for item in valid:
        groups.setdefault(round(item.rz, 7), []).append(item)
    if not groups:
        return 0.0, []
    selected_rz, selected = max(groups.items(), key=lambda pair: len(pair[1]))
    return selected_rz, selected


def color(value: float, low: float, high: float) -> str:
    """Blue-to-red heatmap color."""
    ratio = 0.5 if high <= low else max(0.0, min(1.0, (value - low) / (high - low)))
    stops = [(0.0, (31, 119, 180)), (0.5, (255, 220, 70)), (1.0, (190, 35, 45))]
    for (a, c1), (b, c2) in zip(stops, stops[1:]):
        if ratio <= b:
            t = (ratio - a) / (b - a)
            rgb = tuple(round(x + t * (y - x)) for x, y in zip(c1, c2))
            return "#%02x%02x%02x" % rgb
    return "#be232d"


def interpolated_value(rx: float, ry: float, points: list[tuple[float, float, float]]) -> float:
    weighted = 0.0
    total = 0.0
    for px, py, value in points:
        distance = math.hypot(rx - px, ry - py)
        if distance < 1e-9:
            return value
        weight = 1.0 / distance**2
        weighted += weight * value
        total += weight
    return weighted / total if total else 0.0


def write_contour_svg(path: Path, observations: list[Observation], metric: str, rz: float) -> None:
    width, height = 1100, 760
    # Keep the Y-axis title and tick values in separate horizontal lanes.
    left, top, plot_w, plot_h = 130, 70, 790, 580
    values = [metric_value(item, metric) for item in observations]
    points = [
        (item.rx, item.ry, value)
        for item, value in zip(observations, values)
        if value is not None
    ]
    if not points:
        raise ValueError("No numeric stress values are available for the selected Rz slice")
    min_x, max_x = min(x for x, _, _ in points), max(x for x, _, _ in points)
    min_y, max_y = min(y for _, y, _ in points), max(y for _, y, _ in points)
    if min_x == max_x:
        min_x, max_x = min_x - 1, max_x + 1
    if min_y == max_y:
        min_y, max_y = min_y - 1, max_y + 1
    low, high = min(v for _, _, v in points), max(v for _, _, v in points)
    def sx(x: float) -> float:
        return left + (x - min_x) / (max_x - min_x) * plot_w
    def sy(y: float) -> float:
        return top + plot_h - (y - min_y) / (max_y - min_y) * plot_h
    cells: list[str] = []
    grid = 44
    for ix in range(grid):
        for iy in range(grid):
            x0 = min_x + (max_x - min_x) * ix / grid
            x1 = min_x + (max_x - min_x) * (ix + 1) / grid
            y0 = min_y + (max_y - min_y) * iy / grid
            y1 = min_y + (max_y - min_y) * (iy + 1) / grid
            v = interpolated_value((x0 + x1) / 2, (y0 + y1) / 2, points)
            cells.append(
                f'<rect x="{sx(x0):.2f}" y="{sy(y1):.2f}" width="{plot_w / grid + 0.5:.2f}" '
                f'height="{plot_h / grid + 0.5:.2f}" fill="{color(v, low, high)}"/>'
            )
    measured = []
    for item in observations:
        value = metric_value(item, metric)
        if value is None:
            continue
        measured.append(
            f'<circle cx="{sx(item.rx):.2f}" cy="{sy(item.ry):.2f}" r="5" '
            f'fill="white" stroke="black" stroke-width="1.5"><title>{html.escape(item.run_id)}: '
            f'Rx={item.rx:g}, Ry={item.ry:g}, {metric}={fmt_stress(value)}</title></circle>'
        )
    best = min((item for item in observations if metric_value(item, metric) is not None), key=lambda item: metric_value(item, metric))
    best_marker = (
        f'<circle cx="{sx(best.rx):.2f}" cy="{sy(best.ry):.2f}" r="11" fill="none" '
        f'stroke="#00ff66" stroke-width="4"/><text x="{sx(best.rx)+14:.2f}" y="{sy(best.ry)-12:.2f}" '
        f'font-size="14" font-weight="bold" fill="#006b2e">BEST {html.escape(best.run_id)}</text>'
    )
    labels = []
    for tick in range(6):
        x = min_x + (max_x - min_x) * tick / 5
        y = min_y + (max_y - min_y) * tick / 5
        labels += [
            f'<text x="{sx(x):.2f}" y="{top+plot_h+28}" text-anchor="middle" font-size="13">{x:g}</text>',
            f'<text x="{left-18}" y="{sy(y)+5:.2f}" text-anchor="end" font-size="13">{y:g}</text>',
        ]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white"/>
<text x="{width/2}" y="30" text-anchor="middle" font-size="21" font-weight="bold">LPBF orientation stress contour (Rz={rz:g}°, metric={metric})</text>
<text x="{left+plot_w/2}" y="{height-18}" text-anchor="middle" font-size="15">Rotation X (degrees)</text>
<text x="18" y="{top+plot_h/2}" text-anchor="middle" font-size="15" transform="rotate(-90 18 {top+plot_h/2})">Rotation Y (degrees)</text>
<g>{''.join(cells)}</g>
<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="none" stroke="#333"/>
<g>{''.join(labels)}</g>
<g>{''.join(measured)}</g>{best_marker}
<text x="{left+plot_w+35}" y="{top+20}" font-size="13">Low</text>
<rect x="{left+plot_w+35}" y="{top+30}" width="24" height="240" fill="url(#legend)"/>
<defs><linearGradient id="legend" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#1f77b4"/><stop offset="50%" stop-color="#ffdc46"/><stop offset="100%" stop-color="#be232d"/></linearGradient></defs>
<text x="{left+plot_w+65}" y="{top+42}" font-size="12">{fmt_stress(high)}</text><text x="{left+plot_w+65}" y="{top+275}" font-size="12">{fmt_stress(low)}</text>
</svg>'''
    path.write_text(svg, encoding="utf-8")


def write_summary(
    path: Path,
    observations: list[Observation],
    metric: str,
    rz: float,
    map_path: Path,
    metadata: dict[str, object] | None = None,
) -> None:
    valid = [item for item in observations if item.valid]
    best_avg = min(valid, key=lambda item: item.average_pa) if valid else None
    best_max = min((item for item in valid if item.maximum_pa is not None), key=lambda item: item.maximum_pa, default=None)
    selected = [item for item in valid if math.isclose(item.rz, rz, abs_tol=1e-7)]
    best_metric = min(selected, key=lambda item: metric_value(item, metric)) if selected else best_avg
    baseline = next((item for item in valid if item.rx == item.ry == item.rz == 0), None)
    lines = [
        "LPBF ORIENTATION RESULTS SUMMARY",
        "=" * 34,
    ]
    if metadata:
        lines += [
            "",
            "RUN INFORMATION",
            "---------------",
            f"Run started (UTC): {metadata.get('run_started_at_utc', 'n/a')}",
            f"Run completed (UTC): {metadata.get('run_completed_at_utc', 'n/a')}",
            f"Total run time: {metadata.get('total_runtime', 'n/a')}",
            f"Part: {metadata.get('part_file', 'n/a')}",
            f"Workflow: {metadata.get('workflow', 'n/a')}",
            f"Part mesh size: {metadata.get('part_mesh_size_mm', 'n/a')} mm",
            f"Base mesh size: {metadata.get('base_mesh_size_mm', 'n/a')} mm",
            f"Requested solver cores: {metadata.get('solver_cores', 'n/a')}",
            f"Maximum allowed evaluations: {metadata.get('maximum_evaluations', 'n/a')}",
        ]
    lines += [
        "",
        f"Records read: {len(observations)}",
        f"Successful simulations: {len(valid)}",
        f"Failed/incomplete simulations: {len(observations) - len(valid)}",
        f"Contour-map Rz slice: {rz:g} degrees",
        f"Optimization metric: {metric} stress",
        "",
        "OPTIMIZED ORIENTATION",
        "---------------------",
        f"Best {metric} orientation: " + (f"{best_metric.run_id} (Rx={best_metric.rx:g}°, Ry={best_metric.ry:g}°, Rz={best_metric.rz:g}°)" if best_metric else "n/a"),
        f"Average equivalent stress: {fmt_stress(best_metric.average_pa if best_metric else None)}",
        f"Maximum equivalent stress: {fmt_stress(best_metric.maximum_pa if best_metric else None)}",
        f"STEP file: {best_metric.step_file if best_metric else 'n/a'}",
        f"JSON file: {best_metric.result_file if best_metric else 'n/a'}",
        f"Screenshot: {best_metric.screenshot_file if best_metric else 'n/a'}",
        "",
        "GLOBAL BESTS",
        "------------",
        f"Lowest average stress: {fmt_stress(best_avg.average_pa if best_avg else None)} at " + (f"Rx={best_avg.rx:g}°, Ry={best_avg.ry:g}°, Rz={best_avg.rz:g}°" if best_avg else "n/a"),
        f"Lowest maximum stress: {fmt_stress(best_max.maximum_pa if best_max else None)} at " + (f"Rx={best_max.rx:g}°, Ry={best_max.ry:g}°, Rz={best_max.rz:g}°" if best_max else "n/a"),
    ]
    if baseline and best_avg and baseline.average_pa:
        improvement = (baseline.average_pa - best_avg.average_pa) / baseline.average_pa * 100
        lines += [f"Baseline average stress: {fmt_stress(baseline.average_pa)}", f"Average-stress improvement: {improvement:.2f}%"]
    lines += [
        "",
        f"Contour map: {map_path}",
        f"Contour map PNG: {map_path.with_suffix('.png')}",
        "",
        "TOP ORIENTATIONS BY AVERAGE STRESS",
        "-------------------------------",
    ]
    for rank, item in enumerate(sorted(valid, key=lambda item: item.average_pa)[:10], 1):
        lines.append(f"{rank:2d}. {item.run_id}: Rx={item.rx:g}°, Ry={item.ry:g}°, Rz={item.rz:g}°; avg={fmt_stress(item.average_pa)}; max={fmt_stress(item.maximum_pa)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--output-dir", type=Path, default=None, help="Where to write summary/map; defaults to results directory")
    parser.add_argument("--metric", choices=("average", "max"), default="average")
    parser.add_argument("--rz", type=float, default=None, help="Rz slice to map; defaults to the slice with most results")
    args = parser.parse_args()
    results_dir = args.results_dir.resolve()
    output_dir = (args.output_dir or results_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    observations = load_observations(results_dir)
    valid = [item for item in observations if item.valid]
    if not valid:
        raise SystemExit(f"No successful stress results found in {results_dir}")
    rz, selected = choose_slice(observations, args.rz)
    if not selected:
        raise SystemExit(f"No successful results found for Rz={rz:g} degrees")
    map_path = output_dir / "orientation_contour_map.svg"
    map_png_path = output_dir / "orientation_contour_map.png"
    summary_path = output_dir / "orientation_summary.txt"
    write_contour_svg(map_path, selected, args.metric, rz)
    rendered = render_svg_png(map_path, map_png_path)
    write_summary(summary_path, observations, args.metric, rz, map_path)
    best = min(selected, key=lambda item: metric_value(item, args.metric))
    print(f"Successful simulations: {len(valid)}")
    print(f"Best orientation: Rx={best.rx:g}, Ry={best.ry:g}, Rz={best.rz:g} degrees")
    print(f"Average stress: {fmt_stress(best.average_pa)}")
    print(f"Maximum stress: {fmt_stress(best.maximum_pa)}")
    print(f"Summary: {summary_path}")
    print(f"Contour map: {map_path}")
    print(f"Contour map PNG: {map_png_path if rendered else 'not rendered (no local SVG renderer found)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
