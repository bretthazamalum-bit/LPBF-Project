"""Mechanical module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class MechanicalPanelEnum(Enum):
    """
    
            Specifies the panel type.
            
    """

    DataView = 0
    Worksheet = 1
    TabularData = 2
    Graph = 3
    Outline = 4
    Graphics = 5
    Wizard = 6

class IMechanicalGraphics(object):
    """
    
            Interface for MechanicalGraphics.
            
    """

    @property
    def ModelViewManager(self) -> typing.Optional[Ansys.ACT.Interfaces.Graphics.IModelViewManager]:
        """
        
            An instance of the ModelViewManager.
            
        """
        return None

    @property
    def SectionPlanes(self) -> typing.Optional[Ansys.Mechanical.Graphics.SectionPlanes]:
        """
        
            An instance of the SectionPlanes.
            
        """
        return None


class IMechanicalSelectionInfo(object):
    """
    
            Defines the mechanical selection information.
            
    """

    @property
    def Entities(self) -> typing.Optional[typing.List[Ansys.ACT.Interfaces.Geometry.IGeoEntity]]:
        """
        
            Gets the list of selected geometry entities.
            
        """
        return None

    @property
    def ElementFaceIndices(self) -> typing.Optional[typing.List[int]]:
        """
        
            Gets the list indices needed to define the face of an element.
            
        """
        return None


class IMechanicalDataModel(object):
    """
    
            Defines the data model of the Mechanical application.
            
    """

    @property
    def Project(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Project]:
        """
        
            Gets the project object. Main object of the tree of Mechanical.
            
        """
        return None

    @property
    def Tree(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Tree]:
        """
        
            Gets the tree of Mechanical.
            
        """
        return None

    @property
    def ObjectTags(self) -> typing.Optional[Ansys.Mechanical.Application.ObjectTags]:
        """
        
            Gets the ObjectTags object for the Data Model, which represents the current list of tags visable in the User Interface. 
            
        """
        return None

    def CurrentUnitFromQuantityName(self, quantityName: str) -> str:
        """
        
            Returns the current unit from a quantity name.
            
        """
        pass

    def GetUserObjectById(self, id: int) -> Ansys.ACT.Interfaces.UserObject.IUserObject:
        """
         Gets the user object based on the application id.
        """
        pass


class IMechanicalExtAPI(object):
    """
    
            Exposes the main entry point of all ATC APIs.
            
    """

    def UnlockPrePostLicense(self) -> None:
        """
        R
            Unlocks the license used by the PRE/POST application. This is required if you want to manually launch the Ansys solver.
            You must relock the license after its use. If you don't relock the license, the PRE/POST application will be in read-only mode.
            
        """
        pass

    def LockPrePostLicense(self) -> None:
        """
        
            Locks the license used by the PRE/POST application.
            
        """
        pass


class IMechanicalUserLoad(object):
    """
    
            Defines a Mechanical user load.
            
    """

    pass

class IMechanicalUserObject(object):
    """
    
            Defines a Mechanical user object.
            
    """

    @property
    def Analysis(self) -> typing.Optional[Ansys.ACT.Interfaces.Analysis.IAnalysis]:
        """
        
            Gets the associated analysis.
            
        """
        return None


class IMechanicalUserResult(object):
    """
    
            Defines a Mechanical user result.
            
    """

    pass

class IMechanicalUserSolver(object):
    """
    
            Defines a Mechanical user solver.
            
    """

    pass

