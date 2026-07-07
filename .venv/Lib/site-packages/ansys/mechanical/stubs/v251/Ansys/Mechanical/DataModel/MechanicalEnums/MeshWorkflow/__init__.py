"""MeshWorkflow module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class MaterialPointDefineByType(Enum):
    """
    This enum is referenced in Material Point controls. It specifies how the material point location is defined.
    """

    Location = 1
    CoordinateSystem = 2

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

    AddPrescribedPoints = 75
    AddPrescribedPointsFromFile = 76
    ZoneMaterialAssignment = 13
    ZoneThicknessAssignment = 14
    Checkpoint = 3
    PartEnclosure = 7
    HemisphereEnclosure = 9
    IrregularShapeConvexEnclosure = 10
    IrregularShapeHemiConvexEnclosure = 11
    SphericalEnclosure = 8
    CustomNamesEnclosure = 12
    TopologyCreation = 18
    TopologyDeletion = 19
    Extrusion = 26
    CustomNamesExtrusion = 27
    HoleFilling = 28
    ImproveSurfaceMeshSecondOrderConversion = 69
    ImproveSurfaceMeshQuadsToTrianglesSplitting = 70
    ImproveVolumeMeshAutoNodeMove = 72
    ImproveVolumeMeshSecondOrderConversion = 73
    MaterialPoint = 83
    PartsMerging = 100
    VolumesMerging = 30
    HolePatching = 29
    MeshImport = 4
    ConstantSizeSurfaceMesh = 51
    WrapSpecificSurfaceMesh = 53
    ConstantSizeVolumeMesh = 58
    VolumetricSizeFieldBOI = 25
    VolumetricSizeFieldCurvature = 23
    VolumetricSizeFieldLoad = 21
    VolumetricSizeFieldMaxSize = 22
    VolumetricSizeFieldProximity = 24
    UserNamesVolumetricSizeField = 20
    ConstantSizeWrap = 77
    SizeFieldWrap = 80
    CustomNamesWrap = 81
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

    AddPrescribedPoints = 32
    CreateEnclosure = 7
    CreateTopology = 9
    CreateVolumetricSizeField = 11
    DeleteTopology = 10
    Extrude = 12
    FillHoles = 13
    ImproveSurfaceMesh = 29
    ImproveVolumeMesh = 30
    ManageZoneProperties = 8
    MergeParts = 45
    MergeVolumes = 15
    PatchHoles = 14
    ImportMesh = 4
    CreateSurfaceMesh = 25
    CreateVolumeMesh = 26
    Wrap = 33
    ExportMesh = 5

class OutcomeType(Enum):
    """
    This enum is referenced in the “Outcome” tree node and reflects the type of outcome being configured. Based on the type of an outcome different rules are applied which define the applicable list of outcome data to be used.
    """

    EnclosureExternalScope = 13
    EnclosureInternalScope = 12
    ExtrusionEndScope = 15
    ExtrusionStartScope = 14
    FaceZoneScope = 18
    FailureInfo = 10
    InternalVolumeZoneScope = 20
    Scope = 4
    SizeFieldName = 5
    VolumeZoneScope = 19

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
    MaterialPoint = 4
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

    BEMAcoustics = 9
    FEMAcousticsExternal = 4
    FEMAcousticsFSI = 6
    FEMAcousticsFSISingleBody = 7
    FEMAcousticsFSISingleBodyCutPlane = 8
    FEMAcousticsInternal = 5

class WrapperRegionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of wrapper region being configured.
    """

    External = 2
    MaterialPoint = 1

