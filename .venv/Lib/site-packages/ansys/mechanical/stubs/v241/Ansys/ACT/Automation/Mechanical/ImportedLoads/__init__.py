"""ImportedLoads module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ImportedBodyForceDensity(object):
    """
    Defines a ImportedBodyForceDensity.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedBodyTemperature(object):
    """
    Defines a ImportedBodyTemperature.
    """

    @property
    def ApplyToInitialMesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the ApplyToInitialMesh.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LoadVectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadVectorNumber.
        """
        return None

    @property
    def LoadVectorAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadVectorAssignment]:
        """
        Gets or sets the LoadVectorAssignment.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedConvection(object):
    """
    Defines a ImportedConvection.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def DisplayConnectionLines(self) -> typing.Optional[bool]:
        """
        Gets or sets the DisplayConnectionLines.
        """
        return None

    @property
    def FluidFlow(self) -> typing.Optional[bool]:
        """
        Gets or sets the FluidFlow.
        """
        return None

    @property
    def FluidFlowLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the FluidFlowLocation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedCutBoundaryRemoteConstraint(object):
    """
    Defines a ImportedCutBoundaryRemoteConstraint.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedCutBoundaryRemoteForce(object):
    """
    Defines a ImportedCutBoundaryRemoteForce.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedDisplacement(object):
    """
    Defines a ImportedDisplacement.
    """

    @property
    def ApplyToInitialMesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the ApplyToInitialMesh.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def DisplacementType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadDisplacementType]:
        """
        Gets or sets the DisplacementType.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedSurfaceForceDensity(object):
    """
    Defines a ImportedSurfaceForceDensity.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedTemperature(object):
    """
    Defines a ImportedTemperature.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedVelocity(object):
    """
    Defines a ImportedVelocity.
    """

    @property
    def MappedData(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappedData]:
        """
        Gets or sets the MappedData.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def CutoffFrequency(self) -> typing.Optional[float]:
        """
        Gets or sets the CutoffFrequency.
        """
        return None

    @property
    def MaximumTimeRange(self) -> typing.Optional[float]:
        """
        Gets or sets the MaximumTimeRange.
        """
        return None

    @property
    def MinimumTimeRange(self) -> typing.Optional[float]:
        """
        Gets or sets the MinimumTimeRange.
        """
        return None

    @property
    def SourceTimeDefinitionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SourceTimeDefinitionType]:
        """
        Gets or sets the SourceTimeDefinitionType.
        """
        return None

    @property
    def WindowType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WindowType]:
        """
        Gets or sets the WindowType.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedLoadGroup(object):
    """
    Defines a ImportedLoadGroup.
    """

    @property
    def ResultFile(self) -> typing.Optional[str]:
        """
        Gets or sets the ResultFile.
        """
        return None

    @property
    def ResultFileUnitSystem(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the ResultFileUnitSystem.
        """
        return None

    @property
    def FilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the FilesDirectory.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def TransferStep(self) -> typing.Optional[int]:
        """
        Controls which additive simulation step is used for the data transfer.
        """
        return None

    @property
    def Source(self) -> typing.Optional[str]:
        """
        Gets the Source.
        """
        return None

    @property
    def ResultFileTimestamp(self) -> typing.Optional[str]:
        """
        Gets the ResultFileTimestamp.
        """
        return None

    @property
    def SourceDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SourceDimension]:
        """
        Gets or sets the SourceDimension.
        """
        return None

    @property
    def DeleteMappedDataFilesAfterImport(self) -> typing.Optional[bool]:
        """
        Gets or sets the DeleteMappedDataFilesAfterImport.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def TransferTemperaturesDuringSolve(self) -> typing.Optional[bool]:
        """
        Gets or sets the TransferTemperaturesDuringSolve.
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

    def CreateExternalLoadVelocitiesAndSyncAnalysisSettings(self) -> None:
        """
        Run the CreateExternalLoadVelocitiesAndSyncAnalysisSettings action.
        """
        pass

    def SetResultFile(self, resultFile: str, unitSystem: Ansys.Mechanical.DataModel.Enums.WBUnitSystemType) -> None:
        """
        Sets the ResultFile with unitSystem supplied. For MAPDL Results File without a unit system.
        """
        pass

    def ImportExternalDataFiles(self, externalDataFiles: Ansys.Mechanical.ExternalData.ExternalDataFileCollection) -> None:
        """
        
            
        """
        pass

    def GetExternalDataFiles(self) -> Ansys.Mechanical.ExternalData.ExternalDataFileCollection:
        """
        
            
        """
        pass

    def ReloadExternalDataFiles(self) -> None:
        """
        Reloads the external data files for current Imported Load Group.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
        """
        pass

    def AddImportedBodyTemperature(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedBodyTemperature:
        """
        Creates a new ImportedBodyTemperature
        """
        pass

    def AddImportedTemperature(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedTemperature:
        """
        Creates a new ImportedTemperature
        """
        pass

    def CreateBodyForceDensitiesAndSyncAnalysisSettings(self) -> None:
        """
        Create body force densities for all RPMs.
        """
        pass

    def CreateSurfaceForceDensitiesAndSyncAnalysisSettings(self) -> None:
        """
        Create surface force densities for all RPMs.
        """
        pass

    def CreateVelocitiesAndSyncAnalysisSettings(self) -> None:
        """
        Create velocities for all RPMs.
        """
        pass

    def AddImportedBodyForceDensity(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedBodyForceDensity:
        """
        Creates a new ImportedBodyForceDensity
        """
        pass

    def AddImportedConvection(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedConvection:
        """
        Creates a new ImportedConvection
        """
        pass

    def AddImportedCutBoundaryRemoteConstraint(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedCutBoundaryRemoteConstraint:
        """
        Creates a new ImportedCutBoundaryRemoteConstraint
        """
        pass

    def AddImportedCutBoundaryRemoteForce(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedCutBoundaryRemoteForce:
        """
        Creates a new ImportedCutBoundaryRemoteForce
        """
        pass

    def AddImportedDisplacement(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedDisplacement:
        """
        Creates a new ImportedDisplacement
        """
        pass

    def AddImportedCutBoundaryConstraint(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedDisplacement:
        """
        Creates a new ImportedDisplacement
        """
        pass

    def AddImportedElementOrientation(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedElementOrientation:
        """
        Creates a new ImportedElementOrientation
        """
        pass

    def AddImportedFiberRatio(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedFiberRatio:
        """
        Creates a new ImportedFiberRatio
        """
        pass

    def AddImportedForce(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedForce:
        """
        Creates a new ImportedForce
        """
        pass

    def AddImportedHeatFlux(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedHeatFlux:
        """
        Creates a new ImportedHeatFlux
        """
        pass

    def AddImportedHeatGeneration(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedHeatGeneration:
        """
        Creates a new ImportedHeatGeneration
        """
        pass

    def AddImportedInitialStrain(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedInitialStrain:
        """
        Creates a new ImportedInitialStrain
        """
        pass

    def AddImportedInitialStress(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedInitialStress:
        """
        Creates a new ImportedInitialStress
        """
        pass

    def AddImportedMaterialField(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedMaterialField:
        """
        Creates a new ImportedMaterialField
        """
        pass

    def AddImportedPressure(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedPressure:
        """
        Creates a new ImportedPressure
        """
        pass

    def AddImportedSurfaceForceDensity(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedSurfaceForceDensity:
        """
        Creates a new ImportedSurfaceForceDensity
        """
        pass

    def AddImportedThickness(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedThickness:
        """
        Creates a new ImportedThickness
        """
        pass

    def AddImportedTrace(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedTrace:
        """
        Creates a new ImportedTrace
        """
        pass

    def AddImportedVelocity(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedVelocity:
        """
        Creates a new ImportedVelocity
        """
        pass

    def AddImportedWarpWeftRatio(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedWarpWeftRatio:
        """
        Creates a new ImportedWarpWeftRatio
        """
        pass

    def AddImportedYarnAngle(self) -> Ansys.ACT.Automation.Mechanical.ImportedLoads.ImportedYarnAngle:
        """
        Creates a new ImportedYarnAngle
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def ImportLoad(self) -> None:
        """
        Run the ImportLoad action.
        """
        pass

    def RefreshImportedLoad(self) -> None:
        """
        Run the RefreshImportedLoad action.
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


class ImportedLoad(object):
    """
    Defines a ImportedLoad.
    """

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedTrace(object):
    """
    Defines a ImportedTrace.
    """

    @property
    def Vias(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.WorksheetRow]]:
        """
        Vias property.
        """
        return None

    @property
    def Layers(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.WorksheetRow]]:
        """
        Layers property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedElementOrientation(object):
    """
    Defines a ImportedElementOrientation.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedFiberRatio(object):
    """
    Defines a ImportedFiberRatio.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedForce(object):
    """
    Defines a ImportedForce.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedHeatFlux(object):
    """
    Defines a ImportedHeatFlux.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedHeatGeneration(object):
    """
    Defines a ImportedHeatGeneration.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedInitialStrain(object):
    """
    Defines a ImportedInitialStrain.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedInitialStress(object):
    """
    Defines a ImportedInitialStress.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedMaterialField(object):
    """
    Defines a ImportedMaterialField.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedPressure(object):
    """
    Defines a ImportedPressure.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def LoadVectorNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadVectorNumber.
        """
        return None

    @property
    def LoadVectorNumberImaginary(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadVectorNumberImaginary.
        """
        return None

    @property
    def AppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadAppliedBy]:
        """
        Gets or sets the AppliedBy.
        """
        return None

    @property
    def LoadVectorAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadVectorAssignment]:
        """
        Gets or sets the LoadVectorAssignment.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedThickness(object):
    """
    Defines a ImportedThickness.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedWarpWeftRatio(object):
    """
    Defines a ImportedWarpWeftRatio.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


class ImportedYarnAngle(object):
    """
    Defines a ImportedYarnAngle.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSExternalLoadAuto]:
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
    def Weighting(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeightingType]:
        """
        Weighting property.
        """
        return None

    @property
    def MappingControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingControlType]:
        """
        MappingControl property.
        """
        return None

    @property
    def DisplaySourcePoints(self) -> typing.Optional[bool]:
        """
        DisplaySourcePoints property.
        """
        return None

    @property
    def DisplaySourcePointIds(self) -> typing.Optional[bool]:
        """
        DisplaySourcePointIds property.
        """
        return None

    @property
    def DisplayInteriorPoints(self) -> typing.Optional[bool]:
        """
        DisplayInteriorPoints property.
        """
        return None

    @property
    def DisplayProjectionPlane(self) -> typing.Optional[bool]:
        """
        DisplayProjectionPlane property.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingAlgorithm]:
        """
        Algorithm property.
        """
        return None

    @property
    def BoundingBoxTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        BoundingBoxTolerance property.
        """
        return None

    @property
    def CreateNameSelectionForMappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForMappedNodes property.
        """
        return None

    @property
    def CreateNameSelectionForOutsideNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForOutsideNodes property.
        """
        return None

    @property
    def CreateNameSelectionForUnmappedNodes(self) -> typing.Optional[bool]:
        """
        CreateNameSelectionForUnmappedNodes property.
        """
        return None

    @property
    def Mapping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingInterpolationType]:
        """
        Mapping property.
        """
        return None

    @property
    def LegendMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMaximum property.
        """
        return None

    @property
    def LegendMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        LegendMinimum property.
        """
        return None

    @property
    def LegendRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendRangeType]:
        """
        LegendRange property.
        """
        return None

    @property
    def MaxOutsideDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MaxOutsideDistance property.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingMethod]:
        """
        Method property.
        """
        return None

    @property
    def OutsideDistanceCheck(self) -> typing.Optional[bool]:
        """
        OutsideDistanceCheck property.
        """
        return None

    @property
    def OutsideOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingOutsideOption]:
        """
        OutsideOption property.
        """
        return None

    @property
    def Projection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Projection property.
        """
        return None

    @property
    def RigidBodyTransformationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RigidBodyTransformationType]:
        """
        RigidBodyTransformationType property.
        """
        return None

    @property
    def RigidTransformSourceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformSourceCoordinateSystem property.
        """
        return None

    @property
    def RigidTransformTargetCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        RigidTransformTargetCoordinateSystem property.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        ShellThicknessFactor property.
        """
        return None

    @property
    def SourceMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMaximum property.
        """
        return None

    @property
    def SourceMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        SourceMinimum property.
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MappingVariableType]:
        """
        VariableType property.
        """
        return None

    @property
    def Interpolation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InterpolationType]:
        """
        Interpolation property.
        """
        return None

    @property
    def UnmappedNodesName(self) -> typing.Optional[str]:
        """
        UnmappedNodesName property.
        """
        return None

    @property
    def MappedNodesName(self) -> typing.Optional[str]:
        """
        MappedNodesName property.
        """
        return None

    @property
    def OutsideNodesName(self) -> typing.Optional[str]:
        """
        OutsideNodesName property.
        """
        return None

    @property
    def Pinball(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Pinball property.
        """
        return None

    @property
    def NumberOfPoints(self) -> typing.Optional[int]:
        """
        NumberOfPoints property.
        """
        return None

    @property
    def OrientationRealignment(self) -> typing.Optional[bool]:
        """
        OrientationRealignment property.
        """
        return None

    @property
    def Limit(self) -> typing.Optional[int]:
        """
        Limit property.
        """
        return None

    @property
    def KrigingCorrelationFunction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingCorrFuncType]:
        """
        KrigingCorrelationFunction property.
        """
        return None

    @property
    def KrigingPolynom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.KrigingPolynomType]:
        """
        KrigingPolynom property.
        """
        return None

    @property
    def ExtrapolationTolerancePercent(self) -> typing.Optional[float]:
        """
        ExtrapolationTolerancePercent property.
        """
        return None

    @property
    def ApplyAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExternalLoadApplicationType]:
        """
        This controls how the imported load is applied, either as a boundary condition or an initial condition.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SharedRefBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedRefBody.
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

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def Import(self) -> None:
        """
        Import.
        """
        pass

    def ImportLoad(self) -> None:
        """
        
            Run the ImportLoad action.
            
        """
        pass

    def GetActivateAtLoadStep(self, stepNumber: int) -> bool:
        """
        GetActivateAtLoadStep method.
        """
        pass

    def SetActivateAtLoadStep(self, stepNumber: int, bActive: bool) -> None:
        """
        SetActivateAtLoadStep method.
        """
        pass

    def AddMappingValidation(self) -> Ansys.ACT.Automation.Mechanical.MappingValidation:
        """
        Creates a new MappingValidation
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
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


