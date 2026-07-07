"""Common module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v242.Ansys.ACT.Common.Graphics as Graphics


class BrowserQt(object):

    @property
    def Tag(self) -> typing.Optional[typing.Any]:
        """
        Tag property.
        """
        return None

    @property
    def InvokeRequired(self) -> typing.Optional[bool]:
        """
        InvokeRequired property.
        """
        return None

    @property
    def Parent(self) -> typing.Optional[Ansys.UI.Toolkit.Control]:
        """
        Parent property.
        """
        return None

    @property
    def Enabled(self) -> typing.Optional[bool]:
        """
        Enabled property.
        """
        return None

    @property
    def Visible(self) -> typing.Optional[bool]:
        """
        Visible property.
        """
        return None

    @property
    def Cursor(self) -> typing.Optional[Ansys.UI.Toolkit.Cursor]:
        """
        Cursor property.
        """
        return None

    @property
    def Controls(self) -> typing.Optional[Ansys.UI.Toolkit.ControlCollection]:
        """
        Controls property.
        """
        return None

    @property
    def Font(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Font]:
        """
        Font property.
        """
        return None

    @property
    def BackColor(self) -> typing.Optional[Ansys.Utilities.Color]:
        """
        BackColor property.
        """
        return None

    @property
    def ForeColor(self) -> typing.Optional[Ansys.Utilities.Color]:
        """
        ForeColor property.
        """
        return None

    @property
    def Focused(self) -> typing.Optional[bool]:
        """
        Focused property.
        """
        return None

    @property
    def IsMouseCaptured(self) -> typing.Optional[bool]:
        """
        IsMouseCaptured property.
        """
        return None

    @property
    def Width(self) -> typing.Optional[int]:
        """
        Width property.
        """
        return None

    @property
    def Height(self) -> typing.Optional[int]:
        """
        Height property.
        """
        return None

    @property
    def Size(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Size]:
        """
        Size property.
        """
        return None

    @property
    def Left(self) -> typing.Optional[int]:
        """
        Left property.
        """
        return None

    @property
    def Top(self) -> typing.Optional[int]:
        """
        Top property.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Point]:
        """
        Location property.
        """
        return None

    @property
    def Bounds(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Rectangle]:
        """
        Bounds property.
        """
        return None

    @property
    def Margins(self) -> typing.Optional[Ansys.UI.Toolkit.Padding]:
        """
        Margins property.
        """
        return None

    @property
    def PreferredSize(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Size]:
        """
        PreferredSize property.
        """
        return None

    @property
    def MinimumSize(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Size]:
        """
        MinimumSize property.
        """
        return None

    @property
    def MaximumSize(self) -> typing.Optional[Ansys.UI.Toolkit.Drawing.Size]:
        """
        MaximumSize property.
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        Name property.
        """
        return None

    @property
    def ToolTipText(self) -> typing.Optional[str]:
        """
        ToolTipText property.
        """
        return None

    @property
    def IsDisposed(self) -> typing.Optional[bool]:
        """
        IsDisposed property.
        """
        return None

    def Dispose(self) -> None:
        """
        Dispose method.
        """
        pass

    def FindParentWindow(self) -> Ansys.UI.Toolkit.Window:
        """
        FindParentWindow method.
        """
        pass

    def FindParentDialog(self) -> Ansys.UI.Toolkit.Dialog:
        """
        FindParentDialog method.
        """
        pass

    def FindTopMostParentControl(self) -> Ansys.UI.Toolkit.Control:
        """
        FindTopMostParentControl method.
        """
        pass

    def Focus(self) -> None:
        """
        Focus method.
        """
        pass

    def SendToBack(self) -> None:
        """
        SendToBack method.
        """
        pass

    def BringToFront(self) -> None:
        """
        BringToFront method.
        """
        pass

    def Show(self) -> None:
        """
        Show method.
        """
        pass

    def Hide(self) -> None:
        """
        Hide method.
        """
        pass

    def GetPreferredSize(self) -> Ansys.UI.Toolkit.Drawing.Size:
        """
        GetPreferredSize method.
        """
        pass

    def GetPreferredHeightForWidth(self, width: int) -> int:
        """
        GetPreferredHeightForWidth method.
        """
        pass

    def Invalidate(self) -> None:
        """
        Invalidate method.
        """
        pass

    def Invalidate(self, rectangle: Ansys.UI.Toolkit.Drawing.Rectangle) -> None:
        """
        Invalidate method.
        """
        pass

    def Update(self) -> None:
        """
        Update method.
        """
        pass

    def Refresh(self) -> None:
        """
        Refresh method.
        """
        pass

    def Refresh(self, rectangle: Ansys.UI.Toolkit.Drawing.Rectangle) -> None:
        """
        Refresh method.
        """
        pass

    def Invoke(self, method: "System.Delegate", args: typing.Any) -> typing.Any:
        """
        Invoke method.
        """
        pass

    def BeginInvoke(self, method: "System.Delegate", args: typing.Any) -> "System.IAsyncResult":
        """
        BeginInvoke method.
        """
        pass

    def EndInvoke(self, asyncResult: "System.IAsyncResult") -> typing.Any:
        """
        EndInvoke method.
        """
        pass


class CoordinateSystem(object):
    """
    
            CoordinateSystem class
            
    """

    @property
    def CoordinateSystemType(self) -> typing.Optional[Ansys.ACT.Interfaces.Analysis.CoordinateSystemTypeEnum]:
        """
        
            Gets or sets the coordinate system type.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the name of the coordinate system.
            
        """
        return None

    @property
    def Id(self) -> typing.Optional[int]:
        """
        
            Gets or sets the ID of the coordinate system.
            
        """
        return None

    @property
    def Origin(self) -> typing.Optional[typing.Iterable[float]]:
        """
        
            Gets or sets the origin of the coordinate system.
            
        """
        return None

    @property
    def Matrix(self) -> typing.Optional[typing.Iterable[float]]:
        """
        
            Gets or sets the matrix definition of the coordinate system.
            
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[typing.Iterable[float]]:
        """
        
            Gets or sets the X axis of the coordinate system.
            
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[typing.Iterable[float]]:
        """
        
            Gets or sets the Y axis of the coordinate system.
            
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[typing.Iterable[float]]:
        """
        
            Gets or sets the Z axis of the coordinate system.
            
        """
        return None


class SimpleTransform(object):
    """
    
            Exposes simple getters and setters for rigid body transformations.
            
    """

    @property
    def TransformationMatrix(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.RigidBodyTransformationMatrix]:
        """
        TransformationMatrix property.
        """
        return None

    @property
    def IsOrthonormal(self) -> typing.Optional[bool]:
        """
        
            Returns `true` if the provided axis vectors are all normalized and orthogonal.
            
        """
        return None

    @property
    def Translation(self) -> typing.Optional[Ansys.ACT.Core.Math.Point3D]:
        """
        
            The translation of the transformation with respect to the global/world coordinate
            system.
            
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
            The X-axis orientation of the transformation with respect to the global/world
            coordinate system.
            
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
            The Y-axis orientation of the transformation with respect to the global/world
            coordinate system.
            
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.ACT.Core.Math.Vector3D]:
        """
        
            The X-axis orientation of the transformation with respect to the global/world
            coordinate system.
            
        """
        return None


