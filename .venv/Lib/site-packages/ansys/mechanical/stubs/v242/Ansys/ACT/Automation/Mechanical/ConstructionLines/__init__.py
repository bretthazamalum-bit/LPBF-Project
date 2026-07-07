"""ConstructionLines module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ConstructionLine(object):
    """
    
                
    """

    @property
    def Edges(self) -> typing.Optional[typing.List[typing.Any]]:
        """
        
                Creates for the user an IEdge representation of each edge in this Construction Line.
            
        """
        return None

    @property
    def Points(self) -> typing.Optional[typing.List[typing.Any]]:
        """
        
                Returns all points in this Construction Line, both those that have been created
                as well as virtual representations.
            
        """
        return None

    @property
    def Planes(self) -> typing.Optional[typing.List[typing.Any]]:
        """
        
                Creates for the user an Plane representation of each plane in this Construction Line.
            
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSLines.IDSLinesPythonInteraction]:
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

    def CreatePoints(self, pointDefinitionCollection: typing.Iterable[typing.Any]) -> typing.List[typing.Any]:
        """
        CreatePoints method.
        """
        pass

    def CreatePlanarPoints(self, plane: Ansys.Mechanical.DataModel.ConstructionLines.Plane, pointDefinitionCollection: typing.Iterable[typing.Any]) -> typing.List[typing.Any]:
        """
        CreatePlanarPoints method.
        """
        pass

    def CreatePlane(self, sketchPlaneDefinition: typing.Any) -> Ansys.Mechanical.DataModel.ConstructionLines.Plane:
        """
        
                Create a plane.
            
        """
        pass

    def CreateStraightLines(self, pointCollection: typing.Iterable[Ansys.Mechanical.DataModel.ConstructionLines.Point]) -> typing.List[typing.Any]:
        """
        CreateStraightLines method.
        """
        pass

    def CreateStraightLines(self, pointCollection: typing.Iterable[Ansys.Mechanical.DataModel.ConstructionLines.Point], connectionCollection: typing.Iterable[typing.Iterable[typing.Any]]) -> typing.List[typing.Any]:
        """
        CreateStraightLines method.
        """
        pass

    def FlipEdges(self, edgesToFlip: typing.Iterable[Ansys.Mechanical.DataModel.ConstructionLines.Edges.IEdge]) -> None:
        """
        FlipEdges method.
        """
        pass

    def DeleteEdges(self, edgeCollection: typing.Iterable[Ansys.Mechanical.DataModel.ConstructionLines.Edges.IEdge]) -> None:
        """
        DeleteEdges method.
        """
        pass

    def DeletePlane(self, plane: Ansys.Mechanical.DataModel.ConstructionLines.Plane, forceDelete: bool) -> None:
        """
        
                Delete a plane associated with this construction line.
            
        """
        pass

    def AddToGeometry(self) -> Ansys.ACT.Interfaces.Geometry.IGeoPart:
        """
        
                Add a part to Geometry with line bodies as contained in this ConstructionLine instance.
            
        """
        pass

    def UpdateGeometry(self) -> None:
        """
        
                Update the corresponding part with any changes made in this ConstructionLine instance.
            
        """
        pass

    def RemoveFromGeometry(self) -> None:
        """
        
                Remove the corresponding part from the geometry.
            
        """
        pass

    def GetPartFromGeometry(self) -> Ansys.ACT.Interfaces.Geometry.IGeoPart:
        """
        
                Get the corresponding part for a ConstructionLine instance.
            
        """
        pass

    def Undo(self) -> None:
        """
        
                Undo the last operation in this Construction Line instance.
            
        """
        pass

    def Redo(self) -> None:
        """
        
                Redo and undone operation in this Construction Line instance.
            
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


