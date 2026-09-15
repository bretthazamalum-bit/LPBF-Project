"""Application module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class Progress(object):
    """
    Defines a Progress.
    """

    def SetProgress(self, uiProgress: int, uiMessage: str, uiSubProgress: int, uiSubMessage: str) -> None:
        """
        Set the current progress state
        """
        pass


class ObjectTag(object):
    """
    
            An instance of an ObjectTag.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the tag. If the tag exists in ObjectTags, attempting to set the name to a value of another tag in that collection will lead to an exception.
            
        """
        return None

    @property
    def Objects(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        
            The list of objects which use this tag.
            
        """
        return None

    def AddObject(self, obj: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject) -> None:
        """
        
            Add an object to this tag.
            
        """
        pass

    def RemoveObject(self, obj: Ansys.Mechanical.DataModel.Interfaces.IDataModelObject) -> None:
        """
        
            Remove an object from this tag.
            
        """
        pass

    def ClearObjects(self) -> None:
        """
        
            Clear all objects from this tag.
            
        """
        pass


class ObjectTags(object):
    """
    
            Defines the collection of Mechanical’s tags.
            
    """

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            The number of tags in the collection.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Application.ObjectTag]:
        """
        Item property.
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Application.ObjectTag]:
        """
        Item property.
        """
        return None

    @property
    def TagNames(self) -> typing.Optional[typing.List[str]]:
        """
        
            The names of the tags in the collection.
            
        """
        return None

    def Add(self, tag: Ansys.Mechanical.Application.ObjectTag) -> None:
        """
        
            Adds a new tag to the collection. Throws an error if the tag already exists in the collection.
            
        """
        pass

    def Remove(self, tag: Ansys.Mechanical.Application.ObjectTag) -> bool:
        """
        
            Removes a tag if it exists in the collection.
            
        """
        pass

    def GetTag(self, tagName: str) -> Ansys.Mechanical.Application.ObjectTag:
        """
        
            Returns the tag in the collection with the given name.
            
        """
        pass

    def IndexOf(self, tag: Ansys.Mechanical.Application.ObjectTag) -> int:
        """
        
            Returns the index of the given tag. If the given tag does not exist in the collection, returns -1.
            
        """
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the tag at the given index from the collection.
            
        """
        pass

    def Clear(self) -> None:
        """
        
            Clears the collection, removing all objects from the tags in the collection.
            
        """
        pass

    def Contains(self, tag: Ansys.Mechanical.Application.ObjectTag) -> bool:
        """
        
            Returns whether or not the collection contains the given tag.
            
        """
        pass


class Message(object):
    """
    
            A message.
            
    """

    @property
    def Source(self) -> typing.Optional[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        
            The source object of the message.
            
        """
        return None

    @property
    def StringID(self) -> typing.Optional[str]:
        """
        
            The string ID of the message.
            
        """
        return None

    @property
    def DisplayString(self) -> typing.Optional[str]:
        """
        
            The display string of the message.
            
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        
            The location of the message.
            
        """
        return None

    @property
    def TimeStamp(self) -> typing.Optional[typing.Any]:
        """
        
            The timestamp of the message.
            
        """
        return None

    @property
    def RelatedObjects(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        
            The list of objects related to the message.
            
        """
        return None

    @property
    def Severity(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MessageSeverityType]:
        """
        
            The severity of the message.
            
        """
        return None


class Messages(object):
    """
    
            Defines the collection of Mechanical's messages.
            
    """

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Get the number of messages.
            
        """
        return None

    def Add(self, item: Ansys.Mechanical.Application.Message) -> None:
        """
        
            Add a new message.
            
        """
        pass

    def Remove(self, item: Ansys.Mechanical.Application.Message) -> bool:
        """
        
            Remove a specific message in the list.
            
        """
        pass

    def Clear(self) -> None:
        """
        
            Clear the list of the messages.
            
        """
        pass

    def Contains(self, item: Ansys.Mechanical.Application.Message) -> bool:
        """
        
            Check if a message is in the current list of messages.
            
        """
        pass

    def ShowErrors(self) -> None:
        """
        
            Shows errors with current project.
            
        """
        pass


