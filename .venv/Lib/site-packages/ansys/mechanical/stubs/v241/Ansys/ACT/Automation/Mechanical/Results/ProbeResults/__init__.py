"""ProbeResults module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ReactionProbe(object):
    """
    Defines a ReactionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MaximumHeat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumHeat.
        """
        return None

    @property
    def MinimumHeat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumHeat.
        """
        return None

    @property
    def Heat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Heat.
        """
        return None

    @property
    def Extraction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeExtractionType]:
        """
        Gets or sets the Extraction.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class BoltPretensionProbe(object):
    """
    Defines a BoltPretensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScaleFactorValue(self) -> typing.Optional[float]:
        """
        Gets or sets the ScaleFactorValue.
        """
        return None

    @property
    def Adjustment(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Adjustment.
        """
        return None

    @property
    def MaximumAdjustment(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAdjustment.
        """
        return None

    @property
    def MaximumWorkingLoad(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumWorkingLoad.
        """
        return None

    @property
    def MinimumAdjustment(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumAdjustment.
        """
        return None

    @property
    def MinimumWorkingLoad(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumWorkingLoad.
        """
        return None

    @property
    def WorkingLoad(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the WorkingLoad.
        """
        return None

    @property
    def ScaleFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScaleFactorType]:
        """
        Gets or sets the ScaleFactor.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class BeamProbe(object):
    """
    Defines a BoltPretensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def AxialForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the AxialForce.
        """
        return None

    @property
    def MaximumAxialForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumAxialForce.
        """
        return None

    @property
    def MaximumMomentAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMomentAtI.
        """
        return None

    @property
    def MaximumMomentAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMomentAtJ.
        """
        return None

    @property
    def MaximumShearForceAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumShearForceAtI.
        """
        return None

    @property
    def MaximumShearForceAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumShearForceAtJ.
        """
        return None

    @property
    def MaximumTorque(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTorque.
        """
        return None

    @property
    def MinimumAxialForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumAxialForce.
        """
        return None

    @property
    def MinimumMomentAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMomentAtI.
        """
        return None

    @property
    def MinimumMomentAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMomentAtJ.
        """
        return None

    @property
    def MinimumShearForceAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumShearForceAtI.
        """
        return None

    @property
    def MinimumShearForceAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumShearForceAtJ.
        """
        return None

    @property
    def MinimumTorque(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTorque.
        """
        return None

    @property
    def MomentAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MomentAtI.
        """
        return None

    @property
    def MomentAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MomentAtJ.
        """
        return None

    @property
    def ShearForceAtI(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ShearForceAtI.
        """
        return None

    @property
    def ShearForceAtJ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ShearForceAtJ.
        """
        return None

    @property
    def Torque(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Torque.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class BearingProbe(object):
    """
    Defines a BoltPretensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScaleFactorValue(self) -> typing.Optional[float]:
        """
        Gets or sets the ScaleFactorValue.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def DampingForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the DampingForce1.
        """
        return None

    @property
    def DampingForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the DampingForce2.
        """
        return None

    @property
    def Elongation1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Elongation1.
        """
        return None

    @property
    def Elongation2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Elongation2.
        """
        return None

    @property
    def ElasticForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ElasticForce1.
        """
        return None

    @property
    def ElasticForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ElasticForce2.
        """
        return None

    @property
    def Velocity1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Velocity1.
        """
        return None

    @property
    def Velocity2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Velocity2.
        """
        return None

    @property
    def MaximumDampingForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumDampingForce1.
        """
        return None

    @property
    def MaximumDampingForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumDampingForce2.
        """
        return None

    @property
    def MaximumElongation1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElongation1.
        """
        return None

    @property
    def MaximumElongation2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElongation2.
        """
        return None

    @property
    def MaximumElasticForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElasticForce1.
        """
        return None

    @property
    def MaximumElasticForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElasticForce2.
        """
        return None

    @property
    def MaximumVelocity1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumVelocity1.
        """
        return None

    @property
    def MaximumVelocity2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumVelocity2.
        """
        return None

    @property
    def MinimumDampingForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumDampingForce1.
        """
        return None

    @property
    def MinimumDampingForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumDampingForce2.
        """
        return None

    @property
    def MinimumElongation1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElongation1.
        """
        return None

    @property
    def MinimumElongation2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElongation2.
        """
        return None

    @property
    def MinimumElasticForce1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElasticForce1.
        """
        return None

    @property
    def MinimumElasticForce2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElasticForce2.
        """
        return None

    @property
    def MinimumVelocity1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumVelocity1.
        """
        return None

    @property
    def MinimumVelocity2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumVelocity2.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def PhaseIncrement(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PhaseIncrement.
        """
        return None

    @property
    def ScaleFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScaleFactorType]:
        """
        Gets or sets the ScaleFactor.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ElectricFieldProbe(object):
    """
    Defines a ElectricFieldProbe.
    """

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def YAxisFieldIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisFieldIntensity.
        """
        return None

    @property
    def ZAxisFieldIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisFieldIntensity.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class SpringProbe(object):
    """
    Defines a BoltPretensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScaleFactorValue(self) -> typing.Optional[float]:
        """
        Gets or sets the ScaleFactorValue.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def MaximumDampingForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumDampingForce.
        """
        return None

    @property
    def MaximumElongation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElongation.
        """
        return None

    @property
    def MaximumElasticForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumElasticForce.
        """
        return None

    @property
    def MaximumVelocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumVelocity.
        """
        return None

    @property
    def MinimumDampingForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumDampingForce.
        """
        return None

    @property
    def MinimumElongation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElongation.
        """
        return None

    @property
    def MinimumElasticForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumElasticForce.
        """
        return None

    @property
    def MinimumVelocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumVelocity.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def DampingForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the DampingForce.
        """
        return None

    @property
    def Elongation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Elongation.
        """
        return None

    @property
    def ElasticForce(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ElasticForce.
        """
        return None

    @property
    def Velocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Velocity.
        """
        return None

    @property
    def ScaleFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScaleFactorType]:
        """
        Gets or sets the ScaleFactor.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class JointProbe(object):
    """
    Defines a BoltPretensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Status(self) -> typing.Optional[int]:
        """
        Gets the Status.
        """
        return None

    @property
    def ResultType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets or sets the ResultType.
        """
        return None

    @property
    def OrientationMethod(self) -> typing.Optional[bool]:
        """
        Gets the OrientationMethod.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ResultProbe(object):
    """
    Defines a ResultProbe.
    """

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class AccelerationProbe(object):
    """
    Defines a AccelerationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class AngularAccelerationProbe(object):
    """
    Defines a AngularAccelerationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class AngularVelocityProbe(object):
    """
    Defines a AngularVelocityProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ChargeReactionProbe(object):
    """
    Defines a ChargeReactionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def ChargeReactionImag(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ChargeReactionImag.
        """
        return None

    @property
    def MaximumImagChargeReaction(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumImagChargeReaction.
        """
        return None

    @property
    def MaximumRealChargeReaction(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumRealChargeReaction.
        """
        return None

    @property
    def MinimumImagChargeReaction(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumImagChargeReaction.
        """
        return None

    @property
    def MinimumRealChargeReaction(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumRealChargeReaction.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def ChargeReactionReal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ChargeReactionReal.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ContactDistanceProbe(object):
    """
    Defines a ContactDistanceProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Results(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Results.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class CurrentDensityProbe(object):
    """
    Defines a CurrentDensityProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def CurrentDensityTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the CurrentDensityTotal.
        """
        return None

    @property
    def XAxisCurrentDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisCurrentDensity.
        """
        return None

    @property
    def YAxisCurrentDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisCurrentDensity.
        """
        return None

    @property
    def ZAxisCurrentDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisCurrentDensity.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class DeformationProbe(object):
    """
    Defines a DeformationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def XAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisDeformation.
        """
        return None

    @property
    def YAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisDeformation.
        """
        return None

    @property
    def ZAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisDeformation.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def MaximumTotalDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotalDeformation.
        """
        return None

    @property
    def MaximumXAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxisDeformation.
        """
        return None

    @property
    def MaximumYAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxisDeformation.
        """
        return None

    @property
    def MaximumZAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxisDeformation.
        """
        return None

    @property
    def MinimumTotalDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotalDeformation.
        """
        return None

    @property
    def MinimumXAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxisDeformation.
        """
        return None

    @property
    def MinimumYAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxisDeformation.
        """
        return None

    @property
    def MinimumZAxisDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxisDeformation.
        """
        return None

    @property
    def TotalDeformation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the TotalDeformation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ElectricVoltageProbe(object):
    """
    Defines a ElectricVoltageProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def VoltageProbe(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the VoltageProbe.
        """
        return None

    @property
    def MaximumVoltageProbe(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumVoltageProbe.
        """
        return None

    @property
    def MinimumVoltageProbe(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumVoltageProbe.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ElectromechanicalCouplingCoefficient(object):
    """
    Defines a ElectromechanicalCouplingCoefficient.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ElectromechanicalCouplingCoefficientValue(self) -> typing.Optional[float]:
        """
        Gets the ElectromechanicalCouplingCoefficientValue.
        """
        return None

    @property
    def MaximumElectromechanicalCouplingCoefficient(self) -> typing.Optional[float]:
        """
        Gets the MaximumElectromechanicalCouplingCoefficient.
        """
        return None

    @property
    def MinimumElectromechanicalCouplingCoefficient(self) -> typing.Optional[float]:
        """
        Gets the MinimumElectromechanicalCouplingCoefficient.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class EmagReactionProbe(object):
    """
    Defines a EmagReactionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MaximumCurrent(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumCurrent.
        """
        return None

    @property
    def MinimumCurrent(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumCurrent.
        """
        return None

    @property
    def Current(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Current.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class EnergyProbe(object):
    """
    Defines a EnergyProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def ContactEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ContactEnergy.
        """
        return None

    @property
    def DampingEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the DampingEnergy.
        """
        return None

    @property
    def ExternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ExternalEnergy.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def HourglassEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the HourglassEnergy.
        """
        return None

    @property
    def InternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the InternalEnergy.
        """
        return None

    @property
    def KineticEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the KineticEnergy.
        """
        return None

    @property
    def MagnetostaticCoEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MagnetostaticCoEnergy.
        """
        return None

    @property
    def MaximumContactEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumContactEnergy.
        """
        return None

    @property
    def MaximumDampingEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumDampingEnergy.
        """
        return None

    @property
    def MaximumExternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumExternalEnergy.
        """
        return None

    @property
    def MaximumHourglassEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumHourglassEnergy.
        """
        return None

    @property
    def MaximumInternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumInternalEnergy.
        """
        return None

    @property
    def MaximumKineticEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumKineticEnergy.
        """
        return None

    @property
    def MaxMagnetostaticCoEnergyOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaxMagnetostaticCoEnergyOverTime.
        """
        return None

    @property
    def MaximumPlasticWork(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumPlasticWork.
        """
        return None

    @property
    def MaximumPotentialEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumPotentialEnergy.
        """
        return None

    @property
    def MaximumStrainEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumStrainEnergy.
        """
        return None

    @property
    def MaximumTotalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotalEnergy.
        """
        return None

    @property
    def MinimumContactEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumContactEnergy.
        """
        return None

    @property
    def MinimumDampingEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumDampingEnergy.
        """
        return None

    @property
    def MinimumExternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumExternalEnergy.
        """
        return None

    @property
    def MinimumHourglassEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumHourglassEnergy.
        """
        return None

    @property
    def MinimumInternalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumInternalEnergy.
        """
        return None

    @property
    def MinimumKineticEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumKineticEnergy.
        """
        return None

    @property
    def MinMagnetostaticCoEnergyOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinMagnetostaticCoEnergyOverTime.
        """
        return None

    @property
    def MinimumPlasticWork(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumPlasticWork.
        """
        return None

    @property
    def MinimumPotentialEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumPotentialEnergy.
        """
        return None

    @property
    def MinimumStrainEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumStrainEnergy.
        """
        return None

    @property
    def MinimumTotalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotalEnergy.
        """
        return None

    @property
    def PlasticWork(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PlasticWork.
        """
        return None

    @property
    def PotentialEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the PotentialEnergy.
        """
        return None

    @property
    def StrainEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the StrainEnergy.
        """
        return None

    @property
    def TotalEnergy(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the TotalEnergy.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class FieldIntensityProbe(object):
    """
    Defines a FieldIntensityProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def TotalFieldIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the TotalFieldIntensity.
        """
        return None

    @property
    def YAxisFieldIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisFieldIntensity.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class FlexibleRotationProbe(object):
    """
    Defines a FlexibleRotationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MaximumXAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxisRotation.
        """
        return None

    @property
    def MaximumYAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxisRotation.
        """
        return None

    @property
    def MaximumZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxisRotation.
        """
        return None

    @property
    def MinimumXAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxisRotation.
        """
        return None

    @property
    def MinimumYAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxisRotation.
        """
        return None

    @property
    def MinimumZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxisRotation.
        """
        return None

    @property
    def XAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisRotation.
        """
        return None

    @property
    def YAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisRotation.
        """
        return None

    @property
    def ZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisRotation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class FluxDensityProbe(object):
    """
    Defines a FluxDensityProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Probability(self) -> typing.Optional[float]:
        """
        Gets the Probability.
        """
        return None

    @property
    def TotalFluxDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the TotalFluxDensity.
        """
        return None

    @property
    def XAxisFluxDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisFluxDensity.
        """
        return None

    @property
    def YAxisFluxDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisFluxDensity.
        """
        return None

    @property
    def ZAxisFluxDensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisFluxDensity.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ForceReaction(object):
    """
    Defines a ForceReaction.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Probability(self) -> typing.Optional[float]:
        """
        Gets the Probability.
        """
        return None

    @property
    def ScaleFactorValue(self) -> typing.Optional[float]:
        """
        Gets or sets the ScaleFactorValue.
        """
        return None

    @property
    def Mode(self) -> typing.Optional[int]:
        """
        Gets or sets the Mode.
        """
        return None

    @property
    def SymmetryMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the SymmetryMultiplier.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def PhaseIncrement(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PhaseIncrement.
        """
        return None

    @property
    def SurfaceArea(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the SurfaceArea.
        """
        return None

    @property
    def ContactForce(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactForceType]:
        """
        Gets or sets the ContactForce.
        """
        return None

    @property
    def Extraction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeExtractionType]:
        """
        Gets or sets the Extraction.
        """
        return None

    @property
    def Reference(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultRelativityType]:
        """
        Gets the Reference.
        """
        return None

    @property
    def ScaleFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScaleFactorType]:
        """
        Gets or sets the ScaleFactor.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def Beam(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the Beam.
        """
        return None

    @property
    def RemotePoints(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePoints.
        """
        return None

    @property
    def Spring(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the Spring.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ForceSummationProbe(object):
    """
    Defines a ForceSummationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SymmetryMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the SymmetryMultiplier.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class GeneralizedPlaneStrainProbe(object):
    """
    Defines a GeneralizedPlaneStrainProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class HeatFluxProbe(object):
    """
    Defines a HeatFluxProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def TotalHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the TotalHeatFlux.
        """
        return None

    @property
    def XAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisHeatFlux.
        """
        return None

    @property
    def YAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisHeatFlux.
        """
        return None

    @property
    def ZAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisHeatFlux.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def MaximumTotalHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotalHeatFlux.
        """
        return None

    @property
    def MaximumXAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxisHeatFlux.
        """
        return None

    @property
    def MaximumYAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxisHeatFlux.
        """
        return None

    @property
    def MaximumZAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxisHeatFlux.
        """
        return None

    @property
    def MinimumTotalHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotalHeatFlux.
        """
        return None

    @property
    def MinimumXAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxisHeatFlux.
        """
        return None

    @property
    def MinimumYAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxisHeatFlux.
        """
        return None

    @property
    def MinimumZAxisHeatFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxisHeatFlux.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ImpedanceProbe(object):
    """
    Defines a ImpedanceProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def ImpedanceReal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImpedanceReal.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def ImpedanceImag(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ImpedanceImag.
        """
        return None

    @property
    def MaximumRealImpedance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumRealImpedance.
        """
        return None

    @property
    def MaximumImagImpedance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumImagImpedance.
        """
        return None

    @property
    def MinimumRealImpedance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumRealImpedance.
        """
        return None

    @property
    def MinimumImagImpedance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumImagImpedance.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class JouleHeatProbe(object):
    """
    Defines a JouleHeatProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def JouleHeat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the JouleHeat.
        """
        return None

    @property
    def MaximumJouleHeat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumJouleHeat.
        """
        return None

    @property
    def MinimumJouleHeat(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumJouleHeat.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class MagneticFluxProbe(object):
    """
    Defines a MagneticFluxProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SymmetryMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the SymmetryMultiplier.
        """
        return None

    @property
    def MagneticFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MagneticFlux.
        """
        return None

    @property
    def MaximumMagneticFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMagneticFlux.
        """
        return None

    @property
    def MinimumMagneticFlux(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMagneticFlux.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class MomentReaction(object):
    """
    Defines a MomentReaction.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Probability(self) -> typing.Optional[float]:
        """
        Gets the Probability.
        """
        return None

    @property
    def ScaleFactorValue(self) -> typing.Optional[float]:
        """
        Gets or sets the ScaleFactorValue.
        """
        return None

    @property
    def Mode(self) -> typing.Optional[int]:
        """
        Gets or sets the Mode.
        """
        return None

    @property
    def SymmetryMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the SymmetryMultiplier.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def PhaseIncrement(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PhaseIncrement.
        """
        return None

    @property
    def SurfaceArea(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the SurfaceArea.
        """
        return None

    @property
    def ContactForce(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactForceType]:
        """
        Gets or sets the ContactForce.
        """
        return None

    @property
    def Extraction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeExtractionType]:
        """
        Gets or sets the Extraction.
        """
        return None

    @property
    def Reference(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultRelativityType]:
        """
        Gets the Reference.
        """
        return None

    @property
    def ScaleFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScaleFactorType]:
        """
        Gets or sets the ScaleFactor.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def Beam(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the Beam.
        """
        return None

    @property
    def RemotePoints(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePoints.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class Position(object):
    """
    Defines a Position.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class QualityFactor(object):
    """
    Defines a QualityFactor.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MaximumQualityFactor(self) -> typing.Optional[float]:
        """
        Gets the MaximumQualityFactor.
        """
        return None

    @property
    def MinimumQualityFactor(self) -> typing.Optional[float]:
        """
        Gets the MinimumQualityFactor.
        """
        return None

    @property
    def QualityFactorValue(self) -> typing.Optional[float]:
        """
        Gets the QualityFactorValue.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the SetNumber.
        """
        return None

    @property
    def ReportedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReportedFrequency.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def SweepingPhase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepingPhase.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class RadiationProbe(object):
    """
    Defines a RadiationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def EmittedRadiation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the EmittedRadiation.
        """
        return None

    @property
    def IncidentRadiation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the IncidentRadiation.
        """
        return None

    @property
    def NetRadiation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NetRadiation.
        """
        return None

    @property
    def ReflectedRadiation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ReflectedRadiation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class ResponsePSD(object):
    """
    Defines a ResponsePSD.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Probability(self) -> typing.Optional[float]:
        """
        Gets the Probability.
        """
        return None

    @property
    def RMSPercentage(self) -> typing.Optional[float]:
        """
        Gets the RMSPercentage.
        """
        return None

    @property
    def ExpectedFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ExpectedFrequency.
        """
        return None

    @property
    def RMSValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the RMSValue.
        """
        return None

    @property
    def RangeMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RangeMaximum.
        """
        return None

    @property
    def RangeMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RangeMinimum.
        """
        return None

    @property
    def ResultType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets or sets the ResultType.
        """
        return None

    @property
    def Reference(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultRelativityType]:
        """
        Gets or sets the Reference.
        """
        return None

    @property
    def SelectedFrequencyRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FrequencyRangeType]:
        """
        Gets or sets the SelectedFrequencyRange.
        """
        return None

    @property
    def AccelerationInG(self) -> typing.Optional[bool]:
        """
        Gets or sets the AccelerationInG.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class RotationProbe(object):
    """
    Defines a RotationProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MaximumXAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxisRotation.
        """
        return None

    @property
    def MaximumYAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxisRotation.
        """
        return None

    @property
    def MaximumZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxisRotation.
        """
        return None

    @property
    def MinimumXAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxisRotation.
        """
        return None

    @property
    def MinimumYAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxisRotation.
        """
        return None

    @property
    def MinimumZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxisRotation.
        """
        return None

    @property
    def XAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxisRotation.
        """
        return None

    @property
    def YAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxisRotation.
        """
        return None

    @property
    def ZAxisRotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxisRotation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class StrainProbe(object):
    """
    Defines a StrainProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def EquivalentStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the EquivalentStrain.
        """
        return None

    @property
    def MaximumEquivalentStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumEquivalentStrain.
        """
        return None

    @property
    def MaximumMaximumPrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMaximumPrincipalStrain.
        """
        return None

    @property
    def MaximumMiddlePrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMiddlePrincipalStrain.
        """
        return None

    @property
    def MaximumMinimumPrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMinimumPrincipalStrain.
        """
        return None

    @property
    def MaximumNormalXAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalXAxisStrain.
        """
        return None

    @property
    def MaximumNormalYAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalYAxisStrain.
        """
        return None

    @property
    def MaximumNormalZAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalZAxisStrain.
        """
        return None

    @property
    def MaximumPrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumPrincipalStrain.
        """
        return None

    @property
    def MaximumXYShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXYShearStrain.
        """
        return None

    @property
    def MaximumXZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXZShearStrain.
        """
        return None

    @property
    def MaximumYZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYZShearStrain.
        """
        return None

    @property
    def MaximumStrainIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumStrainIntensity.
        """
        return None

    @property
    def MiddlePrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MiddlePrincipalStrain.
        """
        return None

    @property
    def MinimumEquivalentStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumEquivalentStrain.
        """
        return None

    @property
    def MinimumStrainMaximumPrincipal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumStrainMaximumPrincipal.
        """
        return None

    @property
    def MinimumMiddlePrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMiddlePrincipalStrain.
        """
        return None

    @property
    def MinimumMinimumPrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMinimumPrincipalStrain.
        """
        return None

    @property
    def MinimumNormalXAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalXAxisStrain.
        """
        return None

    @property
    def MinimumNormalYAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalYAxisStrain.
        """
        return None

    @property
    def MinimumNormalZAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalZAxisStrain.
        """
        return None

    @property
    def MinimumPrincipalStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumPrincipalStrain.
        """
        return None

    @property
    def MinimumXYShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXYShearStrain.
        """
        return None

    @property
    def MinimumXZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXZShearStrain.
        """
        return None

    @property
    def MinimumYZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYZShearStrain.
        """
        return None

    @property
    def MinimumStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumStrain.
        """
        return None

    @property
    def MinimumStrainIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumStrainIntensity.
        """
        return None

    @property
    def NormalXAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalXAxisStrain.
        """
        return None

    @property
    def NormalYAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalYAxisStrain.
        """
        return None

    @property
    def NormalZAxisStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalZAxisStrain.
        """
        return None

    @property
    def XYShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XYShearStrain.
        """
        return None

    @property
    def XZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XZShearStrain.
        """
        return None

    @property
    def YZShearStrain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YZShearStrain.
        """
        return None

    @property
    def Strain(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Strain.
        """
        return None

    @property
    def StrainIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the StrainIntensity.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class StressProbe(object):
    """
    Defines a StressProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def EquivalentStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the EquivalentStress.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def MaximumEquivalentStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumEquivalentStress.
        """
        return None

    @property
    def MaximumMaximumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMaximumPrincipalStress.
        """
        return None

    @property
    def MaximumMiddlePrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMiddlePrincipalStress.
        """
        return None

    @property
    def MaximumMinimumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumMinimumPrincipalStress.
        """
        return None

    @property
    def MaximumNormalXAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalXAxisStress.
        """
        return None

    @property
    def MaximumNormalYAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalYAxisStress.
        """
        return None

    @property
    def MaximumNormalZAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumNormalZAxisStress.
        """
        return None

    @property
    def MaximumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumPrincipalStress.
        """
        return None

    @property
    def MaximumXYShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXYShearStress.
        """
        return None

    @property
    def MaximumXZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXZShearStress.
        """
        return None

    @property
    def MaximumYZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYZShearStress.
        """
        return None

    @property
    def MaximumStressIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumStressIntensity.
        """
        return None

    @property
    def MiddlePrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MiddlePrincipalStress.
        """
        return None

    @property
    def MinimumEquivalentStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumEquivalentStress.
        """
        return None

    @property
    def MinimumMaximumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMaximumPrincipalStress.
        """
        return None

    @property
    def MinimumMiddlePrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMiddlePrincipalStress.
        """
        return None

    @property
    def MinimumMinimumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumMinimumPrincipalStress.
        """
        return None

    @property
    def MinimumNormalXAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalXAxisStress.
        """
        return None

    @property
    def MinimumNormalYAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalYAxisStress.
        """
        return None

    @property
    def MinimumNormalZAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumNormalZAxisStress.
        """
        return None

    @property
    def MinimumPrincipalStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumPrincipalStress.
        """
        return None

    @property
    def MinimumXYShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXYShearStress.
        """
        return None

    @property
    def MinimumXZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXZShearStress.
        """
        return None

    @property
    def MinimumYZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYZShearStress.
        """
        return None

    @property
    def MinimumStressIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumStressIntensity.
        """
        return None

    @property
    def NormalXAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalXAxisStress.
        """
        return None

    @property
    def NormalYAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalYAxisStress.
        """
        return None

    @property
    def NormalZAxisStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the NormalZAxisStress.
        """
        return None

    @property
    def XYShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XYShearStress.
        """
        return None

    @property
    def XZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XZShearStress.
        """
        return None

    @property
    def YZShearStress(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YZShearStress.
        """
        return None

    @property
    def StressIntensity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the StressIntensity.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class TemperatureProbe(object):
    """
    Defines a TemperatureProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def MaximumTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTemperature.
        """
        return None

    @property
    def MinimumTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTemperature.
        """
        return None

    @property
    def Temperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Temperature.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class TorqueProbe(object):
    """
    Defines a TorqueProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SymmetryMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the SymmetryMultiplier.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class VelocityProbe(object):
    """
    Defines a VelocityProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
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
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


class VolumeProbe(object):
    """
    Defines a VolumeProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def XCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XCoordinate.
        """
        return None

    @property
    def YCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YCoordinate.
        """
        return None

    @property
    def ZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZCoordinate.
        """
        return None

    @property
    def MaximumVolume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumVolume.
        """
        return None

    @property
    def MinimumVolume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumVolume.
        """
        return None

    @property
    def VolumeResult(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the VolumeResult.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
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

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
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


