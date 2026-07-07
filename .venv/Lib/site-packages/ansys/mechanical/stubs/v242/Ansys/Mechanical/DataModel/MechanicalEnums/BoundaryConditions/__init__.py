"""BoundaryConditions module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class DataRepresentation(Enum):
    """
    enumeration used to set the return object for the magnitude property in boundary conditions.
    """

    Field = 1
    Flexible = 2

