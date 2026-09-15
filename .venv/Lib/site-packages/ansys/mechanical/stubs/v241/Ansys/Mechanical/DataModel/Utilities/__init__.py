"""Utilities module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v241.Ansys.Mechanical.DataModel.Utilities.TabularData as TabularData


class RigidBodyTransformationMatrix(object):
    """
    
             A 4x4 transformation matrix, to be used explicitly for rigid body transformations. The
             transformation matrix is in column-major format. Elements 0-3 represent, respectively,
             the x-components of the X axis, Y axis, Z axis, and translation with respect to global.
             Identically, elements 4-7 represent the y components and elements 8-11 the z components.
             Elements 2-15, per rigid-body requirements, are expected to be [0.0, 0.0, 0.0, 1.0].
            
             The ability to piecewise set rotation and translation components precludes the option of
             validating the matrix data at every operation. Thus, these values ***must*** be checked
             before the data is used.
            
             The class `Ansys.ACT.Common.SimpleTransform` provides a simplified mechanism for working
             with rigid body transformations and getting a `RigidBodyTransformationMatrix` object.
             
    """

    @property
    def Data(self) -> typing.Optional[typing.List[typing.Any]]:
        """
        
            A 16-value list representing a linearized 4x4 transformation matrix.
            
        """
        return None

    @property
    def X_x(self) -> typing.Optional[float]:
        """
        
            Element 0: the x component of the X axis rotation.
            
        """
        return None

    @property
    def X_y(self) -> typing.Optional[float]:
        """
        
            Element 4: the y component of the X axis rotation.
            
        """
        return None

    @property
    def X_z(self) -> typing.Optional[float]:
        """
        
            Element 8: the z component of the X axis rotation.
            
        """
        return None

    @property
    def Y_x(self) -> typing.Optional[float]:
        """
        
            Element 1: the x component of the Y axis rotation.
            
        """
        return None

    @property
    def Y_y(self) -> typing.Optional[float]:
        """
        
            Element 5: the y component of the Y axis rotation.
            
        """
        return None

    @property
    def Y_z(self) -> typing.Optional[float]:
        """
        
            Element 9: the z component of the Y axis rotation.
            
        """
        return None

    @property
    def Z_x(self) -> typing.Optional[float]:
        """
        
            Element 2: the x component of the Z axis rotation.
            
        """
        return None

    @property
    def Z_y(self) -> typing.Optional[float]:
        """
        
            Element 6: the y component of the Z axis rotation.
            
        """
        return None

    @property
    def Z_z(self) -> typing.Optional[float]:
        """
        
            Element 10: the z component of the Z axis rotation.
            
        """
        return None

    @property
    def T_x(self) -> typing.Optional[float]:
        """
        
            Element 3: the x component of the translation.
            
        """
        return None

    @property
    def T_y(self) -> typing.Optional[float]:
        """
        
            Element 7: the y component of the translation.
            
        """
        return None

    @property
    def T_z(self) -> typing.Optional[float]:
        """
        
            Element 11: the z component of the translation.
            
        """
        return None

    @property
    def tau_x(self) -> typing.Optional[float]:
        """
        
            Element 12: the x component of the shear, which must be '0.0' for rigid body
            transformations.
            
        """
        return None

    @property
    def tau_y(self) -> typing.Optional[float]:
        """
        
            Element 13: the y component of the shear, which must be '0.0' for rigid body
            transformations.
            
        """
        return None

    @property
    def tau_z(self) -> typing.Optional[float]:
        """
        
            Element 14: the z component of the shear, which must be '0.0' for rigid body
            transformations.
            
        """
        return None

    @property
    def S(self) -> typing.Optional[float]:
        """
        
            Element 15: the transformation scale, which must be '1.0' for rigid body
            transformations.
            
        """
        return None


class BeamCoordinateSystem(object):

    pass

class CenterOfGravityCoordinateSystem(object):

    pass

