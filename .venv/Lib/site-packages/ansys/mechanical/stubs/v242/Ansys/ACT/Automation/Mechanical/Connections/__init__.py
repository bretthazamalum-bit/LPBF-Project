"""Connections module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AMBondConnection(object):
    """
    Defines a AMBondConnection.
    """

    @property
    def SourceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SourceLocation.
        """
        return None

    @property
    def TargetLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the TargetLocation.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMBondConnectionAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ContactBodies(self) -> typing.Optional[str]:
        """
        Gets the ContactBodies.
        """
        return None

    @property
    def TargetBodies(self) -> typing.Optional[str]:
        """
        Gets the TargetBodies.
        """
        return None

    @property
    def ContactType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactType]:
        """
        Gets or sets the ContactType.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def SearchConnectionsForDuplicatePairs(self) -> None:
        """
        Run the SearchConnectionsForDuplicatePairs action.
        """
        pass

    def FlipContactTarget(self) -> None:
        """
        Run the FlipContactTarget action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
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


class SpotWeldConnection(object):
    """
    Defines a SpotWeldConnection.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSSpotWeldConnectionAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Material(self) -> typing.Optional[str]:
        """
        Gets or sets the Material.
        """
        return None

    @property
    def NumberOfLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfLayers.
        """
        return None

    @property
    def NumWeldPoints(self) -> typing.Optional[int]:
        """
        Gets the NumWeldPoints.
        """
        return None

    @property
    def AngleTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the AngleTolerance.
        """
        return None

    @property
    def PenetrationTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PenetrationTolerance.
        """
        return None

    @property
    def Radius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Radius.
        """
        return None

    @property
    def SnapToEdgeTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SnapToEdgeTolerance.
        """
        return None

    @property
    def SearchDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SearchDistance.
        """
        return None

    @property
    def ConnectionBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StiffnessBehavior]:
        """
        Gets or sets the ConnectionBehavior.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpotWeldTypes]:
        """
        Gets or sets the Type.
        """
        return None

    @property
    def StiffnessBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StiffnessBehavior]:
        """
        Gets or sets the StiffnessBehavior.
        """
        return None

    @property
    def ShellThicknessEffect(self) -> typing.Optional[bool]:
        """
        Gets or sets the ShellThicknessEffect.
        """
        return None

    @property
    def SourceGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SourceGeometry.
        """
        return None

    @property
    def TargetGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the TargetGeometry.
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
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def SetXCoordinate(self, spotWeldId: int, val: Ansys.Core.Units.Quantity) -> None:
        """
        Set the X coordinate given the Spot Weld ID.
        """
        pass

    def SetYCoordinate(self, spotWeldId: int, val: Ansys.Core.Units.Quantity) -> None:
        """
        Set the Y coordinate given the Spot Weld ID.
        """
        pass

    def SetZCoordinate(self, spotWeldId: int, val: Ansys.Core.Units.Quantity) -> None:
        """
        Set the Z coordinate given the Spot Weld ID.
        """
        pass

    def AddNewSpotWeld(self, customId: int) -> None:
        """
        Add a new spot weld with/without a customID.
        """
        pass

    def RemoveSpotWeld(self, spotWeldId: int) -> None:
        """
        Remove an existing spot weld.
        """
        pass

    def ExportToCSVFile(self, fileName: str) -> None:
        """
        Export the contents to a CSV file.
        """
        pass

    def CreateSpotWeldFromHitPoint(self) -> None:
        """
        Add a new spot weld by using a Hit Point.
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


class SpotWeldGroup(object):
    """
    Defines a SpotWeldGroup.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSSpotWeldGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Material(self) -> typing.Optional[str]:
        """
        Gets or sets the Material.
        """
        return None

    @property
    def NumConnections(self) -> typing.Optional[int]:
        """
        Gets the NumConnections.
        """
        return None

    @property
    def NumberOfLayers(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfLayers.
        """
        return None

    @property
    def NumWeldPoints(self) -> typing.Optional[int]:
        """
        Gets the NumWeldPoints.
        """
        return None

    @property
    def SpotWeldFileName(self) -> typing.Optional[str]:
        """
        Gets or sets the SpotWeldFileName.
        """
        return None

    @property
    def AngleTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the AngleTolerance.
        """
        return None

    @property
    def PenetrationTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PenetrationTolerance.
        """
        return None

    @property
    def SnapToEdgeTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SnapToEdgeTolerance.
        """
        return None

    @property
    def WeldRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WeldRadius.
        """
        return None

    @property
    def WeldSearchDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WeldSearchDistance.
        """
        return None

    @property
    def ChildrenCreationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConnectionCreationMethod]:
        """
        Gets or sets the ChildrenCreationMethod.
        """
        return None

    @property
    def ConnectionBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StiffnessBehavior]:
        """
        Gets or sets the ConnectionBehavior.
        """
        return None

    @property
    def Units(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the Units.
        """
        return None

    @property
    def WeldType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpotWeldTypes]:
        """
        Gets or sets the WeldType.
        """
        return None

    @property
    def StiffnessBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StiffnessBehavior]:
        """
        Gets or sets the StiffnessBehavior.
        """
        return None

    @property
    def ShellThicknessEffect(self) -> typing.Optional[bool]:
        """
        Gets or sets the ShellThicknessEffect.
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
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def AddSpotWeldConnection(self) -> Ansys.ACT.Automation.Mechanical.Connections.SpotWeldConnection:
        """
        Creates a new child SpotWeldConnection.
        """
        pass

    def ExportToFile(self, filePath: str) -> None:
        """
        Exports all spot welds to user selected path.
        """
        pass

    def GenerateSpotWeldConnections(self) -> None:
        """
        Generate spot welds provided in the Weld input file.
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


class Beam(object):
    """
    Defines a Beam.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSBeamConnectionAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def BeamElementAPDLName(self) -> typing.Optional[str]:
        """
        Gets or sets the BeamElementAPDLName.
        """
        return None

    @property
    def Material(self) -> typing.Optional[str]:
        """
        Gets or sets the Material.
        """
        return None

    @property
    def MobileBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the MobileBeamMaterial.
        """
        return None

    @property
    def MobileBody(self) -> typing.Optional[str]:
        """
        Gets the MobileBody.
        """
        return None

    @property
    def ReferenceBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the ReferenceBeamMaterial.
        """
        return None

    @property
    def ReferenceBody(self) -> typing.Optional[str]:
        """
        Gets the ReferenceBody.
        """
        return None

    @property
    def MobileBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileBeamRadius.
        """
        return None

    @property
    def MobileXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileXCoordinate.
        """
        return None

    @property
    def MobileYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileYCoordinate.
        """
        return None

    @property
    def MobileZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileZCoordinate.
        """
        return None

    @property
    def MobilePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobilePinballRegion.
        """
        return None

    @property
    def Radius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Radius.
        """
        return None

    @property
    def ReferenceBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceBeamRadius.
        """
        return None

    @property
    def ReferenceXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceXCoordinate.
        """
        return None

    @property
    def ReferenceYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceYCoordinate.
        """
        return None

    @property
    def ReferenceZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceZCoordinate.
        """
        return None

    @property
    def ReferencePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferencePinballRegion.
        """
        return None

    @property
    def CrossSection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CrossSectionType]:
        """
        Gets the CrossSection.
        """
        return None

    @property
    def MobileAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the MobileAppliedBy.
        """
        return None

    @property
    def MobileBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the MobileBehavior.
        """
        return None

    @property
    def ReferenceAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the ReferenceAppliedBy.
        """
        return None

    @property
    def ReferenceBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the ReferenceBehavior.
        """
        return None

    @property
    def Scope(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringScopingType]:
        """
        Gets or sets the Scope.
        """
        return None

    @property
    def Visible(self) -> typing.Optional[bool]:
        """
        Gets or sets the Visible.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def MobileCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the MobileCoordinateSystem.
        """
        return None

    @property
    def ReferenceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ReferenceCoordinateSystem.
        """
        return None

    @property
    def MobileLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MobileLocation.
        """
        return None

    @property
    def ReferenceLocationPoint(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceLocationPoint.
        """
        return None

    @property
    def ReferenceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceLocation.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def PromoteToRemotePoint(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Run the PromoteToRemotePoint action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
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


class Bearing(object):
    """
    Defines a Bearing.
    """

    @property
    def ReferenceSet(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets the ReferenceSet.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSBearingAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def AnsBCType(self) -> typing.Optional[int]:
        """
        Gets the AnsBCType.
        """
        return None

    @property
    def MobileBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the MobileBeamMaterial.
        """
        return None

    @property
    def MobileBody(self) -> typing.Optional[str]:
        """
        Gets the MobileBody.
        """
        return None

    @property
    def ReferenceBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the ReferenceBeamMaterial.
        """
        return None

    @property
    def ReferenceBodyName(self) -> typing.Optional[str]:
        """
        Gets the ReferenceBodyName.
        """
        return None

    @property
    def DampingC11(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the DampingC11.
        """
        return None

    @property
    def DampingC12(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the DampingC12.
        """
        return None

    @property
    def DampingC21(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the DampingC21.
        """
        return None

    @property
    def DampingC22(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the DampingC22.
        """
        return None

    @property
    def StiffnessK11(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the StiffnessK11.
        """
        return None

    @property
    def StiffnessK12(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the StiffnessK12.
        """
        return None

    @property
    def StiffnessK21(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the StiffnessK21.
        """
        return None

    @property
    def StiffnessK22(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the StiffnessK22.
        """
        return None

    @property
    def MobileBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileBeamRadius.
        """
        return None

    @property
    def MobileXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileXCoordinate.
        """
        return None

    @property
    def MobileYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileYCoordinate.
        """
        return None

    @property
    def MobileZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileZCoordinate.
        """
        return None

    @property
    def MobilePinballSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobilePinballSize.
        """
        return None

    @property
    def ReferenceBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceBeamRadius.
        """
        return None

    @property
    def ReferenceXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceXCoordinate.
        """
        return None

    @property
    def ReferenceYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceYCoordinate.
        """
        return None

    @property
    def ReferenceZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceZCoordinate.
        """
        return None

    @property
    def ReferencePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferencePinballRegion.
        """
        return None

    @property
    def MobileBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the MobileBehavior.
        """
        return None

    @property
    def ReferenceBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the ReferenceBehavior.
        """
        return None

    @property
    def ReferenceRotationPlane(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RotationPlane]:
        """
        Gets or sets the ReferenceRotationPlane.
        """
        return None

    @property
    def ConnectionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConnectionScopingType]:
        """
        Gets or sets the ConnectionType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def MobileCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the MobileCoordinateSystem.
        """
        return None

    @property
    def ReferenceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ReferenceCoordinateSystem.
        """
        return None

    @property
    def MobileLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MobileLocation.
        """
        return None

    @property
    def ReferenceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceLocation.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def PromoteToRemotePoint(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Run the PromoteToRemotePoint action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
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


class BodyInteraction(object):
    """
    Defines a BodyInteraction.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSBodyInteractionAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def DecayConstant(self) -> typing.Optional[float]:
        """
        Gets or sets the DecayConstant.
        """
        return None

    @property
    def DynamicCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the DynamicCoefficient.
        """
        return None

    @property
    def NormalForceExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the NormalForceExponent.
        """
        return None

    @property
    def NormalStressExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the NormalStressExponent.
        """
        return None

    @property
    def ShearForceExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearForceExponent.
        """
        return None

    @property
    def ShearStressExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearStressExponent.
        """
        return None

    @property
    def FrictionCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the FrictionCoefficient.
        """
        return None

    @property
    def MaximumOffset(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumOffset.
        """
        return None

    @property
    def NormalForceLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the NormalForceLimit.
        """
        return None

    @property
    def NormalStressLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the NormalStressLimit.
        """
        return None

    @property
    def ShearForceLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ShearForceLimit.
        """
        return None

    @property
    def ShearStressLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ShearStressLimit.
        """
        return None

    @property
    def Breakable(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BondedBreakableType]:
        """
        Gets or sets the Breakable.
        """
        return None

    @property
    def ContactType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactType]:
        """
        Gets or sets the ContactType.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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


class ContactRegion(object):
    """
    Defines a ContactRegion.
    """

    @property
    def ContactAPDLName(self) -> typing.Optional[str]:
        """
        Gets or sets the ContactAPDLName.
        """
        return None

    @property
    def TargetAPDLName(self) -> typing.Optional[str]:
        """
        Gets or sets the TargetAPDLName.
        """
        return None

    @property
    def SourceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SourceLocation.
        """
        return None

    @property
    def TargetLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the TargetLocation.
        """
        return None

    @property
    def AutomaticNormalStiffness(self) -> typing.Optional[bool]:
        """
        Gets or sets the AutomaticNormalStiffness.
        """
        return None

    @property
    def BeamMaterialName(self) -> typing.Optional[str]:
        """
        Gets or sets the BeamMaterialName.
        """
        return None

    @property
    def BeamBeamDetection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BeamBeamContactDetectionType]:
        """
        Gets or sets the BeamBeamDetection.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSContactRegionAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Material(self) -> typing.Optional[str]:
        """
        Gets or sets the Material.
        """
        return None

    @property
    def StabilizationDampingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the StabilizationDampingFactor.
        """
        return None

    @property
    def DecayConstant(self) -> typing.Optional[float]:
        """
        Gets or sets the DecayConstant.
        """
        return None

    @property
    def DynamicCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the DynamicCoefficient.
        """
        return None

    @property
    def ElasticSlipToleranceFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticSlipToleranceFactor.
        """
        return None

    @property
    def FrictionCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the FrictionCoefficient.
        """
        return None

    @property
    def InitialClearanceFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the InitialClearanceFactor.
        """
        return None

    @property
    def NormalForceExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the NormalForceExponent.
        """
        return None

    @property
    def NormalStiffnessFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the NormalStiffnessFactor.
        """
        return None

    @property
    def NormalStressExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the NormalStressExponent.
        """
        return None

    @property
    def PenetrationToleranceFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PenetrationToleranceFactor.
        """
        return None

    @property
    def PinballFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PinballFactor.
        """
        return None

    @property
    def PressureAtZeroPenetrationFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PressureAtZeroPenetrationFactor.
        """
        return None

    @property
    def RestitutionFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the RestitutionFactor.
        """
        return None

    @property
    def ShearForceExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearForceExponent.
        """
        return None

    @property
    def ShearStressExponent(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearStressExponent.
        """
        return None

    @property
    def ContactBodies(self) -> typing.Optional[str]:
        """
        Gets the ContactBodies.
        """
        return None

    @property
    def TargetBodies(self) -> typing.Optional[str]:
        """
        Gets the TargetBodies.
        """
        return None

    @property
    def AutomaticDetectionValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the AutomaticDetectionValue.
        """
        return None

    @property
    def BeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BeamRadius.
        """
        return None

    @property
    def ThreadAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ThreadAngle.
        """
        return None

    @property
    def MeanPitchDiameter(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MeanPitchDiameter.
        """
        return None

    @property
    def PitchDistance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PitchDistance.
        """
        return None

    @property
    def BondedMaximumOffset(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BondedMaximumOffset.
        """
        return None

    @property
    def ElasticSlipToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElasticSlipToleranceValue.
        """
        return None

    @property
    def ElectricCapacitanceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElectricCapacitanceValue.
        """
        return None

    @property
    def ElectricConductanceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElectricConductanceValue.
        """
        return None

    @property
    def InitialClearanceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the InitialClearanceValue.
        """
        return None

    @property
    def NormalForceLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the NormalForceLimit.
        """
        return None

    @property
    def NormalStiffnessValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the NormalStiffnessValue.
        """
        return None

    @property
    def NormalStressLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the NormalStressLimit.
        """
        return None

    @property
    def PenetrationToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PenetrationToleranceValue.
        """
        return None

    @property
    def PinballRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PinballRadius.
        """
        return None

    @property
    def PressureAtZeroPenetrationValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PressureAtZeroPenetrationValue.
        """
        return None

    @property
    def ShearForceLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ShearForceLimit.
        """
        return None

    @property
    def ShearStressLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ShearStressLimit.
        """
        return None

    @property
    def ThermalConductanceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ThermalConductanceValue.
        """
        return None

    @property
    def TrimTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TrimTolerance.
        """
        return None

    @property
    def UserOffset(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the UserOffset.
        """
        return None

    @property
    def LineLineDetection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LineLineContactDetectionType]:
        """
        Gets or sets the LineLineDetection.
        """
        return None

    @property
    def BeamBeamModel(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BeamBeamModel]:
        """
        Gets or sets the BeamBeamModel.
        """
        return None

    @property
    def Handedness(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactBoltThreadHand]:
        """
        Gets or sets the Handedness.
        """
        return None

    @property
    def ThreadType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactBoltThreadType]:
        """
        Gets or sets the ThreadType.
        """
        return None

    @property
    def Breakable(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BondedBreakableType]:
        """
        Gets or sets the Breakable.
        """
        return None

    @property
    def ConstraintType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactConstraintType]:
        """
        Gets or sets the ConstraintType.
        """
        return None

    @property
    def ContactGeometryCorrection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactCorrection]:
        """
        Gets or sets the ContactGeometryCorrection.
        """
        return None

    @property
    def ContactFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactFormulation]:
        """
        Gets or sets the ContactFormulation.
        """
        return None

    @property
    def ContactOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactOrientation]:
        """
        Gets or sets the ContactOrientation.
        """
        return None

    @property
    def ContactShellFace(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShellFaceType]:
        """
        Gets or sets the ContactShellFace.
        """
        return None

    @property
    def ContactType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactType]:
        """
        Gets or sets the ContactType.
        """
        return None

    @property
    def ContinuousDistanceComputation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoProgrammedControlled]:
        """
        Gets or sets the ContinuousDistanceComputation.
        """
        return None

    @property
    def DetectionMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactDetectionPoint]:
        """
        Gets or sets the DetectionMethod.
        """
        return None

    @property
    def EdgeContactType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EdgeContactType]:
        """
        Gets or sets the EdgeContactType.
        """
        return None

    @property
    def InitialClearance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.InitialClearanceType]:
        """
        Gets or sets the InitialClearance.
        """
        return None

    @property
    def InterfaceTreatment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactInitialEffect]:
        """
        Gets or sets the InterfaceTreatment.
        """
        return None

    @property
    def ScopeMode(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticOrManual]:
        """
        Gets the ScopeMode.
        """
        return None

    @property
    def NormalStiffnessValueType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ElementControlsNormalStiffnessType]:
        """
        Gets or sets the NormalStiffnessValueType.
        """
        return None

    @property
    def PinballRegion(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactPinballType]:
        """
        Gets or sets the PinballRegion.
        """
        return None

    @property
    def PressureAtZeroPenetration(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.PressureAtZeroPenetrationType]:
        """
        Gets or sets the PressureAtZeroPenetration.
        """
        return None

    @property
    def RBDContactDetection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DSRBDContactDetection]:
        """
        Gets or sets the RBDContactDetection.
        """
        return None

    @property
    def SmallSliding(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactSmallSlidingType]:
        """
        Gets or sets the SmallSliding.
        """
        return None

    @property
    def Behavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactBehavior]:
        """
        Gets or sets the Behavior.
        """
        return None

    @property
    def TargetGeometryCorrection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TargetCorrection]:
        """
        Gets or sets the TargetGeometryCorrection.
        """
        return None

    @property
    def TargetOrientation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TargetOrientation]:
        """
        Gets or sets the TargetOrientation.
        """
        return None

    @property
    def TargetShellFace(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ShellFaceType]:
        """
        Gets or sets the TargetShellFace.
        """
        return None

    @property
    def TimeStepControls(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactTimeStepControls]:
        """
        Gets or sets the TimeStepControls.
        """
        return None

    @property
    def TrimContact(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactTrimType]:
        """
        Gets or sets the TrimContact.
        """
        return None

    @property
    def UpdateStiffness(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.UpdateContactStiffness]:
        """
        Gets or sets the UpdateStiffness.
        """
        return None

    @property
    def ElasticSlipTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactElasticSlipToleranceType]:
        """
        Gets or sets the ElasticSlipTolerance.
        """
        return None

    @property
    def PenetrationTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactPenetrationToleranceType]:
        """
        Gets or sets the PenetrationTolerance.
        """
        return None

    @property
    def DisplayElementNormal(self) -> typing.Optional[bool]:
        """
        Gets or sets the DisplayElementNormal.
        """
        return None

    @property
    def FlipContact(self) -> typing.Optional[bool]:
        """
        Gets or sets the FlipContact.
        """
        return None

    @property
    def FlipTarget(self) -> typing.Optional[bool]:
        """
        Gets or sets the FlipTarget.
        """
        return None

    @property
    def Protected(self) -> typing.Optional[bool]:
        """
        Gets or sets the Protected.
        """
        return None

    @property
    def ShellThicknessEffect(self) -> typing.Optional[bool]:
        """
        Gets or sets the ShellThicknessEffect.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def AutomaticElectricCapacitance(self) -> typing.Optional[bool]:
        """
        Gets or sets the AutomaticElectricCapacitance.
        """
        return None

    @property
    def AutomaticElectricConductance(self) -> typing.Optional[bool]:
        """
        Gets or sets the AutomaticElectricConductance.
        """
        return None

    @property
    def AutomaticThermalConductance(self) -> typing.Optional[bool]:
        """
        Gets or sets the AutomaticThermalConductance.
        """
        return None

    @property
    def ContactCenterPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ContactCenterPoint.
        """
        return None

    @property
    def ContactEndingPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ContactEndingPoint.
        """
        return None

    @property
    def ContactStartingPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ContactStartingPoint.
        """
        return None

    @property
    def SharedSourceBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedSourceBody.
        """
        return None

    @property
    def SharedTargetBody(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Body]:
        """
        Gets or sets the SharedTargetBody.
        """
        return None

    @property
    def TargetCenterPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the TargetCenterPoint.
        """
        return None

    @property
    def TargetEndingPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the TargetEndingPoint.
        """
        return None

    @property
    def TargetStartingPoint(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the TargetStartingPoint.
        """
        return None

    @property
    def SharedSourceReverseNormalLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SharedSourceReverseNormalLocation.
        """
        return None

    @property
    def SharedTargetReverseNormalLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the SharedTargetReverseNormalLocation.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def SearchConnectionsForDuplicatePairs(self) -> None:
        """
        Run the SearchConnectionsForDuplicatePairs action.
        """
        pass

    def FlipContactTarget(self) -> None:
        """
        Run the FlipContactTarget action.
        """
        pass

    def SetDefaultAPDLNames(self) -> None:
        """
        Run the SetDefaultAPDLNames action.
        """
        pass

    def SaveContactRegionSettings(self, fName: str) -> None:
        """
        Run the SaveContactRegionSettings action.
        """
        pass

    def LoadContactRegionSettings(self, fName: str) -> None:
        """
        Run the LoadContactRegionSettings action.
        """
        pass

    def ResetToDefault(self) -> None:
        """
        Run the ResetToDefault action.
        """
        pass

    def ResetToDefault(self, b_Verify: bool) -> None:
        """
        Run the ResetToDefault action with optional verification dialog.
        """
        pass

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def PromoteToRemotePoint(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Run the PromoteToRemotePoint action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def AddPythonCodeEventBased(self) -> Ansys.ACT.Automation.Mechanical.PythonCodeEventBased:
        """
        Creates a new PythonCodeEventBased
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


class ContactTool(object):
    """
    Defines a ContactTool.
    """

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSContactToolAuto]:
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

    def GenerateInitialContactResults(self) -> None:
        """
        Generate Initial Contact Results and Mesh Parts
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


class Spring(object):
    """
    Defines a Spring.
    """

    @property
    def NonLinearLongitudinalStiffness(self) -> typing.Optional[Ansys.ACT.Mechanical.Fields.Field]:
        """
        Gets the non linear longitudinal stiffness defined in the tabular data.
        """
        return None

    @property
    def LongitudinalStiffness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the constant longitudinal stiffness (expressed in N/m).
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSSpringAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Material(self) -> typing.Optional[str]:
        """
        Gets or sets the Material.
        """
        return None

    @property
    def MobileBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the MobileBeamMaterial.
        """
        return None

    @property
    def MobileBody(self) -> typing.Optional[str]:
        """
        Gets the MobileBody.
        """
        return None

    @property
    def ReferenceBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the ReferenceBeamMaterial.
        """
        return None

    @property
    def ReferenceBody(self) -> typing.Optional[str]:
        """
        Gets the ReferenceBody.
        """
        return None

    @property
    def SpringElementAPDLName(self) -> typing.Optional[str]:
        """
        Gets or sets the SpringElementAPDLName.
        """
        return None

    @property
    def MobileBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileBeamRadius.
        """
        return None

    @property
    def MobileXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileXCoordinate.
        """
        return None

    @property
    def MobileYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileYCoordinate.
        """
        return None

    @property
    def MobileZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileZCoordinate.
        """
        return None

    @property
    def ReferenceBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceBeamRadius.
        """
        return None

    @property
    def ReferenceXCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceXCoordinate.
        """
        return None

    @property
    def ReferenceYCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceYCoordinate.
        """
        return None

    @property
    def ReferenceZCoordinate(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceZCoordinate.
        """
        return None

    @property
    def SpringLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the SpringLength.
        """
        return None

    @property
    def LongitudinalDamping(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LongitudinalDamping.
        """
        return None

    @property
    def MobilePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobilePinballRegion.
        """
        return None

    @property
    def FreeLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FreeLength.
        """
        return None

    @property
    def Load(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Load.
        """
        return None

    @property
    def Rotation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Rotation.
        """
        return None

    @property
    def Torque(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Torque.
        """
        return None

    @property
    def ReferencePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferencePinballRegion.
        """
        return None

    @property
    def TorsionalDamping(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TorsionalDamping.
        """
        return None

    @property
    def TorsionalStiffness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TorsionalStiffness.
        """
        return None

    @property
    def MobileAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the MobileAppliedBy.
        """
        return None

    @property
    def ReferenceAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the ReferenceAppliedBy.
        """
        return None

    @property
    def SpringBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringBehavior]:
        """
        Gets or sets the SpringBehavior.
        """
        return None

    @property
    def MobileBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the MobileBehavior.
        """
        return None

    @property
    def PreloadType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringPreloadType]:
        """
        Gets or sets the PreloadType.
        """
        return None

    @property
    def ReferenceBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the ReferenceBehavior.
        """
        return None

    @property
    def Scope(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringScopingType]:
        """
        Gets or sets the Scope.
        """
        return None

    @property
    def SpringType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringType]:
        """
        Gets or sets the SpringType.
        """
        return None

    @property
    def Visible(self) -> typing.Optional[bool]:
        """
        Gets or sets the Visible.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def MobileCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the MobileCoordinateSystem.
        """
        return None

    @property
    def ReferenceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ReferenceCoordinateSystem.
        """
        return None

    @property
    def MobileLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MobileLocation.
        """
        return None

    @property
    def MobileScopeLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MobileScopeLocation.
        """
        return None

    @property
    def ReferenceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceLocation.
        """
        return None

    @property
    def ReferenceScopeLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceScopeLocation.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def PromoteToRemotePoint(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Run the PromoteToRemotePoint action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
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


class Joint(object):
    """
    Defines a Joint.
    """

    @property
    def BushingWorksheet(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.IWorksheet]:
        """
        
            Returns the Bushing Coeffients worksheet associated with Bushing Joint.
            
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSJointAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def FrictionCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the FrictionCoefficient.
        """
        return None

    @property
    def JointElementAPDLName(self) -> typing.Optional[str]:
        """
        Gets or sets the JointElementAPDLName.
        """
        return None

    @property
    def RestitutionFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the RestitutionFactor.
        """
        return None

    @property
    def MobileBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the MobileBeamMaterial.
        """
        return None

    @property
    def MobileBody(self) -> typing.Optional[str]:
        """
        Gets the MobileBody.
        """
        return None

    @property
    def ReferenceBeamMaterial(self) -> typing.Optional[str]:
        """
        Gets or sets the ReferenceBeamMaterial.
        """
        return None

    @property
    def ReferenceBody(self) -> typing.Optional[str]:
        """
        Gets the ReferenceBody.
        """
        return None

    @property
    def EffectiveLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EffectiveLength.
        """
        return None

    @property
    def InnerRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the InnerRadius.
        """
        return None

    @property
    def OuterRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the OuterRadius.
        """
        return None

    @property
    def Radius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Radius.
        """
        return None

    @property
    def MobilePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobilePinballRegion.
        """
        return None

    @property
    def ReferencePinballRegion(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferencePinballRegion.
        """
        return None

    @property
    def RadialGapHeight(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RadialGapHeight.
        """
        return None

    @property
    def RadialGapInnerDiameter(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RadialGapInnerDiameter.
        """
        return None

    @property
    def RadialOuterDiameter(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RadialOuterDiameter.
        """
        return None

    @property
    def ScrewPitch(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ScrewPitch.
        """
        return None

    @property
    def RXMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RXMaximum.
        """
        return None

    @property
    def RXMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RXMinimum.
        """
        return None

    @property
    def RYMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RYMaximum.
        """
        return None

    @property
    def RYMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RYMinimum.
        """
        return None

    @property
    def RZMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RZMaximum.
        """
        return None

    @property
    def RZMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RZMinimum.
        """
        return None

    @property
    def XMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the XMaximum.
        """
        return None

    @property
    def XMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the XMinimum.
        """
        return None

    @property
    def YMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the YMaximum.
        """
        return None

    @property
    def YMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the YMinimum.
        """
        return None

    @property
    def ZMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ZMaximum.
        """
        return None

    @property
    def ZMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ZMinimum.
        """
        return None

    @property
    def TorsionalDamping(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TorsionalDamping.
        """
        return None

    @property
    def TorsionalStiffness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TorsionalStiffness.
        """
        return None

    @property
    def MobileBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MobileBeamRadius.
        """
        return None

    @property
    def ReferenceBeamRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ReferenceBeamRadius.
        """
        return None

    @property
    def GeneralPrimitiveType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointGeneralPrimitiveType]:
        """
        Gets or sets the GeneralPrimitiveType.
        """
        return None

    @property
    def InitialPosition(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointInitialPosition]:
        """
        Gets or sets the InitialPosition.
        """
        return None

    @property
    def MobileBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the MobileBehavior.
        """
        return None

    @property
    def ReferenceBehavior(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LoadBehavior]:
        """
        Gets or sets the ReferenceBehavior.
        """
        return None

    @property
    def Formulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointFormulation]:
        """
        Gets or sets the Formulation.
        """
        return None

    @property
    def JointFrictionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointFrictionType]:
        """
        Gets or sets the JointFrictionType.
        """
        return None

    @property
    def MobileFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemotePointFormulation]:
        """
        Gets or sets the MobileFormulation.
        """
        return None

    @property
    def RadialGapType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RadialGapType.
        """
        return None

    @property
    def ReferenceFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemotePointFormulation]:
        """
        Gets or sets the ReferenceFormulation.
        """
        return None

    @property
    def ConnectionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointScopingType]:
        """
        Gets or sets the ConnectionType.
        """
        return None

    @property
    def RXMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RXMaximumType.
        """
        return None

    @property
    def RXMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RXMinimumType.
        """
        return None

    @property
    def RYMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RYMaximumType.
        """
        return None

    @property
    def RYMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RYMinimumType.
        """
        return None

    @property
    def RZMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RZMaximumType.
        """
        return None

    @property
    def RZMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the RZMinimumType.
        """
        return None

    @property
    def XMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the XMaximumType.
        """
        return None

    @property
    def XMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the XMinimumType.
        """
        return None

    @property
    def YMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the YMaximumType.
        """
        return None

    @property
    def YMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the YMinimumType.
        """
        return None

    @property
    def ZMaximumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the ZMaximumType.
        """
        return None

    @property
    def ZMinimumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointStopType]:
        """
        Gets or sets the ZMinimumType.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointType]:
        """
        Gets or sets the Type.
        """
        return None

    @property
    def MobileAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the MobileAppliedBy.
        """
        return None

    @property
    def ReferenceAppliedBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RemoteApplicationType]:
        """
        Gets or sets the ReferenceAppliedBy.
        """
        return None

    @property
    def Rotations(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointRotationDOFType]:
        """
        Gets or sets the Rotations.
        """
        return None

    @property
    def SolverElementType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.JointSolverElementType]:
        """
        Gets or sets the SolverElementType.
        """
        return None

    @property
    def TranslationX(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FixedOrFree]:
        """
        Gets or sets the TranslationX.
        """
        return None

    @property
    def TranslationY(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FixedOrFree]:
        """
        Gets or sets the TranslationY.
        """
        return None

    @property
    def TranslationZ(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FixedOrFree]:
        """
        Gets or sets the TranslationZ.
        """
        return None

    @property
    def MobileRelaxationMethod(self) -> typing.Optional[bool]:
        """
        Gets or sets the MobileRelaxationMethod.
        """
        return None

    @property
    def ReferenceRelaxationMethod(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReferenceRelaxationMethod.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def SuppressedForSolve(self) -> typing.Optional[bool]:
        """
        Gets the SuppressedForSolve.
        """
        return None

    @property
    def ElementCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ElementCoordinateSystem.
        """
        return None

    @property
    def MobileCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the MobileCoordinateSystem.
        """
        return None

    @property
    def ReferenceCoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the ReferenceCoordinateSystem.
        """
        return None

    @property
    def MobileLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the MobileLocation.
        """
        return None

    @property
    def CurveOrientationSurface(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the CurveOrientationSurface.
        """
        return None

    @property
    def ReferenceLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the ReferenceLocation.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def PromoteToRemotePoint(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Run the PromoteToRemotePoint action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def FlipReferenceMobile(self) -> None:
        """
        Run the FlipReferenceMobile action.
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


class Connections(object):
    """
    Defines a Connections.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSContactGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets or sets the SolverFilesDirectory.
        """
        return None

    @property
    def GenerateAutomaticConnectionOnRefresh(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticOrManual]:
        """
        Gets or sets the GenerateAutomaticConnectionOnRefresh.
        """
        return None

    @property
    def FixedJoints(self) -> typing.Optional[bool]:
        """
        Gets or sets the FixedJoints.
        """
        return None

    @property
    def TransparencyEnabled(self) -> typing.Optional[bool]:
        """
        Gets or sets the TransparencyEnabled.
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

    def AddContactRegion(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child ContactRegion.
        """
        pass

    def AddContactTool(self) -> Ansys.ACT.Automation.Mechanical.PreContactTool:
        """
        Creates a new ContactTool
        """
        pass

    def AddSpotWeldGroup(self) -> Ansys.ACT.Automation.Mechanical.Connections.SpotWeldGroup:
        """
        Creates a new child SpotWeldGroup.
        """
        pass

    def AddSpotWeld(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child SpotWeld.
        """
        pass

    def AddInterStage(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child InterStage.
        """
        pass

    def AddJoint(self) -> Ansys.ACT.Automation.Mechanical.Connections.Joint:
        """
        Creates a new child Joint.
        """
        pass

    def AddBodyInteraction(self) -> Ansys.ACT.Automation.Mechanical.Connections.BodyInteraction:
        """
        Creates a new child BodyInteraction.
        """
        pass

    def SearchConnectionsForDuplicatePairs(self) -> None:
        """
        Run the SearchConnectionsForDuplicatePairs action.
        """
        pass

    def CreateAutomaticConnections(self) -> None:
        """
        Run the CreateAutomaticConnections action.
        """
        pass

    def ExportModelTopology(self, filename: str) -> None:
        """
        ExportModelTopology method.
        """
        pass

    def AddAMBondConnection(self) -> Ansys.ACT.Automation.Mechanical.Connections.AMBondConnection:
        """
        Creates a new AMBondConnection
        """
        pass

    def AddBeam(self) -> Ansys.ACT.Automation.Mechanical.Connections.Beam:
        """
        Creates a new Beam
        """
        pass

    def AddBearing(self) -> Ansys.ACT.Automation.Mechanical.Connections.Bearing:
        """
        Creates a new Bearing
        """
        pass

    def AddConnectionGroup(self) -> Ansys.ACT.Automation.Mechanical.Connections.ConnectionGroup:
        """
        Creates a new ConnectionGroup
        """
        pass

    def AddContactSolutionInformation(self) -> Ansys.ACT.Automation.Mechanical.ContactSolutionInformation:
        """
        Creates a new ContactSolutionInformation
        """
        pass

    def AddEndRelease(self) -> Ansys.ACT.Automation.Mechanical.EndRelease:
        """
        Creates a new EndRelease
        """
        pass

    def AddSpring(self) -> Ansys.ACT.Automation.Mechanical.Connections.Spring:
        """
        Creates a new Spring
        """
        pass

    def GenerateInitialContactResults(self) -> None:
        """
        Generate Initial Contact Results and Mesh Parts
        """
        pass

    def RepairOverlappingContactRegions(self) -> None:
        """
        Check for Overlapping Contact Regions. However, please note that this action does not result in any actual repair being performed.
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


class ConnectionGroup(object):
    """
    Defines a ConnectionGroup.
    """

    @property
    def ConnectionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutoDetectionType]:
        """
        Gets or sets the ConnectionType.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSConnectionGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ActiveConnections(self) -> typing.Optional[int]:
        """
        Gets the ActiveConnections.
        """
        return None

    @property
    def Connections(self) -> typing.Optional[int]:
        """
        Gets the Connections.
        """
        return None

    @property
    def EdgeOverlapTolerance(self) -> typing.Optional[int]:
        """
        Gets or sets the EdgeOverlapTolerance.
        """
        return None

    @property
    def FaceOverlapTolerance(self) -> typing.Optional[int]:
        """
        Gets or sets the FaceOverlapTolerance.
        """
        return None

    @property
    def MinimumDistancePercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the MinimumDistancePercentage.
        """
        return None

    @property
    def ThicknessScaleFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ThicknessScaleFactor.
        """
        return None

    @property
    def ToleranceSlider(self) -> typing.Optional[int]:
        """
        Gets or sets the ToleranceSlider.
        """
        return None

    @property
    def FaceFaceDetectionAngleTolerence(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FaceFaceDetectionAngleTolerence.
        """
        return None

    @property
    def FaceAngleTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the FaceAngleTolerance.
        """
        return None

    @property
    def MinimumDistanceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumDistanceValue.
        """
        return None

    @property
    def ToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ToleranceValue.
        """
        return None

    @property
    def CylindricalFaces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CylindricalFacesOption]:
        """
        Gets or sets the CylindricalFaces.
        """
        return None

    @property
    def Priority(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactFaceEdgePriority]:
        """
        Gets or sets the Priority.
        """
        return None

    @property
    def GroupBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactGroupingType]:
        """
        Gets or sets the GroupBy.
        """
        return None

    @property
    def SearchAcross(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactSearchingType]:
        """
        Gets or sets the SearchAcross.
        """
        return None

    @property
    def ToleranceType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactToleranceType]:
        """
        Gets or sets the ToleranceType.
        """
        return None

    @property
    def EdgeEdge(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactEdgeEdgeOption]:
        """
        Gets or sets the EdgeEdge.
        """
        return None

    @property
    def FaceEdge(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactFaceEdgeOption]:
        """
        Gets or sets the FaceEdge.
        """
        return None

    @property
    def AutomaticFixedJoints(self) -> typing.Optional[bool]:
        """
        Gets or sets the AutomaticFixedJoints.
        """
        return None

    @property
    def RevoluteJoints(self) -> typing.Optional[bool]:
        """
        Gets or sets the RevoluteJoints.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def FaceFace(self) -> typing.Optional[bool]:
        """
        Gets or sets the FaceFace.
        """
        return None

    @property
    def UseRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the UseRange.
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
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ReadOnly.
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

    def AddContactRegion(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child ContactRegion.
        """
        pass

    def AddJoint(self) -> Ansys.ACT.Automation.Mechanical.Connections.Joint:
        """
        Creates a new child Joint.
        """
        pass

    def SearchConnectionsForDuplicatePairs(self) -> None:
        """
        Run the SearchConnectionsForDuplicatePairs action.
        """
        pass

    def AddSpotWeld(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child SpotWeld.
        """
        pass

    def AddInterStage(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Creates a new child InterStage.
        """
        pass

    def CreateAutomaticConnections(self) -> None:
        """
        Run the CreateAutomaticConnections action.
        """
        pass

    def DeleteChildren(self) -> None:
        """
        Run the DeleteChildren action.
        """
        pass

    def DeleteChildren(self, b_Verify: bool) -> None:
        """
        Run the DeleteChildren action with optional verification dialog.
        """
        pass

    def RenameBasedOnChildren(self) -> bool:
        """
        Rename the Connection group based on the children.
        """
        pass

    def SetDefaultAPDLNames(self) -> None:
        """
        Loop over all the valid contact regions and set the default APDL names.
        """
        pass

    def RepairOverlappingContactRegions(self) -> None:
        """
        Check for Overlapping Contact Regions. However, please note that this action does not result in any actual repair being performed.
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


class BodyInteractions(object):
    """
    Defines a BodyInteractions.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSBodyInteractionGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def PinballFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PinballFactor.
        """
        return None

    @property
    def Tolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the Tolerance.
        """
        return None

    @property
    def ShellThicknessFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ShellThicknessFactor.
        """
        return None

    @property
    def TimestepSafetyFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the TimestepSafetyFactor.
        """
        return None

    @property
    def LimitingTimestepVelocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LimitingTimestepVelocity.
        """
        return None

    @property
    def ContactDetection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactDetection]:
        """
        Gets or sets the ContactDetection.
        """
        return None

    @property
    def Formulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.BodyInteractionFormulation]:
        """
        Gets or sets the Formulation.
        """
        return None

    @property
    def ManualContactTreatment(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ManualContactTreatmentType]:
        """
        Gets or sets the ManualContactTreatment.
        """
        return None

    @property
    def NodalShellThickness(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoProgrammedControlled]:
        """
        Gets or sets the NodalShellThickness.
        """
        return None

    @property
    def SlidingContact(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SlidingContactType]:
        """
        Gets or sets the SlidingContact.
        """
        return None

    @property
    def BodySelfContact(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoProgrammedControlled]:
        """
        Gets or sets the BodySelfContact.
        """
        return None

    @property
    def ElementSelfContact(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.YesNoProgrammedControlled]:
        """
        Gets or sets the ElementSelfContact.
        """
        return None

    @property
    def EdgeOnEdgeContact(self) -> typing.Optional[bool]:
        """
        Gets or sets the EdgeOnEdgeContact.
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

    def AddBodyInteraction(self) -> Ansys.ACT.Automation.Mechanical.Connections.BodyInteraction:
        """
        Creates a new child BodyInteraction.
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


