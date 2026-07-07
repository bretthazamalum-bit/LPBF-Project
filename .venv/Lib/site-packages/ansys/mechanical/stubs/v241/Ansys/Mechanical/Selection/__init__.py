"""Selection module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class GeometryRayCastHit(object):
    """
    
            GeometryRayCastHit, contains geoEntity and vector normal
            
    """

    @property
    def HitVector(self) -> typing.Optional[Ansys.Mechanical.Math.BoundVector]:
        """
        
            BoundVector with location and normal direction on geometry entity to ray cast
            
        """
        return None

    @property
    def Entity(self) -> typing.Optional[Ansys.ACT.Interfaces.Geometry.IGeoEntity]:
        """
        
            Geometry entity hit by ray cast
            
        """
        return None


class GeometryRayCastSettings(object):

    @property
    def HitFaces(self) -> typing.Optional[bool]:
        """
        
            Specifies whether ray casting should hit faces. 
            Defaults to true.
            
        """
        return None

    @property
    def HitEdges(self) -> typing.Optional[bool]:
        """
        
            Specifies whether ray casting should hit edges. 
            Defaults to false.
            
        """
        return None

    @property
    def HitVertices(self) -> typing.Optional[bool]:
        """
        
            Specifies whether ray casting should hit vertices. 
            Defaults to false.
            
        """
        return None

    @property
    def HitBodies(self) -> typing.Optional[bool]:
        """
        
            Specifies whether ray casting should hit bodies. 
            Defaults to false.
            
        """
        return None

    @property
    def MaxHits(self) -> typing.Optional[int]:
        """
        
            Specifies maximum number of ray casting hits. 
            Defaults to 1000.
            
        """
        return None

    @property
    def CastRadius(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Optional; specifies maximum radial distance from BoundVector.
            
        """
        return None

    @property
    def CastLength(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Optional; specifies maximum axial distance from BoundVector origin.
            Defaults to maximum needed length.
            
        """
        return None


class SelectionHelper(object):

    @classmethod
    def CreateVector3D(cls, selection: Ansys.ACT.Interfaces.Common.ISelectionInfo, reversed: bool) -> Ansys.ACT.Math.Vector3D:
        """
        Creates a Vector3D object based on the given selection and reverse flag.  
            The direction is computed as the outward normal of a planar face, the direction between 
            two nodes or vertices from the first to the second, or the axis of an edge.  
            The reversed flag will return the opposite of the computed direction.
            
        """
        pass

    @classmethod
    def CastRayOnGeometry(cls, castVector: Ansys.Mechanical.Math.BoundVector, settings: Ansys.Mechanical.Selection.GeometryRayCastSettings) -> typing.Iterable[Ansys.Mechanical.Selection.GeometryRayCastHit]:
        """
        
            Finds geometry entities intersecting input BoundVector and returns them in list of GeometryRayCastHit.
            These are returned in the order they are hit, each item containing the entity and BoundVector normal to point hit.
            
        """
        pass


