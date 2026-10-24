"""Filesystem locations and defaults shared by the ANSYS runner."""

from pathlib import Path


WORKSPACE_DIR = Path(__file__).resolve().parents[2]
ANSYS_DIR = WORKSPACE_DIR / "ANSYS"
DEFAULT_GEOMETRY_FILE = WORKSPACE_DIR / "Solidworks" / "Part1.step"
TEMPLATE_FILE = ANSYS_DIR / "lpbfsim.mechdb"
RUN_WORK_DIR = ANSYS_DIR / "run_work"
DEFAULT_RESULTS_CSV = WORKSPACE_DIR / "results" / "orientation_results.csv"
DEFAULT_PART_MESH_SIZE_MM = 0.1
DEFAULT_BASE_MESH_SIZE_MM = 0.5
