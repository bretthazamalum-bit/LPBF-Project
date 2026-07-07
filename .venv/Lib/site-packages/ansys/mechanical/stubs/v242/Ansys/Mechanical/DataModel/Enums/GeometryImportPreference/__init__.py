"""GeometryImportPreference module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AnalysisType(Enum):
    """
    
            Specifies the type of analysis to target during import.
            
    """

    Type3D = 0
    Type2D = 1

class ComparePartsOnUpdate(Enum):
    """
    
            Specifies how to enable mesh preservation on parts during update.
            
    """

    None_ = 0
    Associatively = 1
    NonAssociatively = 2

class ComparePartsTolerance(Enum):
    """
    
            Specifies the tolerance to use when comparing parts. This provides comparison robustness due
             to differences/errors in floating-point number representations. Actual geometric
             modifications are not intended to be captured via tolerance loosening.
             
    """

    Tight = 2
    Normal = 1
    Loose = 0

class FacetQuality(Enum):
    """
    
            Used to specify the quality of the facet for the import.
            
    """

    VeryCoarse = 1
    Coarse = 2
    Normal = 3
    Fine = 4
    VeryFine = 5
    Source = 6

class Format(Enum):
    """
    
            Specifies how to interpret the geometry file.
            
    """

    Automatic = 0

class MixedImportResolution(Enum):
    """
    
            Describes how parts of mixed dimension will be treated, i.e., to be imported as components
            of assemblies which have parts of different dimension.
            
    """

    None_ = 0
    Solid = 1
    Surface = 2
    Line = 3
    SolidSurface = 5
    SurfaceLine = 8

class Parameters(Enum):
    """
    
            Defines how parameters in the CAD source are processed.
            
    """

    None_ = 0
    Independent = 1
    All = 3

class StitchSurfacesOnImport(Enum):
    """
    
            Used to specify if and how to join surfaces when imported.
            
    """

    None_ = 0
    Program = 1
    User = 2

