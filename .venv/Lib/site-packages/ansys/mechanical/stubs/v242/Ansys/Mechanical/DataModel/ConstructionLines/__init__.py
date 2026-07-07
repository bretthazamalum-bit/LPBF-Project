"""ConstructionLines module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v242.Ansys.Mechanical.DataModel.ConstructionLines.Edges as Edges


class PlaneType(Enum):
    """
    
                Enumeration for the possible edge vertex types that can be represented.
            
    """

    pass

class PointType(Enum):
    """
    
                Enumeration for the possible edge vertex types that can be represented.
            
    """

    pass

class ConstructionLineHelper(object):
    """
    
                Helper to perform queries and modifications against a ConstructionLine instance.
            
    """

    @classmethod
    def GetEdgeVerticesById(cls, constructionLine: Ansys.ACT.Automation.Mechanical.ConstructionLines.ConstructionLine, edgeVertexIdCollection: typing.Iterable[int]) -> typing.List[typing.Any]:
        """
        GetEdgeVerticesById method.
        """
        pass

    @classmethod
    def GetEdgesById(cls, constructionLine: Ansys.ACT.Automation.Mechanical.ConstructionLines.ConstructionLine, edgeIdCollection: typing.Iterable[int]) -> typing.List[typing.Any]:
        """
        GetEdgesById method.
        """
        pass

    @classmethod
    def GetPlanesById(cls, constructionLine: Ansys.ACT.Automation.Mechanical.ConstructionLines.ConstructionLine, planeIdCollection: typing.Iterable[int]) -> typing.List[typing.Any]:
        """
        GetPlanesById method.
        """
        pass

    @classmethod
    def GetEdgesUsingPoint(cls, point: Ansys.Mechanical.DataModel.ConstructionLines.Point) -> typing.List[typing.Any]:
        """
        
                Get a list of IEdge that use the given Point.
            
        """
        pass

    @classmethod
    def GetContainedEdges(cls, plane: Ansys.Mechanical.DataModel.ConstructionLines.Plane) -> typing.List[typing.Any]:
        """
        
                Get all the edges that have both start and end edge vertices in the given plane.
            
        """
        pass

    @classmethod
    def GetRelatedEdges(cls, plane: Ansys.Mechanical.DataModel.ConstructionLines.Plane) -> typing.List[typing.Any]:
        """
        
                Get all the edges that have only edge vertex in the given plane.
            
        """
        pass

    @classmethod
    def ExportToXML(cls, constructionLine: Ansys.ACT.Automation.Mechanical.ConstructionLines.ConstructionLine, xmlFilePath: str) -> None:
        """
        
                 Collect all the edges and edge vertices, then export them as global points to an XML file.
             
        """
        pass

    @classmethod
    def ClearExistingDataAndImportFromXML(cls, constructionLine: Ansys.ACT.Automation.Mechanical.ConstructionLines.ConstructionLine, xmlFilePath: str) -> typing.List[typing.Any]:
        """
        
                 Import global points and connecting edges from an XML file.
             
        """
        pass


class Plane(object):
    """
    
                A 2D sketching planes in a ConstructionLine instance.
            
    """

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.ConstructionLines.PlaneType]:
        """
        Type property.
        """
        return None

    @property
    def Definition(self) -> typing.Optional[typing.Any]:
        """
        Definition property.
        """
        return None

    @property
    def Origin(self) -> typing.Optional[Ansys.ACT.Core.Math.Point3D]:
        """
        
                The global location of this plane's origin.
            
        """
        return None

    @property
    def PrimaryAxisDirection(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
                The orientation of the plane's primary (X) axis orientation.
            
        """
        return None

    @property
    def SecondaryAxisDirection(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
                The orientation of the plane's secondary (Y) axis orientation.
            
        """
        return None

    @property
    def Normal(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
                The plane's normal vector (Z axis orientation) orientation.
            
        """
        return None

    @property
    def ObjectId(self) -> typing.Optional[int]:
        """
        
                Get the ID of the represented entity.
            
        """
        return None

    @property
    def IsRepresentation(self) -> typing.Optional[bool]:
        """
        
                Check to see if there is a valid entity that this instance represents.
            
        """
        return None

    def Equivalent(self, other: Ansys.Mechanical.DataModel.ConstructionLines.Plane) -> bool:
        """
        
                Checks to see if another plane is equivalent to this one.
            
        """
        pass


class Point(object):
    """
    
                A point in a ConstructionLine instance, may have an associated edge vertex.
            
    """

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.ConstructionLines.PointType]:
        """
        Type property.
        """
        return None

    @property
    def Definition(self) -> typing.Optional[typing.Any]:
        """
        Definition property.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Core.Math.Point3D]:
        """
        
                Get the global location of this point.
            
        """
        return None

    @property
    def ObjectId(self) -> typing.Optional[int]:
        """
        
                Get the ID of the represented entity.
            
        """
        return None

    @property
    def IsRepresentation(self) -> typing.Optional[bool]:
        """
        
                Check to see if there is a valid entity that this instance represents.
            
        """
        return None

    def Equivalent(self, other: Ansys.Mechanical.DataModel.ConstructionLines.Point) -> bool:
        """
        
                Checks to see if another point is equivalent to this one.
            
        """
        pass


