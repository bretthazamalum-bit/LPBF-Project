"""Enums module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ThemeName(Enum):
    """
    
            Represents the different themes that can be set in Mechanical.
            
    """

    Light = 0
    Dark = 1
    Classic = 2

