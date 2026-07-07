"""MeshControls module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class Deviation(object):
    """
    Defines a Deviation.
    """

    @property
    def Tolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Tolerance property.
        """
        return None

    @property
    def MeshSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        MeshSize property.
        """
        return None

    @property
    def NumberOfDivisions(self) -> typing.Optional[int]:
        """
        NumberOfDivisions property.
        """
        return None

    @property
    def ControlType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DeviationControlType]:
        """
        Gets or sets the SagControlType.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class RepairTopology(object):
    """
    Defines a RepairTopology.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def PinchTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PinchTolerance.
        """
        return None

    @property
    def SharpAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SharpAngle.
        """
        return None

    @property
    def ShortEdgeLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ShortEdgeLength.
        """
        return None

    @property
    def ThinFaceWidth(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ThinFaceWidth.
        """
        return None

    @property
    def CollapseShortEdges(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the CollapseShortEdges.
        """
        return None

    @property
    def FillHole(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the FillHole.
        """
        return None

    @property
    def FillHoleGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the FillHoleGeometryDefineBy.
        """
        return None

    @property
    def MergeFaces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the MergeFaces.
        """
        return None

    @property
    def MergeFacesGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the MergeFacesGeometryDefineBy.
        """
        return None

    @property
    def PinchFaces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the PinchFaces.
        """
        return None

    @property
    def PinchFacesGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the PinchFacesGeometryDefineBy.
        """
        return None

    @property
    def PinchFacesUseLocalScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the PinchFacesUseLocalScoping.
        """
        return None

    @property
    def RemoveSharpAngleFaces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the RemoveSharpAngleFaces.
        """
        return None

    @property
    def RemoveThinFaces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the RemoveThinFaces.
        """
        return None

    @property
    def SharpAngleGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the SharpAngleGeometryDefineBy.
        """
        return None

    @property
    def SharpAngleUseLocalScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the SharpAngleUseLocalScoping.
        """
        return None

    @property
    def ShortEdgeGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ShortEdgeGeometryDefineBy.
        """
        return None

    @property
    def ShortEdgeUseLocalScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the ShortEdgeUseLocalScoping.
        """
        return None

    @property
    def SuppressEdgesGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the SuppressEdgesGeometryDefineBy.
        """
        return None

    @property
    def SuppressEdges(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the SuppressEdges.
        """
        return None

    @property
    def ThinFaceGeometryDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ThinFaceGeometryDefineBy.
        """
        return None

    @property
    def ThinFacesUseLocalScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the ThinFacesUseLocalScoping.
        """
        return None

    @property
    def FillHoleNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the FillHoleNamedSelection.
        """
        return None

    @property
    def MergeFacesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the MergeFacesNamedSelection.
        """
        return None

    @property
    def PinchFacesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the PinchFacesNamedSelection.
        """
        return None

    @property
    def SharpAngleNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the SharpAngleNamedSelection.
        """
        return None

    @property
    def ShortEdgeNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the ShortEdgeNamedSelection.
        """
        return None

    @property
    def SuppressEdgesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the SuppressEdgesNamedSelection.
        """
        return None

    @property
    def ThinFaceNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the ThinFaceNamedSelection.
        """
        return None

    @property
    def FillHoleGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the FillHoleGeometrySelection.
        """
        return None

    @property
    def MergeFacesGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MergeFacesGeometrySelection.
        """
        return None

    @property
    def PinchFacesGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the PinchFacesGeometrySelection.
        """
        return None

    @property
    def SharpAngleGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SharpAngleGeometrySelection.
        """
        return None

    @property
    def ShortEdgeGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ShortEdgeGeometrySelection.
        """
        return None

    @property
    def SuppressEdgesGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SuppressEdgesGeometrySelection.
        """
        return None

    @property
    def ThinFaceGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ThinFaceGeometrySelection.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Washer(object):
    """
    Defines a Washer.
    """

    @property
    def NumberOfWasherLayers(self) -> typing.Optional[int]:
        """
        NumberOfWasherLayers property.
        """
        return None

    @property
    def WasherMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WasherMethod]:
        """
        WasherMethod property.
        """
        return None

    @property
    def WasherType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WasherType]:
        """
        WasherType property.
        """
        return None

    @property
    def NumberOfWasherDivisions(self) -> typing.Optional[int]:
        """
        NumberOfWasherDivisions property.
        """
        return None

    @property
    def MinimumNumberOfWasherDivisions(self) -> typing.Optional[int]:
        """
        MinimumNumberOfWasherDivisions property.
        """
        return None

    @property
    def FactorOfDiameter(self) -> typing.Optional[float]:
        """
        FactorOfDiameter property.
        """
        return None

    @property
    def WasherLayerHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        WasherLayerHeight property.
        """
        return None

    @property
    def GrowthRate(self) -> typing.Optional[float]:
        """
        GrowthRate property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Weld(object):
    """
    Defines a Weld.
    """

    @property
    def BottomEntities(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Bottom Entities (Bodies / Faces ) or Extension.
        """
        return None

    @property
    def TopEntities(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Top Entities (Bodies / Faces ) or Extension.
        """
        return None

    @property
    def WeldCurves(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Weld Curves.
        """
        return None

    @property
    def WeldCurvesBody(self) -> typing.Optional[int]:
        """
        WeldCurvesBody property.
        """
        return None

    @property
    def EdgeSelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Edges.
        """
        return None

    @property
    def ControlType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldType]:
        """
        Gets or sets the WeldControlType.
        """
        return None

    @property
    def Source(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldSource]:
        """
        Gets or sets the WeldControlSource.
        """
        return None

    @property
    def ModeledAs(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldModeledAs]:
        """
        Gets or sets the WeldControlModeledAs.
        """
        return None

    @property
    def WeldElementRows(self) -> typing.Optional[int]:
        """
        Gets or sets the WeldControlElementRows.
        """
        return None

    @property
    def Relaxation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldRelaxation]:
        """
        Gets or sets the WeldControlRelaxation.
        """
        return None

    @property
    def WeldTargetShellFace(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldTargetShellFaceType]:
        """
        Gets or sets the WeldTargetShellFace.
        """
        return None

    @property
    def WeldFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactFormulation]:
        """
        Gets or sets the WeldFormulation.
        """
        return None

    @property
    def WeldPinballRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldPinballRadius
            
        """
        return None

    @property
    def AngledDirection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldAngledDirection]:
        """
        Gets or sets the WeldControlAngledDirection.
        """
        return None

    @property
    def CreateUsing(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldCreateUsing]:
        """
        Gets or sets the WeldControlCreateUsing.
        """
        return None

    @property
    def UseWorksheet(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlUseWorksheet.
        """
        return None

    @property
    def CurveScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldCurveScoping]:
        """
        Gets or sets the WeldControlCurveScoping.
        """
        return None

    @property
    def CreationCriteria(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldCreationCriteria]:
        """
        Gets or sets the WeldControlCreationCriteria.
        """
        return None

    @property
    def ThicknessAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldThickness]:
        """
        Gets or sets the WeldControlThicknessAssignment.
        """
        return None

    @property
    def WeldWidthAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldWidthAssignment]:
        """
        Gets or sets the WeldControlWeldWidthAssignment.
        """
        return None

    @property
    def EdgeMeshSizeAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldEdgeMeshSizeAssignment]:
        """
        Gets or sets the WeldControlEdgeMeshSizeAssignment.
        """
        return None

    @property
    def WeldHeightAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldHeightAssignment]:
        """
        Gets or sets the WeldControlWeldHeightAssignment.
        """
        return None

    @property
    def HAZDistanceAssignment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldHAZDistanceAssignment]:
        """
        Gets or sets the WeldControlHAZDistanceAssignment.
        """
        return None

    @property
    def HAZDistanceOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldHAZDistanceOption]:
        """
        Gets or sets the WeldControlHAZDistanceOption.
        """
        return None

    @property
    def WeldThicknessExpression(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlThicknessExpression Value.
        """
        return None

    @property
    def EdgeMeshSizeExpression(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlEdgeMeshSizeExpression Value.
        """
        return None

    @property
    def WeldWidthExpression(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlWeldWidthExpression Value.
        """
        return None

    @property
    def WeldHeightExpression(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlWeldHeightExpression Value.
        """
        return None

    @property
    def HAZDistanceExpressionTopPlate(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlHAZDistanceExpression Value.
        """
        return None

    @property
    def HAZDistanceExpressionBottomPlate(self) -> typing.Optional[str]:
        """
        Gets or sets HAZDistanceExpressionBottomPlate Value.
        """
        return None

    @property
    def MaxThicknessFactor(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlMaxThicknessFactor
            
        """
        return None

    @property
    def MinThicknessFactor(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlMinThicknessFactor
            
        """
        return None

    @property
    def Thickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlThickness
            
        """
        return None

    @property
    def AdjustWeldHeight(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlAdjustWeldHeight.
        """
        return None

    @property
    def CreateHAZLayer(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlCreateHAZLayer.
        """
        return None

    @property
    def WeldHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlOffsetLayerHeight
            
        """
        return None

    @property
    def WeldAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WeldAngle.
        """
        return None

    @property
    def SharpAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WeldSharpAngle.
        """
        return None

    @property
    def LapWeldAngleTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LapWeldAngleTolerance.
        """
        return None

    @property
    def EdgeMeshSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlEdgeMeshSize
            
        """
        return None

    @property
    def WeldControlWeldWidth(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlWeldWidth
            
        """
        return None

    @property
    def HAZDistanceTopPlate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets HAZDistanceTopPlate
            
        """
        return None

    @property
    def HAZDistanceBottomPlate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets HAZDistanceBottomPlate
            
        """
        return None

    @property
    def WeldLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlOffsetLayerHeight
            
        """
        return None

    @property
    def WeldPitch(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlOffsetLayerHeight
            
        """
        return None

    @property
    def NumberOfWelds(self) -> typing.Optional[int]:
        """
        
            Gets or sets WeldControlNumberOfLayers
            
        """
        return None

    @property
    def Offset1(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlOffsetLayerHeight
            
        """
        return None

    @property
    def Offset2(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlOffsetLayerHeight
            
        """
        return None

    @property
    def HAZGrowthRate(self) -> typing.Optional[float]:
        """
        
             Gets or sets the WeldControlHAZGrowthRate
            
        """
        return None

    @property
    def ConnectionTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
             Gets or sets the WeldControlConnectionTolerance
            
        """
        return None

    @property
    def NumberOfLayers(self) -> typing.Optional[int]:
        """
        
            Gets or sets WeldControlNumberOfLayers
            
        """
        return None

    @property
    def GenerateNamedSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeldGeneratedNamedSelection]:
        """
        Gets or sets the WeldControlGenerateNamedSelection.
        """
        return None

    @property
    def GenerateEndCaps(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlSmoothing.
        """
        return None

    @property
    def WriteDefinitionFile(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlSmoothing.
        """
        return None

    @property
    def WeldDefinitionFileLocation(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldDefinitionFile Location.
        """
        return None

    @property
    def WeldIntersectionTag(self) -> typing.Optional[str]:
        """
        Gets or sets the WeldControlIntersectionTag Value.
        """
        return None

    @property
    def WeldIntersectionTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the WeldControlIntersectionTolerance Value.
        """
        return None

    @property
    def Smoothing(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the WeldControlSmoothing.
        """
        return None

    @property
    def CrossSectionId(self) -> typing.Optional[int]:
        """
        Gets or sets the WeldControlCrossSectionId.
        """
        return None

    @property
    def MaterialId(self) -> typing.Optional[int]:
        """
        Gets or sets the WeldControlMaterialId.
        """
        return None

    @property
    def NameFilter(self) -> typing.Optional[str]:
        """
        Gets or sets the NameFilter.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def WeldEdgesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the WeldEdgesNamedSelection.
        """
        return None

    @property
    def BottomEntitiesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the BottomEntitiesNamedSelection.
        """
        return None

    @property
    def TopEntitiesNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the TopEntitiesNamedSelection.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def ClearWeldControlIntersectionTag(self) -> None:
        """
        
             clear the WeldControlIntersectionTag
            
        """
        pass

    def AppendWeldControlIntersectionTag(self, val: str) -> None:
        """
        
             append the WeldControlIntersectionTag
            
        """
        pass

    def GenerateWeldIntersectionTag(self) -> None:
        """
        
             Auto detect Intersection Tags within specified tolerance
            
        """
        pass

    def ClearAutoWeldIntersectionTag(self, includeInactive: bool) -> None:
        """
        
             Clear Auto Intersection Tags
            
        """
        pass

    def WeldWorksheetStatus(self, rowIndex: int) -> Ansys.Mechanical.DataModel.Enums.WeldStatus:
        """
        
             Get state of a given row
            
        """
        pass

    def GetWeldWorksheetNumWarning(self) -> int:
        """
        
             Get Number of rows with warnings
            
        """
        pass

    def GetWeldWorksheetNumError(self) -> int:
        """
        
             Get Number of Errored rows
            
        """
        pass

    def ActivateAllWorksheetEntries(self) -> None:
        """
        
             set the ActivateAllWorksheetEntries
            
        """
        pass

    def DeactivateAllWorksheetEntries(self) -> None:
        """
        
             set the DeactivateAllWorksheetEntries
            
        """
        pass

    def SetWeldWorksheetActive(self, rowIndices: typing.Iterable[int], val: bool) -> None:
        """
        SetWeldWorksheetActive method.
        """
        pass

    def GetWeldWorksheetActive(self, rowIndex: int) -> bool:
        """
        
             get the WeldWorksheetActive
            
        """
        pass

    def SetWeldWorksheetEdgeMeshSize(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetEdgeMeshSize method.
        """
        pass

    def GetWeldWorksheetEdgeMeshSize(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetEdgeMeshSize
            
        """
        pass

    def SetWeldWorksheetWeldAngle(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetWeldAngle method.
        """
        pass

    def GetWeldWorksheetWeldAngle(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetWeldAngle
            
        """
        pass

    def GetWeldWorksheetHAZDistanceBottomPlate(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetHAZDistance
            
        """
        pass

    def SetWeldWorksheetHAZDistanceTopPlate(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetHAZDistanceTopPlate method.
        """
        pass

    def SetWeldWorksheetHAZDistanceBottomPlate(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetHAZDistanceBottomPlate method.
        """
        pass

    def GetWeldWorksheetSharpAngle(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetSharpAngle
            
        """
        pass

    def SetWeldWorksheetSharpAngle(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetSharpAngle method.
        """
        pass

    def GetWeldWorksheetHeight(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetHeight
            
        """
        pass

    def SetWeldWorksheetHeight(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetHeight method.
        """
        pass

    def GetWeldWorksheetLength(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetLength
            
        """
        pass

    def SetWeldWorksheetLength(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetLength method.
        """
        pass

    def GetWeldWorksheetWidth(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetWidth
            
        """
        pass

    def SetWeldWorksheetWidth(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetWidth method.
        """
        pass

    def WeldWorksheetNumEntries(self) -> int:
        """
        
             Get total number of entries in worksheet
            
        """
        pass

    def GetWeldWorksheetPitch(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetPitch
            
        """
        pass

    def SetWeldWorksheetPitch(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetPitch method.
        """
        pass

    def GetWeldWorksheetThickness(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetThickness
            
        """
        pass

    def SetWeldWorksheetThickness(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetThickness method.
        """
        pass

    def GetWeldWorksheetAbsTol(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetAbsTol
            
        """
        pass

    def SetWeldWorksheetAbsTol(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetAbsTol method.
        """
        pass

    def GetWeldWorksheetNumWelds(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetNumWelds
            
        """
        pass

    def SetWeldWorksheetNumWelds(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetNumWelds method.
        """
        pass

    def GetWeldWorksheetOffset1(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetOffset1
            
        """
        pass

    def SetWeldWorksheetOffset1(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetOffset1 method.
        """
        pass

    def GetWeldWorksheetOffset2(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetOffset2
            
        """
        pass

    def SetWeldWorksheetOffset2(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetOffset2 method.
        """
        pass

    def GetWeldWorksheetSmoothing(self, rowIndex: int) -> bool:
        """
        
             get the WeldControlWorksheetSmoothing option
            
        """
        pass

    def SetWeldWorksheetSmoothing(self, rowIndices: typing.Iterable[int], val: bool) -> None:
        """
        SetWeldWorksheetSmoothing method.
        """
        pass

    def GetWeldWorksheetLapAngleTol(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetLapAngleTol
            
        """
        pass

    def SetWeldWorksheetLapAngleTol(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetLapAngleTol method.
        """
        pass

    def GetWeldWorksheetGenerateEndCaps(self, rowIndex: int) -> bool:
        """
        
             get the WeldControlWorksheetGenerateEndCaps
            
        """
        pass

    def SetWeldWorksheetGenerateEndCaps(self, rowIndices: typing.Iterable[int], val: bool) -> None:
        """
        SetWeldWorksheetGenerateEndCaps method.
        """
        pass

    def GetWeldWorksheetHAZGrowthRate(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetHAZGrowthRate
            
        """
        pass

    def SetWeldWorksheetNumLayers(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetNumLayers method.
        """
        pass

    def GetWeldWorksheetNumLayers(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetNumLayers
            
        """
        pass

    def SetWeldWorksheetHAZGrowthRate(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetHAZGrowthRate method.
        """
        pass

    def GetWeldWorksheetMaxThicknessFactor(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetMaxThicknessFactor
            
        """
        pass

    def SetWeldWorksheetMaxThicknessFactor(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetMaxThicknessFactor method.
        """
        pass

    def GetWeldWorksheetMinThicknessFactor(self, rowIndex: int) -> float:
        """
        
             get the WeldControlWorksheetMinThicknessFactor
            
        """
        pass

    def SetWeldWorksheetMinThicknessFactor(self, rowIndices: typing.Iterable[int], val: float) -> None:
        """
        SetWeldWorksheetMinThicknessFactor method.
        """
        pass

    def GetWeldWorksheetThicknessExpression(self, rowIndex: int) -> str:
        """
        
             get the WeldControlWorksheetThicknessExpression
            
        """
        pass

    def SetWeldWorksheetThicknessExpression(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetThicknessExpression method.
        """
        pass

    def GetWeldWorksheetEdgeMeshSizeExpression(self, rowIndex: int) -> str:
        """
        
             get the WeldControlWorksheetEdgeMeshSizeExpression
            
        """
        pass

    def SetWeldWorksheetEdgeMeshSizeExpression(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetEdgeMeshSizeExpression method.
        """
        pass

    def GetWeldWorksheetWeldWidthExpression(self, rowIndex: int) -> str:
        """
        
             get the WeldControlWorksheetWeldWidth
            
        """
        pass

    def SetWeldWorksheetWeldWidthExpression(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetWeldWidthExpression method.
        """
        pass

    def GetWeldWorksheetWeldHeightExpression(self, rowIndex: int) -> str:
        """
        
             get the WeldControlWorksheetWeldHeight
            
        """
        pass

    def SetWeldWorksheetWeldHeightExpression(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetWeldHeightExpression method.
        """
        pass

    def GetWeldWorksheetHAZDistanceExpressionTopPlate(self, rowIndex: int) -> str:
        """
        
             get WorksheetHAZDistanceExpressionTopPlate
            
        """
        pass

    def GetWeldWorksheetHAZDistanceExpressionBottomPlate(self, rowIndex: int) -> str:
        """
        
             get WorksheetHAZDistanceExpressionBottomPlate
            
        """
        pass

    def SetWeldWorksheetHAZDistanceExpressionTopPlate(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetHAZDistanceExpressionTopPlate method.
        """
        pass

    def SetWeldWorksheetHAZDistanceExpressionBottomPlate(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetHAZDistanceExpressionBottomPlate method.
        """
        pass

    def GetWeldWorksheetWeldCurve(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetWeldCurve
            
        """
        pass

    def SetWeldWorksheetWeldCurve(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetWeldCurve method.
        """
        pass

    def DeactivateProblematicWorksheetEntries(self) -> None:
        """
        
             Deactivate Problematic Worksheet Entries
            
        """
        pass

    def GetWeldWorksheetEdges(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetEdges
            
        """
        pass

    def SetWeldWorksheetEdges(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetEdges method.
        """
        pass

    def GetWeldWorksheetBottomEntities(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetBottomEntities
            
        """
        pass

    def SetWeldWorksheetBottomEntities(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetBottomEntities method.
        """
        pass

    def GetWeldWorksheetIntersectionTag(self, rowIndex: int) -> str:
        """
        
             get the WeldControlWorksheetIntersectionTag
            
        """
        pass

    def SetWeldWorksheetIntersectionTag(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        SetWeldWorksheetIntersectionTag method.
        """
        pass

    def ClearWeldWorksheetIntersectionTag(self, rowIndices: typing.Iterable[int]) -> None:
        """
        ClearWeldWorksheetIntersectionTag method.
        """
        pass

    def AppendWeldWorksheetIntersectionTag(self, rowIndices: typing.Iterable[int], val: str) -> None:
        """
        AppendWeldWorksheetIntersectionTag method.
        """
        pass

    def GetWeldWorksheetTopEntities(self, rowIndex: int) -> int:
        """
        
             get the WeldControlWorksheetTopEntities
            
        """
        pass

    def SetWeldWorksheetTopEntities(self, rowIndices: typing.Iterable[int], val: int) -> None:
        """
        SetWeldWorksheetTopEntities method.
        """
        pass

    def GetCrossSectionIds(self, rowIndex: int) -> Ansys.Common.Interop.AnsCoreObjects.IAnsUINTColl:
        """
        
             get CrossSection Ids
            
        """
        pass

    def GetMaterialIds(self, rowIndex: int) -> Ansys.Common.Interop.AnsCoreObjects.IAnsUINTColl:
        """
        
             get Material Ids
            
        """
        pass

    def WeldWorksheetAddEntry(self) -> None:
        """
        
             add an entry to WeldWorksheet
            
        """
        pass

    def WeldWorksheetDeleteEntry(self, indices: typing.Iterable[int]) -> None:
        """
        WeldWorksheetDeleteEntry method.
        """
        pass

    def WeldWorksheetImport(self, fileName: str) -> None:
        """
        
             import WeldWorksheet
            
        """
        pass

    def WeldWorksheetExport(self, fileName: str) -> None:
        """
        
             export WeldWorksheet
            
        """
        pass

    def WeldWorksheetCreateControlForCurveBodies(self) -> None:
        """
        
             Create worksheet entries for all curve bodies
            
        """
        pass

    def AddWeldWorksheetScopeToSelection(self, index: int, subset: int) -> bool:
        """
        
             Create worksheet entry scope to selection
            
        """
        pass

    def PromoteToWeldControl(self, indices: typing.Iterable[int]) -> int:
        """
        PromoteToWeldControl method.
        """
        pass

    def PreviewMeshOnWeldWorksheet(self, rowIndices: typing.Iterable[int]) -> None:
        """
        PreviewMeshOnWeldWorksheet method.
        """
        pass

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Sizing(object):
    """
    Defines a Sizing.
    """

    @property
    def BodyOfInfluence(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets the BodyOfInfluence.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def BiasGrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the BiasGrowthRate.
        """
        return None

    @property
    def NumberOfDivisions(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfDivisions.
        """
        return None

    @property
    def GrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the GrowthRate.
        """
        return None

    @property
    def BiasFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the BiasFactor.
        """
        return None

    @property
    def ElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElementSize.
        """
        return None

    @property
    def SphereRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SphereRadius.
        """
        return None

    @property
    def DefeatureSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DefeatureSize.
        """
        return None

    @property
    def LocalMinimumSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LocalMinimumSize.
        """
        return None

    @property
    def ProximityGapFactor(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ProximityGapFactor.
        """
        return None

    @property
    def ProximityMinimumSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ProximityMinimumSize.
        """
        return None

    @property
    def CurvatureNormalAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CurvatureNormalAngle.
        """
        return None

    @property
    def OriginX(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the OriginX.
        """
        return None

    @property
    def OriginY(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the OriginY.
        """
        return None

    @property
    def OriginZ(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the OriginZ.
        """
        return None

    @property
    def BiasOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BiasOptionType]:
        """
        Gets or sets the BiasOption.
        """
        return None

    @property
    def ProximitySizeSources(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProximitySFSourcesType]:
        """
        Gets or sets the ProximitySizeSources.
        """
        return None

    @property
    def Behavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SizingBehavior]:
        """
        Gets or sets the Behavior.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SizingType]:
        """
        Gets or sets the Type.
        """
        return None

    @property
    def BiasType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BiasType]:
        """
        Gets or sets the BiasType.
        """
        return None

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        Gets the Active.
        """
        return None

    @property
    def CaptureCurvature(self) -> typing.Optional[bool]:
        """
        Gets or sets the CaptureCurvature.
        """
        return None

    @property
    def CaptureProximity(self) -> typing.Optional[bool]:
        """
        Gets or sets the CaptureProximity.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
        """
        return None

    @property
    def SphereCenter(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the SphereCenter.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def ReverseBias(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReverseBias.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class AutomaticMethod(object):
    """
    Defines a AutomaticMethod.
    """

    @property
    def AggressiveInflateOption(self) -> typing.Optional[bool]:
        """
        Gets or sets the AggressiveInflateOption.
        """
        return None

    @property
    def AggressiveTetImprovement(self) -> typing.Optional[bool]:
        """
        Gets or sets the AggressiveTetImprovement.
        """
        return None

    @property
    def ControlMessages(self) -> typing.Optional[bool]:
        """
        Gets the ControlMessages.
        """
        return None

    @property
    def CornerAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CornerAngle.
        """
        return None

    @property
    def DefeatureLayerVolume(self) -> typing.Optional[float]:
        """
        Gets or sets the DefeatureLayerVolume.
        """
        return None

    @property
    def ElementMidsideNodes(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ElementMidsideNodesType]:
        """
        Gets or sets the ElementMidsideNodes.
        """
        return None

    @property
    def ElementOrder(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ElementOrder]:
        """
        Gets or sets the ElementOrder.
        """
        return None

    @property
    def GenerateLayersUsingFacets(self) -> typing.Optional[bool]:
        """
        Gets or sets the GenerateLayersUsingFacets.
        """
        return None

    @property
    def InflateRelativeTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the InflateRelativeTolerance.
        """
        return None

    @property
    def LayerHeight(self) -> typing.Optional[float]:
        """
        Gets or sets the LayerHeight.
        """
        return None

    @property
    def LayerStart(self) -> typing.Optional[float]:
        """
        Gets or sets the LayerStart.
        """
        return None

    @property
    def MeshInCenter(self) -> typing.Optional[int]:
        """
        Gets or sets the MeshInCenter.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MethodType]:
        """
        Gets or sets the Method.
        """
        return None

    @property
    def OverlappingAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the OverlappingAngle.
        """
        return None

    @property
    def ProjectCornersToTop(self) -> typing.Optional[bool]:
        """
        Gets or sets the ProjectCornersToTop.
        """
        return None

    @property
    def RelativeTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the PrimeRelativeTolerance.
        """
        return None

    @property
    def RepairFacets(self) -> typing.Optional[bool]:
        """
        Gets or sets the RepairFacets.
        """
        return None

    @property
    def SlicerFeatureAngle(self) -> typing.Optional[float]:
        """
        Gets or sets the SlicerFeatureAngle.
        """
        return None

    @property
    def SliverTriangleHeight(self) -> typing.Optional[float]:
        """
        Gets or sets the SliverTriangleHeight.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ProjectionFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ProjectionFactor.
        """
        return None

    @property
    def StretchFactorX(self) -> typing.Optional[float]:
        """
        Gets or sets the StretchFactorX.
        """
        return None

    @property
    def StretchFactorY(self) -> typing.Optional[float]:
        """
        Gets or sets the StretchFactorY.
        """
        return None

    @property
    def StretchFactorZ(self) -> typing.Optional[float]:
        """
        Gets or sets the StretchFactorZ.
        """
        return None

    @property
    def SpacingOption(self) -> typing.Optional[int]:
        """
        Gets or sets the SpacingOption.
        """
        return None

    @property
    def SubsampleRate(self) -> typing.Optional[int]:
        """
        Gets or sets the SubsampleRate.
        """
        return None

    @property
    def BFCartSubType(self) -> typing.Optional[int]:
        """
        Gets the BFCartSubType.
        """
        return None

    @property
    def Refinement(self) -> typing.Optional[int]:
        """
        Gets or sets the Refinement.
        """
        return None

    @property
    def FillingFraction(self) -> typing.Optional[float]:
        """
        Gets or sets the FillingFraction.
        """
        return None

    @property
    def ApproximativeNumberOfElementsPerPart(self) -> typing.Optional[int]:
        """
        Gets or sets the ApproximativeNumberOfElementsPerPart.
        """
        return None

    @property
    def DecompositionType(self) -> typing.Optional[int]:
        """
        Gets or sets the MZDecompositionType in Multizone ( 0 = Standard, 1 = ThinSweep, 2 = CartSweep).
        """
        return None

    @property
    def CartSweepSpacingOption(self) -> typing.Optional[int]:
        """
        Gets or sets the  CartSweep SpacingOption in Multizone ( 0 = Uniform, 1 = Key-Points).
        """
        return None

    @property
    def SurfaceMeshMethod(self) -> typing.Optional[int]:
        """
        Gets or sets the SurfaceMeshMethod.
        """
        return None

    @property
    def SweepNumberDivisions(self) -> typing.Optional[int]:
        """
        Gets or sets the SweepNumberDivisions.
        """
        return None

    @property
    def NumberOfCellsAcrossGap(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfCellsAcrossGap.
        """
        return None

    @property
    def FaceProximityGapFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the FaceProximityGapFactor for PCTet.
        """
        return None

    @property
    def FilletCollapse(self) -> typing.Optional[int]:
        """
        Gets or sets the FilletCollapse for AutoNodeMove under PCTet ( 0 = No, 1 = ProgramControlled ).
        """
        return None

    @property
    def ImprovementIterations(self) -> typing.Optional[int]:
        """
        Gets or sets the ImprovementIterations for AutoNodeMove under PCTet.
        """
        return None

    @property
    def NumberOfElementLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfElementLayers for PCTet.
        """
        return None

    @property
    def TetraGrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the TetraGrowthRate.
        """
        return None

    @property
    def PreserveBoundaries(self) -> typing.Optional[int]:
        """
        Gets or sets the PreserveBoundaries.
        """
        return None

    @property
    def SourceTargetSelection(self) -> typing.Optional[int]:
        """
        Gets or sets the SourceTargetSelection.
        """
        return None

    @property
    def LateralDefeatureSize(self) -> typing.Optional[float]:
        """
        Gets or sets the LateralDefeatureSize.
        """
        return None

    @property
    def StackingDefeatureSize(self) -> typing.Optional[float]:
        """
        Gets or sets the StackingDefeatureSize.
        """
        return None

    @property
    def FreeMeshType(self) -> typing.Optional[int]:
        """
        Gets or sets the FreeMeshType.
        """
        return None

    @property
    def MappedSweptType(self) -> typing.Optional[int]:
        """
        Gets or sets the MappedSweptType.
        """
        return None

    @property
    def SweepBiasValue(self) -> typing.Optional[float]:
        """
        Gets or sets the SweepBiasValue.
        """
        return None

    @property
    def SweepESizeType(self) -> typing.Optional[int]:
        """
        Gets or sets the SweepESizeType.
        """
        return None

    @property
    def RadialGrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the RadialGrowthRate.
        """
        return None

    @property
    def FreeFaceMeshType(self) -> typing.Optional[int]:
        """
        Gets or sets the FreeFaceMeshType.
        """
        return None

    @property
    def SweepSizeBehavior(self) -> typing.Optional[int]:
        """
        Gets or sets the SweepSizeBehavior.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def BFCartTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the BFCartTolerance.
        """
        return None

    @property
    def CartesianSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CartesianSize in Multizone.
        """
        return None

    @property
    def CurvatureNormalAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CurvatureNormalAngle.
        """
        return None

    @property
    def Clearence(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Clearence.
        """
        return None

    @property
    def SweepElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepElementSize.
        """
        return None

    @property
    def MaximumElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumElementSize.
        """
        return None

    @property
    def MinimumSizeLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumSizeLimit.
        """
        return None

    @property
    def KeyPointsTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the KeyPoints Tolerance in Multizone.
        """
        return None

    @property
    def MinimumEdgeLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumEdgeLength.
        """
        return None

    @property
    def DefeaturingTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DefeaturingTolerance.
        """
        return None

    @property
    def ParticleDiameter(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ParticleDiameter.
        """
        return None

    @property
    def FeatureProtectionAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DihedralAngle for AutoNodeMove under PCTet.
        """
        return None

    @property
    def MinimumThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumThickness for PCTet.
        """
        return None

    @property
    def FeatureAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FeatureAngle.
        """
        return None

    @property
    def SplitAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SplitAngle in Multizone.
        """
        return None

    @property
    def SweepThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SweepThickness in Multizone.
        """
        return None

    @property
    def KeyPointsSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticOrManual]:
        """
        Gets or sets the KeyPointsSelection.
        """
        return None

    @property
    def FillingDirection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CoordinateSystemAxisType]:
        """
        Gets or sets the FillingDirection.
        """
        return None

    @property
    def DefinedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.PatchIndependentDefineType]:
        """
        Gets or sets the DefinedBy.
        """
        return None

    @property
    def ElementOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SweepElementOptionType]:
        """
        Gets or sets the ElementOption.
        """
        return None

    @property
    def AutomaticNodeMovement(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticNodeMovementMethod]:
        """
        Gets or sets the AutomaticNodeMovement method under PCTet.
        """
        return None

    @property
    def MeshFlowControl(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshFlowControlMethod]:
        """
        Gets or sets the MeshFlowControl.
        """
        return None

    @property
    def MeshType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MethodMeshType]:
        """
        Gets or sets the MeshType.
        """
        return None

    @property
    def TriangleReduction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TriangleReduction]:
        """
        Gets or sets the TriangleReduction.
        """
        return None

    @property
    def SolidShellElementForStacker(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoType]:
        """
        Gets or sets the SolidShellElementForStacker.
        """
        return None

    @property
    def SolidShellElementForStackerScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the SolidShellElementForStackerScopingMethod.
        """
        return None

    @property
    def StackingAxis(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CoordinateSystemAxisType]:
        """
        Gets or sets the StackingAxis.
        """
        return None

    @property
    def StackerFreeFaceMeshType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StackerMethodMeshType]:
        """
        Gets or sets the StackerFreeFaceMeshType.
        """
        return None

    @property
    def StackerTriangleReduction(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TriangleReduction]:
        """
        Gets or sets the StackerTriangleReduction.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshMethodAlgorithm]:
        """
        Gets or sets the Algorithm.
        """
        return None

    @property
    def SweepBiasType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BiasType]:
        """
        Gets or sets the SweepBiasType.
        """
        return None

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        Gets the Active.
        """
        return None

    @property
    def ProjectInConstantZPlane(self) -> typing.Optional[bool]:
        """
        Gets or sets the ProjectInConstantZPlane.
        """
        return None

    @property
    def MeshUsingVoxelization(self) -> typing.Optional[bool]:
        """
        Gets or sets the MeshUsingVoxelization.
        """
        return None

    @property
    def ConstrainBoundary(self) -> typing.Optional[bool]:
        """
        Gets or sets the ConstrainBoundary.
        """
        return None

    @property
    def MeshBasedDefeaturing(self) -> typing.Optional[bool]:
        """
        Gets or sets the MeshBasedDefeaturing.
        """
        return None

    @property
    def PartialFill(self) -> typing.Optional[bool]:
        """
        Gets or sets the PartialFill.
        """
        return None

    @property
    def MatchMeshWherePossible(self) -> typing.Optional[bool]:
        """
        Gets or sets the MatchMeshWherePossible.
        """
        return None

    @property
    def SmoothMeshSpacing(self) -> typing.Optional[bool]:
        """
        Gets or sets the SmoothMeshSpacing in Multizone.
        """
        return None

    @property
    def RefineAtThinSection(self) -> typing.Optional[bool]:
        """
        Gets or sets the RefineAtThinSection for PCTet.
        """
        return None

    @property
    def RefineSurfaceMesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the RefineSurfaceMesh for PCTet.
        """
        return None

    @property
    def RestrictNodeMovementsToSurface(self) -> typing.Optional[bool]:
        """
        Gets or sets the RestrictNodeMovementsToSurface for AutoNodeMove under PCTet.
        """
        return None

    @property
    def ShowAdvancedImproveOptions(self) -> typing.Optional[bool]:
        """
        Gets or sets the ShowAdvancedImproveOptions for AutoNodeMove under PCTet.
        """
        return None

    @property
    def SmoothTransition(self) -> typing.Optional[bool]:
        """
        Gets or sets the SmoothTransition.
        """
        return None

    @property
    def ReuseBlocking(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReuseBlocking.
        """
        return None

    @property
    def UseSplitAngle(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseSplitAngle in Multizone.
        """
        return None

    @property
    def WriteICEMCFDFiles(self) -> typing.Optional[bool]:
        """
        Gets or sets the WriteICEMCFDFiles.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystem.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
        """
        return None

    @property
    def ParticleCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ParticleCoordinateSystem.
        """
        return None

    @property
    def SolidShellElementForStackerNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the SolidShellElementForStackerNamedSelection.
        """
        return None

    @property
    def StackerCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the StackerCoordinateSystem.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def SolidShellElementForStackerGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SolidShellElementForStackerGeometrySelection.
        """
        return None

    @property
    def SourceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SourceLocation.
        """
        return None

    @property
    def SweepEdges(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SweepEdges.
        """
        return None

    @property
    def TargetLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the TargetLocation.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Inflation(object):
    """
    Defines a Inflation.
    """

    @property
    def BoundaryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the BoundaryLocation.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def GrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the GrowthRate.
        """
        return None

    @property
    def InflationAlgorithm(self) -> typing.Optional[int]:
        """
        Gets or sets the InflationAlgorithm.
        """
        return None

    @property
    def InflationOption(self) -> typing.Optional[int]:
        """
        Gets or sets the InflationOption.
        """
        return None

    @property
    def AspectRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the AspectRatio.
        """
        return None

    @property
    def MaximumLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumLayers.
        """
        return None

    @property
    def NumberOfLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfLayers.
        """
        return None

    @property
    def TransitionRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the TransitionRatio.
        """
        return None

    @property
    def FirstLayerHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FirstLayerHeight.
        """
        return None

    @property
    def MaximumThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumThickness.
        """
        return None

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        Gets the Active.
        """
        return None

    @property
    def BoundaryNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the BoundaryNamedSelection.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Mesh(object):
    """
    Defines a Mesh.
    """

    @property
    def Worksheet(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.IWorksheet]:
        """
        Get the MeshControlWorksheet action.
        """
        return None

    @property
    def ElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElementSize.
        """
        return None

    @property
    def RigidBodyFaceMeshType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshControlGroupRigidBodyFaceMeshType]:
        """
        Gets or sets the RigidBodyFaceMeshType.
        """
        return None

    @property
    def RigidBodyBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshControlGroupRigidBodyBehaviorType]:
        """
        Gets or sets the BoundaryCondition.
        """
        return None

    @property
    def CurrentConfiguration(self) -> typing.Optional[int]:
        """
        Gets the Assembly Mesh's current configuration Id.
        """
        return None

    @property
    def MinimizeNumTriangles(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TriangleReduction]:
        """
        Gets or sets the TriangleReduction option for Batch Connections.
        """
        return None

    @property
    def NumberOfShellMeshQualityMetrics(self) -> typing.Optional[int]:
        """
        
            Gets the number of Mesh Quality Metrics
            
        """
        return None

    @property
    def GlobalUseCustomTargetLimit(self) -> typing.Optional[int]:
        """
        Gets or sets the GlobalUseCustomTargetLimit.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ConnectionTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the ConnectionTolerance.
        """
        return None

    @property
    def ConnectionToleranceList(self) -> typing.Optional[str]:
        """
        Gets or sets the ConnectionToleranceList.
        """
        return None

    @property
    def UseAdvancedSizeFunction(self) -> typing.Optional[int]:
        """
        Gets or sets the UseAdvancedSizeFunction.
        """
        return None

    @property
    def Method(self) -> typing.Optional[int]:
        """
        Gets or sets the Method.
        """
        return None

    @property
    def UseAutomaticInflation(self) -> typing.Optional[int]:
        """
        Gets or sets the UseAutomaticInflation.
        """
        return None

    @property
    def AutomaticMeshBasedDefeaturing(self) -> typing.Optional[int]:
        """
        Gets or sets the AutomaticMeshBasedDefeaturing.
        """
        return None

    @property
    def Beam3(self) -> typing.Optional[int]:
        """
        Gets the Beam3.
        """
        return None

    @property
    def Beam4(self) -> typing.Optional[int]:
        """
        Gets the Beam4.
        """
        return None

    @property
    def BeamElements(self) -> typing.Optional[int]:
        """
        Gets the BeamElements.
        """
        return None

    @property
    def CheckMeshQuality(self) -> typing.Optional[int]:
        """
        Gets or sets the CheckMeshQuality.
        """
        return None

    @property
    def CollisionAvoidance(self) -> typing.Optional[int]:
        """
        Gets or sets the CollisionAvoidance.
        """
        return None

    @property
    def ConnectionSize(self) -> typing.Optional[float]:
        """
        Gets or sets the ConnectionSize.
        """
        return None

    @property
    def CornerNodes(self) -> typing.Optional[int]:
        """
        Gets the CornerNodes.
        """
        return None

    @property
    def Elements(self) -> typing.Optional[int]:
        """
        Gets the Elements.
        """
        return None

    @property
    def GrowthRate(self) -> typing.Optional[float]:
        """
        Gets or sets the GrowthRate.
        """
        return None

    @property
    def GrowthRateType(self) -> typing.Optional[int]:
        """
        Gets or sets the GrowthRateType.
        """
        return None

    @property
    def GasketElements(self) -> typing.Optional[int]:
        """
        Gets the GasketElements.
        """
        return None

    @property
    def Hex20(self) -> typing.Optional[int]:
        """
        Gets the Hex20.
        """
        return None

    @property
    def Hex8(self) -> typing.Optional[int]:
        """
        Gets the Hex8.
        """
        return None

    @property
    def HoleRemovalTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the HoleRemovalTolerance.
        """
        return None

    @property
    def InflationAlgorithm(self) -> typing.Optional[int]:
        """
        Gets or sets the InflationAlgorithm.
        """
        return None

    @property
    def MaximumHeightOverBase(self) -> typing.Optional[float]:
        """
        Gets or sets the MaximumHeightOverBase.
        """
        return None

    @property
    def FilletRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the FilletRatio.
        """
        return None

    @property
    def InflationOption(self) -> typing.Optional[int]:
        """
        Gets or sets the InflationOption.
        """
        return None

    @property
    def InitialSizeSeed(self) -> typing.Optional[int]:
        """
        Gets or sets the InitialSizeSeed.
        """
        return None

    @property
    def AspectRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the AspectRatio.
        """
        return None

    @property
    def Line2(self) -> typing.Optional[int]:
        """
        Gets the Line2.
        """
        return None

    @property
    def Line3(self) -> typing.Optional[int]:
        """
        Gets the Line3.
        """
        return None

    @property
    def MaximumLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumLayers.
        """
        return None

    @property
    def MidNodes(self) -> typing.Optional[int]:
        """
        Gets the MidNodes.
        """
        return None

    @property
    def Nodes(self) -> typing.Optional[int]:
        """
        Gets the Nodes.
        """
        return None

    @property
    def NumberOfRetries(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfRetries.
        """
        return None

    @property
    def ProximityGapFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ProximityGapFactor.
        """
        return None

    @property
    def NumberOfCPUsForParallelPartMeshing(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfCPUsForParallelPartMeshing.
        """
        return None

    @property
    def OrientationNodes(self) -> typing.Optional[int]:
        """
        Gets the OrientationNodes.
        """
        return None

    @property
    def GeneratePinchOnRefresh(self) -> typing.Optional[int]:
        """
        Gets or sets the GeneratePinchOnRefresh.
        """
        return None

    @property
    def Pyramid13(self) -> typing.Optional[int]:
        """
        Gets the Pyramid13.
        """
        return None

    @property
    def Pyramid5(self) -> typing.Optional[int]:
        """
        Gets the Pyramid5.
        """
        return None

    @property
    def Quad4(self) -> typing.Optional[int]:
        """
        Gets the Quad4.
        """
        return None

    @property
    def Quad8(self) -> typing.Optional[int]:
        """
        Gets the Quad8.
        """
        return None

    @property
    def Relevance(self) -> typing.Optional[int]:
        """
        Gets or sets the Relevance.
        """
        return None

    @property
    def RelevanceCenter(self) -> typing.Optional[int]:
        """
        Gets or sets the RelevanceCenter.
        """
        return None

    @property
    def Resolution(self) -> typing.Optional[int]:
        """
        Gets or sets the Resolution.
        """
        return None

    @property
    def ShapeChecking(self) -> typing.Optional[int]:
        """
        Gets or sets the ShapeChecking.
        """
        return None

    @property
    def SharedNodes(self) -> typing.Optional[int]:
        """
        Gets the SharedNodes.
        """
        return None

    @property
    def ShellElements(self) -> typing.Optional[int]:
        """
        Gets the ShellElements.
        """
        return None

    @property
    def SmoothingIterations(self) -> typing.Optional[int]:
        """
        Gets or sets the SmoothingIterations.
        """
        return None

    @property
    def Smoothing(self) -> typing.Optional[int]:
        """
        Gets or sets the Smoothing.
        """
        return None

    @property
    def SolidElements(self) -> typing.Optional[int]:
        """
        Gets the SolidElements.
        """
        return None

    @property
    def SolidShellElements(self) -> typing.Optional[int]:
        """
        Gets the SolidShellElements.
        """
        return None

    @property
    def SpanAngleCenter(self) -> typing.Optional[int]:
        """
        Gets or sets the SpanAngleCenter.
        """
        return None

    @property
    def TargetExplicitAspectRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the TargetExplicitAspectRatio.
        """
        return None

    @property
    def TargetQuality(self) -> typing.Optional[float]:
        """
        Gets or sets the TargetQuality.
        """
        return None

    @property
    def Tet10(self) -> typing.Optional[int]:
        """
        Gets the Tet10.
        """
        return None

    @property
    def Tet4(self) -> typing.Optional[int]:
        """
        Gets the Tet4.
        """
        return None

    @property
    def TransitionOption(self) -> typing.Optional[int]:
        """
        Gets or sets the TransitionOption.
        """
        return None

    @property
    def TransitionRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the TransitionRatio.
        """
        return None

    @property
    def GrowthRateSF(self) -> typing.Optional[float]:
        """
        Gets or sets the GrowthRateSF.
        """
        return None

    @property
    def Tri3(self) -> typing.Optional[int]:
        """
        Gets the Tri3.
        """
        return None

    @property
    def Tri6(self) -> typing.Optional[int]:
        """
        Gets the Tri6.
        """
        return None

    @property
    def TriangleSurfaceMesher(self) -> typing.Optional[int]:
        """
        Gets or sets the TriangleSurfaceMesher.
        """
        return None

    @property
    def UsePostSmoothing(self) -> typing.Optional[int]:
        """
        Gets or sets the UsePostSmoothing.
        """
        return None

    @property
    def Wedge15(self) -> typing.Optional[int]:
        """
        Gets the Wedge15.
        """
        return None

    @property
    def Wedge6(self) -> typing.Optional[int]:
        """
        Gets the Wedge6.
        """
        return None

    @property
    def CoplanarAngleTol(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CoplanarAngleTol.
        """
        return None

    @property
    def FirstLayerHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FirstLayerHeight.
        """
        return None

    @property
    def MaximumAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumAngle.
        """
        return None

    @property
    def MaximumThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumThickness.
        """
        return None

    @property
    def MaximumSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumSize.
        """
        return None

    @property
    def DefeatureTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DefeatureTolerance.
        """
        return None

    @property
    def Average(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Average.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def StandardDeviation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the StandardDeviation.
        """
        return None

    @property
    def MinimumEdgeLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumEdgeLength.
        """
        return None

    @property
    def MinimumSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumSize.
        """
        return None

    @property
    def PinchTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PinchTolerance.
        """
        return None

    @property
    def ProximityMinimumSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ProximityMinimumSize.
        """
        return None

    @property
    def CurvatureNormalAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CurvatureNormalAngle.
        """
        return None

    @property
    def TargetCharacteristicLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TargetCharacteristicLength.
        """
        return None

    @property
    def TargetSkewness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TargetSkewness.
        """
        return None

    @property
    def DisplayStyle(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshDisplayStyle]:
        """
        Gets or sets the DisplayStyle.
        """
        return None

    @property
    def ElementOrder(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ElementOrder]:
        """
        Gets or sets the ElementOrder.
        """
        return None

    @property
    def ExportFormat(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FluentExportMeshType]:
        """
        Gets or sets the ExportFormat.
        """
        return None

    @property
    def InflationElementType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshInflationElementType]:
        """
        Gets or Sets the InflationElementType
        """
        return None

    @property
    def MeshMetric(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshMetricType]:
        """
        Gets or sets the MeshMetric.
        """
        return None

    @property
    def PhysicsPreference(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshPhysicsPreferenceType]:
        """
        Gets or sets the PhysicsPreference.
        """
        return None

    @property
    def ExportUnit(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.PolyflowExportUnit]:
        """
        Gets or sets the ExportUnit.
        """
        return None

    @property
    def ProximitySizeSources(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProximitySFSourcesType]:
        """
        Gets or sets the ProximitySizeSources.
        """
        return None

    @property
    def SolverPreference(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshSolverPreferenceType]:
        """
        Gets or sets the SolverPreference.
        """
        return None

    @property
    def ViewAdvancedOptions(self) -> typing.Optional[bool]:
        """
        Gets or sets the ViewAdvancedOptions.
        """
        return None

    @property
    def CaptureCurvature(self) -> typing.Optional[bool]:
        """
        Gets or sets the CaptureCurvature.
        """
        return None

    @property
    def CaptureProximity(self) -> typing.Optional[bool]:
        """
        Gets or sets the CaptureProximity.
        """
        return None

    @property
    def ExtraRetriesForAssembly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExtraRetriesForAssembly.
        """
        return None

    @property
    def MeshMorphing(self) -> typing.Optional[bool]:
        """
        Gets or sets the MeshMorphing.
        """
        return None

    @property
    def MultiConnectionSteps(self) -> typing.Optional[bool]:
        """
        Gets or sets the MultiConnectionSteps.
        """
        return None

    @property
    def UseSheetThicknessForPinch(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseSheetThicknessForPinch.
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets the ReadOnly.
        """
        return None

    @property
    def SheetLoopRemoval(self) -> typing.Optional[bool]:
        """
        Gets or sets the SheetLoopRemoval.
        """
        return None

    @property
    def ShowDetailedStatistics(self) -> typing.Optional[bool]:
        """
        Gets or sets the ShowDetailedStatistics.
        """
        return None

    @property
    def StraightSidedElements(self) -> typing.Optional[bool]:
        """
        Gets or sets the StraightSidedElements.
        """
        return None

    @property
    def TopologyChecking(self) -> typing.Optional[bool]:
        """
        Gets or sets the TopologyChecking.
        """
        return None

    @property
    def UseAdaptiveSizing(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseAdaptiveSizing.
        """
        return None

    @property
    def UseFixedSizeFunctionForSheets(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseFixedSizeFunctionForSheets.
        """
        return None

    @property
    def QuadMesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the QuadMesh.
        """
        return None

    @property
    def MeshBasedConnection(self) -> typing.Optional[bool]:
        """
        Gets or sets the MeshBasedConnection.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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

    def PreviewWelds(self) -> None:
        """
        Preview Welds.
        """
        pass

    def PreviewMeshOnWelds(self, dataModelObjects: typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> None:
        """
        PreviewMeshOnWelds method.
        """
        pass

    def PreviewMeshOnWeld(self, dataModelObject: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject) -> None:
        """
        
            Preview model mesh on one weld control provided.
            
        """
        pass

    def PreviewMeshOnAllWelds(self) -> None:
        """
        
            Preview model mesh on all weld controls of the Mesh.
            
        """
        pass

    def ShowOverlappingFaces(self) -> None:
        """
        Run the ShowOverlappingFaces action.
        """
        pass

    def ShowUnconnectedFacesNearEdges(self) -> None:
        """
        Run the  ShowUnconnectedFreeEdges action.
        """
        pass

    def PreviewMeshOnWeldWorksheet(self, dataModelObject: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject, indices: typing.Iterable[int]) -> None:
        """
        PreviewMeshOnWeldWorksheet method.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def CleanPartOrBody(self, dataModelObjects: typing.Iterable) -> None:
        """
        
            Clear generated data for parts and/or bodies provided.
            
        """
        pass

    def AddNodeMergeGroup(self) -> Ansys.ACT.Automation.Mechanical.NodeMergeGroup:
        """
        Add a new NodeMergeGroup.
        """
        pass

    def AddNodeMerge(self) -> None:
        """
        Add a new NodeMerge.
        """
        pass

    def AddAutomaticMethod(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.AutomaticMethod:
        """
        Creates a new AutomaticMethod
        """
        pass

    def AddMeshConnectionGroup(self) -> Ansys.ACT.Automation.Mechanical.MeshConnectionGroup:
        """
        
            Add a new MeshConnectionGroup.
            
        """
        pass

    def AddContactMatchGroup(self) -> Ansys.ACT.Automation.Mechanical.ContactMatchGroup:
        """
        
            Add a new AddContactMatchGroup.
            
        """
        pass

    def AddManualMeshConnection(self) -> None:
        """
        
            Add a new ManualMeshConnection
            
        """
        pass

    def AddPullExtrude(self) -> Ansys.ACT.Automation.Mechanical.MeshExtrude:
        """
        
            Add a new Pull (Extrude).
            
        """
        pass

    def AddPullRevolve(self) -> Ansys.ACT.Automation.Mechanical.MeshExtrude:
        """
        
            Add a new Pull (Revolve).
            
        """
        pass

    def AddPullSurfaceCoating(self) -> Ansys.ACT.Automation.Mechanical.MeshExtrude:
        """
        
            Add a new Pull (Surface Coating)).
            
        """
        pass

    def AddDirectMorph(self) -> Ansys.ACT.Automation.Mechanical.DirectMorph:
        """
        
            Add a new DirectMorph.
            
        """
        pass

    def AddDeviation(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Deviation:
        """
        Creates a new SagControl
        """
        pass

    def AddWasher(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Washer:
        """
        Creates a new SagControl
        """
        pass

    def AddWeld(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Weld:
        """
        Creates a new WeldControl
        """
        pass

    def AddRepairTopology(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.RepairTopology:
        """
        Creates a new RepairTopology
        """
        pass

    def AddConnect(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Connect:
        """
        Creates a new Connect Control
        """
        pass

    def AddFeatureSuppress(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.FeatureSuppress:
        """
        Creates a new FeatureSuppress
        """
        pass

    def AddGeometryFidelity(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.GeometryFidelity:
        """
        Creates a new GeometryFidelity
        """
        pass

    def AddMeshCopy(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.MeshCopy:
        """
        Creates a new MeshCopy
        """
        pass

    def PinchControlGeomtry(self, geomType: Ansys.Mechanical.DataModel.Enums.MeshControlPinchGeomtryType) -> None:
        """
        Set the geometry type for the Pinch Control.
        """
        pass

    def IsMeshMetricVisible(self, index: int) -> bool:
        """
        IsMeshMetricVisible method.
        """
        pass

    def GetIsShellTargetMetric(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
            Get Shell Target Metric
            
        """
        pass

    def GetActiveSurfaceMeshQuality(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> bool:
        """
        
             Get Active User Mesh Quality
             
        """
        pass

    def GetSurfaceMeshQualityName(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> str:
        """
        
             Get Mesh Quality Name
             
        """
        pass

    def GetSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get User Mesh Quality Warning Limit
             
        """
        pass

    def GetSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get User Mesh Quality Error Limit
             
        """
        pass

    def GetSurfaceMeshQualityPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Percentage Failed 
             
        """
        pass

    def GetSurfaceMeshQualityCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Count Failed
             
        """
        pass

    def GetSurfaceMeshQualityWarningPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Warning Percentage Failed 
             
        """
        pass

    def GetSurfaceMeshQualityWarningCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Warning Count Failed
             
        """
        pass

    def GetSurfaceMeshQualityWorstMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Worst Metric Value
             
        """
        pass

    def GetSurfaceMeshQualityAverageMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Average Metric Value
             
        """
        pass

    def SetActiveSurfaceMeshQuality(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, activeMetric: float) -> None:
        """
        
             Set Active Mesh Quality 
             
        """
        pass

    def SetSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: float) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: float) -> None:
        """
        
              Set Mesh Quality Error Level
             
        """
        pass

    def SetSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Error Level
             
        """
        pass

    def CreateMQSurfaceElementsNamedSelection(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, failCode: int) -> None:
        """
        
              Create Mesh Quality Surface Element Named Selection
             
        """
        pass

    def GetIsSolidTargetMetric(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
            Get Solid Target Metric
            
        """
        pass

    def GetVolumeMeshQualityName(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> str:
        """
        
             Get Mesh Quality Name
             
        """
        pass

    def GetVolumeMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Warning Limit
             
        """
        pass

    def GetVolumeMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Error Limit
             
        """
        pass

    def GetVolumeMeshQualityPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Percentage Failed 
             
        """
        pass

    def GetVolumeMeshQualityCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Count Failed
             
        """
        pass

    def GetVolumeMeshQualityWarningPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Warning Percentage Failed 
             
        """
        pass

    def GetVolumeMeshQualityWarningCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Warning Count Failed
             
        """
        pass

    def GetVolumeMeshQualityWorstMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Worst Metric Value
             
        """
        pass

    def GetVolumeMeshQualityAverageMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Average Metric Value
             
        """
        pass

    def GetVolumeMeshQualityWorstMetricBackgroundColor(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> str:
        """
        
             Get Mesh Quality Worst Metric BackgroundColor
             
        """
        pass

    def SetActiveVolumeMeshQuality(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, activeMetric: float) -> None:
        """
        
             Set Active Mesh Quality 
             
        """
        pass

    def SetVolumeMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: float) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetVolumeMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetVolumeMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: float) -> None:
        """
        
              Set Mesh Quality Error Limit
             
        """
        pass

    def SetVolumeMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Error Limit
             
        """
        pass

    def CreateMQVolumeElementsNamedSelection(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, failCode: int) -> None:
        """
        
              Create Mesh Quality Volume Element Name Selection
             
        """
        pass

    def GetIsSolidSurfaceTargetMetric(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
            Get SolidSurface Target Metric
            
        """
        pass

    def GetSolidSurfaceMeshQualityName(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> str:
        """
        
             Get Mesh Quality Name
             
        """
        pass

    def GetSolidSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Warning Limit
             
        """
        pass

    def GetSolidSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Error Limit
             
        """
        pass

    def GetSolidSurfaceMeshQualityPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Percentage Failed 
             
        """
        pass

    def GetSolidSurfaceMeshQualityCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Count Failed
             
        """
        pass

    def GetSolidSurfaceMeshQualityWarningPercentageFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> float:
        """
        
             Get Mesh Quality Warning Percentage Failed 
             
        """
        pass

    def GetSolidSurfaceMeshQualityWarningCountFailed(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> int:
        """
        
             Get Mesh Quality Warning Count Failed
             
        """
        pass

    def GetSolidSurfaceMeshQualityWorstMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Worst Metric Value
             
        """
        pass

    def GetSolidSurfaceMeshQualityAverageMetricValue(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Core.Units.Quantity:
        """
        
             Get Mesh Quality Average Metric Value
             
        """
        pass

    def GetSolidSurfaceMeshQualityWorstMetricBackgroundColor(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> str:
        """
        
             Get Mesh Quality Worst Metric BackgroundColor
             
        """
        pass

    def SetActiveSolidSurfaceMeshQuality(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, activeMetric: float) -> None:
        """
        
             Set Active Mesh Quality 
             
        """
        pass

    def SetSolidSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: float) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetSolidSurfaceMeshQualityWarningLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Warning Limit
             
        """
        pass

    def SetSolidSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: float) -> None:
        """
        
              Set Mesh Quality Error Limit
             
        """
        pass

    def SetSolidSurfaceMeshQualityErrorLimit(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, errorLevel: Ansys.Core.Units.Quantity) -> None:
        """
        
              Set Mesh Quality Error Limit
             
        """
        pass

    def CreateMQSolidSurfaceElementsNamedSelection(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, failCode: int) -> None:
        """
        
              Create Mesh Quality SolidSurface Element Name Selection
             
        """
        pass

    def LoadMQWorksheetFile(self, filePath: str) -> None:
        """
        LoadMQWorksheetFile method.
        """
        pass

    def SaveMQWorksheetFile(self, filePath: str) -> None:
        """
        SaveMQWorksheetFile method.
        """
        pass

    def GetVolumeMeshMetrics(self) -> Ansys.Mechanical.DataModel.Enums.MeshMetricType:
        """
        GetVolumeMeshMetrics method.
        """
        pass

    def GetSolidSurfaceMeshMetrics(self) -> Ansys.Mechanical.DataModel.Enums.MeshMetricType:
        """
        GetSolidSurfaceMeshMetrics method.
        """
        pass

    def SetSurfaceMeshMetricLimits(self, metricType: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLimit: Ansys.Core.Units.Quantity, ErrorLimit: Ansys.Core.Units.Quantity) -> None:
        """
        SetSurfaceMeshMetricLimits method.
        """
        pass

    def SetSolidMeshMetricLimits(self, metricType: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLimit: Ansys.Core.Units.Quantity, ErrorLimit: Ansys.Core.Units.Quantity) -> None:
        """
        SetSolidMeshMetricLimits method.
        """
        pass

    def SetSolidSurfaceMeshMetricLimits(self, metricType: Ansys.Mechanical.DataModel.Enums.MeshMetricType, warningLimit: Ansys.Core.Units.Quantity, ErrorLimit: Ansys.Core.Units.Quantity) -> None:
        """
        SetSolidSurfaceMeshMetricLimits method.
        """
        pass

    def ActivateAllSurfaceWorksheetRows(self) -> None:
        """
        ActivateAllSurfaceWorksheetRows method.
        """
        pass

    def ActivateAllVolumeWorksheetRows(self) -> None:
        """
        ActivateAllVolumeWorksheetRows method.
        """
        pass

    def ActivateAllSolidSurfaceWorksheetRows(self) -> None:
        """
        ActivateAllSolidSurfaceWorksheetRows method.
        """
        pass

    def DeactivateAllSurfaceWorksheetRows(self) -> None:
        """
        DeactivateAllSurfaceWorksheetRows method.
        """
        pass

    def DeactivateAllVolumeWorksheetRows(self) -> None:
        """
        DeactivateAllVolumeWorksheetRows method.
        """
        pass

    def DeactivateAllSolidSurfaceWorksheetRows(self) -> None:
        """
        DeactivateAllSolidSurfaceWorksheetRows method.
        """
        pass

    def SetMeshMetricOptions(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType, prefValue: Ansys.Mechanical.DataModel.Enums.MetricPreference) -> None:
        """
        SetMeshMetricOptions method.
        """
        pass

    def GetMeshMetricOptions(self, meshMetric: Ansys.Mechanical.DataModel.Enums.MeshMetricType) -> Ansys.Mechanical.DataModel.Enums.MetricPreference:
        """
        GetMeshMetricOptions method.
        """
        pass

    def AddContactSizing(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.ContactSizing:
        """
        Creates a new ContactSizing
        """
        pass

    def AddFaceMeshing(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.FaceMeshing:
        """
        Creates a new FaceMeshing
        """
        pass

    def AddInflation(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Inflation:
        """
        Creates a new Inflation
        """
        pass

    def AddMatchControl(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.MatchControl:
        """
        Creates a new MatchControl
        """
        pass

    def AddPinch(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Pinch:
        """
        Creates a new Pinch
        """
        pass

    def AddRefinement(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Refinement:
        """
        Creates a new Refinement
        """
        pass

    def AddSizing(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.Sizing:
        """
        Creates a new Sizing
        """
        pass

    def CreatePinchControls(self) -> None:
        """
        Run the CreatePinchControls action.
        """
        pass

    def GenerateMesh(self) -> None:
        """
        Run the GenerateMesh action.
        """
        pass

    def PreviewInflation(self) -> None:
        """
        Run the PreviewInflation action.
        """
        pass

    def PreviewSurfaceMesh(self) -> None:
        """
        Run the PreviewSurfaceMesh action.
        """
        pass

    def ShowFeatureSuppressibleFaces(self) -> None:
        """
        Run the ShowFeatureSuppressibleFaces action.
        """
        pass

    def ShowMappableBodies(self) -> None:
        """
        Run the ShowMappableBodies action.
        """
        pass

    def ShowSweepableBodies(self) -> None:
        """
        Run the ShowSweepableBodies action.
        """
        pass

    def Update(self) -> None:
        """
        Run the Update action.
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


class MeshControl(object):
    """
    Defines a MeshControl.
    """

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Connect(object):
    """
    Defines a Connect.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ConnectionToleranceList(self) -> typing.Optional[str]:
        """
        Gets or sets the ConnectionToleranceList.
        """
        return None

    @property
    def ConnectionTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ConnectionTolerance.
        """
        return None

    @property
    def ConnectionSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ConnectionSize.
        """
        return None

    @property
    def CoplanarAngleTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CoplanarAngleTolerance.
        """
        return None

    @property
    def ConnectionOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConnectionOptions]:
        """
        Gets or sets the ConnectionOption.
        """
        return None

    @property
    def MultipleConnectionStep(self) -> typing.Optional[bool]:
        """
        Gets or sets the MultipleConnectionStep.
        """
        return None

    @property
    def PerformIntersections(self) -> typing.Optional[bool]:
        """
        Gets or sets the PerformIntersections.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class ContactSizing(object):
    """
    Defines a ContactSizing.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Relevance(self) -> typing.Optional[float]:
        """
        Gets or sets the Relevance.
        """
        return None

    @property
    def Type(self) -> typing.Optional[int]:
        """
        Gets or sets the Type.
        """
        return None

    @property
    def ElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElementSize.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class FaceMeshing(object):
    """
    Defines a FaceMeshing.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ConstrainBoundary(self) -> typing.Optional[int]:
        """
        Gets or sets the ConstrainBoundary.
        """
        return None

    @property
    def InternalNumberOfDivisions(self) -> typing.Optional[int]:
        """
        Gets or sets the InternalNumberOfDivisions.
        """
        return None

    @property
    def Method(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FaceMeshingMethod]:
        """
        Gets or sets the Method.
        """
        return None

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        Gets the Active.
        """
        return None

    @property
    def MappedMesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the MappedMesh.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def SpecifiedCorners(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SpecifiedCorners.
        """
        return None

    @property
    def SpecifiedEnds(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SpecifiedEnds.
        """
        return None

    @property
    def SpecifiedSides(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SpecifiedSides.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class FeatureSuppress(object):
    """
    Defines a FeatureSuppress.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def FeatureHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        To specify the Feature Height.
        """
        return None

    @property
    def SourceSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FeatureSuppressMethod]:
        """
        To select the FeatureSuppress method.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
        """
        return None

    @property
    def SourceNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the SourceNamedSelection.
        """
        return None

    @property
    def SourceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        To specify the face selections for the method: Defeature Faces or Parent Faces.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class GeometryFidelity(object):
    """
    Defines a GeometryFidelity.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class MatchControl(object):
    """
    Defines a MatchControl.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Transformation(self) -> typing.Optional[int]:
        """
        Gets or sets the Transformation.
        """
        return None

    @property
    def ControlMessages(self) -> typing.Optional[bool]:
        """
        Gets the ControlMessages.
        """
        return None

    @property
    def HighNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the HighNamedSelection.
        """
        return None

    @property
    def LowNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the LowNamedSelection.
        """
        return None

    @property
    def RotationAxis(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the RotationAxis.
        """
        return None

    @property
    def HighCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the HighCoordinateSystem.
        """
        return None

    @property
    def LowCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the LowCoordinateSystem.
        """
        return None

    @property
    def HighGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the HighGeometrySelection.
        """
        return None

    @property
    def LowGeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the LowGeometrySelection.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class MeshCopy(object):
    """
    Defines a MeshCopy.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def NodeMergeTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the NodeMergeTolerance.
        """
        return None

    @property
    def PercentageOfElementSize(self) -> typing.Optional[float]:
        """
        Gets or sets the PercentageOfElementSize.
        """
        return None

    @property
    def NodeMergeToleranceOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NodeMergeToleranceMethod]:
        """
        Gets or sets the NodeMergeToleranceOption.
        """
        return None

    @property
    def TargetScoping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the TargetScoping.
        """
        return None

    @property
    def SourceAnchorsNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the SourceAnchorsNamedSelection.
        """
        return None

    @property
    def TargetAnchorsNamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the TargetAnchorsNamedSelection.
        """
        return None

    @property
    def SourceAnchors(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SourceAnchors.
        """
        return None

    @property
    def TargetAnchors(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the TargetAnchors.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Pinch(object):
    """
    Defines a Pinch.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def AutoManualMode(self) -> typing.Optional[int]:
        """
        Gets the AutoManualMode.
        """
        return None

    @property
    def Tolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Tolerance.
        """
        return None

    @property
    def MasterGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MasterGeometry.
        """
        return None

    @property
    def SlaveGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SlaveGeometry.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Refinement(object):
    """
    Defines a Refinement.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def NumberOfRefinements(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfRefinements.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


class Relevance(object):
    """
    Defines a Relevance.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSMeshControlAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def PartRelavance(self) -> typing.Optional[int]:
        """
        Gets the PartRelavance.
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Gets or sets the NamedSelection.
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
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
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

    def GenerateMesh(self) -> None:
        """
        Generate the Mesh.
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


