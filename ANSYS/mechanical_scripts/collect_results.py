"""Embedded Mechanical stage: extract stress values and export a screenshot."""

import json
import re


SCREENSHOT_FILE = __SCREENSHOT_FILE__

# Camera values copied from Mechanical with "Copy View > Copy as MAPDL
# Command".  The source commands use metres, as indicated by the exported
# header.  Mechanical's ViewVector is normalized below because the copied
# /VIEW vector is scaled to approximately 0.001.
VIEW_FOCUS_M = (0.008342013301263, -0.012573704245853, 0.015762699464743)
VIEW_VECTOR = (0.655792665976, 0.694077745751, 0.296971483657)
VIEW_ROLL_DEGREES = -107.872213543911641


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


def apply_export_camera():
    """Apply the camera copied from Mechanical's APDL view commands."""
    from Ansys.ACT.Math import Vector3D
    from Ansys.Mechanical.Graphics import Point

    camera = ExtAPI.Graphics.Camera
    camera.FocalPoint = Point(list(VIEW_FOCUS_M), "m")
    camera.ViewVector = Vector3D(*VIEW_VECTOR)

    # /ANG is the roll about the view axis.  RotateView preserves the focal
    # point and view direction while applying that roll to the screenshot.
    camera.RotateView(VIEW_ROLL_DEGREES)

    # /DIST is not the same thing as SceneHeight or SceneWidth.  Fit the
    # complete imported model in the current view instead of using the APDL
    # camera distance as a viewport size, which can crop the result badly.
    camera.SetFit(None)


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

screenshot_error = ""
if SCREENSHOT_FILE:
    try:
        from Ansys.Mechanical.DataModel.Enums import GraphicsImageExportFormat
        from Ansys.Mechanical.Graphics import GraphicsImageExportSettings

        equivalent_stress.Activate()
        apply_export_camera()
        screenshot_settings = GraphicsImageExportSettings()
        # ANSYS requires this to be false when Width/Height are specified.
        # With True, v261 reports: "Invalid image export setting".
        screenshot_settings.CurrentGraphicsDisplay = False
        screenshot_settings.Width = 1920
        screenshot_settings.Height = 1080
        ExtAPI.Graphics.ExportImage(
            SCREENSHOT_FILE,
            GraphicsImageExportFormat.PNG,
            screenshot_settings,
        )
        ExtAPI.Log.WriteMessage("Stress screenshot exported: " + SCREENSHOT_FILE)
    except Exception as error:
        screenshot_error = "Custom-resolution export failed: " + str(error)
        ExtAPI.Log.WriteMessage(
            "Stress screenshot export failed; continuing: " + screenshot_error
        )
        # The documented default-settings path is a useful compatibility
        # fallback for Mechanical installations that reject custom settings.
        try:
            equivalent_stress.Activate()
            apply_export_camera()
            fallback_settings = GraphicsImageExportSettings()
            ExtAPI.Graphics.ExportImage(
                SCREENSHOT_FILE,
                GraphicsImageExportFormat.PNG,
                fallback_settings,
            )
            screenshot_error = (
                screenshot_error + "; default-settings fallback succeeded"
            )
            ExtAPI.Log.WriteMessage(
                "Stress screenshot exported with default settings: "
                + SCREENSHOT_FILE
            )
        except Exception as fallback_error:
            screenshot_error = (
                screenshot_error + "; default-settings fallback failed: "
                + str(fallback_error)
            )
            ExtAPI.Log.WriteMessage(
                "Stress screenshot fallback failed; continuing: "
                + str(fallback_error)
            )

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
    "screenshot_file": SCREENSHOT_FILE,
    "screenshot_error": screenshot_error,
}

json.dumps(stress_results)



