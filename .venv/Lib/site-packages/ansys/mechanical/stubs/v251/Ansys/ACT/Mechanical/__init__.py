"""Mechanical module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v251.Ansys.ACT.Mechanical.Application as Application
import ansys.mechanical.stubs.v251.Ansys.ACT.Mechanical.AdditionalProperties as AdditionalProperties
import ansys.mechanical.stubs.v251.Ansys.ACT.Mechanical.Utilities as Utilities
import ansys.mechanical.stubs.v251.Ansys.ACT.Mechanical.Fields as Fields


class Transaction(object):
    """
    
            Speeds up bulk user interactions.
            
    """

    pass

class UnitsHelper(object):
    """
    
            Defines set of methods that can be used to find mechanical unit information
            
    """

    @classmethod
    def ConvertMechanicalUnitToCoreUnit(cls, mechanicalUnit: str, unitCategory: str) -> str:
        """
        
            Takes input mechanical unit string and category string
            And returns framework unit string which can be used for conversion
            
        """
        pass

    @classmethod
    def GetValidQuantityNamesAndUnits(cls) -> dict[str,str]:
        """
        
            Retrieve a dictionary of quantity names to unit strings.
            These quantity names represent valid quantity names that can be used when defining quantities in 
            Mechanical ACT extensions.        
            
        """
        pass


