"""ResultTrackers module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ContactForceTracker(object):
    """
    Defines a ContactForceTracker.
    """

    @property
    def ContactRegion(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the ContactRegion.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class LSDYNAGeneralTracker(object):
    """
    Defines a LSDYNAGeneralTracker.
    """

    @property
    def LSDYNABranchName(self) -> typing.Optional[str]:
        """
        Gets or sets the LSDYNA BranchName.
        """
        return None

    @property
    def LSDYNASubBranchName(self) -> typing.Optional[str]:
        """
        Gets or sets the LSDYNA SubBranchName.
        """
        return None

    @property
    def LSDYNAComponentName(self) -> typing.Optional[str]:
        """
        Gets or sets the LSDYNA ComponentName.
        """
        return None

    @property
    def ContactRegion(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the ContactRegion.
        """
        return None

    @property
    def Joint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the Joint.
        """
        return None

    @property
    def ACTLoad(self) -> typing.Optional[Ansys.ACT.Interfaces.DataModel.IDataModelObject]:
        """
        Gets or sets the ACT Load.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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

    def GetBranches(self) -> typing.List[str]:
        """
        GetBranches method.
        """
        pass

    def GetComponents(self, branch: str) -> typing.List[str]:
        """
        GetComponents method.
        """
        pass

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


class CampbellDiagram(object):
    """
    Defines a CampbellDiagram.
    """

    @property
    def RotationalVelocitySelection(self) -> typing.Optional[typing.Any]:
        """
        Gets or sets the Rotational Velocity Selection Type.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Ratio(self) -> typing.Optional[float]:
        """
        Gets or sets the Ratio.
        """
        return None

    @property
    def XAxisLabel(self) -> typing.Optional[str]:
        """
        Gets or sets the XAxisLabel.
        """
        return None

    @property
    def YAxisLabel(self) -> typing.Optional[str]:
        """
        Gets or sets the YAxisLabel.
        """
        return None

    @property
    def XAxisMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the XAxisMaximum.
        """
        return None

    @property
    def XAxisMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the XAxisMinimum.
        """
        return None

    @property
    def YAxisMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the YAxisMaximum.
        """
        return None

    @property
    def YAxisMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the YAxisMinimum.
        """
        return None

    @property
    def XAxisRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DSCampbellAxisRange]:
        """
        Gets or sets the XAxisRange.
        """
        return None

    @property
    def YAxisData(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DSCampbellYAxisDataType]:
        """
        Gets or sets the YAxisData.
        """
        return None

    @property
    def YAxisRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DSCampbellAxisRange]:
        """
        Gets or sets the YAxisRange.
        """
        return None

    @property
    def CriticalSpeed(self) -> typing.Optional[bool]:
        """
        Gets or sets the CriticalSpeed.
        """
        return None

    @property
    def Sorting(self) -> typing.Optional[bool]:
        """
        Gets or sets the Sorting.
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


class AddedMassTracker(object):
    """
    Defines a AddedMassTracker.
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


class ArtificialEnergyTracker(object):
    """
    Defines a ArtificialEnergyTracker.
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


class ContactChatteringTracker(object):
    """
    Defines a ContactChatteringTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactClosedPenetrationTracker(object):
    """
    Defines a ContactClosedPenetrationTracker.
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


class ContactDepthTracker(object):
    """
    Defines a ContactDepthTracker.
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


class ContactElasticSlipTracker(object):
    """
    Defines a ContactElasticSlipTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactEnergyTracker(object):
    """
    Defines a ContactEnergyTracker.
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


class ContactFluidPressureTracker(object):
    """
    Defines a ContactFluidPressureTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactFrictionalDissipationEnergyTracker(object):
    """
    Defines a ContactFrictionalDissipationEnergyTracker.
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


class ContactFrictionalStressTracker(object):
    """
    Defines a ContactFrictionalStressTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactGapTracker(object):
    """
    Defines a ContactGapTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactHeatFluxTracker(object):
    """
    Defines a ContactHeatFluxTracker.
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


class ContactingAreaTracker(object):
    """
    Defines a ContactingAreaTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMaximumDampingPressureTracker(object):
    """
    Defines a ContactMaximumDampingPressureTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMaximumGeometricSlidingDistanceTracker(object):
    """
    Defines a ContactMaximumGeometricSlidingDistanceTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMaximumNormalStiffnessTracker(object):
    """
    Defines a ContactMaximumNormalStiffnessTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMaximumTangentialStiffnessTracker(object):
    """
    Defines a ContactMaximumTangentialStiffnessTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMaxTangentialFluidPressureTracker(object):
    """
    Defines a ContactMaxTangentialFluidPressureTracker.
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


class ContactMinimumGeometricSlidingDistanceTracker(object):
    """
    Defines a ContactMinimumGeometricSlidingDistanceTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactMinimumNormalStiffnessTracker(object):
    """
    Defines a ContactMinimumNormalStiffnessTracker.
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


class ContactMinimumTangentialStiffnessTracker(object):
    """
    Defines a ContactMinimumTangentialStiffnessTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactNumberStickingTracker(object):
    """
    Defines a ContactNumberStickingTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactNumberWithLargePenetrationTracker(object):
    """
    Defines a ContactNumberWithLargePenetrationTracker.
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


class ContactNumberWithTooMuchSlidingTracker(object):
    """
    Defines a ContactNumberWithTooMuchSlidingTracker.
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


class ContactPairForceConvergenceNormTracker(object):
    """
    Defines a ContactPairForceConvergenceNormTracker.
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


class ContactPenetrationTracker(object):
    """
    Defines a ContactPenetrationTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactPossibleOverconstraintTracker(object):
    """
    Defines a ContactPossibleOverconstraintTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactPressureTracker(object):
    """
    Defines a ContactPressureTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactResultingPinballTracker(object):
    """
    Defines a ContactResultingPinballTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactSlidingDistanceTracker(object):
    """
    Defines a ContactSlidingDistanceTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class ContactSlidingIndicationTracker(object):
    """
    Defines a ContactSlidingIndicationTracker.
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


class ContactStabilizationEnergyTracker(object):
    """
    Defines a ContactStabilizationEnergyTracker.
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


class ContactStrainEnergyTracker(object):
    """
    Defines a ContactStrainEnergyTracker.
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


class ContactTangentialDampingStressTracker(object):
    """
    Defines a ContactTangentialDampingStressTracker.
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


class ContactTotalForceFromContactPressureXTracker(object):
    """
    Defines a ContactTotalForceFromContactPressureXTracker.
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


class ContactTotalForceFromContactPressureYTracker(object):
    """
    Defines a ContactTotalForceFromContactPressureYTracker.
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


class ContactTotalForceFromContactPressureZTracker(object):
    """
    Defines a ContactTotalForceFromContactPressureZTracker.
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


class ContactTotalForceFromTangentialStressXTracker(object):
    """
    Defines a ContactTotalForceFromTangentialStressXTracker.
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


class ContactTotalForceFromTangentialStressYTracker(object):
    """
    Defines a ContactTotalForceFromTangentialStressYTracker.
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


class ContactTotalForceFromTangentialStressZTracker(object):
    """
    Defines a ContactTotalForceFromTangentialStressZTracker.
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


class ContactVolumeLossDueToWearTracker(object):
    """
    Defines a ContactVolumeLossDueToWearTracker.
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


class DampingEnergyTracker(object):
    """
    Defines a DampingEnergyTracker.
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


class DensityTracker(object):
    """
    Defines a DensityTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class DirectionalAccelerationTracker(object):
    """
    Defines a DirectionalAccelerationTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class DirectionalDeformationTracker(object):
    """
    Defines a DirectionalDeformationTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class DirectionalVelocityTracker(object):
    """
    Defines a DirectionalVelocityTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class EffectiveStrainTracker(object):
    """
    Defines a EffectiveStrainTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class EffectiveStressTracker(object):
    """
    Defines a EffectiveStressTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class ErodedInternalEnergyTracker(object):
    """
    Defines a ErodedInternalEnergyTracker.
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


class ErodedKineticEnergyTracker(object):
    """
    Defines a ErodedKineticEnergyTracker.
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


class ExternalForceTracker(object):
    """
    Defines a ExternalForceTracker.
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


class ForceReactionTracker(object):
    """
    Defines a ForceReactionTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def ForceComponentMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ForceComponentSelectionType]:
        """
        Gets or sets the ForceComponentMethod.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class HourglassEnergyTracker(object):
    """
    Defines a HourglassEnergyTracker.
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


class InternalEnergyTracker(object):
    """
    Defines a InternalEnergyTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class KineticEnergyTracker(object):
    """
    Defines a KineticEnergyTracker.
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


class MomentReactionTracker(object):
    """
    Defines a MomentReactionTracker.
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


class MomentumTracker(object):
    """
    Defines a MomentumTracker.
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


class NonLinearStabilizationEnergyTracker(object):
    """
    Defines a NonLinearStabilizationEnergyTracker.
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


class NumberContactingTracker(object):
    """
    Defines a NumberContactingTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactSide(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactScopingType]:
        """
        Gets or sets the ContactSide.
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


class PlasticWorkTracker(object):
    """
    Defines a PlasticWorkTracker.
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


class PositionTracker(object):
    """
    Defines a PositionTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class PressureTracker(object):
    """
    Defines a PressureTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class RigidBodyVelocityTracker(object):
    """
    Defines a RigidBodyVelocityTracker.
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


class SpringDampingForceTracker(object):
    """
    Defines a SpringDampingForceTracker.
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


class SpringElasticForceTracker(object):
    """
    Defines a SpringElasticForceTracker.
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


class SpringElongationTracker(object):
    """
    Defines a SpringElongationTracker.
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


class SpringVelocityTracker(object):
    """
    Defines a SpringVelocityTracker.
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


class StiffnessEnergyTracker(object):
    """
    Defines a StiffnessEnergyTracker.
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


class TemperatureTracker(object):
    """
    Defines a TemperatureTracker.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultChartAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LocationXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationXCoordinate.
        """
        return None

    @property
    def LocationYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationYCoordinate.
        """
        return None

    @property
    def LocationZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocationZCoordinate.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def LocationCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LocationCoordinateSystem.
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


class TotalEnergyTracker(object):
    """
    Defines a TotalEnergyTracker.
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


class TotalMassAverageVelocityTracker(object):
    """
    Defines a TotalMassAverageVelocityTracker.
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


