"""Embedded Mechanical stage: configure local solving and solve analyses."""

if "mechanical_model" not in globals():
    mechanical_model = ExtAPI.DataModel.Project.Model

solver_configuration = None
try:
    # Use the local foreground solver configuration.  The background and
    # distributed modes require a different license/MPI path and have been
    # observed to leave these analyses in SolveRequired without result files.
    solver_configuration = ExtAPI.Application.SolveConfigurations["My Computer"]
except Exception as error:
    ExtAPI.Log.WriteMessage("Named local solve configuration unavailable: " + str(error))
    for candidate_configuration in ExtAPI.Application.SolveConfigurations:
        if candidate_configuration.Default:
            solver_configuration = candidate_configuration
            break

if solver_configuration is None:
    raise Exception("Could not find a default Ansys solve configuration.")

solver_configuration.SetAsDefault()
solver_configuration.SolveProcessSettings.MaxNumberOfCores = 16
ExtAPI.Log.WriteMessage(
    "Ansys solver configuration=My Computer; distributed=False; maximum cores="
    + str(solver_configuration.SolveProcessSettings.MaxNumberOfCores)
)

# Apply the process values documented in the Miral Patel Inconel 718 report.
# These assignments are made to the disposable Mechanical copy only; the
# repository template is never saved back over.  The values are explicit here
# rather than relying on whatever process settings happen to be stored in the
# template.
am_build_settings = None
for am_child in am_process.Children:
    if str(am_child.Name).strip().lower() == "build settings":
        am_build_settings = am_child
        break
if am_build_settings is None:
    raise Exception("Could not find AM Process Build Settings.")

am_build_settings.DepositionThickness = Quantity("0.03 [mm]")
am_build_settings.HatchSpacing = Quantity("0.07 [mm]")
am_build_settings.ScanSpeed = Quantity("1000 [mm sec^-1]")
am_build_settings.DwellTime = Quantity("10 [sec]")
am_build_settings.PreheatTemperature = Quantity("170 [C]")
am_build_settings.RoomTemperature = Quantity("21 [C]")
am_build_settings.BuildGasTemperature = Quantity("170 [C]")
am_build_settings.BuildPowderTemperature = Quantity("170 [C]")
am_build_settings.CooldownGasTemperature = Quantity("21 [C]")
am_build_settings.CooldownPowderTemperature = Quantity("21 [C]")

# Keep the AM process display/deposition layer height consistent with the
# report's 30-micron deposition thickness where the property is available.
try:
    am_process.LayerHeight = Quantity("0.03 [mm]")
except Exception as error:
    ExtAPI.Log.WriteMessage("Could not set AM process LayerHeight: " + str(error))

ExtAPI.Log.WriteMessage(
    "Applied IN718 process settings: deposition=0.03 mm; hatch=0.07 mm; "
    "scan=1000 mm/s; dwell=10 s; preheat/gas/powder=170 C; "
    "room/cooldown=21 C"
)

temperature_load = DataModel.GetObjectsByName("Temperature")[0]
temperature_load.Location = base_selection
temperature_load.Magnitude = Quantity("170 [C]")
ExtAPI.Log.WriteMessage("Applied build-phase base temperature: 170 C")


def point_coordinates(point):
    """Return a geometry point as numeric x/y/z coordinates."""
    coordinates = getattr(point, "Coordinates", point)
    try:
        return [float(coordinates[index]) for index in range(3)]
    except Exception:
        return [float(coordinates.X), float(coordinates.Y), float(coordinates.Z)]


def face_is_on_z_zero(face, tolerance=1.0e-7):
    """Identify a horizontal face whose centroid lies on global z=0."""
    try:
        centroid = point_coordinates(face.Centroid)
        if abs(centroid[2]) > tolerance:
            return False
    except Exception:
        return False

    # Confirm that the face is parallel to the XY plane.  This prevents a
    # vertical face that happens to cross z=0 from being selected.
    try:
        parameters = face.ParamAtPoint(face.Centroid)
        normal = face.NormalAtParam(parameters[0], parameters[1])
        if abs(float(normal[2])) < 0.99:
            return False
    except Exception:
        return False

    return True


# The build platform is the intended support surface.  Prefer its z=0 face;
# fall back to the part only for templates that do not contain a separate base.
support_body_candidates = [base_body]
if part_body is not base_body:
    support_body_candidates.append(part_body)

z_zero_face_ids = []
for support_body in support_body_candidates:
    try:
        support_faces = list(support_body.GetGeoBody().Faces)
    except Exception as error:
        raise Exception("Could not enumerate support body faces: " + str(error))
    z_zero_face_ids = [face.Id for face in support_faces if face_is_on_z_zero(face)]
    if z_zero_face_ids:
        log_message(
            "Found z=0 support face(s) on body "
            + str(support_body.Name)
            + ": IDs="
            + str(z_zero_face_ids)
        )
        break

if not z_zero_face_ids:
    raise Exception(
        "Could not find an imported support face on the global z=0 plane. "
        "The rotated STEP geometry may not be seated on the build plane."
    )

fixed_support_selection = ExtAPI.SelectionManager.CreateSelectionInfo(
    Ansys.ACT.Interfaces.Common.SelectionTypeEnum.GeometryEntities
)
fixed_support_selection.Ids = z_zero_face_ids

static_analysis = None
for candidate_analysis in mechanical_model.Analyses:
    if str(candidate_analysis.Name).strip().lower() == "static structural":
        static_analysis = candidate_analysis
        break
if static_analysis is None:
    raise Exception("Could not find the Static Structural analysis.")

for existing_support in list(DataModel.GetObjectsByName("LPBF Fixed Support")):
    existing_support.Delete()

fixed_support = static_analysis.AddFixedSupport()
fixed_support.Name = "LPBF Fixed Support"
fixed_support.Location = fixed_support_selection
log_message(
    "Applied LPBF Fixed Support to part face(s) on z=0; face IDs="
    + str(z_zero_face_ids)
)

for selected_analysis in mechanical_model.Analyses:
    log_message(
        "Starting analysis: index="
        + str(list(mechanical_model.Analyses).index(selected_analysis))
        + ", name="
        + str(selected_analysis.Name)
    )
    try:
        # Solve the analysis itself so Mechanical schedules the complete
        # analysis chain and populates fresh result data in this disposable
        # project copy.
        selected_analysis.Solve(True)
    except Exception as error:
        log_message("Analysis solve failed; using synchronous solution call: " + str(error))
        selected_analysis.Solution.Solve(True)
    log_message("Finished analysis: " + str(selected_analysis.Name))



