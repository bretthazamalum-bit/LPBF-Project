"""ExternalData module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CGNSImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.CGNSImportSettings defines how to import external data from a CGNS file.
            
    """

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


class H5ImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.H5ImportSettings defines how to import external data from a H5 file.
            
    """

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


class AXDTImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.AXDTImportSettings defines how to import external data from an AXDT file.
            
    """

    @property
    def Dimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SourceDimension]:
        """
        
            The dimension of the AXDT file.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


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
    def VariableType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.VariableType]:
        """
        
            Gets or sets the variable type of the column.
            
        """
        return None

    @property
    def UserFieldVariable(self) -> typing.Optional[str]:
        """
        
            
        """
        return None


class ColumnarDataSourceBase(object):
    """
    
            T:Ansys.Mechanical.ExternalData.ColumnarDataSourceBase is a class that provides foundational behavior for
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
    def Item(self) -> typing.Optional[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
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
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.VariableType, unit: str, name: str) -> Ansys.Mechanical.ExternalData.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class DelimitedImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.DelimitedImportSettings defines how to import external data from a delimited source file.
            
    """

    @property
    def Delimiter(self) -> typing.Optional[str]:
        """
        
            The delimiter used to separate columns.
            
        """
        return None

    @property
    def AverageCornerNodesToMidsideNodes(self) -> typing.Optional[bool]:
        """
        
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of column definitions.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
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
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.VariableType, unit: str, name: str) -> Ansys.Mechanical.ExternalData.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class ECADImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.ECADImportSettings defines how to import external data from an ECAD file.
            
    """

    @property
    def UseDummyNetData(self) -> typing.Optional[bool]:
        """
        
            The UseDummyNetData falg of the ECAD file. For External Data files that include trace mapping, 
            selecting this option enables you to import trace data belonging to the dummy net of the file.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


class ExternalDataFile(object):
    """
    
            A basic definition of the external data file. 
            
    """

    @property
    def FilePath(self) -> typing.Optional[str]:
        """
        
            Gets or sets the file path of the external data file.
            
        """
        return None

    @property
    def Identifier(self) -> typing.Optional[str]:
        """
        
            Gets or sets the identifier of the external data file.
            
        """
        return None

    @property
    def Description(self) -> typing.Optional[str]:
        """
        
            Gets or sets the optional description of the external data file.
            
        """
        return None

    @property
    def IsMainFile(self) -> typing.Optional[bool]:
        """
        
            
        """
        return None

    @property
    def ImportSettings(self) -> typing.Optional[Ansys.Mechanical.ExternalData.ImportSettingsBase]:
        """
        
            
        """
        return None


class ExternalDataFileCollection(object):
    """
    
            T:Ansys.Mechanical.ExternalData.ExternalDataFileCollection is a class that provides foundational behavior for
            holding external data files.
            
    """

    @property
    def SaveFilesWithProject(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the flag controlling if the external data files will be copied to the project directory. 
            If this flag is set to False, the external data files will directly reference the file path. 
            The default is False. 
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.ExternalData.ExternalDataFile]:
        """
        Item property.
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of external data files.
            
        """
        return None

    def Add(self, item: Ansys.Mechanical.ExternalData.ExternalDataFile) -> None:
        pass

    def Clear(self) -> None:
        pass

    def Contains(self, item: Ansys.Mechanical.ExternalData.ExternalDataFile) -> bool:
        pass

    def CopyTo(self, array: Ansys.Mechanical.ExternalData.ExternalDataFile, arrayIndex: int) -> None:
        """
        CopyTo method.
        """
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.ExternalData.ExternalDataFile]:
        pass

    def IndexOf(self, item: Ansys.Mechanical.ExternalData.ExternalDataFile) -> int:
        pass

    def Insert(self, index: int, item: Ansys.Mechanical.ExternalData.ExternalDataFile) -> None:
        pass

    def Remove(self, item: Ansys.Mechanical.ExternalData.ExternalDataFile) -> bool:
        pass

    def RemoveAt(self, index: int) -> None:
        pass


class FixedWidthImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.FixedWidthImportSettings defines how to import external data from a fixed-width source file.
            
    """

    @property
    def ColumnWidths(self) -> typing.Optional[str]:
        """
        
            
        """
        return None

    @property
    def AverageCornerNodesToMidsideNodes(self) -> typing.Optional[bool]:
        """
        
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of column definitions.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
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
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None

    def Clear(self) -> None:
        pass

    def GetEnumerator(self) -> typing.Iterator[Ansys.Mechanical.ExternalData.ColumnarDataImportDefinition]:
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Removes the import definition at the specified index.
            
        """
        pass

    def UseColumn(self, index: int, variableType: Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.VariableType, unit: str, name: str) -> Ansys.Mechanical.ExternalData.ColumnarDataSourceBase:
        """
        
            
        """
        pass


class ICEPAKImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.ICEPAKImportSettings defines how to import external data from an ICEPAK BOOL or ICEPAK COND file. 
            
    """

    @property
    def SupportingFilePath(self) -> typing.Optional[str]:
        """
        
            The supporting file path of the ICEPAK INFO file.
            
        """
        return None

    @property
    def SupportingFileIdentifier(self) -> typing.Optional[str]:
        """
        
            The supporting file identifier. The identifier should be unique, otherwise, an exception will be 
            thrown during the import. 
            
        """
        return None

    @property
    def SupportingFileDescription(self) -> typing.Optional[str]:
        """
        
            The supporting file description. This is optional.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


class ImportSettingsBase(object):
    """
    
            A base class for Table import settings.
            
    """

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


class ImportSettingsFactory(object):

    @classmethod
    def GetSettingsForFormat(cls, format: Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat) -> Ansys.Mechanical.ExternalData.ImportSettingsBase:
        """
        
            M:Ansys.Mechanical.ExternalData.ImportSettingsFactory.GetSettingsForFormat(Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat) constructs and returns the correct settings class
            instance based on the specified format.
            
        """
        pass


class MAPDLImportSettings(object):
    """
    
            T:Ansys.Mechanical.ExternalData.MAPDLImportSettings defines how to import external data from a MAPDL CDB file.
            
    """

    @property
    def Dimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SourceDimension]:
        """
        
            The dimension of the MAPDL CDB file.
            
        """
        return None

    @property
    def LengthUnit(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.LengthUnit]:
        """
        
            The length unit of the MAPDL CDB file.
            
        """
        return None

    @property
    def Format(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.ExternalData.ImportFormat]:
        """
        
            Gets the existing corresponding format.
            
        """
        return None


