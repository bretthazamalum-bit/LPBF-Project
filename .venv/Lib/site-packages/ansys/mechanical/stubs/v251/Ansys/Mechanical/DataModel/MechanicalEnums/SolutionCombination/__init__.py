"""SolutionCombination module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class EnvelopeType(Enum):
    """
    Specifies the Solution Combination Envelope Type
    """

    Maximum = 0
    Minimum = 1
    MaximumLoadCase = 2
    MinimumLoadCase = 3

class Type(Enum):
    """
    Specifies the Solution Combination Type
    """

    LoadCombinations = 1
    Envelope = 2

