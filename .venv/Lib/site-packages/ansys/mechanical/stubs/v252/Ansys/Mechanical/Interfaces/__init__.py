"""Interfaces module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class IDataSeries(object):

    @property
    def DataType(self) -> typing.Optional[type]:
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the name of the data series.
            
        """
        return None

    @property
    def QuantityName(self) -> typing.Optional[str]:
        """
        
            Gets or sets the quantity name of the data series, e.g., “Length”, “Pressure”, or “Heat Flux”.
            
        """
        return None

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        
            Gets or sets a string representation of the data series units, e.g., “m”,
            “kg m^-1 s^-2”, or “kg m^2 s^-3”.
            
        """
        return None

    @property
    def Values(self) -> typing.Optional[typing.Collection]:
        """
        
            Explicitly gets or sets the values of the data series.
            
        """
        return None


class IDataTable(object):

    @property
    def ColumnNames(self) -> typing.Optional[tuple[str]]:
        return None

    @property
    def Columns(self) -> typing.Optional[typing.List[Ansys.Mechanical.Interfaces.IDataSeries]]:
        """
        
            Explicitly get the columns of the data table.
            
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of columns in the table.
            
        """
        return None

    @property
    def IsFixedColumnCount(self) -> typing.Optional[bool]:
        """
        
            Get whether additional columns can be added or removed from the contained T:Ansys.Mechanical.Interfaces.IDataSeries.
            
        """
        return None

    @property
    def IsFixedRowCount(self) -> typing.Optional[bool]:
        """
        
            Get whether additional rows can be added or removed from the contained
            T:Ansys.Mechanical.Interfaces.IDataSeries.
            
        """
        return None

    @property
    def IsReadOnly(self) -> typing.Optional[bool]:
        """
        
            Gets whether the data table is read-only.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Interfaces.IDataSeries]:
        """
        Item property.
        """
        return None

    @property
    def Metadata(self) -> typing.Optional[dict[str,typing.Any]]:
        """
        
            Gets or set a dictionary with additional information that may be useful to understanding
            the context of data in the table.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Get or set the name of the table.
            
        """
        return None

    @property
    def RowCount(self) -> typing.Optional[int]:
        return None

    def Add(self, dataSeries: Ansys.Mechanical.Interfaces.IDataSeries) -> None:
        """
        
            Add a new column to the data table.
            
        """
        pass

    def Clear(self) -> None:
        """
        
            Drops all columns from the data table.
            
        """
        pass

    def Contains(self, name: str) -> bool:
        """
        
            Returns whether the data table contains a column with the specified name.
            
        """
        pass

    def GetRow(self, rowIndex: int) -> typing.Iterable:
        pass

    def Insert(self, columnIndex: int, dataSeries: Ansys.Mechanical.Interfaces.IDataSeries) -> None:
        """
        
            Insert a column at the specified index.
            
        """
        pass

    def Remove(self, key: typing.Any) -> None:
        """
        
            Removes the specified column. If the specifier of the column to remove is an T:System.Int32, it will
            be interpreted as an index. If the specifier of the column to remove is a T:System.String, it will
            be interpreted as a column name.
            
        """
        pass

    def TryInsertRow(self, rowIndex: int, values: typing.Iterable) -> bool:
        """
        
            Try to insert the values at the specified row index.
            
        """
        pass

    def TryRemoveRow(self, rowIndex: int) -> bool:
        """
        
            Try to remove the specified row.
            
        """
        pass


class IReadOnlyDataSeries(object):

    @property
    def Item(self) -> typing.Optional[typing.Any]:
        """
        Item property.
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        
            Gets the number of data points.
            
        """
        return None

    @property
    def DataType(self) -> typing.Optional[type]:
        """
        
            Gets the type stored by the data series.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets the name of the data series.
            
        """
        return None

    @property
    def QuantityName(self) -> typing.Optional[str]:
        """
        
            Gets the quantity name of the data series, e.g., “Length”, “Pressure”, or “Heat Flux”.
            
        """
        return None

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        
            Gets the string representation of the data series units, e.g., “m”, “kg m^-1 s^-2”,
            or “kg m^2 s^-3”.
            
        """
        return None

    @property
    def Values(self) -> typing.Optional[typing.Collection]:
        """
        
            Explicitly get the values of the data series.
            
        """
        return None


class IReadOnlyDataTable(object):

    @property
    def ColumnNames(self) -> typing.Optional[tuple[str]]:
        """
        
            Gets a list of the column names.
            
        """
        return None

    @property
    def Columns(self) -> typing.Optional[tuple[Ansys.Mechanical.Interfaces.IReadOnlyDataSeries]]:
        """
        
            Explicitly get the columns of the table.
            
        """
        return None

    @property
    def Item(self) -> typing.Optional[Ansys.Mechanical.Interfaces.IReadOnlyDataSeries]:
        """
        Item property.
        """
        return None

    @property
    def Metadata(self) -> typing.Optional[dict[str,typing.Any]]:
        """
        
            Gets a dictionary with additional information that may be useful to understanding the
            context of data in the table.
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Get the name of the table.
            
        """
        return None

    @property
    def RowCount(self) -> typing.Optional[int]:
        """
        
            Gets the maximum number of data points (rows) among all columns in the table
            
        """
        return None

    def GetRow(self, rowIndex: int) -> typing.Iterable:
        """
        
            Returns an enumerable to iterate over the values in a row.
            
        """
        pass


class ITable(object):
    """
    
            Exposes a table, which is a two-dimensional tabular data structure with labeled columns.
            The columns are usually instances of IVariable but can be any sort of array
            
    """

    @property
    def Independents(self) -> typing.Optional[dict[str,typing.Iterable]]:
        """
        The portion of the table corresponding to independent variables.
        """
        return None

    @property
    def Dependents(self) -> typing.Optional[dict[str,typing.Iterable]]:
        """
        The portion of the table corresponding to dependent variables.
        """
        return None


class IVariable(object):
    """
    Exposes a variable, which is a one dimensional array of real numbers with a unit.
    """

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        The unit of the variable.  For example, this could be "mm".
        """
        return None

    @property
    def QuantityName(self) -> typing.Optional[str]:
        """
        The quantity name of the variable.  For example, this could be "Length".
        """
        return None


