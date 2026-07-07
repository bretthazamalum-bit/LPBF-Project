"""FluidPenetrationPressure module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CriterionDefinedByType(Enum):
    """
    Specifies the CriterionDefinedByType.
    """

    ProgramControlled = 1
    UserSpecifiedCriterion = 2

class FluidPathType(Enum):
    """
    Specifies the FluidPathType.
    """

    HistoryDependentPath = 2
    HistoryIndependentPath = 1

class GraphDisplay(Enum):
    """
    Specifies the GraphDisplay.
    """

    FluidPressureCriterionGraph = 2
    FluidPressureGraph = 1

class PenetrationPressureUpdateType(Enum):
    """
    Specifies the PenetrationPressureUpdateType.
    """

    EachIterationUpdate = 2
    EachSubstepUpdate = 1

class StartPointScopingType(Enum):
    """
    Specifies the StartPointScopingType.
    """

    StartPointDefineByGeometry = 1
    StartPointDefineByNamedSelection = 2

