"""Math module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class BoundVector(object):
    """
    
            A vector with fixed intial point and terminal point.
            Or a vector with fixed initial point(origin) and a direction(vector).
            
    """

    @property
    def Origin(self) -> typing.Optional[Ansys.Mechanical.Graphics.Point]:
        """
        
            The location at the start of the BoundVector.
            
        """
        return None

    @property
    def Vector(self) -> typing.Optional[Ansys.ACT.Math.Vector3D]:
        """
        
            The direction of the BoundVector.
            
        """
        return None


