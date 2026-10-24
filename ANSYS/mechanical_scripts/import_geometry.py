"""Embedded Mechanical stage: import STEP and scope the LPBF bodies."""

import os

from Ansys.ACT.Mechanical.Utilities import GeometryImportPreferences
from Ansys.Mechanical.DataModel.Enums import GeometryImportPreference


LOG_LINES = []
GEOMETRY_FILE = __GEOMETRY_FILE__


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



