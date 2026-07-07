"""Common module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AngleUnitType(Enum):
    """
    Specifies the AngleUnitType.
    """

    Radian = 1
    Degree = 0

class AngularVelocityUnitType(Enum):
    """
    Specifies the AngularVelocityUnitType.
    """

    RadianPerMilliSecond = 2
    RadianPerSecond = 1
    RPM = 0

class MechanicalUnitSystemEnum(Enum):
    """
    Specifies the WBUnitSystemType.
    """

    ConsistentBFT = 7
    ConsistentBIN = 8
    ConsistentCGS = 5
    ConsistentMKS = 11
    ConsistentNMM = 6
    ConsistentUMKS = 10
    NoUnitSystem = 19
    StandardBFT = 3
    StandardBIN = 4
    StandardCGS = 1
    StandardCUST = 12
    StandardMKS = 0
    StandardNMM = 2
    StandardNMMdat = 14
    StandardNMMton = 13
    StandardUMKS = 9
    StandardKNMS = 15
    StandardGMMS = 17

class MetricTemperatureUnitType(Enum):
    """
    Specifies the MetricTemperatureUnitType.
    """

    Celsius = 1
    Kelvin = 0

class SelectionTypeEnum(Enum):
    """
    
            Specifies the selection type.
            
    """

    GeometryEntities = 0
    MeshNodes = 1
    MeshElements = 2
    PathSpecific = 3
    SurfaceSpecific = 4
    WorksheetSpecific = 5
    MeshElementFaces = 6

class State(Enum):
    """
    
            General state enumeration to be used across ACT Apps.
            
    """

    UpToDate = 0
    RefreshRequired = 1
    OutOfDate = 2
    UpdateRequired = 3
    Modified = 4
    Unfulfilled = 5
    Disabled = 6
    Error = 7
    EditRequired = 8
    Interrupted = 9
    UpstreamChangesPending = 10
    Unknown = 11

class StateMessageTypes(Enum):
    """
    
            Specifies the selection type.
            
    """

    Information = 0
    Warning = 1
    Error = 2

class IProcessUtilities(object):

    def Start(self, target: str, args: str) -> int:
        """
        Start method.
        """
        pass

    def Start(self, target: str, useShell: bool, args: str) -> int:
        """
        Start method.
        """
        pass


class ISourceFile(object):
    """
    
            A file containing source code.
            
    """

    @property
    def FilePath(self) -> typing.Optional[str]:
        """
        
            Represents the absolute path of the source file.
            
        """
        return None

    @property
    def Content(self) -> typing.Optional[str]:
        """
        
            Reads or writes the content of the file.
            
        """
        return None

    def Save(self) -> None:
        """
        
            Saves the modified content.
            
        """
        pass


class IWorksheet(object):
    """
    
            Defines a worksheets information.
            
    """

    @property
    def RowCount(self) -> typing.Optional[int]:
        """
        
            Gets the number of rows contained in the worksheet.
            
        """
        return None

    def AddRow(self) -> int:
        """
        
            Adds a row to the worksheet.
            
        """
        pass

    def DeleteRow(self, index: int) -> None:
        """
        
            Deletes a row from the worksheet at index.
            
        """
        pass


class IParameter(object):
    """
    
            Defines a design parameter.
            
    """

    @property
    def Key(self) -> typing.Optional[str]:
        """
        
            Gets the identifier of the parameter.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets the name of the parameter.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[float]:
        """
        
            Gets the value of the parameter.
            
        """
        return None


class IAttributeCollection(object):
    """
    
            Defines a collection of attributes.
            
    """

    @property
    def Item(self) -> typing.Optional[typing.Any]:
        """
        Item property.
        """
        return None

    @property
    def Keys(self) -> typing.Optional[System.Collections.Generic.ICollection[str]]:
        """
        
            Gets the list of attribute names.
            
        """
        return None

    def GetValue(self, name: str, defaultValue: typing.Any) -> typing.Any:
        """
        
            Returns the value of the attribute identified by its name.
            
        """
        pass

    def GetValue(self, name: str) -> typing.Any:
        """
        
            Returns the value of the attribute identified by its name.
            
        """
        pass

    def GetStringValue(self, name: str) -> str:
        """
        
            Returns the string value of the attribute identified by its name.
            
        """
        pass

    def SetValue(self, name: str, value: typing.Any) -> None:
        """
        
            Sets the value of an attribute identified by its name.
            
        """
        pass

    def Remove(self, name: str) -> bool:
        """
        
            Removes the attribute identified by its name.
            
        """
        pass

    def Contains(self, name: str) -> bool:
        """
        
            Checks if the collection contains the attribute identified by its name.
            
        """
        pass


class IExtension(object):
    """
    
            Defines an extension.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets the name of the extension.
            
        """
        return None

    @property
    def Version(self) -> typing.Optional[int]:
        """
        
            Gets the version of the extension.
            
        """
        return None

    @property
    def MinorVersion(self) -> typing.Optional[int]:
        """
        
            Gets the minor version of the extension.
            
        """
        return None

    @property
    def UniqueId(self) -> typing.Optional[str]:
        """
        
            Gets the unique identifier of the extension.
            
        """
        return None

    @property
    def InstallDir(self) -> typing.Optional[str]:
        """
        
            Gets the folder where the extension is installed.
            
        """
        return None

    @property
    def Attributes(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.IAttributeCollection]:
        """
        
            Gets the attributes of the extension.
            
        """
        return None


class IExtensionManager(object):
    """
    
            Defines an extension manager.
            
    """

    @property
    def CurrentExtension(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.IExtension]:
        """
        
            Gets the current extension.
            
        """
        return None

    @property
    def Extensions(self) -> typing.Optional[typing.List[Ansys.ACT.Interfaces.Common.IExtension]]:
        """
        
            Gets the list of loaded extensions.
            
        """
        return None


class ILog(object):
    """
    
            Defines log engine.
            
    """

    def WriteMessage(self, message: str) -> None:
        """
        
            Adds a new message entry into the log. 
            
        """
        pass

    def WriteWarning(self, message: str) -> None:
        """
        
            Adds a new warning message entry into the log. 
            
        """
        pass

    def WriteError(self, message: str) -> None:
        """
        
            Adds a new error message entry into the log.
            
        """
        pass


class IParameterManager(object):
    """
    
            Defines a parameter manager.
            
    """

    pass

class ISelectionInfo(object):
    """
    
            Defines a selection information.
            
    """

    @property
    def Id(self) -> typing.Optional[int]:
        """
        
            Gets the selection identifier.
            
        """
        return None

    @property
    def Ids(self) -> typing.Optional[typing.List[int]]:
        """
        
            Gets or sets selected IDs.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the selection name.
            
        """
        return None

    @property
    def SelectionType(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.SelectionTypeEnum]:
        """
        
            Gets or sets the selection type.
            
        """
        return None


class ISelectionManager(object):
    """
    
            Defines a selection manager.
            
    """

    @property
    def CurrentSelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        
            Gets the current selection.
            
        """
        return None

    def AddSelection(self, info: Ansys.ACT.Interfaces.Common.ISelectionInfo) -> None:
        """
        
            Adds a new selection to the current selection.
            
        """
        pass

    def NewSelection(self, info: Ansys.ACT.Interfaces.Common.ISelectionInfo) -> None:
        """
        
            Creates a new selection.
            
        """
        pass

    def ClearSelection(self) -> None:
        """
        
            Clears the current selection.
            
        """
        pass

    def CreateSelectionInfo(self, selectionType: Ansys.ACT.Interfaces.Common.SelectionTypeEnum) -> Ansys.ACT.Interfaces.Common.ISelectionInfo:
        """
        
            Creates a new selection information based on its type.
            
        """
        pass


class ITools(object):
    """
    
            Defines common tools.
            
    """

    def GetResultsDataFromFile(self, filename: str) -> Ansys.ACT.Interfaces.Post.IResultReader:
        """
        
            Returns the result reader object associated to the file name specified.
            
        """
        pass

    def GetMeshDataFromFile(self, filename: str, bodyGrouping: str) -> Ansys.ACT.Interfaces.Mesh.IMeshData:
        """
        
            Returns the mesh data model associated to the file name specified.
            
        """
        pass

    def GetGeoDataFromFile(self, filename: str) -> Ansys.ACT.Interfaces.Geometry.IGeoData:
        """
        
            Returns the geo data model object for the CAD file name specified.
            
        """
        pass


class UserErrorMessageException(object):
    """
    
            Defines a user exception used to send error message to the end user.
            
    """

    pass

class IBreakpoint(object):
    """
    
            A stop point in the source file of a code.
            
    """

    @property
    def Line(self) -> typing.Optional[int]:
        """
        
            The line number on which the breakpoint is.
            
        """
        return None

    @property
    def SourceFile(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISourceFile]:
        """
        
            The file to which the breakpoint is attached.
            
        """
        return None

    @property
    def IsEnabled(self) -> typing.Optional[bool]:
        """
        
            Specifies whether the breakpoint is enabled or not.
            
        """
        return None


