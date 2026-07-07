"""ABAQUS module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ABAQUSCommand(object):

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


class AbaqusKeyword(object):
    """
    
            Represents an Abaqus keyword (with arguments and data lines).
            
    """

    @property
    def Arguments(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.FE.ABAQUS.AbaqusKeywordArgumentColl]:
        """
        
            Gets the arguments.
            
        """
        return None

    @property
    def DataLines(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.FE.ABAQUS.AbaqusKeywordDataLineColl]:
        """
        
            Gets the data lines.
            
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


class AbaqusKeywordArgumentColl(object):
    """
    
            Collection of keyword arguments.
            
    """

    @property
    def Items(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.FE.ABAQUS.AbaqusKeywordArgument]]:
        """
        
            Gets the list of arguments.
            
        """
        return None


class AbaqusKeywordArgument(object):
    """
    
            Represents a keyword argument (with Key and Value).
            
    """

    @property
    def Key(self) -> typing.Optional[str]:
        """
        
            Gets the Key.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[str]:
        """
        
            Gets the Value.
            
        """
        return None


class AbaqusKeywordDataLineColl(object):
    """
    
            Collection of keyword data lines.
            
    """

    @property
    def Items(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.FE.ABAQUS.AbaqusKeywordDataLine]]:
        """
        
            Gets the list of data lines.
            
        """
        return None


class AbaqusKeywordDataLine(object):
    """
    
            Represents a keyword data line.
            
    """

    @property
    def Items(self) -> typing.Optional[tuple[str]]:
        """
        
            Gets the data line values.
            
        """
        return None


