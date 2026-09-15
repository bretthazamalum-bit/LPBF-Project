"""CompositeFailure module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class FailureDimension(Enum):
    """
    This enum defines the dimension values for configuring failure criteria.
            In particular, the Tsai – Wu, Tsai – Hill, Hoffman, Hashin and Cuntze criteria
            can be configured in this way.
    """

    pass

class LaRCFormulation(Enum):
    """
    This enum defines the different formulations which can be used for
            evaluating the LaRC failure criterion.
    """

    pass

class PuckFormulation(Enum):
    """
    This enum defines the different formulations which can be used for
            evaluating the Puck failure criterion.
    """

    pass

