"""CondensedParts module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ExportSettings(object):

    @property
    def ForExpansion(self) -> typing.Optional[bool]:
        """
        
            Specifies whether to prepare the export for expansion. That allows for postprocessing results on physical nodes of an imported condensed part. 
            Default: false. 
            
        """
        return None


