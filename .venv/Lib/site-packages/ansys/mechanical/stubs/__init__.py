try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:  # pragma: no cover
    import importlib_metadata  # type: ignore

__version__ = importlib_metadata.version("ansys-mechanical-stubs")
"""Patch version for the ansys-mechanical-stubs package."""

from .v251 import *
"""Mechanical installation version."""
from .v241 import *
"""Mechanical installation version."""
from .v252 import *
"""Mechanical installation version."""
from .v242 import *
"""Mechanical installation version."""
