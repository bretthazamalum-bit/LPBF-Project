"""FE module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v241.Ansys.ACT.Automation.Mechanical.FE.NASTRAN as NASTRAN
import ansys.mechanical.stubs.v241.Ansys.ACT.Automation.Mechanical.FE.CDB as CDB
import ansys.mechanical.stubs.v241.Ansys.ACT.Automation.Mechanical.FE.ABAQUS as ABAQUS


class CommandsType(Enum):
    """
    
            Commands type.
            
    """

    Processed = 1
    UnProcessed = 2
    All = 3

class CommandColl(object):
    """
    
            Collection of commands.
            
    """

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the count of commands.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Common.Interop.FECommandsModel.ICommand]:
        """
        Item property.
        """
        return None


class CommandRepository(object):
    """
    
            Command repository.
            
    """

    def GetCommandsByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.FE.CommandColl:
        """
        Gets the commands by name.
        """
        pass

    def GetCommandByIndex(self, index: int) -> Ansys.Common.Interop.FECommandsModel.ICommand:
        """
        Gets the commands by index.
        """
        pass

    def GetCommandNamesCount(self, eCommandsType: Ansys.ACT.Automation.Mechanical.FE.CommandsType) -> int:
        """
        Gets the number of commands of a type specified by param=eCommandsType in the repository.
        """
        pass

    def GetCommandName(self, eCommandsType: Ansys.ACT.Automation.Mechanical.FE.CommandsType, index: int) -> str:
        """
        Gets the name of commands of a type specified by params eCommandsType and index in the repository.
        """
        pass

    def GetCommandNames(self, eCommandsType: Ansys.ACT.Automation.Mechanical.FE.CommandsType) -> tuple[str]:
        """
        Gets the command names of a type specified by params eCommandsType and index in the repository.
        """
        pass


class Command(object):
    """
    
            Base class for all Commands.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets the command name.
            
        """
        return None

    @property
    def Index(self) -> typing.Optional[int]:
        """
        
            Gets the command index.
            
        """
        return None


class FEParser(object):
    """
    
            FE parser object.
            
    """

    pass

