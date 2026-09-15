"""Adapters module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AAPCustomLoadAdapter(object):

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, fieldType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSThicknessAdapter(object):
    """
    
            Adapter dedicated to IDSThicknessAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSTopoConstraintAdapter(object):
    """
    
            Adapter dedicated to IDSRSLoad objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSPSDLoadAdapter(object):
    """
    
            Adapter dedicated to IDSRSLoad objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSRSLoadAdapter(object):
    """
    
            Adapter dedicated to IDSRSLoad objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSBoltPretensionAdapter(object):
    """
    
            Adapter dedicated to IDSBoltPretensionAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSJointLoadAdapter(object):
    """
    
            Adapter dedicated to IDSJointConditionAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSRotationAdapter(object):
    """
    
            Adapter dedicated to IDSRotationAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSAccelerationAdapter(object):
    """
    
            Adapter dedicated to IDSAccelerationAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSBearingAdapter(object):
    """
    
            Adapter dedicated to IDSBearingAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSLoadAdapter(object):
    """
    
            Adapter dedicated to IDSLoadAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class DSSpringAdapter(object):
    """
    
            Adapter dedicated to IDSSpringAuto objects.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, componentType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        ChangeFieldDefinitionType method.
        """
        pass


class FieldAdapter(object):
    """
    
            Base class for objects that handle the interface between the generic boundary condition wrapper and the various types of concrete object implemented in Mechanical.
            
    """

    @property
    def FieldProvider(self) -> typing.Optional[Ansys.Common.Interop.DSObjects.IDSBCInformation]:
        """
        
            Gets the wrapped object from Mechanical.
            
        """
        return None

    def ChangeFieldDefinitionType(self, fieldType: Ansys.Common.Interop.CAERepObjects.AnsBCLVType, newType: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> None:
        """
        
            Changes the definition type for a field of the wrapped object from Mechanical.
            
        """
        pass


class FieldAdapterManager(object):
    """
    
            Static class that operates like a factory to create field adapters from Mechanical objects.
            
    """

    @classmethod
    @property
    def AdapterDefinitions(cls) -> typing.Optional[typing.List[Ansys.ACT.Mechanical.Fields.Adapters.FieldAdapter.IDefinition]]:
        """
        
            Gets the collection of adapters in this manager.
            
        """
        return System.Collections.ObjectModel.ReadOnlyCollection[Ansys.ACT.Mechanical.Fields.Adapters.FieldAdapter.IDefinition]

    @classmethod
    def RegisterNewAdapter(cls, definition: Ansys.ACT.Mechanical.Fields.Adapters.FieldAdapter.IDefinition) -> None:
        """
        
            Register the instance object that defines a type of field adapter.
            
        """
        pass

    @classmethod
    def UnregisterAdapter(cls, index: int) -> None:
        """
        
            Removes the instance object that defines a type of field adapter from this manager.
            
        """
        pass


class Keywords(object):

    @classmethod
    def Get(cls, type: Ansys.Common.Interop.AnsMaterial.kEDDataType) -> str:
        """
        Get method.
        """
        pass


class IDefinition(object):

    def Adapt(self, load: Ansys.Common.Interop.DSObjects.IDSBCInformation) -> Ansys.ACT.Mechanical.Fields.Adapters.FieldAdapter:
        """
        
            Creates an adapter for a given load object from Mechanical.
            
        """
        pass


