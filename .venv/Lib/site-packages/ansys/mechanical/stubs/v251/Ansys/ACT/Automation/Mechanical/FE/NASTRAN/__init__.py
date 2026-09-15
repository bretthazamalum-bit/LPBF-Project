"""NASTRAN module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class NASTRANCommand(object):

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


class GenericCommand(object):
    """
    
            Generic command.
            
    """

    @property
    def Arguments(self) -> typing.Optional[tuple[typing.Any]]:
        """
        
            Gets the arguments.
            
        """
        return None

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


class CaseControlCommand(object):
    """
    
            Case control command.
            
    """

    @property
    def Text(self) -> typing.Optional[str]:
        """
        
            Gets the text.
            
        """
        return None

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


class NastranOption(object):
    """
    
            Option.
            
    """

    pass

class NastranOptionLine(object):
    """
    
            Option line.
            
    """

    pass

class OptionsControlCommand(object):
    """
    
            Options control command.
            
    """

    @property
    def Arguments(self) -> typing.Optional[tuple[typing.Any]]:
        """
        
            Gets the arguments.
            
        """
        return None

    @property
    def OptionLines(self) -> typing.Optional[tuple[typing.Any]]:
        """
        
            Gets the option lines.
            
        """
        return None

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


