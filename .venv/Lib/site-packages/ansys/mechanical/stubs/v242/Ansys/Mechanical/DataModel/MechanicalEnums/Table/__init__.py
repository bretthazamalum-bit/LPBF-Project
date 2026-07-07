"""Table module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ImportFormat(Enum):
    """
    
            Specifies how to interpret the variable data source.
            
    """

    Delimited = 1
    FixedWidth = 2

class TableRefreshImportOn(Enum):
    """
    Allows control on when an import should be refreshed.
    """

    BeforeSolve = 1
    None_ = 0

class VariableClassification(Enum):
    """
    
             This enum represents the classification of variables that can be represented by Table
             variables/columns.
            
             A full variable definition requires both a T:Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableType and an
             T:Ansys.Mechanical.DataModel.MechanicalEnums.Table.VariableClassification.
            
             The explicit enum values need to be kept in-sync with the Typescript enumeration of the
             same name in the frontend Angular project.
             
    """

    Independent = 1
    Real = 2
    Real_i = 201
    Real_j = 202
    Real_k = 203

class VariableType(Enum):
    """
    
            An enumeration of the different variable types supported by the tabular data
            T:Ansys.Mechanical.Interfaces.IDataSeries implementation "Ansys.ACT.Automation.Mechanical.Table.Column".
            
    """

    ID = 3
    Pressure = 4
    HeatTransferCoefficient = 5
    Temperature = 7
    ThetaCoordinate = 8
    Time = 9
    XCoordinate = 10
    YCoordinate = 11
    ZCoordinate = 12

