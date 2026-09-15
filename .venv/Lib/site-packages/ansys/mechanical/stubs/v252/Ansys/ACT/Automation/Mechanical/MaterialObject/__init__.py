"""MaterialObject module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class MaterialModel(object):
    """
    
            The material model class holds the data for a particular material model. Examples of a material model would be;: density, isotropic elasticity, or gasket model.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets the name that identifies the material model 
            
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        
            Gets or sets whether this material model should be used in the analysis.
            
        """
        return None


