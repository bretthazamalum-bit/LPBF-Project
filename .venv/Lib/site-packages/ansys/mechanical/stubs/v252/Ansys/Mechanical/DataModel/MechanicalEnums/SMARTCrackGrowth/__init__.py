"""SMARTCrackGrowth module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class EquivalentSIFMethod(Enum):
    """
    Enum to specify the Equivalent SIF Method for SMART Crack Growth.
    """

    EmpiricalFunction = 4
    MaximumTangentialStress = 1
    PookCriterion = 3
    ProgramControlled = 0
    RichardFunction = 2

class MultiplicativeFactorsType(Enum):
    """
    Enum to specify the Multiplicative Factors type for Equivalent SIF Method.
    """

    Manual = 1
    ProgramControlled = 0

class RichardCoefficientsType(Enum):
    """
    Enum to specify the Richard Coefficients type for Kink Angle Method.
    """

    Manual = 1
    ProgramControlled = 0

