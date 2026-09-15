"""ExternalModel module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ImportedSurfaceLoadType(Enum):
    """
    Specifies the ImportedSurfaceLoadType.
    """

    Pressure = 1
    HeatFlux = 22
    Convection = 23

