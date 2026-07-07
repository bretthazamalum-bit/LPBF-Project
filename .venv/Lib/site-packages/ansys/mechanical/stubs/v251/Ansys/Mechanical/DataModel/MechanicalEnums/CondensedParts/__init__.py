"""CondensedParts module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ExportFormat(Enum):
    """
    Specifies the Condensed Part Export Format.
    """

    Unspecified = 0
    Automatic = 1

