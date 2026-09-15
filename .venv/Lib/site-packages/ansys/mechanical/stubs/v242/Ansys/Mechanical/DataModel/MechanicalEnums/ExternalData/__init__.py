"""ExternalData module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class LengthUnit(Enum):
    """
    
            Specifies how to interpret the variable data source.
            
    """

    meter = 0
    centimeter = 1
    foot = 2
    inch = 3
    millimeter = 4
    micrometer = 5

class ImportFormat(Enum):
    """
    
            Specifies how to interpret the variable data source.
            
    """

    Delimited = 0
    FixedWidth = 1
    MAPDL = 2
    AXDT = 3
    ECAD = 4
    ICEPAK = 5
    CGNS = 6
    H5 = 7

class VariableType(Enum):
    """
    
            An enumeration of the different variable types supported by the tabular data
            T:Ansys.Mechanical.Interfaces.IDataSeries implementation "Ansys.ACT.Automation.Mechanical.Table.Column".
            
    """

    XCoordinate = 0
    YCoordinate = 1
    ZCoordinate = 2
    NodeId = 3
    ElementId = 4
    Temperature = 5
    Pressure = 6
    HeatTransferCoefficient = 7
    HeatFlux = 8
    HeatGeneration = 9
    HeatRate = 10
    Thickness = 11
    Displacement = 12
    Force = 13
    Velocity = 14
    Stress = 15
    Strain = 16
    BodyForceDensity = 17
    OrientationAngle = 18
    Volume = 19
    UserField = 20

