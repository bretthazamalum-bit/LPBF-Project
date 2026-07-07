"""Materials module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ImportSettings(object):

    @property
    def Filter(self) -> typing.Optional[typing.List[str]]:
        """
        
            All materials will be imported if this list of the names of
            specific materials to be imported is not specified.
            
        """
        return None


