from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from ansys.mechanical.core import launch_mechanical


WORKSPACE_DIR = Path(__file__).resolve().parent.parent
ANSYS_DIR = Path(__file__).resolve().parent
DEFAULT_GEOMETRY_FILE = WORKSPACE_DIR / "Solidworks" / "Part1.step"
TEMPLATE_FILE = ANSYS_DIR / "lpbfsim.mechdb"
RUN_WORK_DIR = ANSYS_DIR / "run_work"
DEFAULT_RESULTS_CSV = WORKSPACE_DIR / "results" / "orientation_results.csv"


def close_open_ansys_guis() -> None:
    """Release seats held by already-open Ansys GUI processes."""
    if os.name != "nt":
        return

    for image_name in ("AnsysWBU.exe", "RunWB2.exe"):
        subprocess.run(
            ["taskkill", "/F", "/T", "/IM", image_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    # Allow the licensing client to receive the GUI process release.
    time.sleep(2)


def find_mechanical_executable() -> Path:
    configured_path = os.environ.get("ANSYS_MECHANICAL_EXECUTABLE")
    if configured_path:
        executable = Path(configured_path).expanduser().resolve()
        if not executable.is_file():
            raise FileNotFoundError(
                "ANSYS_MECHANICAL_EXECUTABLE does not point to a file: "
                f"{executable}"
            )
        return executable

    candidates = []
    for environment_name, environment_value in os.environ.items():
        if not environment_name.startswith("AWP_ROOT") or not environment_value:
            continue
        ansys_root = Path(environment_value).expanduser()
        if ansys_root.name.casefold() == "ansys":
            ansys_root = ansys_root.parent
        candidates.append(ansys_root / "aisol" / "bin" / "winx64" / "AnsysWBU.exe")

    install_root = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "ANSYS Inc"
    candidates.extend(install_root.glob(r"v*\aisol\bin\winx64\AnsysWBU.exe"))
    candidates = sorted(
        {candidate.resolve() for candidate in candidates if candidate.is_file()},
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError(
            "Could not find Ansys Mechanical. Set ANSYS_MECHANICAL_EXECUTABLE "
            "to the full path of AnsysWBU.exe."
        )
    return candidates[0]


MECHANICAL_EXECUTABLE = find_mechanical_executable()


def mechanical_version_from_executable(executable: Path) -> int:
    for parent in executable.parents:
        if parent.name.startswith("v") and parent.name[1:].isdigit():
            return int(parent.name[1:])
    raise ValueError(f"Could not determine Ansys version from: {executable}")


MECHANICAL_VERSION = mechanical_version_from_executable(MECHANICAL_EXECUTABLE)


DELETE_GEOMETRY_SCRIPT = r'''
existing_geometry_parts = ExtAPI.DataModel.GeoData.Assemblies[0].AllParts
Model.DeleteParts(existing_geometry_parts)
'''


def import_geometry_script(step_file: Path) -> str:
    return f'''
import os

from Ansys.ACT.Mechanical.Utilities import GeometryImportPreferences
from Ansys.Mechanical.DataModel.Enums import GeometryImportPreference


LOG_LINES = []
GEOMETRY_FILE = {str(step_file)!r}


def log_message(message):
    LOG_LINES.append(str(message))
    ExtAPI.Log.WriteMessage(str(message))


mechanical_model = ExtAPI.DataModel.Project.Model

if not os.path.exists(GEOMETRY_FILE):
    raise Exception("STEP file not found: " + GEOMETRY_FILE)

geometry_import_group = mechanical_model.GeometryImportGroup
if geometry_import_group is None:
    geometry_import_group = mechanical_model.AddGeometryImportGroup()

geometry_import = geometry_import_group.AddGeometryImport()
geometry_import_preferences = GeometryImportPreferences()

geometry_import.Import(
    GEOMETRY_FILE,
    GeometryImportPreference.Format.Automatic,
    geometry_import_preferences,
)

log_message("Imported STEP file: " + GEOMETRY_FILE)

imported_bodies = ExtAPI.DataModel.GetObjectsByType(
    Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.Body
)

part_body = None
base_body = None

log_message("Bodies found after import:")
for imported_body in imported_bodies:
    log_message("  " + str(imported_body.Name))

for imported_body in imported_bodies:
    body_name = imported_body.Name.strip().lower()

    if part_body is None and body_name.endswith("|part"):
        part_body = imported_body

    if base_body is None and body_name.endswith("|base"):
        base_body = imported_body

if part_body is None:
    raise Exception('Could not find imported body ending with "|part".')

if base_body is None:
    raise Exception('Could not find imported body ending with "|base".')

log_message("Using part body: " + part_body.Name)
log_message("Using base body: " + base_body.Name)

selection_manager = ExtAPI.SelectionManager

part_selection = selection_manager.CreateSelectionInfo(
    Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities
)
part_selection.Ids = [part_body.GetGeoBody().Id]

base_selection = selection_manager.CreateSelectionInfo(
    Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities
)
base_selection.Ids = [base_body.GetGeoBody().Id]

am_process = DataModel.GetObjectsByName("AM Process")[0]
log_message("Using existing AM Process")

for am_child in list(am_process.Children):
    if am_child.Name == "Body Fitted Cartesian":
        am_child.Delete()
        break

am_process.PartGeometry = part_selection
am_process.BuildGeometry = part_selection
am_process.BaseGeometry = base_selection

log_message("AM geometry scoped.")
'''


MESH_SCRIPT = r'''
from Ansys.Mechanical.DataModel.Enums import AMMultiplierEntryType


if "mechanical_model" not in globals():
    mechanical_model = ExtAPI.DataModel.Project.Model

if "log_message" not in globals():
    def log_message(message):
        ExtAPI.Log.WriteMessage(str(message))


def get_one_by_name(object_name):
    matching_objects = DataModel.GetObjectsByName(object_name)
    if not matching_objects:
        raise Exception("Object not found: " + object_name)
    return matching_objects[0]


body_fitted_mesh = get_one_by_name("Body Fitted Cartesian")
body_fitted_mesh.Delete()

model_mesh = mechanical_model.Mesh
model_mesh.ElementSize = Quantity("0.3 [mm]")

cartesian_mesh = None
try:
    cartesian_mesh = am_process.AddCartesianMesh()
    log_message("Cartesian mesh object added.")
except Exception as error:
    log_message("AddCartesianMesh() failed or mesh already exists: " + str(error))
    for am_child in am_process.Children:
        child_name = str(am_child.Name)
        child_type_name = str(am_child.GetType().Name)
        if "Cartesian" in child_name or "Cartesian" in child_type_name:
            cartesian_mesh = am_child
            log_message("Using existing Cartesian mesh object: " + child_name)
            break

if cartesian_mesh is None:
    raise Exception("Could not create or find Cartesian mesh object for voxelized part.")

try:
    cartesian_mesh.Location = part_selection
except Exception as error:
    log_message("Could not assign Cartesian mesh location directly: " + str(error))

try:
    cartesian_mesh.ElementSize = Quantity("0.1 [mm]")
except Exception as error:
    log_message("Could not set Cartesian mesh ElementSize: " + str(error))

try:
    cartesian_mesh.XSize = Quantity("0.5 [mm]")
    cartesian_mesh.YSize = Quantity("0.5 [mm]")
    cartesian_mesh.ZSize = Quantity("0.5 [mm]")
except Exception as error:
    log_message("Could not set Cartesian mesh XYZ sizes: " + str(error))

base_mesh_sizing = model_mesh.AddSizing()
base_mesh_sizing.Location = base_selection
base_mesh_sizing.ElementSize = Quantity("0.5 [mm]")
log_message("Base sizing assigned.")

try:
    base_mesh_method = model_mesh.AddAutomaticMethod()
    base_mesh_method.Location = base_selection
    log_message("Automatic mesh method added for base.")
except Exception as error:
    log_message("AddAutomaticMethod() failed: " + str(error))

model_mesh.GenerateMesh()
log_message("Mesh generated.")

try:
    secondary_support = get_one_by_name("Generated Support 2")
    secondary_support.MultiplierEntry = AMMultiplierEntryType.All
    secondary_support.MaterialMultiplier = 0.5
    log_message("Configured Generated Support 2.")
except Exception as error:
    log_message("Optional Generated Support 2 not present; continuing: " + str(error))

try:
    primary_support = get_one_by_name("Generated Support")
    primary_support.Delete()
    log_message("Deleted Generated Support.")
except Exception as error:
    log_message("Optional Generated Support not present; continuing: " + str(error))

part_body.Material = "Inconel 718"
'''

SOLVE_SCRIPT = r'''
if "mechanical_model" not in globals():
    mechanical_model = ExtAPI.DataModel.Project.Model

solver_configuration = None
try:
    solver_configuration = ExtAPI.Application.SolveConfigurations["My Computer, Background"]
except Exception as error:
    ExtAPI.Log.WriteMessage("Named background solve configuration unavailable: " + str(error))
    for candidate_configuration in ExtAPI.Application.SolveConfigurations:
        if candidate_configuration.Default:
            solver_configuration = candidate_configuration
            break

if solver_configuration is None:
    raise Exception("Could not find a default Ansys solve configuration.")

solver_configuration.SetAsDefault()
solver_configuration.SolveProcessSettings.MaxNumberOfCores = 6
ExtAPI.Log.WriteMessage(
    "Ansys solver maximum cores set to "
    + str(solver_configuration.SolveProcessSettings.MaxNumberOfCores)
)

temperature_load = DataModel.GetObjectsByName("Temperature")[0]
temperature_load.Location = base_selection
temperature_load.Magnitude = Quantity("80 [C]")

for selected_analysis in mechanical_model.Analyses:
    log_message(
        "Starting analysis: index="
        + str(list(mechanical_model.Analyses).index(selected_analysis))
        + ", name="
        + str(selected_analysis.Name)
    )
    try:
        # The True argument makes Mechanical block until solver results are
        # available before the result-extraction stage runs.
        selected_analysis.Solution.Solve(True)
    except Exception as error:
        log_message("Synchronous solution call failed; using analysis solve: " + str(error))
        selected_analysis.Solve()
    log_message("Finished analysis: " + str(selected_analysis.Name))
'''

RESULTS_SCRIPT = r'''
import json
import re


def numeric_value(value):
    try:
        return float(value)
    except Exception:
        match = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", str(value))
        if match:
            return float(match.group(0))
    return None


def result_values(result_object):
    try:
        average = result_object.Average
        numeric = numeric_value(average)
        if numeric is not None:
            return [numeric]
    except Exception:
        pass

    candidates = []
    try:
        plot_data = result_object.PlotData
        for attribute_name in ["Values", "ResultValues", "YValues"]:
            try:
                candidates.append(getattr(plot_data, attribute_name))
            except Exception:
                pass

        try:
            candidates.append(plot_data["Values"])
        except Exception:
            pass
    except Exception:
        pass

    values = []
    for candidate in candidates:
        try:
            for value in candidate:
                numeric = numeric_value(value)
                if numeric is not None:
                    values.append(numeric)
        except Exception:
            numeric = numeric_value(candidate)
            if numeric is not None:
                values.append(numeric)
    return values


selected_analysis = Model.Analyses[1]
analysis_solution = selected_analysis.Solution

analysis_diagnostics = []
for analysis_index, candidate_analysis in enumerate(Model.Analyses):
    diagnostic = {
        "index": analysis_index,
        "name": str(candidate_analysis.Name),
    }
    try:
        candidate_solution = candidate_analysis.Solution
        diagnostic["solution_type"] = str(candidate_solution.GetType().Name)
        try:
            diagnostic["solution_status"] = str(candidate_solution.Status)
        except Exception as error:
            diagnostic["solution_status_error"] = str(error)
        try:
            diagnostic["solution_children"] = len(list(candidate_solution.Children))
        except Exception as error:
            diagnostic["solution_children_error"] = str(error)
    except Exception as error:
        diagnostic["solution_error"] = str(error)
    analysis_diagnostics.append(diagnostic)

ExtAPI.Log.WriteMessage("Analysis diagnostics: " + json.dumps(analysis_diagnostics))

equivalent_stress = analysis_solution.AddEquivalentStress()
analysis_solution.EvaluateAllResults()

maximum = str(equivalent_stress.Maximum)
average_values = result_values(equivalent_stress)
average = "Average unavailable"
try:
    average_property = equivalent_stress.Average
    if numeric_value(average_property) is not None:
        average = str(average_property)
except Exception:
    pass
if average == "Average unavailable" and average_values:
    average = str(sum(average_values) / len(average_values))

stress_results = {
    "max_stress": maximum,
    "average_stress": average,
    "min_stress": str(equivalent_stress.Minimum),
    "selected_analysis_index": 1,
    "selected_analysis_name": str(selected_analysis.Name),
    "analysis_diagnostics": analysis_diagnostics,
}

json.dumps(stress_results)
'''


def prepare_template_copy(run_id: str) -> Path:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template Mechanical database not found: {TEMPLATE_FILE}")

    RUN_WORK_DIR.mkdir(parents=True, exist_ok=True)
    safe_run_id = "".join(char if char.isalnum() or char in "-_" else "_" for char in run_id)
    run_template = RUN_WORK_DIR / f"{safe_run_id}.mechdb"
    # Mechanical stores project state beside the database. Remove only the
    # disposable sidecar for this run so a prior interrupted session cannot
    # force the newly copied database into read-only mode.
    stale_sidecar = RUN_WORK_DIR / f"{safe_run_id}_Mech_Files"
    if stale_sidecar.exists():
        shutil.rmtree(stale_sidecar)

    for lock_file in RUN_WORK_DIR.glob(f"{safe_run_id}*.lock"):
        try:
            lock_file.unlink()
        except OSError:
            pass

    shutil.copy2(TEMPLATE_FILE, run_template)
    return run_template


def execute_writable_script(mechanical_session, script: str):
    """Execute in Mechanical's full scripting context, not light/read-only mode."""
    public_runner = getattr(mechanical_session, "run_python_script", None)
    if callable(public_runner):
        # Visible PyMechanical sessions expose the public remote scripting API
        # but do not necessarily expose the embedded script_engine attribute.
        return public_runner(script)

    scope_name = "lpbf-workflow"
    if not hasattr(mechanical_session, "script_engine"):
        import clr

        clr.AddReference("Ansys.Mechanical.Scripting")
        import Ansys

        script_engine = Ansys.Mechanical.Scripting.EngineFactory.CreateEngine()
        script_engine.CreateScope(scope_name, False, False)
        mechanical_session.script_engine = script_engine

    result = mechanical_session.script_engine.ExecuteCode(
        script,
        scope_name,
        False,
        None,
        None,
    )
    if result is None:
        raise RuntimeError("Mechanical returned no script result.")
    if result.Error is not None:
        raise RuntimeError(f"Mechanical script failed: {result.Error.Message}")
    return result.Value


def run_stage(mechanical_session, stage_name: str, script: str):
    print(stage_name)
    result = execute_writable_script(mechanical_session, script)
    if result:
        print(result)
    return result


def close_mechanical(mechanical_session) -> None:
    try:
        mechanical_session.exit(force=True)
        return
    except TypeError:
        pass
    except Exception:
        pass

    for method_name in ("exit", "close"):
        method = getattr(mechanical_session, method_name, None)
        if callable(method):
            try:
                method()
                return
            except Exception:
                pass


def parse_result(raw_result: str) -> dict:
    if isinstance(raw_result, dict):
        return raw_result
    if isinstance(raw_result, bytes):
        raw_result = raw_result.decode("utf-8", errors="replace")
    try:
        parsed = json.loads(raw_result)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass
    return {"raw_result": raw_result}


def numeric_result(value):
    """Convert Mechanical's formatted result strings to numeric values."""
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        import re

        match = re.search(r"[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?", str(value))
        return float(match.group(0)) if match else None


def stress_result_status(stress_results: dict) -> tuple[str, str]:
    average = numeric_result(stress_results.get("average_stress"))
    maximum = numeric_result(stress_results.get("max_stress"))
    if average is None or maximum is None:
        return "invalid", "Stress result did not contain numeric average and maximum values."
    if average <= 0.0 or maximum <= 0.0:
        return "invalid", "Stress result was non-positive; excluding it from optimization."
    return "success", ""


def write_orientation_csv(
    args: argparse.Namespace,
    stress_results: dict | None,
    *,
    status: str,
    error: str = "",
    started_at: str | None = None,
) -> None:
    """Append one flat, optimizer-friendly record for this simulation."""
    csv_file = Path(args.results_csv)
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    stress_results = stress_results or {}
    fieldnames = [
        "run_id", "status", "rot_x_deg", "rot_y_deg", "rot_z_deg",
        "average_stress_pa", "max_stress_pa", "min_stress_pa", "stress_units",
        "step_file", "result_file", "started_at_utc", "completed_at_utc", "error",
    ]
    row = {
        "run_id": args.run_id,
        "status": status,
        "rot_x_deg": args.rot_x,
        "rot_y_deg": args.rot_y,
        "rot_z_deg": args.rot_z,
        "average_stress_pa": numeric_result(stress_results.get("average_stress")),
        "max_stress_pa": numeric_result(stress_results.get("max_stress")),
        "min_stress_pa": numeric_result(stress_results.get("min_stress")),
        "stress_units": "Pa",
        "step_file": str(Path(args.step_file).resolve()),
        "result_file": str(Path(args.result_file).resolve()) if args.result_file else "",
        "started_at_utc": started_at or "",
        "completed_at_utc": datetime.now(timezone.utc).isoformat(),
        "error": error,
    }
    file_exists = csv_file.exists() and csv_file.stat().st_size > 0
    with csv_file.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print(f"Orientation record appended: {csv_file}")


def write_result_file(args: argparse.Namespace, stress_results: dict, *, status: str = "success", error: str = "") -> None:
    if not args.result_file:
        return

    result_file = Path(args.result_file)
    result_file.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": args.run_id,
        "status": status,
        "step_file": str(Path(args.step_file).resolve()),
        "rotation_degrees": {
            "rot_x": args.rot_x,
            "rot_y": args.rot_y,
            "rot_z": args.rot_z,
        },
        "stress_results": stress_results,
    }
    if error:
        payload["error"] = error
    result_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Result file written: {result_file}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one LPBF Ansys simulation from a STEP file.")
    parser.add_argument("--step-file", default=str(DEFAULT_GEOMETRY_FILE))
    parser.add_argument("--run-id", default="manual_run")
    parser.add_argument("--rot-x", type=float, default=0.0)
    parser.add_argument("--rot-y", type=float, default=0.0)
    parser.add_argument("--rot-z", type=float, default=0.0)
    parser.add_argument("--result-file")
    parser.add_argument(
        "--results-csv",
        default=str(DEFAULT_RESULTS_CSV),
        help="CSV file to which one optimizer record is appended per run.",
    )
    parser.add_argument(
        "--pause-before-close",
        action="store_true",
        help="Wait for Enter before closing Mechanical.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    step_file = Path(args.step_file).resolve()
    started_at = datetime.now(timezone.utc).isoformat()

    if not step_file.exists():
        raise FileNotFoundError(f"STEP file not found: {step_file}")

    run_template = prepare_template_copy(args.run_id)

    close_open_ansys_guis()

    # Launch the visible Mechanical desktop first, using the same direct
    # PyMechanical GUI path as launch_mechanical_gui.py.
    mechanical_session = launch_mechanical(
        exec_file=str(MECHANICAL_EXECUTABLE),
        version=MECHANICAL_VERSION,
        batch=False,
        cleanup_on_exit=False,
    )

    try:
        print("Mechanical GUI launched and connected; opening template...")
        mechanical_session.run_python_script(
            f"ExtAPI.DataModel.Project.Open(r'{run_template}')"
        )
        # The visible remote Mechanical API owns the active license internally;
        # editability is validated by the first model mutation below.

        print("mechopen")
        print(f"run_id={args.run_id}")
        print(f"step_file={step_file}")
        print(f"template_copy={run_template}")
        print(f"rotation_degrees=({args.rot_x}, {args.rot_y}, {args.rot_z})")

        print("template opened in visible Mechanical GUI")
        # Do not issue a separate Project.Save() here.  In the visible
        # PyMechanical session that call can wait indefinitely on Mechanical's
        # UI even though the remote scripting channel is healthy.  The
        # mutation stages below validate writability and the run copy is
        # disposable; save only through the stage scripts when needed.
        run_stage(mechanical_session, "deleting old geometry", DELETE_GEOMETRY_SCRIPT)
        run_stage(mechanical_session, "importing geometry", import_geometry_script(step_file))
        run_stage(mechanical_session, "meshing geometry", MESH_SCRIPT)
        run_stage(mechanical_session, "solving analyses", SOLVE_SCRIPT)

        raw_result = execute_writable_script(mechanical_session, RESULTS_SCRIPT)
        stress_results = parse_result(raw_result)
        print(json.dumps(stress_results, indent=2))
        result_status, result_error = stress_result_status(stress_results)
        write_result_file(args, stress_results, status=result_status, error=result_error)
        write_orientation_csv(
            args,
            stress_results,
            status=result_status,
            error=result_error,
            started_at=started_at,
        )

        if args.pause_before_close:
            input("Press Enter to close Mechanical...")
    except Exception as error:
        error_text = f"{type(error).__name__}: {error}"
        write_result_file(args, {}, status="failed", error=error_text)
        write_orientation_csv(
            args,
            {},
            status="failed",
            error=error_text,
            started_at=started_at,
        )
        raise
    finally:
        close_mechanical(mechanical_session)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
