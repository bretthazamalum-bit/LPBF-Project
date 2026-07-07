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

class ControlType(Enum):
    """
    To select the mesh workflow control type.
    """

    ZoneMaterialAssignment = 13
    Checkpoint = 3
    PartEnclosure = 7
    IrregularShapeConvexEnclosure = 11
    SphericalEnclosure = 8
    CustomNamesEnclosure = 12
    TopologyCreation = 16
    Extrusion = 21
    CustomNamesExtrusion = 22
    HoleFilling = 23
    ImproveSurfaceMeshSecondOrderConversion = 48
    ImproveVolumeMeshAutoNodeMove = 49
    ImproveVolumeMeshSecondOrderConversion = 50
    MaterialPoint = 55
    VolumesMerging = 24
    MeshImport = 4
    ConstantSizeSurfaceMesh = 41
    WrapSpecificSurfaceMesh = 43
    ConstantSizeVolumeMesh = 47
    ConstantSizeWrap = 51
    CustomNamesWrap = 53
    MeshExport = 5

class DataTransferType(Enum):
    """
    This enum is referenced in the “Output” tree node and defines how the generated Mesh Workflow data should be transferred back into Mechanical geometry part(s) together with the associated mesh.
    """

    ByTopology = 1
    ByZones = 2
    ProgramControlled = 0

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
    ImproveSurfaceMesh = 21
    ImproveVolumeMesh = 22
    ManageZoneProperties = 8
    MergeVolumes = 13
    ImportMesh = 4
    CreateSurfaceMesh = 19
    CreateVolumeMesh = 20
    Wrap = 23
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
    Scope = 4
    VolumeZoneScope = 15

class ScopeDefinedByType(Enum):
    """
    This enum is referenced in the “Control” tree node and reflects how a scope is being defined. Based on the type of a scope definition different rules are applied which define the applicable list of scope definitions to be used.
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

class SphereCenterDefinitionType(Enum):
    """
    This enum is referenced in the “Control” tree node and reflects the type of sphere center modality being configured. Based on the type of an sphere center modality different rules are applied which define the applicable list of modality data to be used for creating a spherical enclosure.
    """

    Centered = 2
    Minimal = 1
    UserDefined = 3

class SurfaceMeshType(Enum):
    """
    This enum is referenced in the “Control” tree node and reflects the type of surface mesh being configured.
    """

    Quadrilaterals = 2
    Triangles = 1

class VolumeMeshType(Enum):
    """
    This enum is referenced in the “Control” tree node and reflects the type of volume mesh being configured.
    """

    HexCore = 3
    Tetrahedral = 1

class WorkflowType(Enum):
    """
    This enum is referenced in the “Steps” tree node and reflects the type of workflow being configured. Based on the type of workflow different rules are applied which define the applicable order and type of operations which can be added.
    """

    BEMAcoustics = 6
    FEMAcousticsExternal = 4
    FEMAcousticsInternal = 5

class WrapperRegionType(Enum):
    """
    This enum is referenced in the “Control” tree node and reflects the type of wrapper region being configured.
    """

    External = 2
    MaterialPoint = 1

