"""Graphics module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v252.Ansys.Mechanical.Graphics.Tools as Tools


class GraphicsViewportsExportSettings(object):
    """
    
            Settings object to control Graphics.ExportViewports behavior.
            
    """

    @property
    def BorderStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsViewportsExportBorderStyle]:
        """
        
            Specifies which borders to add, if any, to the exported viewports image.
            Border style enum values can be combined via bitwise-or ( | ).
            Defaults to None.
            
        """
        return None

    @property
    def CurrentGraphicsDisplay(self) -> typing.Optional[bool]:
        """
        
            Specifies whether to use the current graphics display settings. Defaults to true.
            
        """
        return None

    @property
    def AppendGraph(self) -> typing.Optional[bool]:
        """
        
            Specifies whether to append the viewport graph(s) to the exported image. Defaults to false.
            
        """
        return None

    @property
    def Resolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsResolutionType]:
        """
        
            Specifies the resolution type. Defaults to NormalResolution.
            
        """
        return None

    @property
    def Capture(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsCaptureType]:
        """
        
            Specifies what to include in the capture. Defaults to ImageAndLegend.
            
        """
        return None

    @property
    def Background(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsBackgroundType]:
        """
        
            Specifies the background color. Defaults to GraphicsAppearanceSetting.
            
        """
        return None

    @property
    def FontMagnification(self) -> typing.Optional[float]:
        """
        
            Specifies the font magnification factor. Defaults to 1.0.
            
        """
        return None

    @property
    def Width(self) -> typing.Optional[int]:
        """
        
            Specifies the image width. Defaults to 0. If width AND height are zero, this uses the current dimensions. If only one of the two are nonzero, the current dimension’s ratio is used along with the nonzero of the two properties to determine the computed value of the zero property.
            
        """
        return None

    @property
    def Height(self) -> typing.Optional[int]:
        """
        
            Specifies the image height. Defaults to 0. If width AND height are zero, this uses the current dimensions. If only one of the two are nonzero, the current dimension’s ratio is used along with the nonzero of the two properties to determine the computed value of the zero property.
            
        """
        return None


class AnnotationPreferences(object):

    @property
    def ShowAllAnnotations(self) -> typing.Optional[bool]:
        """
        Sets the visibility of all annotations.
        """
        return None

    @property
    def ShowCustomAnnotations(self) -> typing.Optional[bool]:
        """
        Sets the visibility of user defined annotations.
        """
        return None

    @property
    def ShowLabels(self) -> typing.Optional[bool]:
        """
        Sets the visibility of annotation labels.
        """
        return None

    @property
    def ShowPointMasses(self) -> typing.Optional[bool]:
        """
        Sets the visibility of point mass annotations.
        """
        return None

    @property
    def ShowBeams(self) -> typing.Optional[bool]:
        """
        Sets the visibility of beam annotations.
        """
        return None

    @property
    def ShowSprings(self) -> typing.Optional[bool]:
        """
        Sets the visibility of spring annotations.
        """
        return None

    @property
    def ShowBearings(self) -> typing.Optional[bool]:
        """
        Sets the visibility of bearing annotations.
        """
        return None

    @property
    def ShowCracks(self) -> typing.Optional[bool]:
        """
        Sets the visibility of crack annotations.
        """
        return None

    @property
    def ShowForceArrows(self) -> typing.Optional[bool]:
        """
        Sets the visibility of force arrows on surface reaction.
        """
        return None

    @property
    def ShowBodyScopings(self) -> typing.Optional[bool]:
        """
        Sets the visibility of body scoping annotations.
        """
        return None

    @property
    def ShowMeshAnnotations(self) -> typing.Optional[bool]:
        """
        Sets the visibility of mesh node and mesh element annotations in named selection displays.
        """
        return None

    @property
    def ShowNodeNumbers(self) -> typing.Optional[bool]:
        """
        Sets the visibility of mesh node numbers in named selection, mesh, and result displays.
        """
        return None

    @property
    def ShowElementNumbers(self) -> typing.Optional[bool]:
        """
        Sets the visibility of mesh element numbers in named Selection, mesh, and result displays.
        """
        return None

    @property
    def ShowNamedSelectionElements(self) -> typing.Optional[bool]:
        """
        Sets the visibility of elements for all items in the named selection group.
        """
        return None

    @property
    def PointMassSize(self) -> typing.Optional[int]:
        """
        Sets the size for point mass annotation. (Small-Large ; 1-100) 
        """
        return None

    @property
    def SpringSize(self) -> typing.Optional[int]:
        """
        Sets the size for spring annotation. (Small-Large ; 1-100)
        """
        return None

    def SetNodeNumbering(self, begin: int, end: int, inc: int) -> None:
        """
        Sets the begin, end and increment values to display node numbering.
        """
        pass

    def SetElementNumbering(self, begin: int, end: int, inc: int) -> None:
        """
        Sets the begin, end and increment values to display element numbering.
        """
        pass


class ResultPreference(object):

    @property
    def GeometryView(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.GeometryView]:
        """
        Sets the result geometry view.
        """
        return None

    @property
    def ContourView(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.ContourView]:
        """
        Sets the result contour view.
        """
        return None

    @property
    def ExtraModelDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.ExtraModelDisplay]:
        """
        Sets the result edge display option.
        """
        return None

    @property
    def DeformationScaling(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.DeformationScaling]:
        """
        Sets the deformation scale multiplier to either AutoScale or TrueScale.
        """
        return None

    @property
    def DeformationScaleMultiplier(self) -> typing.Optional[float]:
        """
        Sets the deformation scale multiplier.
        """
        return None

    @property
    def IsoSurfaceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Sets the capping value for capped iso surface view .
        """
        return None

    @property
    def CappingType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.CappingType]:
        """
        Sets the result capping type.
        """
        return None

    @property
    def ScopingDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Graphics.ScopingDisplay]:
        """
        Sets the result scoping display.
        """
        return None

    @property
    def ShowMinimum(self) -> typing.Optional[bool]:
        """
        Displays the result minimum value annotation label.
        """
        return None

    @property
    def ShowMaximum(self) -> typing.Optional[bool]:
        """
        Displays the result maximum value annotation label.
        """
        return None


class VectorDisplay(object):

    @property
    def LengthType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.VectorLengthType]:
        """
        Sets the result vector length type.
        """
        return None

    @property
    def DisplayType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.VectorDisplayType]:
        """
        Sets the vector display type.
        """
        return None

    @property
    def ControlDisplayDensity(self) -> typing.Optional[bool]:
        """
        Allows control of the vector display density.
        """
        return None

    @property
    def DisplayDensity(self) -> typing.Optional[float]:
        """
        Sets the vector display density in percentage.
        """
        return None

    @property
    def LengthMultiplier(self) -> typing.Optional[float]:
        """
        Sets the vector length multiplier.
        """
        return None

    @property
    def ShowTriadXAxis(self) -> typing.Optional[bool]:
        """
        Displays the X axis vector of the triad/tensor.
        """
        return None

    @property
    def ShowTriadYAxis(self) -> typing.Optional[bool]:
        """
        Displays the Y axis vector of the triad/tensor.
        """
        return None

    @property
    def ShowTriadZAxis(self) -> typing.Optional[bool]:
        """
        Displays the Z axis vector of the triad/tensor.
        """
        return None


class AnalysisSettingsGraph(object):

    @property
    def BoundaryConditionVisibility(self) -> typing.Optional[Ansys.Mechanical.Graphics.BoundaryConditionVisibilityDictionary]:
        """
        BoundaryConditionVisibility property.
        """
        return None


class GlobalLegendSettings(object):
    """
    Defines global legend settings.
    """

    @property
    def LegendOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendOrientationType]:
        """
        Whether the orientation of the legend.
        """
        return None

    @property
    def ShowDateAndTime(self) -> typing.Optional[bool]:
        """
        Whether the  date and time of the legend is shown.
        """
        return None

    @property
    def ShowMinMax(self) -> typing.Optional[bool]:
        """
        Whether the Min and Max value are shown.
        """
        return None

    @property
    def ShowDeformingScaling(self) -> typing.Optional[bool]:
        """
        Whether the Deformation Scaling is shown.
        """
        return None


class AnimationExportSettings(object):

    @property
    def Width(self) -> typing.Optional[int]:
        """
        
            Specifies the video width.
            
        """
        return None

    @property
    def Height(self) -> typing.Optional[int]:
        """
        
            Specifies the video height.
            
        """
        return None


class ResultAnimationOptions(object):

    @property
    def NumberOfFrames(self) -> typing.Optional[int]:
        """
        
            Gets or Sets the Number Of Frames for Distributed Result Animation.
            
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or Sets the Duration for Result Animation.
            
        """
        return None

    @property
    def RangeType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultAnimationRangeType]:
        """
        
            Gets or Sets the Range Type for Result Animation.
            
        """
        return None

    @property
    def UpdateContourRangeAtEachFrame(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets if the Legend Contours will Update at Each Frame.
            
        """
        return None

    @property
    def FitDeformationScalingToAnimation(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets if the Animation Displacement Fits for full range of Time Steps in the Screen.
            
        """
        return None

    @property
    def TimeDecayCycles(self) -> typing.Optional[int]:
        """
        
            Gets or Sets the Number of Cycles for Time Decay.
            
        """
        return None

    @property
    def TimeDecay(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets the Time Decay.
            
        """
        return None

    @property
    def DisplacementTraces(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets if the Displacement Traces are Enabled/Disabled
            
        """
        return None


class SectionPlane(object):
    """
    
            Represents a SectionPlane object. This object holds properties of the Plane.
            
    """

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets the Active State of the Section Plane
            
        """
        return None

    @property
    def Center(self) -> typing.Optional[Ansys.Mechanical.Graphics.Point]:
        """
        
            Gets or Sets the Center point of the Section Plane
            
        """
        return None

    @property
    def Direction(self) -> typing.Optional[Ansys.ACT.Math.Vector3D]:
        """
        
            Gets or Sets the Direction(Normal) of the Section Plane
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or Sets the Name of the Section Plane
            
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SectionPlaneType]:
        """
        
            Gets or Sets the SectionPlane Type of the Section Plane
            
        """
        return None

    def Equals(self, sectionPlane: Ansys.Mechanical.Graphics.SectionPlane) -> bool:
        """
        
             Indicates whether the current SectionPlane properties are equal to the properties of another SectionPlane object.
            
        """
        pass


class SectionPlanes(object):
    """
    
            Represents the collection of section planes used by graphics
            
    """

    @property
    def ShowWholeElement(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets the Element Visibility of the Section Plane
            
        """
        return None

    @property
    def ShowHatching(self) -> typing.Optional[bool]:
        """
        
            Controls whether to render hatch lines (the black parallel lines) on the capped surfaces of section planes. Default: true
            
        """
        return None

    @property
    def Capping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SectionPlaneCappingType]:
        """
        
            Gets or Sets the Capping style of the Section Plane
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            The number of section planes in the collection.
            
        """
        return None

    def CreateSectionPlane(self, coordinateSystem: Ansys.ACT.Automation.Mechanical.CoordinateSystem, planeOrientation: Ansys.Mechanical.DataModel.MechanicalEnums.Common.PlaneOrientation) -> Ansys.Mechanical.Graphics.SectionPlane:
        """
        Creates a SectionPlane based on a coordinate system and plane orientation.
        """
        pass

    def Add(self, sectionPlane: Ansys.Mechanical.Graphics.SectionPlane) -> None:
        """
        
            Adds the given SectionPlane object to the collection to modify the view. Currently only 6 SectionPlane objects in the collection can be activated at once.
            
        """
        pass

    def Clear(self) -> None:
        """
        
            Clears the collection of all SectionPlane objects.
            
        """
        pass

    def Remove(self, sectionPlane: Ansys.Mechanical.Graphics.SectionPlane) -> bool:
        """
        
            Removes the requested SectionPlane from the collection.
            
        """
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the SectionPlane at the given index.
            
        """
        pass


class Graphics3DExportSettings(object):

    @property
    def Background(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsBackgroundType]:
        """
        
            Specifies the background color.
            
        """
        return None


class GraphicsImageExportSettings(object):

    @property
    def CurrentGraphicsDisplay(self) -> typing.Optional[bool]:
        """
        
            Specifies whether to use the current graphics display settings. Defaults to true.
            
        """
        return None

    @property
    def AppendGraph(self) -> typing.Optional[bool]:
        """
        
            Specifies whether to append the viewport graph(s) to the exported image. Defaults to false.
            
        """
        return None

    @property
    def Resolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsResolutionType]:
        """
        
            Specifies the resolution type. Defaults to NormalResolution.
            
        """
        return None

    @property
    def Capture(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsCaptureType]:
        """
        
            Specifies what to include in the capture. Defaults to ImageAndLegend.
            
        """
        return None

    @property
    def Background(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphicsBackgroundType]:
        """
        
            Specifies the background color. Defaults to GraphicsAppearanceSetting.
            
        """
        return None

    @property
    def FontMagnification(self) -> typing.Optional[float]:
        """
        
            Specifies the font magnification factor. Defaults to 1.0.
            
        """
        return None

    @property
    def Width(self) -> typing.Optional[int]:
        """
        
            Specifies the image width. Defaults to 0. If width AND height are zero, this uses the current dimensions. If only one of the two are nonzero, the current dimension’s ratio is used along with the nonzero of the two properties to determine the computed value of the zero property.
            
        """
        return None

    @property
    def Height(self) -> typing.Optional[int]:
        """
        
            Specifies the image height. Defaults to 0. If width AND height are zero, this uses the current dimensions. If only one of the two are nonzero, the current dimension’s ratio is used along with the nonzero of the two properties to determine the computed value of the zero property.
            
        """
        return None


class Point(object):

    @property
    def Location(self) -> typing.Optional[typing.List[float]]:
        """
        
             The location of the Point.
            
        """
        return None

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        
            The length unit of the Point.
            
        """
        return None

    @classmethod
    def ConvertUnit(cls, inPoint: Ansys.Mechanical.Graphics.Point, outputUnit: str) -> Ansys.Mechanical.Graphics.Point:
        """
        
            Returns a new Point given new unit.
            
        """
        pass

    @classmethod
    def op_Equality(cls, a: Ansys.Mechanical.Graphics.Point, b: Ansys.Mechanical.Graphics.Point) -> bool:
        """
        Equal operator
        """
        pass

    @classmethod
    def op_Inequality(cls, a: Ansys.Mechanical.Graphics.Point, b: Ansys.Mechanical.Graphics.Point) -> bool:
        """
        Not-Equal operator
        """
        pass

    def Equals(self, o: typing.Any) -> bool:
        """
        Object.Equals(object o) override
        """
        pass

    def GetHashCode(self) -> int:
        """
        Object.GetHashCode() override
        """
        pass


class ViewOptions(object):

    @property
    def VectorDisplay(self) -> typing.Optional[Ansys.Mechanical.Graphics.VectorDisplay]:
        """
        VectorDisplay property.
        """
        return None

    @property
    def ResultPreference(self) -> typing.Optional[Ansys.Mechanical.Graphics.ResultPreference]:
        """
        ResultPreference property.
        """
        return None

    @property
    def AnnotationPreferences(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnnotationPreferences]:
        """
        AnnotationPreferences property.
        """
        return None

    @property
    def ShowShellThickness(self) -> typing.Optional[bool]:
        """
        Displays the thickness of shells.
        """
        return None

    @property
    def ShowBeamThickness(self) -> typing.Optional[bool]:
        """
        Displays the thickness of beams.
        """
        return None

    @property
    def ShowSPHExpansion(self) -> typing.Optional[bool]:
        """
        Displays the expansion for SPH elements.
        """
        return None

    @property
    def ShowMesh(self) -> typing.Optional[bool]:
        """
        Display the model's mesh.
        """
        return None

    @property
    def ShowRandomColors(self) -> typing.Optional[bool]:
        """
        Sets random colors for each object of the application.
        """
        return None

    @property
    def ShowVertices(self) -> typing.Optional[bool]:
        """
        Display all the vertices of the model.
        """
        return None

    @property
    def ShowClusteredVertices(self) -> typing.Optional[bool]:
        """
        Displays all closely clustered vertices of the model.
        """
        return None

    @property
    def ShowEdgeDirection(self) -> typing.Optional[bool]:
        """
        Displays the edge direction arrow.
        """
        return None

    @property
    def ShowMeshConnection(self) -> typing.Optional[bool]:
        """
        Displays edge connection using a color scheme based on the mesh connection information.
        """
        return None

    @property
    def ShowThickEdgeScoping(self) -> typing.Optional[bool]:
        """
        Thicken the display of edge scoping.
        """
        return None

    @property
    def ModelDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ModelDisplay]:
        """
        Sets the model display option.
        """
        return None

    @property
    def ModelColoring(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ModelColoring]:
        """
        Sets the Model display Coloring.
        """
        return None

    @property
    def ShowCoordinateSystems(self) -> typing.Optional[bool]:
        """
        Displays all coordinate system defined.
        """
        return None

    @property
    def ClusteredVertexTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Sets the clustered vertices custom tolerance value.
        """
        return None

    @property
    def ShowLegend(self) -> typing.Optional[bool]:
        """
        Displays the legend.
        """
        return None

    @property
    def ShowTriad(self) -> typing.Optional[bool]:
        """
        Displays the triad.
        """
        return None

    @property
    def ShowRuler(self) -> typing.Optional[bool]:
        """
        Displays the ruler.
        """
        return None

    @property
    def ShowResultVectors(self) -> typing.Optional[bool]:
        """
        Displays the result vectors.
        """
        return None

    @property
    def ShowRemotePointConnections(self) -> typing.Optional[bool]:
        """
        Displays the Remote Point Connections.
        """
        return None

    @property
    def DisplayGraphOverlay(self) -> typing.Optional[bool]:
        """
        Display Graph overlay in the current viewport.
        """
        return None

    def RescaleAnnotations(self) -> None:
        """
        Rescale size of annotation following a zoom in or zoom out of the model.
        """
        pass


