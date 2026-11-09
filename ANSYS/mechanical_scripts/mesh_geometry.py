"""Embedded Mechanical stage: apply mesh sizing and generate the mesh."""

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
part_mesh_size = Quantity("__PART_MESH_SIZE__ [mm]")
base_mesh_size = Quantity("__BASE_MESH_SIZE__ [mm]")
model_mesh.ElementSize = part_mesh_size

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
    cartesian_mesh.ElementSize = part_mesh_size
except Exception as error:
    log_message("Could not set Cartesian mesh ElementSize: " + str(error))

try:
    cartesian_mesh.XSize = part_mesh_size
    cartesian_mesh.YSize = part_mesh_size
    cartesian_mesh.ZSize = part_mesh_size
except Exception as error:
    log_message("Could not set Cartesian mesh XYZ sizes: " + str(error))

base_mesh_sizing = model_mesh.AddSizing()
base_mesh_sizing.Location = base_selection
base_mesh_sizing.ElementSize = base_mesh_size
log_message("Base sizing assigned.")
log_message(
    "Mesh sizes: part=" + str(part_mesh_size) + ", base=" + str(base_mesh_size)
)

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

part_body.Material = __PART_MATERIAL__
base_body.Material = __BASE_MATERIAL__
log_message(
    "Material assignments: part="
    + str(part_body.Material)
    + "; base="
    + str(base_body.Material)
)

