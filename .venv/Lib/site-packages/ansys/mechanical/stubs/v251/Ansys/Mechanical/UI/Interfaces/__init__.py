"""Interfaces module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class IMechanicalTheme(object):

    @property
    def Name(self) -> typing.Optional[Ansys.Mechanical.UI.Enums.ThemeName]:
        """
        
            The name of the theme as an enum value.
            
        """
        return None

    @property
    def HexadecimalPalette(self) -> typing.Optional[Ansys.Mechanical.UI.Palette]:
        """
        
            Palette object, which provides an entry point to get Mechnical UI's theme colors represented in Hexadecimal. ei. #FFFFFF
            
        """
        return None

    @property
    def ColorPalette(self) -> typing.Optional[Ansys.Mechanical.UI.Palette]:
        """
        
            Palette object, which provides an entry point to get Mechnical UI's theme colors represented as Ansys.Utilities.Color objects
            
        """
        return None

    @property
    def IntPalette(self) -> typing.Optional[Ansys.Mechanical.UI.Palette]:
        """
        
            Palette object, which provides an entry point to get Mechnical UI's theme colors represented as integers formatted as BGR
            
        """
        return None


class IMechanicalUserInterface(object):

    @property
    def Theme(self) -> typing.Optional[Ansys.Mechanical.UI.Interfaces.IMechanicalTheme]:
        """
        
            Information about the current theme being in Mechanical.
            
        """
        return None


