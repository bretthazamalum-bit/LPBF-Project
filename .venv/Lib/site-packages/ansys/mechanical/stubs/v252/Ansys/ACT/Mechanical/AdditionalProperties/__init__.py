"""AdditionalProperties module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class Control(Enum):
    """
    
            The control type for an additional property.
            
    """

    Expression = 64
    Double = 1310720
    ApplyCancel = 131072
    Options = 2097152

class ApplyCancelProperty(object):
    """
    
            Provides a way to create properties with Apply/Cancel buttons.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the property.
            
        """
        return None

    @property
    def DisplayName(self) -> typing.Optional[str]:
        """
        
            The name of the property shown in the UI. If not set, the Name property is used.
            
        """
        return None

    @property
    def GroupName(self) -> typing.Optional[str]:
        """
        
            The group name of the property shown in the UI, and used to separate properties based on group name.
            
        """
        return None

    @property
    def Tooltip(self) -> typing.Optional[str]:
        """
        
            The tooltip of the property in the UI.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[typing.Any]:
        """
        
            The stored value of the property.
            
        """
        return None

    @property
    def ValueString(self) -> typing.Optional[str]:
        """
        
            Get the string representation of the value.
            
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        
            Returns whether a property is readonly.
            
        """
        return None


class DoubleProperty(object):
    """
    
            Provides a way to create properties that can hold double type values.
            
    """

    @property
    def ValidRange(self) -> typing.Optional[tuple]:
        """
        
            Tuple that can be used to control the upper and lower bounds of a double property.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the property.
            
        """
        return None

    @property
    def DisplayName(self) -> typing.Optional[str]:
        """
        
            The name of the property shown in the UI. If not set, the Name property is used.
            
        """
        return None

    @property
    def GroupName(self) -> typing.Optional[str]:
        """
        
            The group name of the property shown in the UI, and used to separate properties based on group name.
            
        """
        return None

    @property
    def Tooltip(self) -> typing.Optional[str]:
        """
        
            The tooltip of the property in the UI.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[typing.Any]:
        """
        
            The stored value of the property.
            
        """
        return None

    @property
    def ValueString(self) -> typing.Optional[str]:
        """
        
            Get the string representation of the value.
            
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        
            Returns whether a property is readonly.
            
        """
        return None


class ExpressionProperty(object):
    """
    
            Provides a way to create properties that can hold expressions.
            
    """

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the property.
            
        """
        return None

    @property
    def DisplayName(self) -> typing.Optional[str]:
        """
        
            The name of the property shown in the UI. If not set, the Name property is used.
            
        """
        return None

    @property
    def GroupName(self) -> typing.Optional[str]:
        """
        
            The group name of the property shown in the UI, and used to separate properties based on group name.
            
        """
        return None

    @property
    def Tooltip(self) -> typing.Optional[str]:
        """
        
            The tooltip of the property in the UI.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[typing.Any]:
        """
        
            The stored value of the property.
            
        """
        return None

    @property
    def ValueString(self) -> typing.Optional[str]:
        """
        
            Get the string representation of the value.
            
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        
            Returns whether a property is readonly.
            
        """
        return None


class OptionsProperty(object):
    """
    
            Provides a way to create properties that show up as a drop down in the UI.
            
    """

    @property
    def Options(self) -> typing.Optional[dict[typing.Any,typing.Any]]:
        """
        
            Options shown in the drop-down, represented by a dictionary of int -> string.
            Where the int represents the option, and string represents string shown in the UI.
            When an option is selected the Value property of the property is set to to the option int.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            The name of the property.
            
        """
        return None

    @property
    def DisplayName(self) -> typing.Optional[str]:
        """
        
            The name of the property shown in the UI. If not set, the Name property is used.
            
        """
        return None

    @property
    def GroupName(self) -> typing.Optional[str]:
        """
        
            The group name of the property shown in the UI, and used to separate properties based on group name.
            
        """
        return None

    @property
    def Tooltip(self) -> typing.Optional[str]:
        """
        
            The tooltip of the property in the UI.
            
        """
        return None

    @property
    def Value(self) -> typing.Optional[typing.Any]:
        """
        
            The stored value of the property.
            
        """
        return None

    @property
    def ValueString(self) -> typing.Optional[str]:
        """
        
            Get the string representation of the value.
            
        """
        return None

    @property
    def ReadOnly(self) -> typing.Optional[bool]:
        """
        
            Returns whether a property is readonly.
            
        """
        return None


