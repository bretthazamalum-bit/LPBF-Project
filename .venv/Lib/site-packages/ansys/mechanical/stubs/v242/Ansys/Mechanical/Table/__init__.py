"""Table module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ColumnarDataImportDefinition(object):
    """
    
            A simple class to hold the import definitions for how a column from a data source in
            columnar format should be processed.
            
    """

    @property
    def Index(self) -> typing.Optional[int]:
        """
        
            Gets or sets the specified data source column index from which this variable will be
            imported.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets an identifier for the data source column.
            
        """
        return None

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        
            Gets or sets the unit of the column.
            
        """
        return None

    @property
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableType]:
        """
        
            Gets or sets the variable type of the column.
            
        """
        return None

    @property
    def VariableClassification(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableClassification]:
        """
        
            Gets or sets the variable classification of the column.
            
        """
        return None


class ColumnarDataSourceBase(object):
    """
    
            T:Ansys.Mechanical.Table.ColumnarDataSourceBase is a class that provides foundational behavior for
            import settings that consume data from columnar data sources (such as delimited or
            fixed-width files).
            
    """

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of column definitions.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        """
        Item property.
        """
        return None

    @property
    def SkipFooter(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to ignore at the end of the file during import.
            
        """
        return None

    @property
    def SkipRows(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to skip over at the start of the file during import.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    @property
    def PathType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType]:
        """
        
            Gets or sets the type of URI provided for Table import.
            Default: F:Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType.Absolute
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableType, variableClassification: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableClassification, unit: str, name: str) -> Ansys.Mechanical.Table.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class FixedWidthImportSettings(object):
    """
    
            T:Ansys.Mechanical.Table.FixedWidthImportSettings defines how to import data from a delimited source
            for tabular data.
            
    """

    @property
    def ColumnWidths(self) -> typing.Optional[typing.Any]:
        """
        
            Gets or sets the specified column widths.
            When setting, The value provided to P:Ansys.Mechanical.Table.FixedWidthImportSettings.ColumnWidths may be either:
            number
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of column definitions.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        """
        Item property.
        """
        return None

    @property
    def SkipFooter(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to ignore at the end of the file during import.
            
        """
        return None

    @property
    def SkipRows(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to skip over at the start of the file during import.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    @property
    def PathType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType]:
        """
        
            Gets or sets the type of URI provided for Table import.
            Default: F:Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType.Absolute
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableType, variableClassification: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableClassification, unit: str, name: str) -> Ansys.Mechanical.Table.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class DelimitedImportSettings(object):
    """
    
            T:Ansys.Mechanical.Table.DelimitedImportSettings defines how to import data from a delimited source
            for tabular data.
            
    """

    @property
    def Delimiter(self) -> typing.Optional[str]:
        """
        
            The delimiter used to separate columns.
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of column definitions.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        """
        Item property.
        """
        return None

    @property
    def SkipFooter(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to ignore at the end of the file during import.
            
        """
        return None

    @property
    def SkipRows(self) -> typing.Optional[int]:
        """
        
            Gets or sets the number of rows to skip over at the start of the file during import.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    @property
    def PathType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType]:
        """
        
            Gets or sets the type of URI provided for Table import.
            Default: F:Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType.Absolute
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.Table.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableType, variableClassification: Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableClassification, unit: str, name: str) -> Ansys.Mechanical.Table.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class ImportHelpers(object):

    pass

class ImportSettingsBase(object):
    """
    
            A base class for Table import settings.
            
    """

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    @property
    def PathType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType]:
        """
        
            Gets or sets the type of URI provided for Table import.
            Default: F:Ansys.Mechanical.DataModel.MechanicalEnums.Common.PathType.Absolute
            
        """
        return None


class ImportSettingsFactory(object):

    @classmethod
    def GetSettingsForFormat(cls, format: Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat) -> Ansys.Mechanical.Table.ImportSettingsBase:
        """
        
            M:Ansys.Mechanical.Table.ImportSettingsFactory.GetSettingsForFormat(Ansys.Mechanical.DataModel.MechanicalEnums.Table.ImportFormat) constructs and returns the correct settings class
            instance based on the specified format.
            
        """
        pass


