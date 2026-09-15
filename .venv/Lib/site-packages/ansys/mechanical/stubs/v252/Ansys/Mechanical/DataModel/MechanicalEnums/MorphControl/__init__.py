"""MorphControl module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class MorphDefinitionType(Enum):
    """
    To specify what the Morph Control is based on. The available options are Mesh Workflow and Displacement File.
    """

    MeshWorkflowMorph = 2
    DisplacementFile = 1

