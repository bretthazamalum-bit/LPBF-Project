"""Graphics module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class IModelViewManager(object):
    """
    
            
            
    """

    @property
    def NumberOfViews(self) -> typing.Optional[int]:
        """
        
            The number of views currently defined.
            
        """
        return None

    def ApplyModelView(self, viewIndex: int) -> None:
        """
        
            Apply the view specified by index.
            
        """
        pass

    def ApplyModelView(self, viewLabel: str) -> None:
        """
        
            Apply the view specified by name.
            
        """
        pass

    def CaptureModelView(self, index: int, mode: str) -> None:
        """
        
            Save the view specified by index as a PNG image to the project userfiles.
            
        """
        pass

    def CaptureModelView(self, viewLabel: str, mode: str) -> None:
        """
        
            Save the view specified as an image to the project userfiles.
            
        """
        pass

    def CreateView(self) -> None:
        """
        
            Create a view from current graphics with default naming.
            
        """
        pass

    def CreateView(self, viewName: str) -> None:
        """
        
            Create a view from current graphics with the specified name.
            
        """
        pass

    def DeleteView(self, viewIndex: int) -> None:
        """
        
            Delete the specified view by index.
            
        """
        pass

    def DeleteView(self, viewLabel: str) -> None:
        """
        
            Apply the view specified by name.
            
        """
        pass

    def ExportModelViews(self, viewfilepath: str) -> None:
        """
        
            Export model views to the specified file.
            
        """
        pass

    def ImportModelViews(self, viewfilepath: str) -> None:
        """
        
            Import model views from the specified file.
            
        """
        pass

    def RenameView(self, viewIndex: int, newLabel: str) -> None:
        """
        
            Rename the model view specified by viewIndex to newLabel.
            
        """
        pass

    def RenameView(self, viewLabel: str, newLabel: str) -> None:
        """
        
            Rename the model view specified  to newLabel.
            
        """
        pass


