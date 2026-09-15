"""PhaseResponseResults module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AccelerationPhaseResponse(object):
    """
    Defines a AccelerationPhaseResponse.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactRegion(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegion.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def ChartDimensions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartDimensions]:
        """
        Gets or sets the Chart Dimensions
        """
        return None

    @property
    def BoundaryCondition(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.BoundaryConditions.GenericBoundaryCondition]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CutFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutFrequency.
        """
        return None

    @property
    def SectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SectorNumber.
        """
        return None

    @property
    def GeometrySelectionString(self) -> typing.Optional[str]:
        """
        Gets or sets the GeometrySelectionString.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Duration.
        """
        return None

    @property
    def FilterMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMaximum.
        """
        return None

    @property
    def FilterMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMinimum.
        """
        return None

    @property
    def FrequencyAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FrequencyAtMaximumAmplitude.
        """
        return None

    @property
    def ImaginaryAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImaginaryAtMaximumAmplitude.
        """
        return None

    @property
    def MaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAmplitude.
        """
        return None

    @property
    def MaximumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumFrequency.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MinimumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumFrequency.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def PhaseAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PhaseAngle.
        """
        return None

    @property
    def RealAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RealAtMaximumAmplitude.
        """
        return None

    @property
    def RequestedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RequestedFrequency.
        """
        return None

    @property
    def AccelerationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the AccelerationType.
        """
        return None

    @property
    def ChartViewingStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartAxisScaleType]:
        """
        Gets or sets the ChartViewingStyle.
        """
        return None

    @property
    def DeformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the DeformationType.
        """
        return None

    @property
    def FilterType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FilterType]:
        """
        Gets or sets the FilterType.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultipleNodeType]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def NormalOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NormalOrientationType]:
        """
        Gets or sets the NormalOrientation.
        """
        return None

    @property
    def CurvesAppearanceDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartPlotStyle]:
        """
        Gets or sets the CurvesAppearanceDisplay.
        """
        return None

    @property
    def ResultChartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartResultType]:
        """
        Gets the ResultChartType.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def XAxisValues(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.XAxisValues]:
        """
        Gets or sets the XAxisValues.
        """
        return None

    @property
    def ShearOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShearOrientationType]:
        """
        Gets or sets the ShearOrientation.
        """
        return None

    @property
    def StressStrainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StressStrainType]:
        """
        Gets or sets the StressStrainType.
        """
        return None

    @property
    def TimeHistoryDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeHistoryDisplayType]:
        """
        Gets or sets the TimeHistoryDisplay.
        """
        return None

    @property
    def VelocityType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the VelocityType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def EnhancedTracking(self) -> typing.Optional[bool]:
        """
        Gets the EnhancedTracking.
        """
        return None

    @property
    def UseParentFrequencyRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseParentFrequencyRange.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class DeformationPhaseResponse(object):
    """
    Defines a DeformationPhaseResponse.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def ChartDimensions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartDimensions]:
        """
        Gets or sets the Chart Dimensions
        """
        return None

    @property
    def BoundaryCondition(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.BoundaryConditions.GenericBoundaryCondition]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CutFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutFrequency.
        """
        return None

    @property
    def SectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SectorNumber.
        """
        return None

    @property
    def GeometrySelectionString(self) -> typing.Optional[str]:
        """
        Gets or sets the GeometrySelectionString.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Duration.
        """
        return None

    @property
    def FilterMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMaximum.
        """
        return None

    @property
    def FilterMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMinimum.
        """
        return None

    @property
    def FrequencyAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FrequencyAtMaximumAmplitude.
        """
        return None

    @property
    def ImaginaryAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImaginaryAtMaximumAmplitude.
        """
        return None

    @property
    def MaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAmplitude.
        """
        return None

    @property
    def MaximumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumFrequency.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MinimumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumFrequency.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def PhaseAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PhaseAngle.
        """
        return None

    @property
    def RealAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RealAtMaximumAmplitude.
        """
        return None

    @property
    def RequestedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RequestedFrequency.
        """
        return None

    @property
    def AccelerationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the AccelerationType.
        """
        return None

    @property
    def ChartViewingStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartAxisScaleType]:
        """
        Gets or sets the ChartViewingStyle.
        """
        return None

    @property
    def DeformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the DeformationType.
        """
        return None

    @property
    def FilterType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FilterType]:
        """
        Gets or sets the FilterType.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultipleNodeType]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def NormalOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NormalOrientationType]:
        """
        Gets or sets the NormalOrientation.
        """
        return None

    @property
    def CurvesAppearanceDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartPlotStyle]:
        """
        Gets or sets the CurvesAppearanceDisplay.
        """
        return None

    @property
    def ResultChartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartResultType]:
        """
        Gets the ResultChartType.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def XAxisValues(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.XAxisValues]:
        """
        Gets or sets the XAxisValues.
        """
        return None

    @property
    def ShearOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShearOrientationType]:
        """
        Gets or sets the ShearOrientation.
        """
        return None

    @property
    def StressStrainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StressStrainType]:
        """
        Gets or sets the StressStrainType.
        """
        return None

    @property
    def TimeHistoryDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeHistoryDisplayType]:
        """
        Gets or sets the TimeHistoryDisplay.
        """
        return None

    @property
    def VelocityType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the VelocityType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def EnhancedTracking(self) -> typing.Optional[bool]:
        """
        Gets the EnhancedTracking.
        """
        return None

    @property
    def UseParentFrequencyRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseParentFrequencyRange.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class ElasticStrainPhaseResponse(object):
    """
    Defines a ElasticStrainPhaseResponse.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactRegion(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegion.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def ChartDimensions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartDimensions]:
        """
        Gets or sets the Chart Dimensions
        """
        return None

    @property
    def BoundaryCondition(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.BoundaryConditions.GenericBoundaryCondition]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CutFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutFrequency.
        """
        return None

    @property
    def SectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SectorNumber.
        """
        return None

    @property
    def GeometrySelectionString(self) -> typing.Optional[str]:
        """
        Gets or sets the GeometrySelectionString.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Duration.
        """
        return None

    @property
    def FilterMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMaximum.
        """
        return None

    @property
    def FilterMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMinimum.
        """
        return None

    @property
    def FrequencyAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FrequencyAtMaximumAmplitude.
        """
        return None

    @property
    def ImaginaryAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImaginaryAtMaximumAmplitude.
        """
        return None

    @property
    def MaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAmplitude.
        """
        return None

    @property
    def MaximumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumFrequency.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MinimumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumFrequency.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def PhaseAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PhaseAngle.
        """
        return None

    @property
    def RealAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RealAtMaximumAmplitude.
        """
        return None

    @property
    def RequestedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RequestedFrequency.
        """
        return None

    @property
    def AccelerationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the AccelerationType.
        """
        return None

    @property
    def ChartViewingStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartAxisScaleType]:
        """
        Gets or sets the ChartViewingStyle.
        """
        return None

    @property
    def DeformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the DeformationType.
        """
        return None

    @property
    def FilterType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FilterType]:
        """
        Gets or sets the FilterType.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultipleNodeType]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def NormalOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NormalOrientationType]:
        """
        Gets or sets the NormalOrientation.
        """
        return None

    @property
    def CurvesAppearanceDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartPlotStyle]:
        """
        Gets or sets the CurvesAppearanceDisplay.
        """
        return None

    @property
    def ResultChartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartResultType]:
        """
        Gets the ResultChartType.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def XAxisValues(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.XAxisValues]:
        """
        Gets or sets the XAxisValues.
        """
        return None

    @property
    def ShearOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShearOrientationType]:
        """
        Gets or sets the ShearOrientation.
        """
        return None

    @property
    def StressStrainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StressStrainType]:
        """
        Gets or sets the StressStrainType.
        """
        return None

    @property
    def TimeHistoryDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeHistoryDisplayType]:
        """
        Gets or sets the TimeHistoryDisplay.
        """
        return None

    @property
    def VelocityType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the VelocityType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def EnhancedTracking(self) -> typing.Optional[bool]:
        """
        Gets the EnhancedTracking.
        """
        return None

    @property
    def UseParentFrequencyRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseParentFrequencyRange.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class StressPhaseResponse(object):
    """
    Defines a StressPhaseResponse.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def ChartDimensions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartDimensions]:
        """
        Gets or sets the Chart Dimensions
        """
        return None

    @property
    def BoundaryCondition(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.BoundaryConditions.GenericBoundaryCondition]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CutFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutFrequency.
        """
        return None

    @property
    def SectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SectorNumber.
        """
        return None

    @property
    def GeometrySelectionString(self) -> typing.Optional[str]:
        """
        Gets or sets the GeometrySelectionString.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Duration.
        """
        return None

    @property
    def FilterMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMaximum.
        """
        return None

    @property
    def FilterMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMinimum.
        """
        return None

    @property
    def FrequencyAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FrequencyAtMaximumAmplitude.
        """
        return None

    @property
    def ImaginaryAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImaginaryAtMaximumAmplitude.
        """
        return None

    @property
    def MaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAmplitude.
        """
        return None

    @property
    def MaximumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumFrequency.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MinimumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumFrequency.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def PhaseAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PhaseAngle.
        """
        return None

    @property
    def RealAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RealAtMaximumAmplitude.
        """
        return None

    @property
    def RequestedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RequestedFrequency.
        """
        return None

    @property
    def AccelerationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the AccelerationType.
        """
        return None

    @property
    def ChartViewingStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartAxisScaleType]:
        """
        Gets or sets the ChartViewingStyle.
        """
        return None

    @property
    def DeformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the DeformationType.
        """
        return None

    @property
    def FilterType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FilterType]:
        """
        Gets or sets the FilterType.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultipleNodeType]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def NormalOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NormalOrientationType]:
        """
        Gets or sets the NormalOrientation.
        """
        return None

    @property
    def CurvesAppearanceDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartPlotStyle]:
        """
        Gets or sets the CurvesAppearanceDisplay.
        """
        return None

    @property
    def ResultChartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartResultType]:
        """
        Gets the ResultChartType.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def XAxisValues(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.XAxisValues]:
        """
        Gets or sets the XAxisValues.
        """
        return None

    @property
    def ShearOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShearOrientationType]:
        """
        Gets or sets the ShearOrientation.
        """
        return None

    @property
    def StressStrainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StressStrainType]:
        """
        Gets or sets the StressStrainType.
        """
        return None

    @property
    def TimeHistoryDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeHistoryDisplayType]:
        """
        Gets or sets the TimeHistoryDisplay.
        """
        return None

    @property
    def VelocityType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the VelocityType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def EnhancedTracking(self) -> typing.Optional[bool]:
        """
        Gets the EnhancedTracking.
        """
        return None

    @property
    def UseParentFrequencyRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseParentFrequencyRange.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class VelocityPhaseResponse(object):
    """
    Defines a VelocityPhaseResponse.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactRegion(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegion.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def ChartDimensions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartDimensions]:
        """
        Gets or sets the Chart Dimensions
        """
        return None

    @property
    def BoundaryCondition(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.BoundaryConditions.GenericBoundaryCondition]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CutFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutFrequency.
        """
        return None

    @property
    def SectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SectorNumber.
        """
        return None

    @property
    def GeometrySelectionString(self) -> typing.Optional[str]:
        """
        Gets or sets the GeometrySelectionString.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Duration(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Duration.
        """
        return None

    @property
    def FilterMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMaximum.
        """
        return None

    @property
    def FilterMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FilterMinimum.
        """
        return None

    @property
    def FrequencyAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the FrequencyAtMaximumAmplitude.
        """
        return None

    @property
    def ImaginaryAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImaginaryAtMaximumAmplitude.
        """
        return None

    @property
    def MaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAmplitude.
        """
        return None

    @property
    def MaximumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumFrequency.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MinimumFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumFrequency.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def PhaseAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PhaseAngle.
        """
        return None

    @property
    def RealAtMaximumAmplitude(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RealAtMaximumAmplitude.
        """
        return None

    @property
    def RequestedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RequestedFrequency.
        """
        return None

    @property
    def AccelerationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the AccelerationType.
        """
        return None

    @property
    def ChartViewingStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartAxisScaleType]:
        """
        Gets or sets the ChartViewingStyle.
        """
        return None

    @property
    def DeformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the DeformationType.
        """
        return None

    @property
    def FilterType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FilterType]:
        """
        Gets or sets the FilterType.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultipleNodeType]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def NormalOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NormalOrientationType]:
        """
        Gets or sets the NormalOrientation.
        """
        return None

    @property
    def CurvesAppearanceDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartPlotStyle]:
        """
        Gets or sets the CurvesAppearanceDisplay.
        """
        return None

    @property
    def ResultChartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ChartResultType]:
        """
        Gets the ResultChartType.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def XAxisValues(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.XAxisValues]:
        """
        Gets or sets the XAxisValues.
        """
        return None

    @property
    def ShearOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShearOrientationType]:
        """
        Gets or sets the ShearOrientation.
        """
        return None

    @property
    def StressStrainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StressStrainType]:
        """
        Gets or sets the StressStrainType.
        """
        return None

    @property
    def TimeHistoryDisplay(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeHistoryDisplayType]:
        """
        Gets or sets the TimeHistoryDisplay.
        """
        return None

    @property
    def VelocityType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TotalOrDirectional]:
        """
        Gets or sets the VelocityType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def EnhancedTracking(self) -> typing.Optional[bool]:
        """
        Gets the EnhancedTracking.
        """
        return None

    @property
    def UseParentFrequencyRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseParentFrequencyRange.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


