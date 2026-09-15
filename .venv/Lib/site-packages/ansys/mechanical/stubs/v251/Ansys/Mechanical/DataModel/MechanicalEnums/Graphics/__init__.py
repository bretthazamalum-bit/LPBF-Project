"""Graphics module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CappingType(Enum):
    """
    Specifies the CappingType.
    """

    Iso = 0
    Top = -1
    Bottom = 1

class ContourView(Enum):
    """
    Specifies the ContourView.
    """

    SmoothContours = 0
    ContourBands = 1
    Isolines = 2
    SolidFill = 3

class DeformationScaling(Enum):
    """
    Specifies the DeformationScaling.
    """

    True_ = 0
    Auto = 1

class ExtraModelDisplay(Enum):
    """
    Specifies the ExtraModelDisplay.
    """

    NoWireframe = 0
    UndeformedWireframe = 1
    UndeformedModel = 2
    ShowElements = 3

class GeometryView(Enum):
    """
    Specifies the GeometryView.
    """

    Exterior = 0
    Isosurface = 1
    CappedIsosurface = 2
    SlicePlane = 3

class ScopingDisplay(Enum):
    """
    Specifies the ScopingDisplay.
    """

    ScopedBodies = 0
    AllBodies = 1
    ResultOnly = 2

