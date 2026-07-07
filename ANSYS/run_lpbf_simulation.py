from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from ansys.mechanical.core import launch_mechanical


WORKSPACE_DIR = Path(r"C:\Users\018219877\Downloads\LBPF")
ANSYS_DIR = WORKSPACE_DIR / "ANSYS"
DEFAULT_GEOMETRY_FILE = WORKSPACE_DIR / "Solidworks" / "Part1.step"
TEMPLATE_FILE = ANSYS_DIR / "lpbfsim.mechdb"
RUN_WORK_DIR = ANSYS_DIR / "run_work"
MECHANICAL_EXECUTABLE = r"C:\Program Files\ANSYS Inc\v251\aisol\bin\winx64\AnsysWBU.exe"


DELETE_GEOMETRY_SCRIPT = r'''
existing_geometry_parts = ExtAPI.DataModel.GeoData.Assemblies[0].AllParts
Model.DeleteParts(existing_geometry_parts)
'''


def open_template_script(template_file: Path) -> str:
    return f'''
TEMPLATE_FILE = {str(template_file)!r}
ExtAPI.DataModel.Project.Open(TEMPLATE_FILE)
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

secondary_support = get_one_by_name("Generated Support 2")
secondary_support.MultiplierEntry = AMMultiplierEntryType.All
secondary_support.MaterialMultiplier = 0.5

primary_support = get_one_by_name("Generated Support")
primary_support.Delete()

part_body.Material = "Inconel 718"
'''

SOLVE_SCRIPT = r'''
if "mechanical_model" not in globals():
    mechanical_model = ExtAPI.DataModel.Project.Model

temperature_load = DataModel.GetObjectsByName("Temperature")[0]
temperature_load.Location = base_selection
temperature_load.Magnitude = Quantity("80 [C]")

for selected_analysis in mechanical_model.Analyses:
    selected_analysis.Solve()
'''

RESULTS_SCRIPT = r'''
import json


def result_average(result_object):
    try:
        return result_object.Average
    except Exception:
        pass

    try:
        plot_data = result_object.PlotData
        values = []

        for attribute_name in ["Values", "ResultValues", "YValues"]:
            try:
                candidate_values = getattr(plot_data, attribute_name)
                for value in candidate_values:
                    values.append(float(value))
                if values:
                    return sum(values) / len(values)
            except Exception:
                pass

        try:
            candidate_values = plot_data["Values"]
            for value in candidate_values:
                values.append(float(value))
            if values:
                return sum(values) / len(values)
        except Exception:
            pass
    except Exception:
        pass

    return "Average unavailable"


selected_analysis = Model.Analyses[1]
analysis_solution = selected_analysis.Solution

equivalent_stress = analysis_solution.AddEquivalentStress()
analysis_solution.EvaluateAllResults()

stress_results = {
    "max_stress": str(equivalent_stress.Maximum),
    "min_stress": str(equivalent_stress.Minimum),
    "average_stress": str(result_average(equivalent_stress)),
}

json.dumps(stress_results)
'''


def prepare_template_copy(run_id: str) -> Path:
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Template Mechanical database not found: {TEMPLATE_FILE}")

    RUN_WORK_DIR.mkdir(parents=True, exist_ok=True)
    safe_run_id = "".join(char if char.isalnum() or char in "-_" else "_" for char in run_id)
    run_template = RUN_WORK_DIR / f"{safe_run_id}.mechdb"

    for lock_file in RUN_WORK_DIR.glob(f"{safe_run_id}*.lock"):
        try:
            lock_file.unlink()
        except OSError:
            pass

    shutil.copy2(TEMPLATE_FILE, run_template)
    return run_template


def run_stage(mechanical_session, stage_name: str, script: str):
    print(stage_name)
    result = mechanical_session.run_python_script(script)
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
    try:
        parsed = json.loads(raw_result)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass
    return {"raw_result": raw_result}


def write_result_file(args: argparse.Namespace, stress_results: dict) -> None:
    if not args.result_file:
        return

    result_file = Path(args.result_file)
    result_file.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": args.run_id,
        "step_file": str(Path(args.step_file).resolve()),
        "rotation_degrees": {
            "rot_x": args.rot_x,
            "rot_y": args.rot_y,
            "rot_z": args.rot_z,
        },
        "stress_results": stress_results,
    }
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
        "--pause-before-close",
        action="store_true",
        help="Wait for Enter before closing Mechanical.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    step_file = Path(args.step_file).resolve()

    if not step_file.exists():
        raise FileNotFoundError(f"STEP file not found: {step_file}")

    run_template = prepare_template_copy(args.run_id)

    mechanical_session = launch_mechanical(
        exec_file=MECHANICAL_EXECUTABLE,
        transport_mode="insecure",
        batch=False,
        start_instance=True,
        loglevel="INFO",
        log_mechanical="pymechanical_log.txt",
        verbose_mechanical=True,
    )

    try:
        print("mechopen")
        print(f"run_id={args.run_id}")
        print(f"step_file={step_file}")
        print(f"template_copy={run_template}")
        print(f"rotation_degrees=({args.rot_x}, {args.rot_y}, {args.rot_z})")

        run_stage(mechanical_session, "opening template", open_template_script(run_template))
        run_stage(mechanical_session, "deleting old geometry", DELETE_GEOMETRY_SCRIPT)
        run_stage(mechanical_session, "importing geometry", import_geometry_script(step_file))
        run_stage(mechanical_session, "meshing geometry", MESH_SCRIPT)
        run_stage(mechanical_session, "solving analyses", SOLVE_SCRIPT)

        raw_result = mechanical_session.run_python_script(RESULTS_SCRIPT)
        stress_results = parse_result(raw_result)
        print(json.dumps(stress_results, indent=2))
        write_result_file(args, stress_results)

        if args.pause_before_close:
            input("Press Enter to close Mechanical...")
    finally:
        close_mechanical(mechanical_session)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
