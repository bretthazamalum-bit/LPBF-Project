"""Edges module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class StraightLineEdge(object):
    """
    
                Representation of a straight line edge between to edge vertices.
            
    """

    @property
    def Length(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Length property.
        """
        return None

    @property
    def EndPoint(self) -> typing.Optional[Ansys.Mechanical.DataModel.ConstructionLines.Point]:
        """
        
                A Point representing the end vertex of the edge.
            
        """
        return None

    @property
    def StartPoint(self) -> typing.Optional[Ansys.Mechanical.DataModel.ConstructionLines.Point]:
        """
        
                A Point representing the start vertex of an edge.
            
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


class IEdge(object):
    """
    
                Interface for edges created by ConstructionLine.
            
    """

    @property
    def Length(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
                Get the length of this edge.
            
        """
        return None


