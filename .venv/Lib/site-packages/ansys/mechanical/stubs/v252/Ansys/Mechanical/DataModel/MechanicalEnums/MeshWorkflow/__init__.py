"""MeshWorkflow module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ControlDataDefinedByType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of the definition for the control data of the specific control.
    """

    BySettings = 1
    ByValue = 0

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

class ControlType(Enum):
    """
    To select the mesh workflow control type.
    """

    AddPrescribedPoints = 86
    AddPrescribedPointsFromFile = 87
    ZoneMaterialAssignment = 14
    ZoneThicknessAssignment = 15
    Checkpoint = 3
    PartEnclosure = 7
    HemisphereEnclosure = 9
    IrregularShapeConvexEnclosure = 11
    IrregularShapeHemiConvexEnclosure = 12
    SphericalEnclosure = 8
    CustomNamesEnclosure = 13
    TopologyCreation = 19
    TopologyDeletion = 20
    Extrusion = 27
    CustomNamesExtrusion = 28
    HoleFilling = 29
    ImproveSurfaceMeshSecondOrderConversion = 79
    ImproveSurfaceMeshProjectionOnGeometry = 81
    ImproveSurfaceMeshQuadsToTrianglesSplitting = 80
    ImproveVolumeMeshAutoNodeMove = 83
    ImproveVolumeMeshSecondOrderConversion = 84
    MaterialPoint = 94
    MergeNodes = 133
    PartsMerging = 117
    VolumesMerging = 31
    MeshReplication = 85
    TopologyProtectionMultiZoneMesher = 78
    ConstantSizeMultiZoneVolumeMesher = 72
    SizeFieldMultiZoneVolumeMesher = 73
    NumberOfDivisionsOnEdges = 101
    HolePatching = 30
    MeshImport = 4
    StackableBodiesDetection = 134
    UserNamesStackableBodiesDetection = 135
    StackerVolumeFlattening = 98
    UserNamesStackerVolumeFlattening = 99
    StackerVolumeMeshing = 100
    StackerDiagnostics = 136
    QuadMeshAdvancedOptions = 62
    ConstantSizeSurfaceMesh = 59
    QuadBoundaryLayer = 63
    WrapSpecificSurfaceMesh = 61
    ConstantSizeVolumeMesh = 66
    VolumetricSizeFieldBOI = 26
    VolumetricSizeFieldCurvature = 24
    VolumetricSizeFieldLoad = 22
    VolumetricSizeFieldMaxSize = 23
    VolumetricSizeFieldProximity = 25
    UserNamesVolumetricSizeField = 21
    ConstantSizeWrap = 88
    SizeFieldWrap = 91
    CustomNamesWrap = 92
    MeshExport = 5

class DataTransferType(Enum):
    """
    This enum is referenced in the "Output" tree node and defines how the generated Mesh Workflow data should be transferred back into Mechanical geometry part(s) together with the associated mesh.
    """

    ByTopology = 1
    ByZones = 2
    ProgramControlled = 0

class DecompositionType(Enum):
    """
    This enum is referenced in MultiZone mesher controls. It specifies the decomposition type used to generate the MultiZone mesh.
    """

    AxisSweep = 6
    ProgramControlled = 7
    Standard = 2

class DefeatureToleranceDefineBy(Enum):
    """
    This enum is referenced in MultiZone mesher controls. It specifies how the MultiZone Defeature Tolerance is defined.
    """

    ProgramControlled = 1
    UserDefined = 2

class FreeFaceMeshType(Enum):
    """
    This enum is referenced in MultiZone mesher controls. It specifies the element type for the MultiZone free face mesh.
    """

    AllQuads = 4
    AllTris = 3
    SomeTris = 2

class FreeVolumeMeshType(Enum):
    """
    This enum is referenced in MultiZone mesher controls. It specifies how free blocks are treated by the MultiZone meshing algorithm.
    """

    NotAllowed = 1
    TetraPyramid = 2

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

class MergeNodesToleranceType(Enum):
    """
    This enum specifies the merge nodes tolerance type to be used when executing Merge Nodes operation.
    """

    Absolute = 1
    Relative = 2

class MeshFlowControl(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the mesh flow control being configured.
    """

    Global = 2
    None_ = 1

class OperationType(Enum):
    """
    This enum is referenced in the “Step” tree node and reflects the type of operation being configured. Based on the type of an operation different rules are applied which define the applicable list of controls and outcomes which can be added.
    """

    AddPrescribedPoints = 33
    CreateEnclosure = 7
    CreateTopology = 9
    CreateVolumetricSizeField = 11
    DeleteTopology = 10
    DetectStackableBodies = 38
    Extrude = 12
    FillHoles = 13
    ImproveSurfaceMesh = 30
    ImproveVolumeMesh = 31
    ManageZoneProperties = 8
    MergeNodes = 50
    MergeParts = 46
    MergeVolumes = 15
    ReplicateMesh = 32
    MultiZoneVolumeMesher = 29
    PatchHoles = 14
    ImportMesh = 4
    StackerFlattenVolume = 36
    StackerDiagnostics = 39
    StackerMeshVolume = 37
    CreateSurfaceMesh = 26
    CreateVolumeMesh = 27
    Wrap = 34
    ExportMesh = 5

class OutcomeType(Enum):
    """
    This enum is referenced in the “Outcome” tree node and reflects the type of outcome being configured. Based on the type of an outcome different rules are applied which define the applicable list of outcome data to be used.
    """

    CSVProcessingInfo = 27
    EnclosureExternalScope = 14
    EnclosureInternalScope = 13
    ExtrusionEndScope = 16
    ExtrusionStartScope = 15
    FaceZoneScope = 19
    FailureInfo = 11
    InternalVolumeZoneScope = 21
    MultiZoneVolumeMesherDiagnostics = 41
    NonStackableBodies = 25
    Scope = 4
    SizeFieldName = 5
    StackerBaseEdge = 23
    StackerBaseFace = 22
    StackerDiagnostics = 29
    StackerSeedFace = 24
    VolumeZoneScope = 20
    WarningInfo = 26

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
    Global = 5
    Stacker = 4

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

class TriangleCountReductionMode(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the mode of triangle count reduction during surface meshing.
    """

    Aggressive = 3
    Conservative = 2
    None_ = 1

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
    Stacker = 11

class WrapperRegionType(Enum):
    """
    This enum is referenced in the 'Control' tree node and reflects the type of wrapper region being configured.
    """

    External = 2
    MaterialPoint = 1

