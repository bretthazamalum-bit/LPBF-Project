"""Materials module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class IdentifierType(Enum):
    """
    
            The primary identifier to use when searching for existing materials. The name and the uuid must
            always be unique across all materials in the database.  There can be
            Name        UUID
            material1   DEA8407F-4029-4919-94F0-5BDC6FBF203A
            material2   7ED99748-4885-4AAA-8600-CE21253325FA
            
            but not  (same name different UUID)
            material1   DEA8407F-4029-4919-94F0-5BDC6FBF203A
            material1   7ED99748-4885-4AAA-8600-CE21253325FA
            
            or  (different name same UUID)
            material1   DEA8407F-4029-4919-94F0-5BDC6FBF203A
            material2   DEA8407F-4029-4919-94F0-5BDC6FBF203A
            
            The reason to use this is if the name of the material changed for a "refresh" (search by UUID) or if the UUID
            needs changed (search by Name).  Either way a material cannot be added which would violate the above rules.
            
    """

    Name = 1
    UUID = 2

class ExistingMaterialOperation(Enum):
    """
    
            Specifies what should occur when a material being imported has the same identifiers as
            a material which already exists in Mechanical.
            
    """

    New = 1
    Replace = 2

class ImportFormat(Enum):
    """
    
            Specifies how to interpret the material URI when importing.
            
    """

    Automatic = 0

