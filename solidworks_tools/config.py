"""Configuration and constants for the SolidWorks workflow."""

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_PART_FILE = SCRIPT_DIR / "Part1.SLDPRT"

SW_DOC_PART = 1
SW_OPEN_SILENT = 1
DEFAULT_PART_BODY = "part"
DEFAULT_BASE_BODY = "base"

# Retained for CLI compatibility with older callers. Placement is now solved
# directly from bounding boxes instead of by repeated incremental Z moves.
DEFAULT_Z_STEP_MM = 0.25
DEFAULT_Z_MAX_STEPS = 400
DEFAULT_SUPPORT_LIFT_MM = 2.0
DEFAULT_PLATE_MARGIN_MM = 0.0
M_PER_MM = 0.001
SOLIDWORKS_STARTUP_TIMEOUT_SECONDS = 120

FILE_LOAD_ERROR_FLAGS = {
    1: "generic file-load error",
    2: "file not found or referenced file suppressed",
    1024: "invalid file type",
    8192: "future-version file: saved in a newer SolidWorks version",
    65536: "a document with the same title is already open",
    131072: "file is encrypted by Liquid Machines",
    262144: "blocked because system resources are low",
    524288: "file contains no display data",
    1048576: "open operation was interrupted",
    2097152: "file requires non-critical repair",
    4194304: "file has critical data corruption",
}


def describe_file_load_errors(error_value):
    descriptions = [
        description
        for flag, description in FILE_LOAD_ERROR_FLAGS.items()
        if int(error_value) & flag
    ]
    return "; ".join(descriptions) if descriptions else "no decoded file-load errors"

