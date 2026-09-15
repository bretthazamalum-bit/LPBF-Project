"""Common module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class PathType(Enum):
    """
    This enum specifies how a path should be interpreted.
    """

    Absolute = 1
    RelativeToProject = 2

