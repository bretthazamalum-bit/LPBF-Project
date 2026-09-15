"""MeshWorkflow module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CheckpointDefinitionType(Enum):
    """
    To select the MeshWorkflow Process Entity Type.
    """

    Disabled = 1
    Enabled = 2

class ControlDataDefinedByType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of the definition for the control data of the specific control.
    """

    ByOutcome = 1
    ByValue = 0

class ControlType(Enum):
    """
    To select the mesh workflow control type.
    """

    ZoneMaterialAssignment = 15
    ZoneThicknessAssignment = 16
    Checkpoint = 3
    PartEnclosure = 7
    HemisphereEnclosure = 9
    IrregularShapeConvexEnclosure = 12
    IrregularShapeHemiConvexEnclosure = 13
    SphericalEnclosure = 8
    CustomNamesEnclosure = 14
    TopologyCreation = 20
    Extrusion = 27
    CustomNamesExtrusion = 28
    HoleFilling = 29
    ImproveSurfaceMeshSecondOrderConversion = 58
    ImproveVolumeMeshAutoNodeMove = 59
    ImproveVolumeMeshSecondOrderConversion = 60
    MaterialPoint = 66
    PartsMerging = 81
    VolumesMerging = 31
    HolePatching = 30
    MeshImport = 4
    ConstantSizeSurfaceMesh = 48
    WrapSpecificSurfaceMesh = 50
    ConstantSizeVolumeMesh = 54
    ConstantSizeWrap = 61
    SizeFieldWrap = 63
    CustomNamesWrap = 64
    MeshExport = 5

class DataTransferType(Enum):
    """
    This enum is referenced in the "Output" tree node and defines how the generated Mesh Workflow data should be transferred back into Mechanical geometry part(s) together with the associated mesh.
    """

    ByTopology = 1
    ByZones = 2
    ProgramControlled = 0

class HemisphereCenterDefinitionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of hemisphere center modality being configured. Based on the type of an hemisphere center modality different rules are applied which define the applicable list of modality data to be used for creating a hemispherical enclosure.
    """

    Centered = 1
    UserDefined = 2

class HemisphereOrientationDefinitionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of hemisphere orientation modality being configured.
    """

    NegativeX = 4
    NegativeY = 5
    NegativeZ = 6
    PositiveX = 1
    PositiveY = 2
    PositiveZ = 3

class MaterialPointDefineByType(Enum):
    """
    This enum is referenced in Material Point controls. It specifies how the material point location is defined.
    """

    CoordinateSystem = 2
    Location = 1

class MaterialPointType(Enum):
    """
    To select the MeshWorkflow Surface Scope Modality Type.
    """

    Exclude = 2
    Include = 1

class OperationType(Enum):
    """
    This enum is referenced in the “Step” tree node and reflects the type of operation being configured. Based on the type of an operation different rules are applied which define the applicable list of controls and outcomes which can be added.
    """

    CreateEnclosure = 7
    CreateTopology = 9
    Extrude = 11
    FillHoles = 12
    ImproveSurfaceMesh = 23
    ImproveVolumeMesh = 24
    ManageZoneProperties = 8
    MergeParts = 33
    MergeVolumes = 14
    PatchHoles = 13
    ImportMesh = 4
    CreateSurfaceMesh = 20
    CreateVolumeMesh = 21
    Wrap = 25
    ExportMesh = 5

class OutcomeType(Enum):
    """
    This enum is referenced in the “Outcome” tree node and reflects the type of outcome being configured. Based on the type of an outcome different rules are applied which define the applicable list of outcome data to be used.
    """

    EnclosureExternalScope = 9
    EnclosureInternalScope = 8
    ExtrusionEndScope = 11
    ExtrusionStartScope = 10
    FaceZoneScope = 14
    FailureInfo = 6
    InternalVolumeZoneScope = 16
    Scope = 4
    VolumeZoneScope = 15

class ScopeDefinedByType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects how a scope is being defined. Based on the type of a scope definition different rules are applied which define the applicable list of scope definitions to be used.
    """

    Outcome = 1
    Value = 0

class ScopeType(Enum):
    """
    To select the MeshWorkflow Process Entity Type.
    """

    Label = 2
    Part = 1
    Zone = 3

class SettingsType(Enum):
    """
    A SettingsType allows the user to add the additional specific Settings type entries to the Steps. The additional entries can be set by the user to automatically define the attributes of different operation Controls.
    """

    Acoustic = 2

class SphereCenterDefinitionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of sphere center modality being configured. Based on the type of an sphere center modality different rules are applied which define the applicable list of modality data to be used for creating a spherical enclosure.
    """

    Centered = 2
    Minimal = 1
    UserDefined = 3

class SurfaceMeshType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of surface mesh being configured.
    """

    Quadrilaterals = 2
    Triangles = 1

class VolumeMeshType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of volume mesh being configured.
    """

    HexCore = 3
    Tetrahedral = 1

class WorkflowType(Enum):
    """
    This enum is referenced in the “Steps” tree node and reflects the type of workflow being configured. Based on the type of workflow different rules are applied which define the applicable order and type of operations which can be added.
    """

    BEMAcoustics = 8
    FEMAcousticsExternal = 4
    FEMAcousticsFSI = 6
    FEMAcousticsFSICutPlane = 7
    FEMAcousticsInternal = 5

class WrapperRegionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of wrapper region being configured.
    """

    External = 2
    MaterialPoint = 1

