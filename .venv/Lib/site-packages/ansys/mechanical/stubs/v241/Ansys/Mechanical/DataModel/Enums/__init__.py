"""Enums module."""
from __future__ import annotations
from enum import Enum
import typing
if typing.TYPE_CHECKING:
    import Ansys
import ansys.mechanical.stubs.v241.Ansys.Mechanical.DataModel.Enums.ExternalModel as ExternalModel
import ansys.mechanical.stubs.v241.Ansys.Mechanical.DataModel.Enums.GeometryImportPreference as GeometryImportPreference


class BeamBeamContactDetectionType(Enum):
    """
    Specifies the BeamBeamContactDetectionType.
    """

    External8Segments = 2
    External4Segments = 1
    External1Segment = 0
    InternalPipe = 3

class WaterfallDisplaySelectionMode(Enum):
    """
    Specifies the Selection Mode Type.
    """

    RPM = 0
    Order = 1
    NotApplicable = 2

class DBWeightingType(Enum):
    """
    Specifies the dB Weighting Type.
    """

    pass

class GraphicsViewportsExportBorderStyle(Enum):
    """
    
            Specifies which borders to add, if any, to the images produced by MechanicalGraphicsWrapper.ExportViewports.
            Border style enum values can be combined via bitwise-or ( | ).
            
    """

    None_ = 0
    Interior = 1
    Exterior = 2

class KrigingPolynomType(Enum):
    """
    
            Represents the various types of Polynomial which combines with Kriging model.
            
    """

    PolyNone = 0
    PolyConst = 1
    PolyLinear = 2
    PolyPureQuad = 3
    PolyCrossQuad = 4

class KrigingCorrFuncType(Enum):

    CorrFuncNone = 0
    CorrFuncExp = 1
    CorrFuncGauss = 2
    CorrFuncLin = 3
    CorrFuncSpherical = 4
    CorrFuncCubic = 5
    CorrFuncMultiQuadratic = 6
    CorrFuncThinPlateSpine = 7

class HarmonicVariationalTechnology(Enum):
    """
    Specifies the HarmonicVariationalTechnology.
    """

    No = 3
    ProgramControlled = 1
    Yes = 2

class AMCooldownTimeType(Enum):
    """
    Specifies the AMCooldownTimeType.
    """

    ProgramControlled = 0
    UserSpecified = 1

class AMReferenceTemperatureType(Enum):
    """
    Specifies the AMReferenceTemperatureType.
    """

    ProgramControlled = 0
    UserSpecified = 1

class AMRelaxationTemperatureType(Enum):
    """
    Specifies the AMRelaxationTemperatureType.
    """

    None_ = 0
    UserSpecified = 1

class AMLayerHeightType(Enum):
    """
    Specifies the AMLayerHeightType.
    """

    ProgramControlled = 0
    Manual = 1

class AMMultiplierEntryType(Enum):
    """
    Specifies the AMSupportSubtype.
    """

    Manual = 0
    All = 1

class AMProcessStepType(Enum):
    """
    Specifies the AMProcessStepType.
    """

    BuildStep = 0
    CooldownStep = 1
    BaseRemovalStep = 2
    SupportRemovalStep = 3
    UserStep = 4
    HeatTreatmentStep = 5
    BaseUnboltStep = 6

class AMThermalStrainMaterialModel(Enum):
    """
    Specifies the AMThermalStrainMaterialModel.
    """

    Al357 = 3
    AlSi10Mg = 4
    CoCr = 5
    Inconel625 = 6
    Inconel718 = 7
    SS17_4 = 1
    SS316L = 2
    Ti6Al4V = 8
    Undefined = 0

class ApplicationType(Enum):
    """
    
            Specifies the Application type.
            
    """

    Mechanical = 0
    MAPDL = 1

class BeamToolStressResultType(Enum):
    """
    Specifies the BeamToolStressResultType.
    """

    DirectStress = 0
    MinimumBendingStress = 1
    MaximumBendingStress = 2
    MinimumCombinedStress = 3
    MaximumCombinedStress = 4

class BodyType(Enum):
    """
    Specifies the BodyType.
    """

    Solid = 8
    Surface = 16
    Line = 17

class BoltResultType(Enum):
    """
    Specifies the BoltResultType.
    """

    Adjustment = 0
    WorkingLoad = 1

class BoundaryConditionSelectionType(Enum):
    """
    Specifies the BoundaryConditionSelection.
    """

    None_ = 0
    AllFixedSupports = 1

class CameraAxisType(Enum):
    """
    
            Specifies the Axis type.
            
    """

    ScreenX = 0
    ScreenY = 1
    ScreenZ = 2
    GlobalX = 3
    GlobalY = 4
    GlobalZ = 5

class CampbellDiagramRotationalVelocitySelectionType(Enum):
    """
    Specifies the Campbell Diagram Rotational Velocity Selection Type.
    """

    None_ = 0

class ChartAxisScaleType(Enum):
    """
    Specifies the Chart Axis Scale Type.
    """

    Linear = 0
    LogX = 1
    LogY = 2
    LogLog = 3

class ChartDimensions(Enum):
    """
    Specifies the Chart Viewing Style.
    """

    ThreeDimensional = 0
    TwoDimensional = 1

class ChartResultType(Enum):
    """
    Specifies the Chart Result Type.
    """

    ContactResultPressure = 0
    ContactResultPenetration = 1
    ContactResultGap = 2
    ContactResultFrictionalStress = 3
    ContactResultSlidingDistance = 4
    ContactNumElementInStickingDefaultName = 5
    ContactNumElementInContact = 6
    ContactCNOS = 7
    ContactElasticSlip = 8
    ContactNormalStiffness = 9
    ContactMaxTangentialStiffness = 10
    ContactMinTangentialStiffness = 11
    ContactResultContactingArea = 12
    ContactMaxDampingPressure = 13
    ContactResultFluidPressure = 14
    MinGeometricSlidingDistance = 15
    MaxGeometricSlidingDistance = 16

class ComparePartsOnUpdateType(Enum):
    """
    Specifies the ComparePartsOnUpdateType.
    """

    No = 0
    Associatively = 1
    NonAssociatively = 2

class ComparePartsToleranceType(Enum):
    """
    Specifies the ComparePartsTolerance Type.
    """

    Loose = 0
    Normal = 1
    Tight = 2

class CondensedPartInterfaceType(Enum):

    Unknown = 0
    General = 1
    Remote = 2
    All = 3

class ContactResultType(Enum):
    """
    Specifies the ContactResultType.
    """

    Pressure = 68
    Penetration = 69
    Gap = 70
    FrictionalStress = 71
    SlidingDistance = 72
    Status = 73
    FluidPressure = 265

class CrackMeshMethod(Enum):
    """
    Specifies the CrackMeshMethod.
    """

    HexDominant = 1
    Tetrahedrons = 2

class CylindricalFacesOption(Enum):
    """
    Specifies the CylindricalFacesOption.
    """

    Include = 0
    Exclude = 1
    Only = 2

class DamageResultType(Enum):
    """
    Specifies the DamageResultType.
    """

    MullinsDamageVariable = 274
    MullinsMaximumPreviousStrainEnergy = 275
    MaximumFailureCriteria = 276
    FiberTensileFailureCriterion = 277
    FiberCompressiveFailureCriterion = 278
    MatrixTensileFailureCriterion = 279
    MatrixCompressiveFailureCriterion = 280
    DamageStatus = 281
    FiberTensileDamageVariable = 282
    FiberCompressiveDamageVariable = 283
    MatrixTensileDamageVariable = 284
    MatrixCompressiveDamageVariable = 285
    ShearDamageVariable = 286
    EnergyDissipatedPerUnitVolume = 287

class DataModelObjectCategory(Enum):
    """
    Specifies the category of the F:Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory.DataModelObject.
    """

    EarthGravity = 0
    Acceleration = 1
    Image = 2
    Alert = 3
    AMBuildSettings = 4
    AMProcess = 5
    AMSupport = 6
    PredefinedAMSupport = 7
    GeneratedAMSupport = 8
    STLAMSupport = 9
    AMSupportGroup = 10
    AnalysisPly = 11
    AnalysisSettings = 12
    ANSYSAnalysisSettings = 13
    TopoOptAnalysisSettings = 14
    Solution = 15
    Beam = 16
    EndRelease = 17
    BeamTool = 18
    Bearing = 19
    Part = 20
    BodyInteraction = 21
    BodyInteractions = 22
    BoltTool = 23
    Chart = 24
    CommandSnippet = 25
    Comment = 26
    NamedSelection = 27
    NamedSelections = 28
    CondensedGeometry = 29
    CondensedPartBase = 30
    CondensedPart = 31
    ImportedCondensedPart = 32
    CondensedPartInfoTool = 33
    ConnectionGroup = 34
    NodeMergeGroup = 35
    MeshConnectionGroup = 36
    ContactMatchGroup = 37
    ConstraintEquation = 38
    ConstructionGeometry = 39
    ConstructionLine = 40
    ContactDataTable = 41
    Connections = 42
    ContactSolutionInformation = 43
    ContactRegion = 44
    ContactTool = 45
    PreContactTool = 46
    PostContactTool = 47
    Convergence = 48
    CoordinateSystem = 49
    CoordinateSystems = 50
    Coupling = 51
    GenericCrack = 52
    PreMeshedCrack = 53
    SemiEllipticalCrack = 54
    ArbitraryCrack = 55
    CrossSection = 56
    CircularCrossSection = 57
    HatCrossSection = 58
    HollowRectangularCrossSection = 59
    UserDefinedCrossSection = 60
    RectangularCrossSection = 61
    ChannelCrossSection = 62
    CircularTubeCrossSection = 63
    ZCrossSection = 64
    LCrossSection = 65
    ICrossSection = 66
    TCrossSection = 67
    CrossSections = 68
    UserDefinedResult = 69
    GenericDelamination = 70
    InterfaceDelamination = 71
    ContactDebonding = 72
    SMARTCrackGrowth = 73
    ElementControls = 74
    ElementBirthAndDeath = 75
    ContactStepControl = 76
    ElementOrientation = 77
    Analysis = 78
    ExpansionSettings = 79
    ExternalEnhancedModel = 80
    ImportedLayeredSection = 81
    ImportedPlies = 82
    ImportedLoad = 83
    ImportedVelocity = 84
    ImportedCutBoundaryRemoteConstraint = 85
    ImportedTrace = 86
    ImportedConvection = 87
    ImportedSurfaceForceDensity = 88
    ImportedBodyForceDensity = 89
    ImportedBodyTemperature = 90
    ImportedTemperature = 91
    ImportedDisplacement = 92
    ImportedCutBoundaryRemoteForce = 93
    ImportedLoadGroup = 94
    ExternalModelDataColl = 95
    ImportedCoordinateSystems = 96
    ImportedBoltPretensions = 97
    ImportedPremeshedBoltPretensions = 98
    ImportedShellThicknesses = 99
    ImportedStresses = 100
    ImportedElementOrientations = 101
    ImportedPointMasses = 102
    ImportedNodalOrientations = 103
    ImportedRigidRemoteConnectors = 104
    ImportedConstraintEquations = 105
    ImportedFlexibleRemoteConnectors = 106
    ImportedSpringConnectors = 107
    ImportedContacts = 108
    FatigueTool = 109
    FeatureDetection = 110
    Figure = 111
    Fracture = 112
    FractureTool = 113
    GeneralAxisymmetric = 114
    GeneralizedPlaneStrain = 115
    GeometryFileContainer = 116
    Smoothing = 117
    STL = 118
    InitialConditions = 119
    InitialCondition = 120
    Joint = 121
    JointLoad = 122
    GenericBoundaryCondition = 123
    FixedSupport = 124
    FixedRotation = 125
    RemoteDisplacement = 126
    CylindricalSupport = 127
    RotatingForce = 128
    MagneticFluxParallel = 129
    Voltage = 130
    Current = 131
    Displacement = 132
    Pressure = 133
    BearingLoad = 134
    Temperature = 135
    FrictionlessSupport = 136
    PerfectlyInsulated = 137
    MassFlowRate = 138
    RemoteForce = 139
    LinePressure = 140
    SimplySupported = 141
    ElasticSupport = 142
    CompressionOnlySupport = 143
    Velocity = 144
    PipePressure = 145
    HeatFlow = 146
    PipeTemperature = 147
    NodalForce = 148
    NodalDisplacement = 149
    NodalPressure = 150
    NodalRotation = 151
    HydrostaticPressure = 152
    EMTransducer = 153
    ThermalCondition = 154
    AcousticPressure = 155
    AcousticImpedanceBoundary = 156
    HeatFlux = 157
    AcousticAbsorptionSurface = 158
    AcousticRadiationBoundary = 159
    AcousticAbsorptionElement = 160
    AcousticFreeSurface = 161
    AcousticImpedanceSheet = 162
    AcousticStaticPressure = 163
    AcousticPort = 164
    AcousticThermoViscousBLIBoundary = 165
    AcousticRigidWall = 166
    AcousticMassSource = 167
    InternalHeatGeneration = 168
    AcousticSurfaceVelocity = 169
    AcousticFarFieldRadationSurface = 170
    AcousticTransferAdmittanceMatrix = 171
    AcousticDiffuseSoundField = 172
    AcousticIncidentWaveSource = 173
    AcousticPortInDuct = 174
    AcousticTemperature = 175
    AcousticSymmetryPlane = 176
    FluidSolidInterface = 177
    AcousticLowReducedFrequency = 178
    Convection = 179
    BodyControl = 180
    ImpedanceBoundary = 181
    DetonationPoint = 182
    ElectricCharge = 183
    SurfaceChargeDensity = 184
    VolumeChargeDensity = 185
    LimitBoundary = 186
    Force = 187
    Radiation = 188
    Moment = 189
    LoadGroup = 190
    MaterialAssignment = 191
    Material = 192
    Materials = 193
    MaterialPlot = 194
    MeshConnectionBase = 195
    MeshConnection = 196
    NodeMerge = 197
    ContactMatch = 198
    MeshEdit = 199
    MeshControl = 200
    Sizing = 201
    AutomaticMethod = 202
    Refinement = 203
    FaceMeshing = 204
    Pinch = 205
    Inflation = 206
    MatchControl = 207
    ContactSizing = 208
    Relevance = 209
    Mesh = 210
    NumberingControl = 211
    MeshNumbering = 212
    Model = 213
    NodalOrientation = 214
    NodeMove = 215
    NonlinearAdaptiveRegion = 216
    OptimizationRegion = 217
    ExclusionRegion = 218
    PartTransform = 219
    PartTransformGroup = 220
    Path = 221
    PhysicsRegion = 222
    PipeIdealization = 223
    CoupledPhysicsHeatingObjects = 224
    PlasticHeating = 225
    ViscoelasticHeating = 226
    GenericPointMass = 227
    PointMass = 228
    DistributedMass = 229
    ThermalPointMass = 230
    BoltPretension = 231
    ResultProbe = 232
    VelocityProbe = 233
    SpringProbe = 234
    RadiationProbe = 235
    TemperatureProbe = 236
    HeatFluxProbe = 237
    ReactionProbe = 238
    ElectricVoltageProbe = 239
    CurrentDensityProbe = 240
    EmagReactionProbe = 241
    BearingProbe = 242
    ElectricFieldProbe = 243
    ForceReaction = 244
    MagneticFluxProbe = 245
    BeamProbe = 246
    EnergyProbe = 247
    BoltPretensionProbe = 248
    AngularAccelerationProbe = 249
    AngularVelocityProbe = 250
    GeneralizedPlaneStrainProbe = 251
    JointProbe = 252
    Position = 253
    RotationProbe = 254
    ResponsePSD = 255
    AccelerationProbe = 256
    FractureToolProbe = 257
    FractureCrackExtensionProbe = 258
    FractureTotalNumberOfCyclesProbe = 259
    FractureEquivalentSIFSRangeProbe = 260
    FractureJINTProbe = 261
    FractureSIFSProbe = 262
    VolumeProbe = 263
    JouleHeatProbe = 264
    ForceSummationProbe = 265
    FluxDensityProbe = 266
    TorqueProbe = 267
    FieldIntensityProbe = 268
    MomentReaction = 269
    DeformationProbe = 270
    StrainProbe = 271
    StressProbe = 272
    Project = 273
    Body = 274
    Geometry = 275
    PSDLoad = 276
    PSDAcceleration = 277
    PSDGAcceleration = 278
    PSDVelocity = 279
    PSDDisplacement = 280
    RemotePoint = 281
    RemotePoints = 282
    ResponsePSDTool = 283
    Result = 284
    DirectionalDeformation = 285
    ShearElasticStrain = 286
    TopologyOptimizationResult = 287
    NewtonRaphsonResidualForce = 288
    TopologyDensity = 289
    NewtonRaphsonResidualHeat = 290
    TopologyElementalDensity = 291
    NewtonRaphsonResidualMoment = 292
    NodalEulerXZAngle = 293
    NodalEulerYZAngle = 294
    GasketResult = 295
    NormalGasketTotalClosure = 296
    Volume = 297
    NormalGasketPressure = 298
    ShapeFinder = 299
    MinimumPrincipalElasticStrain = 300
    ShapeFinderElemental = 301
    ShearDamageVariable = 302
    ShearGasketPressure = 303
    ShearGasketTotalClosure = 304
    DirectionalShearMomentDiagram = 305
    MiddlePrincipalElasticStrain = 306
    AccumulatedEquivalentPlasticStrain = 307
    TotalShearMomentDiagram = 308
    ShellBendingStress = 309
    ShellBottomPeakStress = 310
    ShellMembraneStress = 311
    ShellTopPeakStress = 312
    MaximumPrincipalElasticStrain = 313
    StabilizationEnergy = 314
    StressIntensity = 315
    StructuralError = 316
    StructuralStrainEnergy = 317
    ThermalError = 318
    DirectionalThermalStrain = 319
    ThermalStrainEnergy = 320
    TotalAcceleration = 321
    TotalAxialForce = 322
    BoltAdjustment = 323
    TotalTorsionalMoment = 324
    TotalVelocity = 325
    VariableGraph = 326
    VectorAxialForce = 327
    VectorBendingMoment = 328
    VectorDeformation = 329
    VectorHeatFlux = 330
    VectorShearForce = 331
    VectorTorsionalMoment = 332
    EquivalentElasticStrain = 333
    TemperatureResult = 334
    DirectStress = 335
    MinimumBendingStress = 336
    MaximumBendingStress = 337
    MinimumCombinedStress = 338
    MaximumCombinedStress = 339
    FatigueSafetyFactor = 340
    FatigueEquivalentAlternativeStress = 341
    FatigueDamage = 342
    FatigueBiaxialityIndication = 343
    DirectionalVelocity = 344
    FatigueLife = 345
    ContactFluidPressure = 346
    ContactPenetration = 347
    ContactGap = 348
    ContactFrictionalStress = 349
    ContactSlidingDistance = 350
    ContactPressure = 351
    ContactStatus = 352
    StressSafetyMargin = 353
    StressSafetyFactor = 354
    DirectionalAcceleration = 355
    ContactHeatFlux = 356
    StressResult = 357
    StrainResult = 358
    BeamResult = 359
    BeamToolResult = 360
    ElectricPotential = 361
    BoltToolResult = 362
    ContactToolResult = 363
    CoordinateSystemsResult = 364
    DamageResult = 365
    DeformationResult = 366
    ElectricResult = 367
    ElectromagneticResult = 368
    EnergyResult = 369
    FatigueToolResult = 370
    FractureToolResult = 371
    TotalMagneticFluxDensity = 372
    LinearizedStressResult = 373
    ThermalResult = 374
    StressToolResult = 375
    EquivalentStress = 376
    LinearizedMiddlePrincipalStress = 377
    DirectionalStress = 378
    DirectionalThermalHeatFlux = 379
    AcousticResult = 380
    AcousticPressureResult = 381
    AcousticTotalVelocityResult = 382
    TotalDeformation = 383
    TotalMagneticFieldIntensity = 384
    AcousticDirectionalVelocityResult = 385
    AcousticKineticEnergy = 386
    AcousticPotentialEnergy = 387
    AcousticSoundPressureLevel = 388
    AcousticAWeightedSoundPressureLevel = 389
    AcousticFarFieldResult = 390
    AcousticDiffuseSoundTransmissionLoss = 391
    EquivalentRadiatedPower = 392
    EquivalentRadiatedPowerLevel = 393
    AcousticTransmissionLoss = 394
    VectorPrincipalElasticStrain = 395
    AcousticAbsorptionCoefficient = 396
    AcousticReturnLoss = 397
    AcousticFrequencyBandSPL = 398
    AcousticFrequencyBandAWeightedSPL = 399
    EquivalentRadiatedPowerWaterfallDiagram = 400
    EquivalentRadiatedPowerLevelWaterfallDiagram = 401
    AcousticFarFieldSoundPowerLevelWaterfallDiagram = 402
    AcousticFarFieldSPLMicWaterfallDiagram = 403
    VectorPrincipalStress = 404
    LatticeDensity = 405
    LatticeElementalDensity = 406
    DirectionalElectricFluxDensity = 407
    TotalElectricFluxDensity = 408
    NodalTriads = 409
    ElementalTriads = 410
    TotalHeatFlux = 411
    DirectionalHeatFlux = 412
    DirectionalAxialForce = 413
    DirectionalBendingMoment = 414
    LinearizedEquivalentStress = 415
    NormalStress = 416
    NodalEulerXYAngle = 417
    ElementalEulerXYAngle = 418
    TotalBendingMoment = 419
    DirectionalTorsionalMoment = 420
    TotalShearForce = 421
    MullinsDamageVariable = 422
    MullinsMaximumPreviousStrainEnergy = 423
    BendingStressEquivalent = 424
    MembraneStressEquivalent = 425
    EquivalentPlasticStrain = 426
    ShearStress = 427
    ElectricVoltage = 428
    DirectionalElectricFieldIntensity = 429
    TotalCurrentDensity = 430
    JouleHeat = 431
    TotalElectricFieldIntensity = 432
    DirectionalCurrentDensity = 433
    CurrentDensity = 434
    StressRatio = 435
    BendingStressIntensity = 436
    DamageStatus = 437
    MinimumPrincipalStress = 438
    DirectionalAccelerationPSD = 439
    DirectionalAccelerationRS = 440
    DirectionalMagneticFieldIntensity = 441
    DirectionalMagneticFluxDensity = 442
    DirectionalShearForce = 443
    DirectionalVelocityPSD = 444
    DirectionalVelocityRS = 445
    ElasticStrainIntensity = 446
    ElementalEulerXZAngle = 447
    MiddlePrincipalStress = 448
    ElementalEulerYZAngle = 449
    ElementalStrainEnergy = 450
    BoltWorkingLoad = 451
    EnergyDissipatedPerUnitVolume = 452
    EquivalentCreepStrain = 453
    EquivalentCreepStrainRST = 454
    EquivalentElasticStrainRST = 455
    EquivalentPlasticStrainRST = 456
    EquivalentStressPSD = 457
    EquivalentStressRS = 458
    MaximumPrincipalStress = 459
    EquivalentTotalStrain = 460
    FiberCompressiveDamageVariable = 461
    FiberCompressiveFailureCriterion = 462
    FiberTensileDamageVariable = 463
    FiberTensileFailureCriterion = 464
    FluidFlowRate = 465
    FluidHeatConductionRate = 466
    FluidHeatTransportRate = 467
    LinearizedMaximumPrincipalStress = 468
    LinearizedMaximumShearStress = 469
    LinearizedMinimumPrincipalStress = 470
    LinearizedNormalStress = 471
    LinearizedShearStress = 472
    LinearizedStressIntensity = 473
    MagneticCoenergy = 474
    MagneticDirectionalForces = 475
    MagneticError = 476
    MagneticPotential = 477
    MagneticTotalForces = 478
    NormalElasticStrain = 479
    MatrixCompressiveDamageVariable = 480
    MatrixCompressiveFailureCriterion = 481
    MatrixTensileDamageVariable = 482
    MatrixTensileFailureCriterion = 483
    MaximumFailureCriteria = 484
    MaximumPrincipalThermalStrain = 485
    MaximumShearElasticStrain = 486
    MaximumShearStress = 487
    MembraneStressIntensity = 488
    MiddlePrincipalThermalStrain = 489
    ResultChart = 490
    StressFrequencyResponse = 491
    AccelerationFrequencyResponse = 492
    TemperatureTracker = 493
    TotalEnergyTracker = 494
    ContactForceTracker = 495
    ExternalForceTracker = 496
    PressureTracker = 497
    DensityTracker = 498
    MomentumTracker = 499
    TotalMassAverageVelocityTracker = 500
    PlasticWorkTracker = 501
    StressPhaseResponse = 502
    SpringElongationTracker = 503
    SpringVelocityTracker = 504
    SpringElasticForceTracker = 505
    SpringDampingForceTracker = 506
    ForceReactionTracker = 507
    MomentReactionTracker = 508
    PositionTracker = 509
    StiffnessEnergyTracker = 510
    KineticEnergyTracker = 511
    ContactPenetrationTracker = 512
    ElasticStrainPhaseResponse = 513
    ContactGapTracker = 514
    ContactFrictionalStressTracker = 515
    ContactSlidingDistanceTracker = 516
    ContactPressureTracker = 517
    ContactMinimumGeometricSlidingDistanceTracker = 518
    ContactMaximumGeometricSlidingDistanceTracker = 519
    ContactFluidPressureTracker = 520
    ContactMaximumDampingPressureTracker = 521
    ContactingAreaTracker = 522
    ContactChatteringTracker = 523
    ElasticStrainFrequencyResponse = 524
    ContactElasticSlipTracker = 525
    ContactMaximumNormalStiffnessTracker = 526
    ContactMaximumTangentialStiffnessTracker = 527
    ContactResultingPinballTracker = 528
    ContactNumberStickingTracker = 529
    ContactMinimumTangentialStiffnessTracker = 530
    NumberContactingTracker = 531
    FatigueHysteresis = 532
    FatigueRainflowMatrix = 533
    FatigueDamageMatrix = 534
    DeformationPhaseResponse = 535
    FatigueSensitivity = 536
    AcousticPressureFrequencyResponse = 537
    AcousticVelocityFrequencyResponse = 538
    AcousticKineticEnergyFrequencyResponse = 539
    AcousticPotentialEnergyFrequencyResponse = 540
    AcousticSPLFrequencyResponse = 541
    AcousticAWeightedSPLFrequencyResponse = 542
    ContactDepthTracker = 543
    DeformationFrequencyResponse = 544
    ContactClosedPenetrationTracker = 545
    ContactNumberWithLargePenetrationTracker = 546
    ContactTangentialDampingStressTracker = 547
    ContactVolumeLossDueToWearTracker = 548
    ContactStrainEnergyTracker = 549
    ContactFrictionalDissipationEnergyTracker = 550
    ContactStabilizationEnergyTracker = 551
    ContactNumberWithTooMuchSlidingTracker = 552
    ContactTotalForceFromContactPressureXTracker = 553
    ContactTotalForceFromContactPressureYTracker = 554
    VelocityPhaseResponse = 555
    ContactTotalForceFromContactPressureZTracker = 556
    ContactTotalForceFromTangentialStressXTracker = 557
    ContactTotalForceFromTangentialStressYTracker = 558
    ContactTotalForceFromTangentialStressZTracker = 559
    ContactSlidingIndicationTracker = 560
    HourglassEnergyTracker = 561
    ContactEnergyTracker = 562
    ContactMinimumNormalStiffnessTracker = 563
    CampbellDiagram = 564
    ContactHeatFluxTracker = 565
    DirectionalDeformationTracker = 566
    VelocityFrequencyResponse = 567
    DirectionalVelocityTracker = 568
    DirectionalAccelerationTracker = 569
    InternalEnergyTracker = 570
    EffectiveStressTracker = 571
    EffectiveStrainTracker = 572
    ContactPairForceConvergenceNormTracker = 573
    ContactMaxTangentialFluidPressureTracker = 574
    ForceReactionFrequencyResponse = 575
    AccelerationPhaseResponse = 576
    FrequencyResponseResultChart = 577
    ResultTable = 578
    Inductance = 579
    FluxLinkage = 580
    RotationBoundaryCondition = 581
    RotationalVelocity = 582
    RotationalAcceleration = 583
    RSLoad = 584
    RSAcceleration = 585
    RSVelocity = 586
    RSDisplacement = 587
    Solid = 588
    SolutionCombination = 589
    SolutionInformation = 590
    Spring = 591
    StressTool = 592
    Surface = 593
    SurfaceCoating = 594
    SymmetryGeneral = 595
    PeriodicRegion = 596
    CyclicRegion = 597
    SymmetryRegion = 598
    PreMeshedCyclicRegion = 599
    Symmetry = 600
    LegacyThermalCondition = 601
    Thickness = 602
    LayeredSection = 603
    ResponseConstraint = 604
    MemberSizeManufacturingConstraint = 605
    PullOutDirectionManufacturingConstraint = 606
    ExtrusionManufacturingConstraint = 607
    CyclicManufacturingConstraint = 608
    SymmetryManufacturingConstraint = 609
    AMOverhangConstraint = 610
    TemperatureConstraint = 611
    CenterOfGravityConstraint = 612
    MomentOfInertiaConstraint = 613
    ComplianceConstraint = 614
    CriterionConstraint = 615
    ManufacturingConstraint = 616
    MassConstraint = 617
    VolumeConstraint = 618
    NaturalFrequencyConstraint = 619
    GlobalVonMisesStressConstraint = 620
    LocalVonMisesStressConstraint = 621
    DisplacementConstraint = 622
    ReactionForceConstraint = 623
    Criterion = 624
    PrimaryCriterion = 625
    CompositeCriterion = 626
    Objective = 627
    TreeGroupingFolder = 628
    VirtualCell = 629
    VirtualTopology = 630
    UserLoad = 631
    UserObject = 632
    UserPostObject = 633
    UserResult = 634
    UserSolver = 635
    DataModelObject = 636
    ImportedCFDPressure = 637
    VoltageGround = 638
    VoltageFrequencyResponse = 639
    LinePressureResult = 640
    ChargeReactionFrequencyResponse = 641
    ImpedanceFrequencyResponse = 642
    ChargeReactionProbe = 643
    ImpedanceProbe = 644
    AMBondConnection = 645
    Stage = 646
    AcousticMassSourceRate = 668
    AcousticSurfaceAcceleration = 669
    FlexibleRotationProbe = 670
    MeshExtrude = 671
    PythonResult = 672
    ScriptDefinedResultFolder = 673
    SpotWeldGroup = 674
    SpotWeldConnection = 675
    QualityFactor = 676
    ElectromechanicalCouplingCoefficient = 677
    CompositeFailureTool = 678
    CompositeFailureResult = 679
    ImportedElementOrientationGroup = 680
    ImportedElementOrientation = 681
    ImportedHeatFlux = 682
    ImportedHeatGeneration = 683
    ImportedInitialStrain = 684
    ImportedInitialStress = 685
    ImportedPressure = 686
    ImportedForce = 687
    DirectMorph = 688
    Deviation = 689
    Washer = 690
    CoSimulationPin = 691
    ResultMesh = 692
    ImportedPliesCollection = 693
    ErodedKineticEnergyTracker = 694
    ErodedInternalEnergyTracker = 695
    RigidBodyVelocityTracker = 696
    AddedMassTracker = 697
    PythonCode = 698
    ImportedThicknessGroup = 699
    ImportedThickness = 700
    ConstructionPoint = 701
    ImagePlane = 702
    MappingValidation = 703
    ImportedYarnAngle = 704
    ImportedWarpWeftRatio = 705
    ImportedFiberRatio = 706
    PythonCodeEventBased = 707
    GeometryImportGroup = 708
    GeometryImport = 709
    CompositeSamplingPointTool = 710
    CompositeSamplingPoint = 711
    Weld = 712
    ThermalComplianceConstraint = 713
    DynamicComplianceConstraint = 714
    ImportedMaterialField = 715
    ImportedTraceGroup = 716
    ImportedMaterialFieldsGroup = 717
    FatigueCombination = 718
    UniformConstraint = 719
    PatternRepetitionConstraint = 720
    SubstructureGenerationCondensedPart = 721
    RepairTopology = 722
    HousingConstraint = 723
    Connect = 724
    TableGroup = 725
    Table = 726
    ParameterVariableGroup = 727
    ParameterVariable = 728
    NewtonRaphsonResidualCharge = 729
    FeatureSuppress = 730
    DampingEnergyTracker = 732
    ArtificialEnergyTracker = 733
    NonLinearStabilizationEnergyTracker = 734
    EllipticalCrack = 735
    RingCrack = 736
    ContactDistanceProbe = 737
    LSDYNAGeneralTracker = 738
    TotalElectrostaticForce = 739
    DirectionalElectrostaticForce = 740
    GeometryFidelity = 741
    GeometryBasedAdaptivity = 742
    MeshCopy = 753
    Measures = 754
    MCFWaterfallDiagram = 755
    VelocityWaterfallDiagram = 756
    AccelerationWaterfallDiagram = 757
    MorphingRegion = 758
    CornerCrack = 759
    EdgeCrack = 760
    ThroughCrack = 761
    LineChart2D = 762
    ComplexityIndexConstraint = 764
    ModelImport = 765
    CylindricalCrack = 766

class DeformationType(Enum):
    """
    Specifies the DeformationType.
    """

    Directional = 1
    Total = 0

class ECADFidelity(Enum):

    PCBBlock = 2
    PCBLayers = 1
    BGAFullFidelity = 0
    BGABlock = 1
    BGAWire = 2
    BGABarrel = 3
    MCADFullFidelity = 0
    MCADBlock = 1

class EXDADRConvergenceMethod(Enum):

    ProgramControlled = 0
    CentralDifferenceMethod = 1
    RunningAverageMethod = 2

class EXDLinearViscosityExpansionType(Enum):

    No = 0
    Yes = 1

class EXDArtificialViscosityForShellsType(Enum):

    No = 0
    Yes = 1

class EXDHourglassDampingType(Enum):

    ADStandard = 0
    FlanaganBelytschko = 1

class EXDErosionOnGeomStrainType(Enum):

    No = 0
    Yes = 1

class EXDErosionOnMaterialFailureType(Enum):

    No = 0
    Yes = 1

class EXDErosionOnMinElemTimestepType(Enum):

    No = 0
    Yes = 1

class EXDErosionRetainIntertiaType(Enum):

    No = 0
    Yes = 1

class EXDEulerTrackType(Enum):

    ByBody = 0
    ByMaterial = 1

class EXDEulerDomainType(Enum):

    eWedge = 0
    eGrid = 1

class EXDEulerSizeDefType(Enum):

    eAuto = 0
    eManual = 1

class EXDEulerDomScopeDefType(Enum):

    eAllBodies = 0
    eEulerianOnly = 1

class EXDEulerResolutionDefType(Enum):

    eTotalCells = 0
    eCellSize = 1
    eComponentCells = 2

class EXDEulerGradedDefinition(Enum):

    eNotGraded = 0
    eGraded = 1

class EXDEulerBoundaryDefType(Enum):

    eFlowOut = 0
    eImpedance = 1
    eRigid = 2

class EXDSaveResultsOnType(Enum):

    TimeSteps = 0
    Time = 1
    EquallySpaced = 2

class EXDSaveRestartsOnType(Enum):

    TimeSteps = 0
    Time = 1
    EquallySpaced = 2

class EXDSaveProbeDataOnType(Enum):

    TimeSteps = 0
    Time = 1

class EXDOutputContactForcesOnType(Enum):

    TimeSteps = 0
    Time = 1
    EquallySpaced = 2
    Off = 3

class EXDSavePrintSummaryOnType(Enum):

    TimeSteps = 0
    Time = 1

class EXDSaveUserEditOnType(Enum):

    TimeSteps = 0
    Time = 1

class EXDStepawareOutputControlsType(Enum):

    No = 0
    Yes = 1

class EXDPreferenceType(Enum):

    ProgramControlled = 0
    LowVelocity = 1
    HighVelocity = 2
    Efficiency = 3
    QuasiStatic = 4
    DropTest = 5
    Custom = 6

class EXDSolverPrecisionType(Enum):

    Single = 0
    Double = 1

class EXDSolveUnitsType(Enum):

    umpgms = 0
    mkgs = 1
    cmgus = 2
    mmmgms = 3

class EXDBeamSolutionType(Enum):

    Truss = 0
    Bending = 1

class EXDHexIntegrationType(Enum):

    Exact = 0
    OnePtGauss = 1

class EXDShellWarpCorrectionType(Enum):

    No = 0
    Yes = 1

class EXDShellThicknessUpdateType(Enum):

    Nodal = 0
    Elemental = 1

class EXDTetPressureIntegrationType(Enum):

    AverageNodal = 0
    Constant = 1
    NBS = 2

class EXDShellInertiaUpdateType(Enum):

    Recompute = 0
    Rotate = 1

class EXDDensityUpdateType(Enum):

    ProgramControlled = 0
    Incremental = 1
    Total = 2

class EXDSPHNodeDensityCutoffOption(Enum):

    LimitDensity = 0
    DeleteNode = 1

class EXDDetonationBurnType(Enum):

    ProgramControlled = 0
    Indirect = 1
    Direct = 2

class EXDLoadStepType(Enum):

    Explicit = 0
    DampedADR = 1
    UndampedADR = 2

class EXDAutomaticMassScalingType(Enum):

    No = 0
    Yes = 1

class EXDCharZoneDimensionType(Enum):

    Diagonals = 0
    OppFace = 1
    NearFace = 2

class EdgeType(Enum):
    """
    Specifies the EdgeType.
    """

    Line = 1
    Circle = 3
    Spline = 7
    Faceted = 8

class ElectricType(Enum):
    """
    Specifies the Electric Physics Type.
    """

    Conduction = 4
    ChargeBased = 128
    No = 0

class ElementMidsideNodesType(Enum):
    """
    Specifies the ElementMidsideNodesType.
    """

    GlobalSetting = 0
    Dropped = 1
    Kept = 2

class EnclosureType(Enum):
    """
    Specifies the EnclosureType.
    """

    Open = 0
    Perfect = 1

class FEConnectionLineThicknessType(Enum):
    """
    Specifies the FEConnectionLineThicknessType.
    """

    Single = 0
    Double = 1
    Triple = 2

class FaceMeshingMethod(Enum):

    Quadrilaterals = 0
    TrianglesBestSplit = 1

class FaceType(Enum):
    """
    Specifies the FaceType.
    """

    Plane = 1
    Cylinder = 2
    Cone = 4
    Torus = 6
    Sphere = 7
    Spline = 8
    Faceted = 9

class FatigueAnalysisType(Enum):
    """
    Specifies the Fatigue Analysis Type.
    """

    FatigueToolNone = 0
    FatigueToolGoodman = 1
    FatigueToolSoderberg = 2
    FatigueToolGerber = 3
    FatigueToolSNMeanStressCurves = 4

class FatigueFrequencySelection(Enum):
    """
    Specifies the EnclosureType.
    """

    SingleFrequency = 0
    MultipleFrequency = 1
    SineSweep = 2

class FatigueSensitivityType(Enum):
    """
    Specifies the RadiationType.
    """

    Life = 60
    FactorSaftey = 61
    Damage = 62

class FatigueStressComponentType(Enum):
    """
    Specifies the Fatigue Stress Component Type.
    """

    FatigueToolComponent_X = 0
    FatigueToolComponent_Y = 1
    FatigueToolComponent_Z = 2
    FatigueToolComponent_XY = 3
    FatigueToolComponent_YZ = 4
    FatigueToolComponent_XZ = 5
    FatigueToolVon_Mises = 6
    FatigueToolSignedVonMises = 7
    FatigueToolMaxShear = 8
    FatigueToolMaxPrincipal = 9
    FatigueToolAbsMaxPrincipal = 10

class FatigueToolMethod(Enum):
    """
    Specifies the FatigueToolMethod.
    """

    NarrowBand = 0
    Steinberg = 1
    Wirsching = 2

class FittingMethodType(Enum):
    """
    Specifies the FittingMethodType.
    """

    ProgramControlled = 0
    FastFourierTransform = 1

class FluentExportMeshType(Enum):
    """
    Specifies the Fluent Export Mesh Type.
    """

    Standard = 0
    LargeModelSupport = 1

class FluidDiscretizationType(Enum):
    """
    Specifies the Fluid Discretization Type.
    """

    FluidUpwindLinear = 0
    FluidCentralLinear = 1
    FluidUpwindExponential = 2

class ForceComponentSelectionType(Enum):
    """
    Specifies the ForceComponentType.
    """

    Support = 1
    Coupling = 3
    Contact = 2
    All = 4

class FractureAffectedZone(Enum):
    """
    Specifies the FractureAffectedZone.
    """

    ProgramControlled = 1
    Manual = 2

class FractureSIFSProbeSubType(Enum):
    """
    Specifies the FractureSIFSProbeSubType.
    """

    K1 = 43
    K2 = 44
    K3 = 45

class FrequencyRangeType(Enum):
    """
    Specifies the Selected Frequency Range Type.
    """

    Full = 0
    Manual = 1

class GAPDirectionType(Enum):
    """
    Specifies the GAPDirectionType.
    """

    X = 1
    Y = 2
    Z = 3

class GPUAccelerationDevicesType(Enum):
    """
    Specifies the GPUAccelerationDevicesType.
    """

    None_ = 0
    NVidia = 1
    AMD = 2

class GapDefinedBy(Enum):
    """
    Specifies the GapDefinedBy.
    """

    Range = 0
    CADParameters = 1

class GapDensityType(Enum):
    """
    Specifies the GapDensityType.
    """

    Coarse = 0
    Fine = 1

class GeometryDimensionType(Enum):
    """
    Specifies the GeometryDimensionType.
    """

    Volume = 0
    Surface = 1

class GeometryType(Enum):
    """
    Specifies the GeometryType.
    """

    Solid = 0
    Surface = 1
    Mixed = 2
    Line = 3
    Empty = 4
    Lightweight = 5
    Unknown = 6

class Graphics3DExportFormat(Enum):
    """
    
            Specifies the 3D Format.
            
    """

    AVZ = 0
    BinarySTL = 1
    ASCIISTL = 2

class GraphicsAnimationExportFormat(Enum):
    """
    
            Specifies the Animation Export File Format.
            
    """

    MP4 = 0
    WMV = 1
    AVI = 2
    GIF = 3

class GraphicsBackgroundType(Enum):
    """
    
            Specifies the Graphics Image Background Type.
            
    """

    GraphicsAppearanceSetting = 0
    White = 1

class GraphicsCaptureType(Enum):
    """
    
            Specifies the Graphics Image Capture Type.
            
    """

    ImageAndLegend = 0
    ImageOnly = 1

class GraphicsImageExportFormat(Enum):
    """
    
            Specifies the 2D Image Format.
            
    """

    PNG = 0
    JPG = 1
    TIF = 2
    BMP = 3
    EPS = 4

class GraphicsResolutionType(Enum):
    """
    
            Specifies the Graphics Image Resolution Type.
            
    """

    NormalResolution = 0
    EnhancedResolution = 1
    HighResolution = 2

class ICEMCFDBehavior(Enum):

    GenerateMesh = 0
    SkipMeshing = 1

class JointConditionType(Enum):
    """
    Specifies the Joint Condition Type.
    """

    Displacement = 105
    Rotation = 111
    RotationalVelocity = 109
    Acceleration = 110
    RotationalAcceleration = 113
    Velocity = 112
    Force = 102
    Moment = 106

class LegendColorSchemeType(Enum):
    """
     Specifies the Legend Color Scheme type.
    """

    Rainbow = 0
    ReverseRainbow = 1
    GrayScale = 2
    ReverseGrayScale = 4

class LegendOrientationType(Enum):
    """
     Specifies the Legend Orientation.
    """

    Vertical = 1
    Horizontal = 2

class LifeUnitsType(Enum):
    """
    Specifies the Life Units Type.
    """

    Cycles_LC = 0
    Blocks_LC = 1
    Seconds = 2
    Minutes_LC = 3
    Hours_LC = 4
    Days_LC = 5
    Months_LC = 6
    UserDefined = 7

class LoadCombinationType(Enum):
    """
     Specifies the Load Combination type.
    """

    Linear = 0
    SRSS = 1

class LocationDefinitionMethod(Enum):
    """
    Specifies the LocationDefinitionMethod.
    """

    Beam = 7
    Bearing = 12
    BoundaryCondition = 3
    ContactRegion = 5
    CoordinateSystem = 1
    GeometrySelection = 0
    MeshConnection = 9
    NamedSelection = 2
    NoSelection = 4
    RemotePoint = 6
    Surface = 11
    Spring = 10
    UserDefinedCoordinates = 8
    WeakSprings = -1

class InterpolationType(Enum):

    Nondirectional = 0
    Directional = 1

class LegendRangeType(Enum):

    ProgramControlled = 0
    Manual = 1

class MappingAlgorithm(Enum):

    Unknown = 0
    PointCloud = 1
    BucketSurface = 2
    GGI = 3
    BucketVolume = 4
    UV = 5

class MappingControlType(Enum):

    Undefined = 0
    ProgramControlled = 1
    Manual = 2

class MappingInterpolationType(Enum):

    ProfilePreserving = 0
    Conservative = 1

class MappingIsolineLineType(Enum):

    Solid = 0
    Dashed = 1

class MappingIsolineThicknessType(Enum):

    Single = 0
    Double = 1
    Triple = 2

class MappingMethod(Enum):

    PointPoint = 0
    PointElement = 1
    ElementElement = 2

class MappingOutsideOption(Enum):

    Ignore = 0
    WeightedAvg = 1
    Projection = 2
    NearestNode = 3

class MappingValidationDisplayOption(Enum):

    ScaledSphere = 0
    ColoredSphere = 1
    Boxes = 2
    ColoredPoints = 3
    ColoredDiamonds = 4
    Isolines = 5
    Contours = 6

class MappingValidationType(Enum):

    Undefined = 0
    ReverseMapping = 1
    DistanceBasedAverage = 2
    SourceValue = 3
    UndefinedPoints = 4

class MappingVariableType(Enum):

    MappingTransferUnknown = 0
    MappingTransferTemperature = 1
    MappingTransferConvectionCoefficient = 2
    MappingTransferHeatGeneration = 3
    MappingTransferHeatFlux = 4
    MappingTransferForceDensity = 5
    MappingTransferPressure = 6
    MappingTransferDisplacements = 7
    MappingTransferThickness = 8
    MappingTransferHeatRate = 9
    MappingTransferForce = 10
    MappingTransferVelocity = 11
    MappingTransferRotation = 12
    MappingTransferDisplacementAndRotation = 13
    MappingTransferStress = 14
    MappingTransferStrain = 15
    MappingTransferMetalFraction = 16
    MappingTransferMaterialField = 17
    MappingTransferElementOrientation = 18

class RigidBodyTransformationType(Enum):

    OriginAndEulerAngles = 0
    CoordinateSystem = 1

class WeightingType(Enum):

    WeightUndefined = 0
    RadialBasisFunctions = 1
    ClosestPoint = 2
    ShapeFunctions = 3
    Triangulation = 4
    WeightedAverage = 5
    KrigingFunction = 6
    UVMapping = 7
    VolumeFraction = 8
    Assignment = 9
    Quaternion = 10

class MeanStressTheoryType(Enum):
    """
    Specifies the EnclosureType.
    """

    Goodman = 0
    Soderberg = 1
    Gerber = 2
    MeanStressCurves = 4
    NoneStrain = 6
    NoneStress = 5
    Morrow = 7
    SWT = 8
    MansonHalford = 10
    ASMEElliptical = 15

class MeshControlGroupRigidBodyBehaviorType(Enum):
    """
    Specifies the MeshControlGroupRigidBodyBehaviorType.
    """

    FullMesh = 1
    DimensionallyReduced = 0

class MeshControlGroupRigidBodyFaceMeshType(Enum):
    """
    Specifies the MeshControlGroupRigidBodyFaceMeshType.
    """

    AllTri = 1
    QuadAndTri = 0

class MeshElementShape(Enum):
    """
    
            Defines the Mesh Element Types
            
    """

    Tet10 = 0
    Hex20 = 1
    Wedge15 = 2
    Pyramid13 = 3
    Tri6 = 4
    Quad8 = 6
    Tet4 = 10
    Hex8 = 11
    Wedge6 = 12
    Pyramid5 = 13
    Tri3 = 14
    Quad4 = 16
    Beam3 = 30
    Beam4 = 31

class MeshMethodAlgorithm(Enum):
    """
    Specifies the MeshMethodAlgorithm.
    """

    Axisymmetric = 0
    PatchConforming = 1
    PatchIndependent = 3
    AutomaticSweep = 4

class MeshNodeType(Enum):
    """
    Specifies the MeshNodeType.
    """

    Corner = 1024
    Midside = 262144

class MeshPhysicsPreferenceType(Enum):
    """
    Specifies the Mesh Physics Preference Type.
    """

    Mechanical = 0
    Electromagnetics = 1
    CFD = 2
    Explicit = 3
    Custom = 4
    NonlinearMechanical = 5
    Hydrodynamics = 6

class MeshSolverPreferenceType(Enum):
    """
    Specifies the Mesh Solver Preference Type.
    """

    Fluent = 0
    CFX = 1
    MechanicalAPDL = 2
    ANSYSRigidDynamics = 3
    Polyflow = 4

class MessageSeverityType(Enum):
    """
    Specifies the Message Severity Type.
    """

    Warning = 0
    Error = 1
    Info = 2

class MethodType(Enum):
    """
    Specifies the MethodType.
    """

    Automatic = 0
    AllTriAllTet = 1
    HexDominant = 2
    QuadTri = 3
    AllQuad = 4
    Sweep = 5
    CFXMesh = 6
    MultiZone = 7
    Cartesian = 8
    LayeredTet = 12
    Particle = 13
    Prime = 14
    Stacker = 15

class ModelColoring(Enum):
    """
    Specifies the Model display coloring.
    """

    ByBodyColor = 0
    ByThickness = 1
    ByMaterial = 2
    ByNonLinear = 3
    ByStiffness = 4
    ByPart = 5
    ByVisibleThickness = 6
    ByAssembly = 7
    ByCondensedParts = 8
    ByCrossSection = 9
    ByBodyType = 10

class ModelDisplay(Enum):
    """
    Specifies the Model display options.
    """

    ShadedExterior = 1
    Wireframe = 2
    ShadedExteriorAndEdges = 3

class MomentsAtSummationPointType(Enum):
    """
    Specifies the Moments at summation point type.
    """

    OrientationSystem = 0
    Centroid = 1

class NodeMoveInformationType(Enum):
    """
    Specifies the NodeMoveInformationType.
    """

    F4KeytoMoveAnywhere = 1

class NodeSelection(Enum):
    """
    Specifies the NodeSelection.
    """

    AllNodes = -1
    VisibleNodes = -2

class NonLinearValueType(Enum):
    """
    Specifies the NonLinearValueType.
    """

    CalculatedBySolver = 0
    UserInput = 1

class NonlinearAdaptivityTimeRange(Enum):
    """
    Specifies the NonlinearAdaptivityTimeRange.
    """

    EntireLoadStep = 0
    Manual = 1

class ObjectState(Enum):
    """
    
            Specifies the Object State type.
            
    """

    NoState = 0
    FullyDefined = 1
    UnderDefined = 2
    Suppressed = 3
    NotSolved = 4
    Solved = 5
    Obsolete = 6
    Error = 7
    LicenseConflict = 8
    Ignored = 9
    Hidden = 10
    Solving = 11
    SolvedNotLoaded = 12
    SolveFailed = 13
    SolveFailedNotLoaded = 14
    PartialSolved = 15
    Meshed = 16
    WaitForValidation = 17
    ObsoleteNotLoaded = 19

class ObjectiveType(Enum):
    """
    Specifies the Objective Type.
    """

    MinimizeCompliance = 0
    MinimizeMass = 1
    MinimizeVolume = 2
    MaximizeFrequency = 3
    MinimizeAccumulatedEquivalentPlasticStrain = 4
    MinimizeStress = 5
    MinimizeCriterion = 6
    MaximizeCriterion = 7
    MinimizeThermalCompliance = 8

class OptimizationSolverType(Enum):
    """
    Specifies the OptimizationSolverType.
    """

    OptimalityCriteria = 9
    ProgramControlled = 0
    SequentialConvexProgramming = 8

class PSDBoundaryConditionSelectionType(Enum):
    """
    Specifies the PSDBoundaryConditionSelectionType.
    """

    None_ = 0
    AllFixedSupports = 1
    AllRemoteDisplacements = 2
    AllFixedSupportsAndRemoteDisplacements = 3
    AllSupports = 4

class ImportParameterType(Enum):
    """
    Specifies the MethodType.
    """

    None_ = 0
    Independent = 1
    All = 3

class PatchIndependentDefineType(Enum):
    """
    Specifies the PatchIndependentDefineType.
    """

    MaxElementSize = 0
    ApproxNumElements = 1

class PeriodicRegionType(Enum):
    """
    Specifies the PeriodicRegionType.
    """

    EvenPeriodic = 3
    OddPeriodic = 4

class PeriodicityDirectionType(Enum):
    """
    Specifies the PeriodicityDirectionType.
    """

    XAxis = 0
    YAxis = 1
    ZAxis = 2

class PhaseType(Enum):
    """
    Specifies the Prototype Phase Type.
    """

    DefinedByGeometry = 0
    LiquidGas = 1
    Solid = 2

class PhysicsType(Enum):
    """
    Specifies the PhysicsType.
    """

    Customizable = 32
    ElectricConduction = 4
    Electromagnetic = 8
    ExplicitCDI = 16
    Mechanical = 1
    Thermal = 2
    ThermalElectric = 6
    Acoustic = 64
    MechanicalAcoustic = 65
    ElectricCharge = 128
    MechanicalElectricCharge = 129

class PinNature(Enum):
    """
    
            FMI standards
            
    """

    InputQuantities = 0
    OutputQuantities = 1

class PolyflowExportUnit(Enum):
    """
    Specifies the Polyflow Export Unit Type.
    """

    UseProjectUnit = 0
    Meters = 1
    Centimeters = 2
    Millimeters = 3
    Micrometers = 4
    Inches = 5
    Feet = 6

class ProbeExtractionType(Enum):
    """
    Specifies the ProbeExtractionType.
    """

    Master = 1
    Slave = 2
    MeshPositive = 1
    MeshNegative = 2
    ContactSide = 1
    TargetSide = 2
    ContactElements = 5

class ProximitySFSourcesType(Enum):
    """
    Specifies the ProximitySFSourcesType.
    """

    FacesAndEdges = 0
    Faces = 1
    Edges = 2

class RBDCorrectionType(Enum):

    PureKinematic = 0
    WithInertiaMatrix = 1
    ProgramControlled = 2

class RBDDoStaticAnalysisType(Enum):

    On = 0
    Off = 1

class RBDProgramControlType(Enum):

    ProgramControlled = 0
    On = 1
    Off = 2

class RBDTimeIntegrationType(Enum):

    RungeKutta4 = 0
    RungeKutta5 = 1
    HalfExplicitMethod5 = 2
    RungeKuttaDormandPrince5 = 3
    RungeKuttaHeunEuler2 = 4
    RungeKuttaBogackiShampine3 = 5
    GeneralizedAlpha = 6
    TimeSteppingNSCD = 7
    HybridIntegration = 8
    ProgramControlled = 9
    StabilizedGeneralizedAlpha = 10
    PredictEvaluateCorrect = 11
    NonSmoothGeneralizedAlpha = 12

class RSBoundaryConditionSelectionType(Enum):
    """
    Specifies the RSBoundaryConditionSelectionType.
    """

    None_ = 0
    AllSupports = 1

class RadiationType(Enum):
    """
    Specifies the RadiationType.
    """

    ToAmbient = 0
    SurfaceToSurface = 1

class RadiositySolverType(Enum):
    """
    Specifies the RadiositySolverType.
    """

    ProgramControlled = 0
    Direct = 1
    IterativeJacobi = 2
    IterativeGaussSeidel = 3

class RadiosityViewFactorType(Enum):
    """
    Specifies the RadiosityViewFactorType.
    """

    RadiosityFF2DHidden = 0
    RadiosityFF2DNonHidden = 1

class RadiusOfReferenceSphereDefineBy(Enum):
    """
    Specifies the RadiusOfReferenceSphereDefineBy.
    """

    ProgramControlled = 1
    UserDefined = 0

class ResultAnimationRangeType(Enum):
    """
    
            Specifies the Result Animation Range Type
            
    """

    ResultSets = 0
    Distributed = 1

class ResultAveragingType(Enum):
    """
    Specifies the ResultAveragingType.
    """

    Unaveraged = 0
    Averaged = 1
    NodalDifference = 2
    NodalFraction = 3
    ElementalDifference = 4
    ElementalFraction = 5
    ElementalMean = 6

class ResultFileItemType(Enum):
    """
    Specifies the ResultFileItemType.
    """

    MaterialIDs = 0
    ElementNameIDs = 1
    ElementTypeIDs = 2
    ComponentName = 3
    ElementIDs = 4
    NodeIDs = 5

class SafetyTheoryType(Enum):
    """
    Specifies the Stress Safety Theory Type.
    """

    MaximumEquivalentStress = 0
    MaximumShearStress = 1
    MaximumTensileStress = 2
    MohrCoulombStress = 3

class SecondaryImportPrefType(Enum):
    """
    Specifies the SecondaryImportPrefType.
    """

    None_ = 0
    Solid = 1
    Surface = 2
    Line = 3
    SolidAndSurface = 4
    SurfaceAndLine = 5

class SectionPlaneCappingType(Enum):
    """
    
            Specifies the Section Plane Capping Style
            
    """

    Hide = -1
    Show = 2
    ShowByBodyColor = 3

class SectionPlaneType(Enum):
    """
    
            Specifies the Section Plane type.
            
    """

    AlongDirection = -1
    AgainstDirection = 1
    PlaneOnly = 0

class SelectionActionType(Enum):
    """
    
            Specifies the selction action type.
            
    """

    Filter = 1
    Remove = 2
    Invert = 3
    Add = 4
    Convert = 5
    Diagnostics = 6

class SelectionCriterionType(Enum):
    """
    
            Specifies the selection criterion type.
            
    """

    Size = 1
    Type = 2
    LocationX = 3
    LocationY = 4
    LocationZ = 5
    FaceConnections = 6
    CADAttribute = 7
    Radius = 8
    NamedSelection = 9
    NodeNumber = 10
    Material = 11
    Thickness = 12
    OffsetMode = 13
    Distance = 14
    ElementNumber = 15
    ElementQuality = 16
    AnyNode = 17
    AllNodes = 18
    AspectRatio = 19
    JacobianRatio = 20
    WarpingFactor = 21
    ParallelDeviation = 22
    Skewness = 23
    OrthogonalQuality = 24
    Volume = 25
    Area = 26
    AnalysisPly = 27
    SharedAcrossParts = 28
    Name = 29
    ElementConnections = 30
    EdgeConnections = 31
    AnyVertex = 32
    AllVertices = 33
    AnyEdge = 34
    AllEdges = 35
    ImportedTrace = 36
    SharedAcrossBodies = 37
    MaximumCornerAngle = 38
    MinimumLength = 39
    JacobianRatioCornerNodes = 40
    JacobianRatioGaussPoints = 41
    CrossSection = 42
    NormalTo = 43
    ExcludeSharedFaces = 44
    IncludeSharedFaces = 45
    WeldFeatures = 46
    WithinBody = 47
    SeamWeld = 48
    SeamWeldHAZ1 = 49
    SeamWeldHAZ2 = 50
    SeamWeldHAZ3 = 51
    SeamWeldHAZAll = 52
    SelfIntersectingMesh = 53
    BodyInterferenceMesh = 54
    ExtEdgeFaceLoop = 55
    ExtEdgeNodeLoop = 56
    SharpAngleMesh = 57
    MinimumTriAngle = 58
    MaximumTriAngle = 59
    MinimumQuadAngle = 60
    MaximumQuadAngle = 61
    WarpingAngle = 62
    TetCollapse = 63
    AspectRatioExplicit = 64
    MinimumMeshEdgeLength = 65
    MaximumMeshEdgeLength = 66
    MinimumLengthLSDyna = 67
    PartiallyDefeaturedEdges = 68
    FullyDefeaturedVertices = 69
    FullyDefeaturedEdges = 70
    FullyDefeaturedFaces = 71
    SeamWeldNormal = 72
    SeamWeldAngle = 73

class SelectionOperatorType(Enum):
    """
    
            Specifies the selection operator type.
            
    """

    Equal = 1
    NotEqual = 2
    LessThan = 3
    LessThanOrEqual = 4
    GreaterThan = 5
    GreaterThanOrEqual = 6
    RangeExclude = 7
    RangeInclude = 8
    Smallest = 9
    Largest = 10
    Yes = 11
    No = 12
    Contains = 13

class SelectionType(Enum):
    """
    
            Specifies the selection type.
            
    """

    GeoVertex = 4
    GeoEdge = 3
    GeoFace = 2
    GeoBody = 1
    MeshNode = 5
    MeshElement = 6
    MeshFace = 7
    MeshElementFace = 9

class SequenceSelectionType(Enum):
    """
    Specifies the SequenceSelectionType.
    """

    First = 0
    Last = 1
    All = 2
    ByNumber = 3
    Zero = 4
    ModalSolution = 5
    MsupSolution = 6
    MsupExpansion = 7
    Identifier = 8
    PSDPfact = 9

class ShellBodyDimension(Enum):
    """
    Specifies the ShellBodyDimension.
    """

    Two_D = 2
    Three_D = 3

class ShellMBPOrientationType(Enum):
    """
    Specifies the ShellMBPOrientationType.
    """

    None_ = -99
    LocalElementDirection11 = 0
    LocalElementDirection22 = 1
    LocalElementDirection12 = 2

class SizingBehavior(Enum):
    """
    Specifies the SizingBehaviorType.
    """

    Soft = 0
    Hard = 1

class SizingType(Enum):
    """
    Specifies the SizingType.
    """

    ElementSize = 0
    NumberOfDivisions = 1
    SphereOfInfluence = 2
    BodyOfInfluence = 3

class SnapType(Enum):
    """
    Specifies the SnapType.
    """

    ManualTolerance = 0
    ElementSizeFactor = 1

class SolutionStatusType(Enum):
    """
    Specifies the SolutionStatusType.
    """

    Done = 0
    AdaptiveRefinementRequired = 3
    SolveRequired = 1
    InputFileGenerationRequired = 5
    PostProcessingRequired = 2
    RestartRequired = 6
    ExecutePostCommands = 7
    SolveRequiredPartialResultsAvailable = 4

class SortingType(Enum):
    """
    
            Specifies the Sorting type.
            
    """

    Alphabetical = 0

class SourceConductorType(Enum):
    """
    Specifies the SourceConductorType.
    """

    Solid = 0
    Stranded = 1

class SourceDimension(Enum):
    """
    Specifies the SourceDimension.
    """

    SourceDimension2D = 2
    SourceDimension3D = 3

class SpacingOptionType(Enum):
    """
    Specifies the SpacingOptionType.
    """

    Default = 0
    UserControlled = 1

class SpinSofteningType(Enum):
    """
    Specifies the SpinSofteningType.
    """

    No = 0
    Yes = 1
    ProgramControlled = 2

class IterationOptions(Enum):
    """
    Specifies the IterationOptions.
    """

    AllIterations = 0
    LastIteration = 1
    EquallySpacedPoints = 2
    SpecifiedRecurrenceRate = 3

class SweepElementOptionType(Enum):
    """
    Specifies the SweepElementOptionType.
    """

    SolidShell = 0
    Solid = 1

class SymmetryNormalType(Enum):
    """
    Specifies the SymmetryNormalType.
    """

    XAxis = 0
    YAxis = 1
    ZAxis = 2

class SymmetryRegionType(Enum):
    """
    Specifies the SymmetryRegionType.
    """

    Symmetric = 1
    AntiSymmetric = 2
    LinearPeriodic = 6

class ThermalPointMassBehavior(Enum):
    """
    Specifies the Behavior for ThermalPointMass.
    """

    Isothermal = 0
    HeatFluxDistributed = 1
    ThermalLink = 2
    Coupled = 3

class TimeHistoryDisplayType(Enum):
    """
    Specifies the Time History Display Type.
    """

    Real = 0
    Imaginary = 1
    RealAndImaginary = 2
    Amplitude = 3
    PhaseAngle = 4
    Bode = 5

class TopoEnvironmentType(Enum):
    """
    Specifies the Topology Environment Type.
    """

    Unknown = 0
    AllStaticStructural = 1
    AllModal = 2

class TopologyOptimizationResultShowType(Enum):
    """
    Specifies the Topology Optimization Result Show Type.
    """

    AllRegions = 0
    RetainedRegion = 1
    RemovedRegion = 2

class TreeFilterObjectClass(Enum):
    """
    Specifies the TreeFilterObjectClass.
    """

    All = 0
    Results = 1
    BoundaryConditions = 2
    Connections = 3
    Commands = 4

class TreeFilterObjectState(Enum):
    """
    Specifies the TreeFilterObjectState.
    """

    All = 0
    Suppressed = 2
    Underdefined = 3
    NotLicensed = 4
    Ignored = 5
    Obsolete = 6
    NotSolved = 7
    Failed = 8

class TreeFilterScopingType(Enum):
    """
    Specifies the TreeFilterScopingType.
    """

    All = 0
    Partial = 1

class UnitCategoryType(Enum):
    """
    Specifies the WB Unit Category Type.
    """

    NoUnits = -2
    Undefined = -1
    Acceleration = 0
    Angle = 1
    AngularVelocity = 2
    Area = 3
    Capacitance = 4
    Charge = 5
    ChargeDensity = 6
    Conductivity = 7
    Current = 8
    CurrentDensity = 9
    Density = 10
    Displacement = 11
    ElectricConductivity = 12
    ElectricField = 13
    ElectricFluxDensity = 14
    ElectricResistivity = 15
    Energy = 16
    FilmCoeff = 17
    Force = 18
    ForceIntensity = 19
    Frequency = 20
    HeatFlux = 21
    HeatGeneration = 22
    HeatTransferRate = 23
    Inductance = 24
    InverseStress = 25
    Length = 26
    MagneticFieldIntensity = 27
    MagneticFlux = 28
    MagneticFluxDensity = 29
    Mass = 30
    Moment = 31
    MomentInertia = 32
    Permeability = 33
    Permittivity = 34
    Poisson = 35
    Power = 36
    Pressure = 37
    RelativePermeability = 38
    RelativePermittivity = 39
    SectionModulus = 40
    SpecificHeat = 41
    SpecificWeight = 42
    ShearStrain = 43
    Stiffness = 44
    Strain = 45
    Stress = 46
    Strength = 47
    ThermalExpansion = 48
    Temperature = 49
    Time = 50
    Velocity = 51
    Voltage = 52
    Volume = 53
    GasketStiffness = 54
    MomentInertiaMass = 55
    PSDAcceleration = 56
    PSDAccelerationGrav = 57
    PSDDisplacement = 58
    PSDVelocity = 59
    RotationalDamping = 60
    RotationalStiffness = 61
    TranslationalDamping = 62
    AngularAcceleration = 63
    SeebeckCoefficient = 64
    DecayConstant = 65
    FractureEnergy = 66
    ShockVelocity = 67
    EnergyDensityMass = 68
    ElectricConductancePerUnitArea = 69
    PSDStress = 70
    PSDStrain = 71
    PSDForce = 72
    PSDMoment = 73
    PSDPressure = 74
    ForcePerAngularUnit = 75
    Impulse = 76
    ImpulsePerAngularUnit = 77
    TemperatureDifference = 78
    MaterialImpedance = 79
    RSAcceleration = 80
    RSAccelerationGrav = 81
    RSDisplacement = 82
    RSVelocity = 83
    WarpingFactor = 84
    ThermalConductance = 85
    InverseLength = 86
    InverseAngle = 87
    ThermalCapacitance = 88
    NormalizedValue = 89
    MassFlowRate = 90
    Unitless = 91
    StressIntensityFactor = 92
    SquareRootOfLength = 93
    EnergyPerVolume = 94
    ThermalGradient = 95
    MassMoment = 96
    MassPerArea = 97
    FractureEnergyRate = 98
    ShearRate = 99
    Viscosity = 100
    MassFlowRatePerVolume = 101
    MassFlowRatePerArea = 102
    MassFlowRatePerLength = 103
    AcousticAdmittance = 104
    PowerSpectralDensity = 105
    Decibel = 106
    AWeightedDecibel = 107
    FrequencyRate = 108
    ElectricChargeDensity = 109
    ElectricCapacitancePerArea = 110
    ElectricResistance = 111
    MassSourceRatePerVolume = 112
    MassSourceRatePerArea = 113
    MassSourceRatePerLength = 114
    MassSourceRate = 115
    ThermalCompliance = 116

class UnitSystemIDType(Enum):
    """
    Specifies the Unit System ID Type.
    """

    UnitsMKS = 0
    UnitsCGS = 1
    UnitsNMM = 2
    UnitsBFT = 5
    UnitsBIN = 6
    UnitsUMKS = 7

class UserUnitSystemType(Enum):
    """
    Specifies the UserUnitSystemType.
    """

    NoUnitSystem = 17
    StandardBFT = 3
    StandardBIN = 4
    StandardCGS = 1
    StandardCUST = 12
    StandardMKS = 0
    StandardNMM = 2
    StandardNMMdat = 14
    StandardNMMton = 13
    StandardUMKS = 9
    StandardKNMS = 15

class VectorDisplayType(Enum):
    """
    Specifies the VectorDisplayType.
    """

    Line = 0
    Solid = 1
    Sphere = 2

class VectorLengthType(Enum):
    """
    Specifies the VectorLengthType.
    """

    Proportional = 0
    Uniform = 1

class ViewOrientationType(Enum):
    """
    
            Specifies the View Orientation type.
            
    """

    Front = 0
    Back = 1
    Top = 2
    Bottom = 3
    Left = 4
    Right = 5
    Iso = 6

class VirtualCellClassType(Enum):
    """
    Specifies the VirtualCellClassType.
    """

    VirtualFace = 0
    VirtualEdge = 1

class VirtualCellGroupAutomaticBehaviorType(Enum):
    """
    Specifies the VirtualCellGroupAutomaticBehaviorType.
    """

    Low = 0
    Medium = 1
    High = 2
    EdgesOnly = 3
    Custom = 4

class VirtualCellGroupMethodType(Enum):
    """
    Specifies the VirtualCellGroupMethodType.
    """

    Automatic = 0
    Repair = 1
    UserDefined = 2

class VirtualCellGroupRepairBehaviorType(Enum):
    """
    Specifies the VirtualCellGroupRepairBehaviorType.
    """

    All = 0
    SmallEdges = 1
    Slivers = 2
    SmallFaces = 3

class VisibilityType(Enum):
    """
    
            Specifies the Tree Graphic Filter type.
            
    """

    All = 0
    Visible = 1
    Invisible = 2

class NamedSelectionWorksheetOperator(Enum):
    """
    
            Specifies the Worksheet Enumeration Wrappers.
            
    """

    pass

class YesNoType(Enum):
    """
    Specifies the YesNoType. 
    """

    No = 0
    Yes = 1

class StepVarying(Enum):
    """
    Specifies the StepVarying.
    """

    No = 0
    Yes = 1

class FilterType(Enum):
    """
    Specifies the FilterType.
    """

    Butterworth = 1
    None_ = 0
    SAE = 2

class ActiveOrInactive(Enum):
    """
    Specifies the ActiveOrInactive.
    """

    Active = 0
    Inactive = 1

class AggressiveRemeshingType(Enum):
    """
    Specifies the AggressiveRemeshingType.
    """

    Off = 0
    On = 1

class AlgorithmType(Enum):
    """
    Specifies the AlgorithmType.
    """

    MFD = 1
    ProgramControlled = 0
    SCPIP = 2

class AMBaseRemovalType(Enum):
    """
    Specifies the AMBaseRemovalType.
    """

    Directional = 1
    Instantaneous = 0

class AMBuildMachineType(Enum):
    """
    Specifies the AMBuildMachineType.
    """

    Ai = 1
    Eos = 4
    Hb3d = 6
    Renishaw = 3
    Sisma = 7
    Slm = 2
    Trumpf = 5
    Undefined = 0

class AMHeatingDurationType(Enum):
    """
    Specifies the AMHeatingDurationType.
    """

    Flash = 1
    ScanTime = 2

class AMHeatingMethod(Enum):
    """
    Specifies the AMHeatingMethod.
    """

    MeltingTemperature = 1
    Power = 2

class AMInherentStrainDefinition(Enum):
    """
    Specifies the AMInherentStrainDefinition.
    """

    Anisotropic = 1
    Isotropic = 0
    ScanPattern = 2
    ThermalStrain = 3

class AMMachineLearningModel(Enum):
    """
    Specifies the AMMachineLearningModel.
    """

    Al357 = 3
    AlSi10Mg = 4
    CoCr = 5
    Inconel625 = 6
    Inconel718 = 7
    SS17_4 = 1
    SS316L = 2
    Ti6Al4V = 8
    Undefined = 0

class AMProcessSettingsType(Enum):
    """
    Specifies the AMProcessSettingsType.
    """

    PreheatTemperature = 2
    RoomTemperature = 0
    SpecifiedTemperature = 1

class AMProcessSimulationType(Enum):
    """
    Specifies the AMProcessSimulationType.
    """

    No = 0
    ProgramControlled = 2
    Yes = 1

class AMProcessType(Enum):
    """
    Specifies the AMProcessType.
    """

    DirectedEnergyDeposition = 2
    PowderBedFusion = 1

class AMScanPatternDefinition(Enum):
    """
    Specifies the AMScanPatternDefinition.
    """

    BuildFile = 1
    Generated = 0

class AMStlSource(Enum):
    """
    Specifies the AMStlSource.
    """

    ConstructionGeometry = 1
    File = 0

class AMSupportGroupOutputType(Enum):
    """
    Specifies the AMSupportGroupOutputType.
    """

    NamedSelection = 0
    AMSupport = 1

class AMSupportSTLType(Enum):
    """
    Specifies the AMSupportSTLType.
    """

    Solid = 1
    Volumeless = 0

class AMSupportType(Enum):
    """
    Specifies the AMSupportType.
    """

    UserDefined = 2
    Block = 1

class AMThermalStrainMethod(Enum):
    """
    Specifies the AMThermalStrainMethod.
    """

    FullThermal = 0
    MachineLearning = 1

class AnalysisType(Enum):
    """
    Specifies the AnalysisType.
    """

    Buckling = 4
    DesignAssessment = 11
    ExplicitDynamics = 10
    Harmonic = 1
    MBD = 7
    Modal = 5
    ResponseSpectrum = 9
    Shape = 8
    Spectrum = 3
    Static = 0
    TopologyOptimization = 13
    Transient = 2

class AnalysisTypeDimensionEnum(Enum):
    """
    To select the analysis type dimension for the Model Import Object.
    """

    TwoD = 1
    ThreeD = 2

class ArtificiallyMatchedLayers(Enum):
    """
    Specifies the ArtificiallyMatchedLayers.
    """

    IPML = 2
    Off = 0
    PML = 1

class AutoDetectionType(Enum):
    """
    Specifies the AutoDetectionType.
    """

    Contact = 0
    Joint = 2

class AutomaticNodeMovementMethod(Enum):
    """
    To select the method of AutoNodeMove under PCTet.
    """

    Aggressive = 3
    Conservative = 2
    Custom = 4
    Off = 0
    ProgramControlled = 1

class AutomaticOrManual(Enum):
    """
    Specifies the AutomaticOrManual.
    """

    Automatic = 1
    Manual = 0

class AutomaticTimeStepping(Enum):
    """
    Specifies the AutomaticTimeStepping.
    """

    Off = 2
    On = 1
    ProgramControlled = 0

class AxisSelectionType(Enum):
    """
    Specifies the AxisSelectionType.
    """

    All = 0
    XAxis = 1
    YAxis = 2
    ZAxis = 3

class BaseResultType(Enum):
    """
    Specifies the BaseResultType.
    """

    CenterOfGravity = 3
    Mass = 5
    MomentOfInertia = 4
    Rotation = 7
    Acceleration = 12
    Displacement = 0
    Frequency = 9
    ReactionForce = 2
    ReactionMoment = 8
    Frequencies = 10
    Velocity = 11
    Volume = 6

class BeamBeamModel(Enum):
    """
    Specifies the BeamBeamModel.
    """

    All = 2
    ExcludeCrossingBeams = 1
    OnlyCrossingBeams = 3

class BeamEndReleaseBehavior(Enum):
    """
    Specifies the BeamEndReleaseBehavior.
    """

    Coupled = 0
    Joint = 1

class BeamOffsetType(Enum):
    """
    Specifies the BeamOffsetType.
    """

    Centroid = 0
    CoordinateSystemOrigin = 2
    ShearCenter = 1
    UserDefined = 3

class BeamSolutionType(Enum):
    """
    Specifies the BeamSolutionType.
    """

    Bending = 0
    Truss = 1

class BodyInteractionFormulation(Enum):
    """
    Specifies the BodyInteractionFormulation.
    """

    DECOMPOSITION_RESPONSE = 0
    PENALTY = 1

class BodyTreatment(Enum):
    """
    Specifies the BodyTreatment.
    """

    ConstructionBody = 1
    None_ = 0

class BoltLoadDefineBy(Enum):
    """
    Specifies the BoltLoadDefineBy.
    """

    Increment = 4
    Lock = 2
    Open = 3
    Adjustment = 1
    Load = 0

class BondedBreakableType(Enum):
    """
    Specifies the BondedBreakableType.
    """

    ForceCriteria = 1
    No = 0
    StressCriteria = 2

class BoundaryConditionAlongFiber(Enum):
    """
    Specifies the BoundaryConditionAlongFiber.
    """

    Displacement = 2
    Force = 1
    Free = 0

class BoundaryConditionForRotation(Enum):
    """
    Specifies the BoundaryConditionForRotation.
    """

    Free = 0
    Moment = 1
    Rotation = 2

class BoundaryConditionType(Enum):
    """
    Specifies the BoundaryConditionType.
    """

    AllLoads = 1
    AllLoadsAndSupports = 2
    AllSupports = 3
    None_ = 0

class BrickIntegrationScheme(Enum):
    """
    Specifies the BrickIntegrationScheme.
    """

    Full = 0
    Reduced = 1

class CacheResultsInMemory(Enum):
    """
    Specifies the CacheResultsInMemory.
    """

    DuringSolution = 1
    AsRequested = 2
    Never = 0

class CalculateParticipationFactorResult(Enum):
    """
    Specifies the CalculateParticipationFactorResult.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class ChartGridlines(Enum):
    """
    Specifies the ChartGridlines.
    """

    BothAxis = 0
    NoAxis = 3
    XAxis = 1
    YAxis = 2

class ChartModalType(Enum):
    """
    Specifies the ChartModalType.
    """

    Histogram = 1
    RootLocus = 2

class ChartPlotStyle(Enum):
    """
    Specifies the ChartPlotStyle.
    """

    Both = 2
    Lines = 0
    Points = 1

class ChartReportType(Enum):
    """
    Specifies the ChartReportType.
    """

    ChartAndTabularData = 3
    ChartOnly = 2
    None_ = 4
    TabularDataOnly = 1

class ChartScale(Enum):
    """
    Specifies the ChartScale.
    """

    Linear = 0
    LogLog = 3
    SemiLogX = 1
    SemiLogY = 2

class CombineRestartFilesType(Enum):
    """
    Specifies the CombineRestartFilesType.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class CommandEditorTarget(Enum):
    """
    Specifies the CommandEditorTarget.
    """

    ABAQUS = 5
    ANSYS = 1
    LSDYNA = 3
    MBD = 2
    SAMCEF = 4
    UNKNOWN = 0

class CondensedPartCMSAttachmentMethod(Enum):
    """
    Specifies the CondensedPartCMSAttachmentMethod.
    """

    FixedMaster = 1
    Orthogonalization = 2
    ProgramControlled = 0

class CondensedPartExpansionType(Enum):
    """
    Specifies the CondensedPartExpansionType.
    """

    MechanicalAPDL = 2
    OnDemand = 1
    ProgramControlled = 0

class CondensedPartFileFormat(Enum):
    """
    Specifies the CondensedPartFileFormat.
    """

    ExportedCondensedPart_CPA = 0
    SuperElement_MATRIX = 2
    GenerationPassOutput_SUB = 1

class CondensedPartInterfaceMethod(Enum):
    """
    Specifies the CondensedPartInterfaceMethod.
    """

    Fixed = 0
    Free = 1
    ResidualFlexibleFree = 2

class CondensedPartKeepFilesFor(Enum):
    """
    Specifies the CondensedPartKeepFilesFor.
    """

    UsePassOnly = 0
    MAPDLExpansion = 2
    OnDemandExpansion = 1

class CondensedPartLumpedMassFormulation(Enum):
    """
    Specifies the CondensedPartLumpedMassFormulation.
    """

    Off = 1
    On = 2
    ProgramControlled = 0

class CondensedPartPhysics(Enum):
    """
    Specifies the CondensedPartPhysics.
    """

    Structural = 0
    Thermal = 1

class CondensedPartPointMassTreatment(Enum):
    """
    Specifies the CondensedPartPointMassTreatment.
    """

    Internal = 0
    OnInterface = 1

class CondensedPartReductionMethod(Enum):
    """
    Specifies the CondensedPartReductionMethod.
    """

    CMS = 0
    Guyan = 1

class ConnectionCreationMethod(Enum):
    """
    Specifies the ConnectionCreationMethod.
    """

    InputFile = 0
    Manual = 1

class ConnectionOptions(Enum):
    """
    Specifies the ConnectionOptions.
    """

    AllToAll = 1
    FreeToAll = 2
    FreeToFree = 3

class ConnectionScopingType(Enum):
    """
    Specifies the ConnectionScopingType.
    """

    BodyToBody = 0
    BodyToGround = 1

class ConstantDampingType(Enum):
    """
    Specifies the ConstantDampingType.
    """

    Manual = 1
    ProgramControlled = 0

class ContactBehavior(Enum):
    """
    Specifies the ContactBehavior.
    """

    Asymmetric = 0
    AutoAsymmetric = 2
    ProgramControlled = 3
    Symmetric = 1

class ContactBoltThreadHand(Enum):
    """
    Specifies the ContactBoltThreadHand.
    """

    LeftHand = 1
    RightHand = 0

class ContactBoltThreadType(Enum):
    """
    Specifies the ContactBoltThreadType.
    """

    DoubleThread = 1
    SingleThread = 0
    TripleThread = 2

class ContactConstraintType(Enum):
    """
    Specifies the ContactConstraintType.
    """

    DistributedAllDirections = 0
    DistributedAnywhereInsidePinball = 1
    DistributedNormalOnly = 5
    ProgramControlled = 3
    ProjectedDisplacementOnly = 4
    ProjectedUncoupleUtoROT = 2

class ContactCorrection(Enum):
    """
    Specifies the ContactCorrection.
    """

    Bolt = 2
    No = 0
    Smoothing = 1

class ContactDetection(Enum):
    """
    Specifies the ContactDetection.
    """

    ProximityBased = 1
    Trajectory = 0

class ContactDetectionPoint(Enum):
    """
    Specifies the ContactDetectionPoint.
    """

    NodalNormalFromContact = 2
    NodalNormalToTarget = 3
    NodalProjectedNormalFromContact = 4
    OnGaussPoint = 1
    ProgramControlled = 0
    Combined = 6
    NodalDualShapeFunctionProjection = 5

class ContactEdgeEdgeOption(Enum):
    """
    Specifies the ContactEdgeEdgeOption.
    """

    IfNoEdgeFace = 2
    No = 0
    Yes = 1

class ContactElasticSlipToleranceType(Enum):
    """
    Specifies the ContactElasticSlipToleranceType.
    """

    Factor = 2
    ProgramControlled = 0
    Value = 1

class ContactFaceEdgeOption(Enum):
    """
    Specifies the ContactFaceEdgeOption.
    """

    No = 0
    OnlyBeamBodyEdges = 4
    OnlySolidBodyEdges = 2
    OnlySurfaceBodyEdges = 3
    Yes = 1

class ContactFaceEdgePriority(Enum):
    """
    Specifies the ContactFaceEdgePriority.
    """

    EdgeOverFace = 2
    FaceOverEdge = 1
    IncludeAll = 0

class ContactForceType(Enum):
    """
    Specifies the ContactForceType.
    """

    Normal = 1
    Tangent = 2
    Total = 0

class ContactFormulation(Enum):
    """
    Specifies the ContactFormulation.
    """

    AugmentedLagrange = 0
    Beam = 4
    NormalLagrange = 3
    MPC = 2
    ProgramControlled = 6
    PureLagrange = 5
    PurePenalty = 1

class ContactGroupingType(Enum):
    """
    Specifies the ContactGroupingType.
    """

    Bodies = 1
    Faces = 3
    Parts = 2
    None_ = 0

class ContactInitialEffect(Enum):
    """
    Specifies the ContactInitialEffect.
    """

    AddOffsetNoRamping = 4
    AddOffsetRampedEffects = 0
    AdjustToTouch = 1
    OffsetOnlyNoRampingIgnoreInitialStatus = 9
    OffsetOnlyRampedEffectsIgnoreInitialStatus = 8
    OffsetOnlyNoRamping = 7
    OffsetOnlyRampedEffects = 6

class ContactOrientation(Enum):
    """
    Specifies the ContactOrientation.
    """

    Circle = 1
    Cylinder = 3
    Sphere = 2
    ProgramControlled = 0

class ContactPenetrationToleranceType(Enum):
    """
    Specifies the ContactPenetrationToleranceType.
    """

    Factor = 2
    ProgramControlled = 0
    Value = 1

class ContactPinballType(Enum):
    """
    Specifies the ContactPinballType.
    """

    AutoDetectionValue = 3
    Factor = 2
    Radius = 1
    ProgramControlled = 0

class ContactScopingType(Enum):
    """
    Specifies the ContactScopingType.
    """

    ContactSourceUnderlying = 1
    ContactTargetUnderlying = 2

class ContactSearchingType(Enum):
    """
    Specifies the ContactSearchingType.
    """

    AcrossAssemblies = 3
    AcrossBodies = 0
    AcrossFiles = 4
    AcrossParts = 1
    Anywhere = 2

class ContactSideScopingType(Enum):
    """
    Specifies the ContactSideScopingType.
    """

    Active = 4
    ContactSideBoth = 3
    ContactSourceUnderlying = 1
    SourceContactForcesProperty = 5
    ContactTargetUnderlying = 2

class ContactSmallSlidingType(Enum):
    """
    Specifies the ContactSmallSlidingType.
    """

    Adaptive = 3
    Off = 2
    On = 1
    ProgramControlled = 0

class ContactSplitType(Enum):
    """
    Specifies the ContactSplitType.
    """

    Off = 2
    On = 1
    ProgramControlled = 0

class ContactSummaryType(Enum):
    """
    Specifies the ContactSummaryType.
    """

    CNMFile = 3
    ProgramControlled = 1
    SolverOutput = 2

class ContactTimeStepControls(Enum):
    """
    Specifies the ContactTimeStepControls.
    """

    AutomaticBisection = 1
    None_ = 0
    PredictForImpact = 2
    UseImpactConstraints = 3

class ContactToleranceType(Enum):
    """
    Specifies the ContactToleranceType.
    """

    SheetThickness = 2
    Slider = 0
    Value = 1

class ContactTrimType(Enum):
    """
    Specifies the ContactTrimType.
    """

    On = 3
    Off = 2
    FaceBased = 1
    ProgramControlled = 0

class ContactType(Enum):
    """
    Specifies the ContactType.
    """

    Bonded = 1
    BondedInitial = 9
    ForcedFrictionalSliding = 11
    Frictional = 3
    Frictionless = 2
    GeneralWeld = 7
    InterStage = 12
    NoSeparation = 5
    NoSeparationSliding = 8
    Reinforcement = 10
    Rough = 4
    SpotWeld = 6

class ConvectionTableSelection(Enum):
    """
    Specifies the ConvectionTableSelection.
    """

    AmbientTemperature = 1
    FilmCoefficient = 0

class ConvergenceControlType(Enum):
    """
    Specifies the ConvergenceControlType.
    """

    Manual = 1
    ProgramControlled = 0

class ConvergenceToleranceType(Enum):
    """
    Specifies the ConvergenceToleranceType.
    """

    Remove = 2
    On = 1
    ProgramControlled = 0

class ConvergenceType(Enum):
    """
    Specifies the ConvergenceType.
    """

    Frequency = 4
    Maximum = 1
    Minimum = 0
    ForceSummation = 2
    Torque = 3

class CoordinateSystemAlignmentType(Enum):
    """
    Specifies the CoordinateSystemAlignmentType.
    """

    Associative = 1
    Component = 6
    Fixed = 0
    Free = 5
    GlobalX = 2
    GlobalY = 3
    GlobalZ = 4
    HitPoint = 7

class CoordinateSystemAxisType(Enum):
    """
    Specifies the CoordinateSystemAxisType.
    """

    NegativeXAxis = 4
    NegativeYAxis = 5
    NegativeZAxis = 6
    Origin = 0
    PositiveXAxis = 1
    PositiveYAxis = 2
    PositiveZAxis = 3

class CoordinateSystemBehavior(Enum):
    """
    Specifies the CoordinateSystemBehavior.
    """

    Manual = 1
    ProgramControlled = 0

class CoordinateSystemType(Enum):
    """
    Specifies the CoordinateSystemType.
    """

    Cartesian = 0
    Cylindrical = 1
    Spherical = 2

class CoreResultType(Enum):
    """
    Specifies the CoreResultType.
    """

    Acceleration = 27
    Displacement = 0
    OtherResult = -1
    Velocity = 39

class CoriolisEffectType(Enum):
    """
    Specifies the CoriolisEffectType.
    """

    Off = 0
    OnRotatingReferenceFrame = 2
    OnStationaryReferenceFrame = 1

class CouplingConditionDOFType(Enum):
    """
    Specifies the CouplingConditionDOFType.
    """

    XRotation = 4
    YRotation = 5
    ZRotation = 6
    Temperature = 8
    Unknown = 0
    XDisplacement = 1
    YDisplacement = 2
    ZDisplacement = 3
    Voltage = 7

class CrackGrowthIncrementType(Enum):
    """
    Specifies the CrackGrowthIncrementType.
    """

    Manual = 2
    ProgramControlled = 1

class CrackGrowthMeshCoarsening(Enum):
    """
    Specifies the CrackGrowthMeshCoarsening.
    """

    Aggressive = 2
    Conservative = 0
    Moderate = 1

class CrackGrowthMethodology(Enum):
    """
    Specifies the CrackGrowthMethodology.
    """

    CycleByCycle = 2
    LifeCyclePrediction = 1

class CrackGrowthOption(Enum):
    """
    Specifies the CrackGrowthOption.
    """

    Fatigue = 2
    Static = 1

class CrackSelectionModeType(Enum):
    """
    Specifies the CrackSelectionModeType.
    """

    AllCracks = 1
    SingleCrack = 0

class CrackShapeType(Enum):
    """
    Specifies the CrackShapeType.
    """

    Arbitrary = 2
    Corner = 5
    Cylindrical = 8
    Edge = 6
    Elliptical = 4
    Ring = 3
    SemiElliptical = 1
    Through = 7

class CrackSourceType(Enum):
    """
    Specifies the CrackSourceType.
    """

    PreMeshed = 2
    Crack = 1

class Creep(Enum):
    """
    Specifies the Creep.
    """

    Off = 2
    On = 1

class CriterionFrequencyRangeType(Enum):
    """
    Specifies the CriterionFrequencyRangeType.
    """

    Manual = 1
    UseParent = 0

class CrossSectionType(Enum):
    """
    Specifies the CrossSectionType.
    """

    UserDefined = 12
    Channel = 5
    Circular = 3
    CircularTube = 4
    HatBeam = 10
    HollowRectangular = 11
    IBeam = 8
    LBeam = 7
    MeshBeam = 13
    Quadrilateral = 2
    Rectangular = 1
    TBeam = 9
    UndefinedType = 0
    ZBeam = 6

class CyclicHarmonicIndex(Enum):
    """
    Specifies the CyclicHarmonicIndex.
    """

    Manual = 1
    ProgramControlled = 0

class DampingDefineBy(Enum):
    """
    Specifies the DampingDefineBy.
    """

    ConstantStructuralDampingCoefficient = 1
    DampingRatio = 0

class DampingType(Enum):
    """
    Specifies the DampingType.
    """

    DampingVsFrequency = 1
    DirectInput = 0

class DataImportStatus(Enum):
    """
    Specifies the DataImportStatus.
    """

    Failed = 4
    NoData = 1
    Obsolete = 2
    Unknown = 0
    Uptodate = 3

class DataTypeOptions(Enum):
    """
    Specifies the DataTypeOptions.
    """

    ForceAndMoment = 0
    ForceOnly = 1
    MomentOnly = 2

class DelaminationFailureCriteriaOption(Enum):
    """
    Specifies the DelaminationFailureCriteriaOption.
    """

    EnergyReleaseRate = 2
    JIntegral = 4
    MaterialDataTable = 1
    StressIntensityFactor = 3

class DelaminationGenerationMethod(Enum):
    """
    Specifies the DelaminationGenerationMethod.
    """

    MatchedMeshing = 2
    NodeMatching = 1
    PregeneratedInterface = 4
    SurfaceSplitting = 3

class DelaminationMethod(Enum):
    """
    Specifies the DelaminationMethod.
    """

    CZM = 2
    SMART = 3
    VCCT = 1

class DelaminationType(Enum):
    """
    Specifies the DelaminationType.
    """

    ContactDebonding = 2
    CrackGrowth = 3
    InterfaceDelamination = 1

class DiagonalOrConsistent(Enum):
    """
    Specifies the DiagonalOrConsistent.
    """

    Consistent = 2
    Diagonal = 1
    ProgramControlled = 0

class DistributedMassInputType(Enum):
    """
    Specifies the DistributedMassInputType.
    """

    MassPerUnitArea = 1
    TotalMass = 0

class DpfEvaluationType(Enum):
    """
    Specifies the DpfEvaluationType.
    """

    Off = 1
    ProgramControlled = 0
    CmsFiles = 4
    MsupFiles = 3
    ResultFiles = 2

class DropDirection(Enum):
    """
    Specifies the DropDirection.
    """

    NegativeX = 1
    NegativeY = 3
    NegativeZ = 5
    PositiveX = 0
    PositiveY = 2
    PositiveZ = 4

class DropTestDefineBy(Enum):
    """
    Specifies the DropTestDefineBy.
    """

    DropHeight = 0
    ImpactVelocity = 1

class DSCampbellAxisRange(Enum):
    """
    Specifies the DSCampbellAxisRange.
    """

    Manual = 1
    ProgramControlled = 0

class DSCampbellYAxisDataType(Enum):
    """
    Specifies the DSCampbellYAxisDataType.
    """

    Frequency = 0
    LogarithmicDecrement = 2
    ModalDampingRatio = 3
    Stability = 1

class DSRBDContactDetection(Enum):
    """
    Specifies the DSRBDContactDetection.
    """

    kCDGeometryBased = 1
    kCDMeshBased = 2
    kCDProgramControlled = 0

class DynamicRelaxationBehaviorType(Enum):
    """
    Specifies the DynamicRelaxationBehaviorType.
    """

    Both = 2
    DynamicRelaxationPhaseOnly = 1
    NormalPhaseOnly = 0

class EdgeContactType(Enum):
    """
    Specifies the EdgeContactType.
    """

    LineSegments = 2
    NodesOnEdge = 1
    ProgramControlled = 0

class EigenSolverType(Enum):
    """
    Specifies the EigenSolverType.
    """

    BlockLanczos = 5
    Damped = 4
    Lanczos = 2
    PCGLanczos = 8
    Qrdamp = 6
    Reduced = 0
    Subspace = 1
    Supernode = 7
    Unsymmetric = 3

class ElectrostaticForce(Enum):
    """
    Specifies the ElectrostaticForce.
    """

    AppliedToAirStructureInterfaceSymmetric = 2
    AppliedToAirStructureInterfaceUnsymmetric = 3
    AppliedToAllNodes = 1
    Off = 0

class ElementControl(Enum):
    """
    Specifies the ElementControl.
    """

    Manual = 1
    ProgramControlled = 0

class ElementControlsNormalStiffnessType(Enum):
    """
    Specifies the ElementControlsNormalStiffnessType.
    """

    AbsoluteValue = 2
    Factor = 1
    FromContactRegion = 0

class ElementControlsStatus(Enum):
    """
    Specifies the ElementControlsStatus.
    """

    Alive = 0
    Dead = 1

class ElementMorphingType(Enum):
    """
    Specifies the ElementMorphingType.
    """

    Off = 1
    On = 2
    ProgramControlled = 0

class ElementOrder(Enum):
    """
    Specifies the ElementOrder.
    """

    Quadratic = 2
    Linear = 1
    ProgramControlled = 0

class ElementOrientationAxisType(Enum):
    """
    Specifies the ElementOrientationAxisType.
    """

    AxisUndefined = 0
    NegativeXAxis = 4
    NegativeYAxis = 5
    NegativeZAxis = 6
    PositiveXAxis = 1
    PositiveYAxis = 2
    PositiveZAxis = 3

class ElementOrientationGuide(Enum):
    """
    Specifies the ElementOrientationGuide.
    """

    CoordinateSystemGuide = 2
    SurfaceEdgeGuide = 1

class EquationSolverType(Enum):
    """
    Specifies the EquationSolverType.
    """

    AMG = 6
    Frontal = 0
    ICCG = 3
    JCG = 1
    PCG = 2
    QMR = 7
    Sparse = 4
    Supplied = 5

class ExcitationType(Enum):
    """
    Specifies the ExcitationType.
    """

    Pressure = 0
    Velocity = 1

class ExclusionParticipantType(Enum):
    """
    Specifies the ExclusionParticipantType.
    """

    ExcludeExclusion = 1
    IncludeExclusion = 0

class ExclusionType(Enum):
    """
    Specifies the ExclusionType.
    """

    Isotropic = 0
    Orthotropic = 1

class ExpandResultFrom(Enum):
    """
    Specifies the ExpandResultFrom.
    """

    HarmonicSolution = 1
    ModalSolution = 2
    ProgramControlled = 0
    TransientSolution = 3

class ExpandResultsSubType(Enum):
    """
    Specifies the ExpandResultsSubType.
    """

    HarmonicSolution = 2
    ModalSolution = 1
    TransientSolution = 3

class ExportTopologyFileOption(Enum):
    """
    Specifies the ExportTopologyFileOption.
    """

    No = 2
    GeometryOnly = 1
    ProgramControlled = 0
    Model = 3

class ExternalEnhancedModelType(Enum):
    """
    Specifies the ExternalEnhancedModelType.
    """

    ImportedPlies = 0

class ExternalLoadApplicationType(Enum):
    """
    Specifies the ExternalLoadApplicationType.
    """

    BoundaryCondition = 1
    InitialCondition = 2

class ExternalLoadDefineActiveSequenceBy(Enum):
    """
    Specifies the ExternalLoadDefineActiveSequenceBy.
    """

    Row = 1
    Undefined = 0
    Value = 2

class ExternalLoadDisplacementType(Enum):
    """
    Specifies the ExternalLoadDisplacementType.
    """

    BoundaryPrescribedFinalGeometry = 0
    InitialFoamReferenceGeometry = 1

class ExternalLoadDisplayComponentType(Enum):
    """
    Specifies the ExternalLoadDisplayComponentType.
    """

    All = 2
    Total = 1
    Undefined = 0
    XComponent = 3
    XXComponent = 11
    XYComponent = 14
    XZComponent = 16
    YComponent = 4
    YYComponent = 12
    YZComponent = 15
    ZComponent = 5
    ZZComponent = 13

class ExternalLoadDisplayDataType(Enum):
    """
    Specifies the ExternalLoadDisplayDataType.
    """

    ConvectionCoefficient = 6
    Displacement = 8
    Force = 11
    ForceDensity = 19
    HeatFlux = 16
    HeatGeneration = 17
    MetalFraction = 20
    Pressure = 12
    Rotation = 9
    RotationPrincipals = 10
    Strain = 15
    Stress = 14
    Temperature = 7
    Thickness = 18
    Undefined = 0
    Velocity = 13

class ExtrudeBy(Enum):
    """
    To specify the method of extrusion. The available options are Use Coordinate System, Face Normal and Face Normal (Reversed).
    """

    UseCoordinateSystem = 0
    FaceNormal = 1
    FaceNormalReversed = 2

class FarFieldMicrophoneDefinitionMethodType(Enum):
    """
    Specifies the FarFieldMicrophoneDefinitionMethodType.
    """

    Coordinates = 0
    Worksheet = 1

class FarFieldRadiationSurfaceType(Enum):
    """
    Specifies the FarFieldRadiationSurfaceType.
    """

    Manual = 1
    No = 2
    ProgramControlled = 0

class FatigueLoadType(Enum):
    """
    Specifies the FatigueLoadType.
    """

    FullyReversed = 1
    HistoryData = 3
    NonProportional = 4
    Ratio = 2
    ZeroBased = 0

class FatigueToolAnalysisType(Enum):
    """
    Specifies the FatigueToolAnalysisType.
    """

    StrainLife = 1
    StressLife = 0

class FatigueToolResultsInputType(Enum):
    """
    Specifies the FatigueToolResultsInputType.
    """

    Stress = 0
    Strain = 1

class FeatureSuppressMethod(Enum):
    """
    To select the method of FeatureSuppress.
    """

    Automatic = 0
    DefeatureFaces = 1
    ParentFaces = 2

class FEConnectionDisplay(Enum):
    """
    Specifies the FEConnectionDisplay.
    """

    All = 0
    Beam = 2
    CE = 1
    Cyclic = 5
    None_ = 4
    WeakSprings = 3

class FEConnectionDisplayType(Enum):
    """
    Specifies the FEConnectionDisplayType.
    """

    Lines = 0
    LinesAndPoints = 2
    Points = 1

class FEConnectionLineColor(Enum):
    """
    Specifies the FEConnectionLineColor.
    """

    Object = 2
    Type = 0
    Manual = 1

class FixedOrFree(Enum):
    """
    Specifies the FixedOrFree.
    """

    Fixed = 0
    Free = 1
    MixedConstraints = 2

class FluidBehavior(Enum):
    """
    Specifies the FluidBehavior.
    """

    Compressible = 0
    Incompressible = 1

class FormulationType(Enum):
    """
    Specifies the FormulationType.
    """

    SmallRotation = 1
    Joint = 2
    ProgramControlled = 0

class FractureToolScopeType(Enum):
    """
    Specifies the FractureToolScopeType.
    """

    CrackSelection = 1
    ResultFileItem = 0

class FrequencyReductionType(Enum):
    """
    Specifies the FrequencyReductionType.
    """

    Average = 0

class FrequencySpacingType(Enum):
    """
    Specifies the FrequencySpacingType.
    """

    Linear = 0
    Logarithmic = 1
    OctaveBand1 = 2
    OctaveBand12 = 6
    OctaveBand2 = 3
    OctaveBand24 = 7
    OctaveBand3 = 4
    OctaveBand6 = 5
    OrderBased = 8

class FutureIntentType(Enum):
    """
    Specifies the FutureIntentType.
    """

    HarmonicAnalysis = 2
    ModeSuperpositionAnalysis = 7
    MotionAnalysis = 17
    PrestressedFullHarmonicAnalysis = 9
    PrestressedAnalysis = 4
    PreStressModeSuperpositionAnalysis = 8
    PSDAnalysis = 1
    RBDTransientAnalysis = 10
    RSAnalysis = 6
    TopologyOptimization = 11
    TransientAnalysis = 3
    None_ = 0
    RestartFiles = 5

class GasketResultType(Enum):
    """
    Specifies the GasketResultType.
    """

    NormalGasket = 0
    ShearGasket = 1

class GeneralMiscellaneousOptionType(Enum):
    """
    Specifies the GeneralMiscellaneousOptionType.
    """

    AcousticBodies = 3
    AllBodies = 1
    ProgramControlled = 0
    StructuralBodies = 2

class GeometryDefineByType(Enum):
    """
    Specifies the GeometryDefineByType.
    """

    AllOptimizationRegions = 23
    AnalysisPly = 13
    BeamConnection = 19
    BoundaryCondition = 15
    Component = 1
    ContactRegion = 14
    Coordinates = 11
    Fracture = 9
    FreeStanding = 17
    Geometry = 0
    ImportedAssembly = 12
    ImportedCondensedPart = 29
    ImportedInterface = 10
    ImportedPretension = 21
    Mapping = 8
    NamedSelections = 30
    OptimizationRegion = 16
    Path = 6
    RemotePoint = 5
    RemotePointAndNodes = 22
    ResultFileItem = 18
    Surface = 7
    SurfaceCoating = 20
    VoltageCoupling = 28
    Worksheet = 2
    MaximumValues = 4
    MinimumValues = 3

class GraphControlsXAxis(Enum):
    """
    Specifies the GraphControlsXAxis.
    """

    Frequency = 3
    Mode = 2
    Phase = 4
    S = 1
    Time = 0

class GravityOrientationType(Enum):
    """
    Specifies the GravityOrientationType.
    """

    NegativeXAxis = 1
    NegativeYAxis = 3
    NegativeZAxis = 5
    PositiveXAxis = 0
    PositiveYAxis = 2
    PositiveZAxis = 4

class GrowElbowElementsBy(Enum):
    """
    Specifies the GrowElbowElementsBy.
    """

    Factor = 1
    Length = 2
    NumberOfElements = 3
    No = 0

class HarmonicMethod(Enum):
    """
    Specifies the HarmonicMethod.
    """

    Full = 1
    Krylov = 3
    ModeSuperposition = 0
    ProgramControlled = -1
    VariationalTechnology = 2

class HarmonicMSUPStorage(Enum):
    """
    Specifies the HarmonicMSUPStorage.
    """

    AllFrequencies = 0
    SelectedFrequencies = 1

class HarmonicMultiStepType(Enum):
    """
    Specifies the HarmonicMultiStepType.
    """

    Load_Step = 1
    RPM = 0

class HexIntegrationType(Enum):
    """
    Specifies the HexIntegrationType.
    """

    OnePtGauss = 1
    Exact = 0

class HourglassDampingType(Enum):
    """
    Specifies the HourglassDampingType.
    """

    AutodynStandard = 0
    FlanaganBelytschko = 1

class HyperbolicProjectionType(Enum):
    """
    Specifies the HyperbolicProjectionType.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class ImportedCondensedPartStatus(Enum):
    """
    Specifies the ImportedCondensedPartStatus.
    """

    FileSelectionRequired = 0
    ImportFailed = 3
    ImportRequired = 1
    ImportSuccessful = 2

class ImportedLoadType(Enum):
    """
    Specifies the ImportedLoadType.
    """

    ImportedConvection = 2
    ImportedDisplacement = 14
    ImportedDisplacementAndRotation = 18
    ElementOrientation = 9
    ImportedHeatGeneration = 4
    FiberRatio = 12
    ImportedForce = 15
    BodyForceDensity = 8
    ImportedHeatFlux = 7
    ImportedLatticeKnockdownFactor = 31
    ImportedMaterialField = 30
    ImportedTrace = 26
    ImportedPressure = 0
    ImportedCutBoundaryRemoteConstraint = 28
    ImportedCutBoundaryRemoteForce = 27
    ImportedInitialStrain = 20
    ImportedInitialStress = 19
    SurfaceForceDensity = 13
    ImportedTemperature = 1
    ImportedBodyTemperature = 3
    ImportedThickness = 6
    ImportedVelocity = 16
    WarpWeftRatio = 11
    YarnAngle = 10

class IncidentWaveLocation(Enum):
    """
    Specifies the IncidentWaveLocation.
    """

    InsideTheModel = 1
    OutsideTheModel = 0

class InitialClearanceType(Enum):
    """
    Specifies the InitialClearanceType.
    """

    Factor = 2
    ProgramControlled = 0
    Value = 1

class InitialConditionsType(Enum):
    """
    Specifies the InitialConditionsType.
    """

    Acceleration = 3
    AtRest = 1
    DropHeight = 6
    Environment = 5
    AngularVelocity = 4
    Unknown = 0
    Velocity = 2

class InitializationModifierType(Enum):
    """
    Specifies the InitializationModifierType.
    """

    Holes = 1
    None_ = 0

class InitialTemperatureType(Enum):
    """
    Specifies the InitialTemperatureType.
    """

    NonUniform = 1
    Uniform = 0

class JointFormulation(Enum):
    """
    Specifies the JointFormulation.
    """

    Bushing = 1
    MPC = 0

class JointFrictionType(Enum):
    """
    Specifies the JointFrictionType.
    """

    ProgramControlled = 0
    ForcedFrictionalSliding = 2
    FrictionWithTransitions = 1

class JointGeneralPrimitiveType(Enum):
    """
    Specifies the JointGeneralPrimitiveType.
    """

    InLine = 3
    InPlane = 2
    None_ = 0
    Orientation = 4
    Parallel = 1

class JointInitialPosition(Enum):
    """
    Specifies the JointInitialPosition.
    """

    Override = 1
    Unchanged = 0

class JointRotationDOFType(Enum):
    """
    Specifies the JointRotationDOFType.
    """

    FixAll = 0
    FreeX = 1
    FreeAll = 4
    FreeY = 2
    FreeZ = 3

class JointScopingType(Enum):
    """
    Specifies the JointScopingType.
    """

    BodyToBody = 0
    BodyToGround = 1

class JointSolverElementType(Enum):
    """
    Specifies the JointSolverElementType.
    """

    ContactDirect = 2
    Element = 1
    ProgramControlled = 0

class JointStopType(Enum):
    """
    Specifies the JointStopType.
    """

    Lock = 2
    None_ = 0
    Stop = 1

class JointType(Enum):
    """
    Specifies the JointType.
    """

    RadialGap3D = 13
    Bushing = 9
    ConstantVelocity = 17
    Cylindrical = 4
    Distance = 18
    Fixed = 0
    General = 8
    Planar = 7
    PlaneRadialGap = 11
    PointOnCurve = 10
    Revolute = 1
    Screw = 16
    Slot = 3
    Spherical = 6
    SphericalGap = 12
    Translational = 2
    Universal = 5

class KinematicDOF(Enum):
    """
    Specifies the KinematicDOF.
    """

    RotationX = 4
    RotationY = 5
    RotationZ = 6
    XDisplacement = 1
    YDisplacement = 2
    ZDisplacement = 3

class LatticeType(Enum):
    """
    Specifies the LatticeType.
    """

    Crossed = 6
    Cubic = 1
    Diagonal = 5
    Midpoint = 3
    None_ = 0
    Octahedral1 = 7
    Octahedral2 = 8
    Octet = 4
    Sphere = 2

class LimitBCDirection(Enum):
    """
    Specifies the LimitBCDirection.
    """

    All = 3
    X = 0
    Y = 1
    Z = 2

class Linearized2DBehavior(Enum):
    """
    Specifies the Linearized2DBehavior.
    """

    AxisymmetricCurve = 2
    AxisymmetricStraight = 1
    Planar = 0

class LinearizedSubtype(Enum):
    """
    Specifies the LinearizedSubtype.
    """

    All = 0
    Bending = 2
    Membrane = 1
    MembraneBending = 3
    Peak = 4
    Total = 5

class LineLineContactDetectionType(Enum):
    """
    Specifies the LineLineContactDetectionType.
    """

    External8Segments = 2
    External4Segments = 1
    External1Segment = 0
    InternalPipe = 3

class LinePressureResultBasedOnType(Enum):
    """
    Specifies the LinePressureResultBasedOnType.
    """

    NodalForce = 1
    NormalGasketPressure = 0

class LineSearchType(Enum):
    """
    Specifies the LineSearchType.
    """

    Off = 2
    On = 1
    ProgramControlled = 0

class LoadAppliedBy(Enum):
    """
    Specifies the LoadAppliedBy.
    """

    Direct = 1
    SurfaceEffect = 0

class LoadBehavior(Enum):
    """
    Specifies the LoadBehavior.
    """

    Beam = 2
    Coupled = 3
    Deformable = 1
    Rigid = 0

class LoadDefineBy(Enum):
    """
    Specifies the LoadDefineBy.
    """

    ComplexComponents = 6
    ComplexVector = 7
    ComplexNormalTo = 8
    Components = 0
    ComponentX = 3
    ComponentY = 4
    ComponentZ = 5
    Vector = 1
    NormalToOrTangential = 2
    TableAssignment = 11
    UnknownDefined = -1

class LoadedArea(Enum):
    """
    Specifies the LoadedArea.
    """

    Deformed = 0
    Initial = 1

class LoadGroupingType(Enum):
    """
    Specifies the LoadGroupingType.
    """

    ByLocation = 1
    No = 0

class LoadingApplicationType(Enum):
    """
    Specifies the LoadingApplicationType.
    """

    LoadVector = 0
    Table = 1

class LoadVariableVariationType(Enum):
    """
    Specifies the LoadVariableVariationType.
    """

    Acceleration = 201
    Reactance = 843
    Resistance = 842
    AxisComponentX = 767
    AxisComponentY = 768
    AxisComponentZ = 769
    AxisLocationX = 764
    AxisLocationY = 765
    AxisLocationZ = 766
    BearingDampingC11 = 780
    BearingDampingC12 = 782
    BearingDampingC21 = 783
    BearingDampingC22 = 781
    BearingPropertiesBegin = 775
    BearingPropertiesEnd = 784
    BearingStiffnessK11 = 776
    BearingStiffnessK12 = 778
    BearingStiffnessK21 = 779
    BearingStiffnessK22 = 777
    Behavior = 1014
    BoltBegin = 575
    BoltEnd = 580
    BoltIncrement = 579
    BoltLoadDefineBy = 576
    BulkTemperature = 303
    BushingNonlinStiffness = 754
    Capacitance = 308
    ComponentX = 151
    ComponentY = 152
    ComponentZ = 153
    ConvectionCoefficient = 302
    Current = 402
    HarmonicIndex = 47
    SectorNumber = 48
    Damping = 211
    DependentDataIndex = 676
    DependentsBegin = 150
    DependentsEnd = 678
    Displacement = 202
    ElementFace = 20
    ElementType = 21
    EMagBegin = 400
    EMagEnd = 403
    Emissivity = 307
    End = 1010
    Energy = 215
    EntityId = 19
    ExternalBegin = 600
    ExternalEnd = 619
    ExternalEnhancedModelBegin = 650
    ExternalEnhancedModelEnd = 668
    ExternalImagValue = 605
    ExternalImagValueX = 613
    ExternalImagValueY = 614
    ExternalImagValueZ = 615
    ExternalImagVectorI = 606
    ExternalImagVectorJ = 607
    ExternalImagVectorK = 608
    ExternalRealValue = 601
    ExternalRealValueX = 610
    ExternalRealValueX2 = 616
    ExternalRealValueY = 611
    ExternalRealValueY2 = 617
    ExternalRealValueZ = 612
    ExternalRealValueZ2 = 618
    ExternalRealVectorI = 602
    ExternalRealVectorJ = 603
    ExternalRealVectorK = 604
    ExternalTemperature = 609
    ExtLayeredSectionID = 45
    ExtLayeredSectionOffset = 652
    FluidBegin = 500
    FluidDensity = 501
    FluidEnd = 503
    Force = 203
    ForceIntensity = 209
    FoundationStiffness = 210
    Frequency = 16
    Friction = 212
    GraphEnd = 1013
    GraphPSDFittedValue = 1012
    HeatFlow = 304
    HeatFlux = 306
    HeatGenerationRate = 305
    IndependentsBegin = 10
    IndependentsEnd = 49
    IndexBegin = 675
    IndexEnd = 677
    LocationX = 1019
    LocationY = 1020
    LocationZ = 1021
    Mass = 214
    MassFlowRate = 502
    MaterialID = 651
    Moment = 204
    NodeId0 = 23
    NodeId1 = 24
    NodeId10 = 33
    NodeId11 = 34
    NodeId12 = 35
    NodeId13 = 36
    NodeId14 = 37
    NodeId15 = 38
    NodeId16 = 39
    NodeId17 = 40
    NodeId18 = 41
    NodeId19 = 42
    NodeId2 = 25
    NodeId3 = 26
    NodeId4 = 27
    NodeId5 = 28
    NodeId6 = 29
    NodeId7 = 30
    NodeId8 = 31
    NodeId9 = 32
    NonlinearAdaptivity = 801
    NonlinearAdaptivityBegin = 800
    NonlinearAdaptivityEnd = 802
    NonlinearStiffnessBegin = 752
    NonlinearStiffnessEnd = 755
    NormalizedS = 44
    Offset = 155
    PathLength = 43
    PhaseAngle = 18
    Preadjustment = 578
    Preload = 577
    Pressure = 205
    PSDAcceleration = 552
    PSDBegin = 550
    PSDDisplacement = 553
    PSDEnd = 555
    PSDGAcceleration = 551
    PSDVelocity = 554
    RefId = 22
    RotatingForceBegin = 760
    RotatingForceEnd = 771
    RotatingRadius = 770
    Rotation = 206
    RotationalAcceleration = 213
    RotationalVelocity = 207
    RotationX = 1016
    RotationY = 1017
    RotationZ = 1018
    RSAcceleration = 702
    RSBegin = 700
    RSDisplacement = 703
    RSEnd = 705
    RSGAcceleration = 701
    RSVelocity = 704
    Scale = 154
    Sector = 15
    ShellThickness = 750
    ShellThicknessEnd = 751
    SpringNonLinearStiffness = 753
    Step = 17
    StructuralBegin = 200
    StructuralEnd = 224
    SynchronousRatio = 763
    Temperature = 301
    ThermalBegin = 300
    ThermalCompliance = 309
    ThermalEnd = 310
    Time = 11
    UnbalancedForce = 762
    UnbalancedMass = 761
    Value = 1015
    Velocity = 208
    Voltage = 401
    XValue = 12
    YValue = 13
    ZValue = 14

class LoadVariationSubOption(Enum):
    """
    Specifies the LoadVariationSubOption.
    """

    BulkTemperature = 4
    DifferenceOfSurfaceAndBulkTemperature = 5
    ConvectionEnd = 6
    AverageFilmTemperature = 2
    SurfaceTemperature = 3

class LoadVariationType(Enum):
    """
    Specifies the LoadVariationType.
    """

    ConstantOrHeatFlow = 0
    TemperatureDependent = 3
    LoadHistoryOrHeatFlow = 1
    PerfectInsulation = 2
    CFXResults = 4

class LoadVectorAssignment(Enum):
    """
    Specifies the LoadVectorAssignment.
    """

    LoadVectorAssignment_Manual = 1
    LoadVectorAssignment_ProgramControlled = 0

class LowReducedFrequencyModelType(Enum):
    """
    Specifies the LowReducedFrequencyModelType.
    """

    CircularTube = 2
    RectangularTube = 1
    ThinLayer = 0

class ManualContactTreatmentType(Enum):
    """
    Specifies the ManualContactTreatmentType.
    """

    Lumped = 0
    Pairwise = 1

class ManufacturingConstraintSubtype(Enum):
    """
    Specifies the ManufacturingConstraintSubtype.
    """

    ComplexityIndexConstraint = 9
    CyclicManufacturingConstraint = 3
    ExtrusionManufacturingConstraint = 2
    HousingConstraint = 8
    MemberSizeManufacturingConstraint = 0
    OverhangAngleManufacturingConstraint = 5
    PatternRepetitionConstraint = 7
    PullOutDirectionManufacturingConstraint = 1
    SymmetryManufacturingConstraint = 4
    UniformConstraint = 6

class ManuMemberSizeControlledType(Enum):
    """
    Specifies the ManuMemberSizeControlledType.
    """

    Free = 2
    Manual = 1
    ProgramControlled = 0

class MaterialPolarizationDirection(Enum):
    """
    Specifies the MaterialPolarizationDirection.
    """

    NegativeXDirection = 1
    PositiveXDirection = 0

class MeshControlPinchGeomtryType(Enum):
    """
    Specifies the MeshControlPinchGeomtryType.
    """

    AddPinchMaster = 1
    AddPinchSlave = 3
    SetPinchMaster = 0
    SetPinchSlave = 2

class MeshDisplayStyle(Enum):
    """
    Specifies the MeshDisplayStyle.
    """

    AspectRatio = 2
    ElementQuality = 1
    AspectRatioEXD = 21
    CharacteristicLengthLSD = 24
    Hydrodynamics = 13
    JacobianRatio = 3
    JacobianRatioCornerNodes = 11
    JacobianRatioGaussPoints = 12
    KnockdownFactor = 14
    MaxEdgeLength = 23
    MaximumCornerAngle = 6
    MaxQuadAngle = 18
    MaxTriAngle = 16
    MinEdgeLength = 22
    CharacteristicLength = 10
    MinQuadAngle = 17
    MinTriAngle = 15
    OrthogonalQuality = 8
    ParallelDeviation = 5
    ShellThickness = 9
    Skewness = 7
    TetCollapse = 20
    WarpingAngle = 19
    WarpingFactor = 4

class MeshFlowControlMethod(Enum):

    GlobalCartesian = 2
    None_ = 1
    ProgramControlled = 0

class MeshInflationElementType(Enum):

    Tets = 1
    Wedges = 0

class MeshMetricType(Enum):
    """
    Specifies the MeshMetricType.
    """

    AspectRatio = 2
    ElementQuality = 1
    AspectRatioEXD = 19
    CharacteristicLengthLSD = 22
    Hydrodynamics = 12
    JacobianRatio = 3
    JacobianRatioCornerNodes = 10
    JacobianRatioGaussPoints = 11
    MaxEdgeLength = 21
    MaximumCornerAngle = 6
    MaxQuadAngle = 16
    MaxTriAngle = 14
    MinEdgeLength = 20
    CharacteristicLength = 9
    MinQuadAngle = 15
    MinTriAngle = 13
    None_ = 0
    OrthogonalAngle = 8
    ParallelDeviation = 5
    Skewness = 7
    TetCollapse = 18
    WarpingAngle = 17
    WarpingFactor = 4

class MeshRestartControlsType(Enum):
    """
    Specifies the MeshRestartControlsType.
    """

    Manual = 1
    ProgramControlled = 0

class MeshRestartRetainFilesType(Enum):
    """
    Specifies the MeshRestartRetainFilesType.
    """

    No = 1
    Yes = 0

class MeshRestartSaveAtLoadStep(Enum):
    """
    Specifies the MeshRestartSaveAtLoadStep.
    """

    All = 2
    Last = 1
    None_ = 0

class MeshRestartSaveAtSubstep(Enum):
    """
    Specifies the MeshRestartSaveAtSubstep.
    """

    All = 2
    Last = 1
    SaveAtSubstepSpecified = 3

class MeshSourceType(Enum):
    """
    Specifies the MeshSourceType.
    """

    Mechanical = 1
    ProgramControlled = 0
    ResultFile = 2

class MethodMeshType(Enum):

    Quad = 1
    Triangle = 0

class MinimumOrMaximum(Enum):
    """
    Specifies the MinimumOrMaximum.
    """

    Maximum = 1
    Minimum = 0

class ModalFrequencyRangeType(Enum):
    """
    Specifies the ModalFrequencyRangeType.
    """

    Manual = 1
    ProgramControlled = 0

class Model2DBehavior(Enum):
    """
    Specifies the Model2DBehavior.
    """

    AxiSymmetric = 1
    ByBody = 4
    GeneralAxisymmetric = 5
    GeneralizedPlaneStrain = 3
    MeshExtrude = 6
    PlaneStrain = 2
    PlaneStress = 0

class ModelImportUnitSystemType(Enum):
    """
    To select the Unit System Type for the Model Import File being imported.
    """

    UnitSystemConsistentBFT = 12
    UnitSystemConsistentBIN = 11
    UnitSystemConsistentCGS = 7
    UnitSystemConsistentNMM = 8
    UnitSystemConsistentNMMKGMMMS = 10
    UnitSystemConsistentuMKS = 9
    UnitSystemMetricCGS = 3
    UnitSystemMetricMKS = 1
    UnitSystemMetricNMM = 4
    UnitSystemMetricNMMDton = 6
    UnitSystemMetricNMMton = 2
    UnitSystemMetricUMKS = 5
    UnitSystemSI = 0

class ModelType(Enum):
    """
    Specifies the ModelType.
    """

    Type_2_5YAxisRotationExtrusion = 2
    Type_2_5DZDirectionExtrusion = 1
    Type_3D = 0
    Type_VibratingStructuralPanel = 3

class ModesCombinationType(Enum):
    """
    Specifies the ModesCombinationType.
    """

    CQC = 2
    NONE = 0
    ROSE = 3
    SRSS = 1

class ModeSelectionMethod(Enum):
    """
    Specifies the ModeSelectionMethod.
    """

    ModalEffectiveMass = 1
    None_ = 0

class MPIType(Enum):
    """
    Specifies the MPIType.
    """

    INTELMPI = 1
    MSMPI = 2
    PCMPI = 0

class MultiOptimTypeStrategyType(Enum):
    """
    Specifies the MultiOptimTypeStrategyType.
    """

    Off = 2
    On = 1
    ProgramControlled = 0

class MultipleNodeType(Enum):
    """
    Specifies the MultipleNodeType.
    """

    Average = 2
    Maximum = 1
    Minimum = 0

class NewtonRaphsonType(Enum):
    """
    Specifies the NewtonRaphsonType.
    """

    Full = 2
    Modified = 3
    ProgramControlled = 1
    Unsymmetric = 4

class NLADControlProjectToGeometry(Enum):
    """
    Specifies the NLADControlProjectToGeometry.
    """

    No = 0
    Yes = 1

class NodalPlanesVisible(Enum):
    """
    Specifies the NodalPlanesVisible.
    """

    All = 0
    Range = 1

class NodeAndElementRenumberingMethodType(Enum):
    """
    To select the method of Node And Element Renumbering under the Model Import Object.
    """

    Automatic = 0
    Offset = 1

class NodeMergeToleranceMethod(Enum):
    """
    To select the method of AutoNodeMove under PCTet.
    """

    AbsoluteValue = 2
    PercentageOfElementSize = 1
    ProgramControlled = 0

class NonCyclicLoadingType(Enum):
    """
    Specifies the NonCyclicLoadingType.
    """

    HarmonicIndex = 1
    SectorNumber = 2
    No = 0

class NonlinearAdaptivityControlsRefinementAlgorithmType(Enum):
    """
    Specifies the NonlinearAdaptivityControlsRefinementAlgorithmType.
    """

    GeneralRemeshing = 0
    MeshSplitting = 1

class NonlinearAdaptivityControlsRemeshingGradientType(Enum):
    """
    Specifies the NonlinearAdaptivityControlsRemeshingGradientType.
    """

    NoGradient = 0
    AverageGradient = 1
    PerfectShapeGradient = 2
    PracticalShapeGradient = 3

class NonlinearAdaptivityCriterionType(Enum):
    """
    Specifies the NonlinearAdaptivityCriterionType.
    """

    AMOctree = 5
    Box = 3
    Energy = 2
    Mesh = 4
    Undefined = 0

class NonlinearAdaptivityOptionType(Enum):
    """
    Specifies the NonlinearAdaptivityOptionType.
    """

    JacobianRatio = 3
    Shape = 2
    Skewness = 1
    SkewnessAndJacobianRatio = 4

class NonlinearAdaptivityUpdateType(Enum):
    """
    Specifies the NonlinearAdaptivityUpdateType.
    """

    SpecifiedRecurrenceRate = 1
    EquallySpacedPoints = 2

class NonLinearFormulationType(Enum):
    """
    Specifies the NonLinearFormulationType.
    """

    Full = 1
    ProgramControlled = 0
    Quasi = 2

class NormalOrientationType(Enum):
    """
    Specifies the NormalOrientationType.
    """

    None_ = -99
    Total = 7
    XAxis = 0
    XYAxis = 3
    XYZAxis = 6
    XZAxis = 4
    YAxis = 1
    YZAxis = 5
    ZAxis = 2

class OnDemandExpansionType(Enum):
    """
    Specifies the OnDemandExpansionType.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class OptimizationResponseConstraintComponentType(Enum):
    """
    Specifies the OptimizationResponseConstraintComponentType.
    """

    XComponentMax = 0
    YComponentMax = 1
    ZComponentMax = 2

class OptimizationType(Enum):
    """
    Specifies the OptimizationType.
    """

    Lattice = 2
    TopologyLevelSet = 3
    MixableDensity = 5
    Shape = 4
    Topography = 6
    TopologyDensity = 1

class OutputControlsNodalForcesType(Enum):
    """
    Specifies the OutputControlsNodalForcesType.
    """

    ConstrainNode = 2
    No = 0
    Yes = 1

class PanelsToDisplayType(Enum):
    """
    Specifies the PanelsToDisplayType.
    """

    All = -1
    Top10 = 1
    Top20 = 2
    Top5 = 0

class PartTransformationDefinitionType(Enum):
    """
    Specifies the PartTransformationDefinitionType.
    """

    CoordinateSystem = 2
    RotationAndTranslation = 1

class PassFailResult(Enum):
    """
    Specifies the PassFailResult.
    """

    FailedAbove = 1
    FailedBelow = 0
    PassedAbove = 3
    PassedBelow = 2
    Unknown = 4

class PathScopingType(Enum):
    """
    Specifies the PathScopingType.
    """

    Edge = 1
    Offset = 3
    Points = 0
    Ray = 2

class PeriodicApplyTo(Enum):
    """
    Specifies the PeriodicApplyTo.
    """

    ApplicableDOF = 0
    Displacement = 1
    Voltage = 2

class PFactorResultType(Enum):
    """
    Specifies the PFactorResultType.
    """

    CumulativeEffectiveMassRatio = 2
    EffectiveMass = 1
    ParticipationFactor = 0
    PFactorAll = 3

class PilotNodeScopingType(Enum):
    """
    Specifies the PilotNodeScopingType.
    """

    Point = 1
    CoordinateSystem = 0

class PinBehavior(Enum):
    """
    Specifies the PinBehavior.
    """

    PinAcceleration = 2
    PinForce = 3
    PinPosition = 0
    PinVelocity = 1

class PipeLoadingType(Enum):
    """
    Specifies the PipeLoadingType.
    """

    External = 2
    Internal = 1

class PMLOptions(Enum):
    """
    Specifies the PMLOptions.
    """

    PML1D = 1
    PML3D = 0

class PortAttribution(Enum):
    """
    Specifies the PortAttribution.
    """

    Inlet = 0
    Outlet = 1

class PortBehavior(Enum):
    """
    Specifies the PortBehavior.
    """

    Transparent = 1
    Vibro = 0

class PortPosition(Enum):
    """
    Specifies the PortPosition.
    """

    Exterior = 0
    Interior = 1

class PressureAtZeroPenetrationType(Enum):
    """
    Specifies the PressureAtZeroPenetrationType.
    """

    Factor = 2
    ProgramControlled = 0
    Value = 1

class PressureInitializationType(Enum):
    """
    Specifies the PressureInitializationType.
    """

    FromDeformedState = 0
    FromStressTrace = 1

class PreStressContactStatus(Enum):
    """
    Specifies the PreStressContactStatus.
    """

    ForceBonded = 3
    ForceSticking = 2
    UseTrueStatus = 1

class PreStressLoadControl(Enum):
    """
    Specifies the PreStressLoadControl.
    """

    KeepAll = 0
    KeepAllDisplacementsAsZero = 3
    KeepInertiaAndDisplacementConstraints = 1
    DeleteAll = 4
    KeepDisplacementConstraints = 2

class PreStressMode(Enum):
    """
    Specifies the PreStressMode.
    """

    Displacements = 1
    MaterialState = 0

class PreStressStateType(Enum):
    """
    Specifies the PreStressStateType.
    """

    LoadStep = 2
    ProgramControlled = 1
    Time = 3

class ProbeDisplayFilter(Enum):
    """
    Specifies the ProbeDisplayFilter.
    """

    All = 0
    AxialForce = 25
    DampingForce1 = 41
    DampingForce2 = 42
    Elongation1 = 37
    Elongation2 = 38
    ElasticForce1 = 35
    ElasticForce2 = 36
    Velocity1 = 39
    Velocity2 = 40
    CoEnergy = 24
    Components = 1
    Contact = 46
    Damping = 47
    Dissipative = 17
    EmittedRadiation = 32
    Equivalent = 13
    External = 22
    Hourglass = 45
    IncidentRadiation = 34
    Intensity = 12
    Internal = 43
    Kinetic = 15
    MaximumPrincipal = 11
    MiddlePrincipal = 10
    MinimumPrincipal = 9
    MomentAtI = 29
    MomentAtJ = 30
    NetRadiation = 31
    PlasticWork = 44
    Potential = 16
    Principals = 2
    ReflectedRadiation = 33
    ShearForceAtI = 26
    ShearForceAtJ = 27
    SpringDampingForce = 21
    SpringElongation = 19
    SpringForce = 18
    SpringVelocity = 20
    Strain = 23
    Torque = 28
    Total = 14
    XAxis = 3
    XYPlane = 6
    XZPlane = 8
    YAxis = 4
    YZPlane = 7
    ZAxis = 5

class ProbeResultType(Enum):
    """
    Specifies the ProbeResultType.
    """

    AccelerationProbe = 11
    AngularAccelerationProbe = 19
    AngularVelocityProbe = 18
    BeamProbe = 28
    BearingProbe = 36
    ChargeReaction = 52
    ConstraintForce = 29
    ConstraintMoment = 32
    ContactDistanceProbe = 58
    CurrentDensityProbe = 25
    DampingForce = 31
    DampingMoment = 34
    DeformationProbe = 3
    MagneticFluxProbe = 27
    ElasticForce = 30
    ElasticMoment = 33
    ElasticPlusFrictionMoment = 56
    Impedance = 53
    FieldIntensity = 26
    VoltageProbe = 24
    ElectromechanicalCouplingCoefficient = 55
    EmagReactionProbe = 17
    Energy = 14
    FieldIntensityProbe = 7
    FlexibleRotationProbe = 39
    FluxDensityProbe = 6
    FrictionForceProbe = 37
    FrictionMomentProbe = 38
    GeneralizedPlaneStrainProbe = 22
    HeatFluxProbe = 5
    JointProbe = 12
    JouleHeatProbe = 40
    Position = 20
    BoltPretension = 21
    QualityFactor = 54
    RadiationProbe = 35
    ReactionProbe = 9
    ForceReaction = 15
    MomentReaction = 16
    ResponsePSD = 23
    RotationProbe = 8
    SpringProbe = 13
    ProbeStatus = 57
    StrainProbe = 2
    StressProbe = 1
    TemperatureProbe = 4
    VelocityProbe = 10
    VolumeProbe = 51

class PrototypeDisplayStyleType(Enum):
    """
    Specifies the PrototypeDisplayStyleType.
    """

    AssemblyColor = 7
    BodyColor = 0
    Material = 2
    NonLinearMaterialEffects = 3
    PartColor = 5
    StiffnessBehavior = 4
    ShellThickness = 1
    VisibleThickness = 6

class PrototypeLinkBehavior(Enum):
    """
    Specifies the PrototypeLinkBehavior.
    """

    Compression = 2
    Tension = 1
    TensionCompression = 0

class PrototypeModelType(Enum):
    """
    Specifies the PrototypeModelType.
    """

    AxisymmetricShell = 8
    Beam = 0
    Cable = 5
    ModelPhysicsTypeFluid = 1
    Link = 3
    Pipe = 2
    Reinforcement = 7
    Shell = 6

class PullMethod(Enum):
    """
    To select the method of Pull. There are three methods. They are Extrude, Revolve and Surface Coating.
    """

    Extrude = 0
    LineCoating = 3
    Revolve = 1
    SurfaceCoating = 2

class PullOutConstraintSubtype(Enum):
    """
    Specifies the PullOutConstraintSubtype.
    """

    NoHole = 2
    NoOption = 0
    Stamping = 1

class PullOutDirectionType(Enum):
    """
    Specifies the PullOutDirectionType.
    """

    BothDirections = 2
    OppositeToAxis = 1
    AlongAxis = 0

class PythonCodeTargetCallback(Enum):
    """
    Specifies the PythonCodeTargetCallback.
    """

    GetBodyCommands = 3
    GetContactCommands = 5
    GetPostCommands = 6
    GetSolveCommands = 4
    OnAfterGeometryChanged = 11
    OnAfterMeshGenerated = 9
    OnAfterObjectChanged = 8
    OnAfterPost = 7
    OnAfterSolve = 2
    OnBeforeSolve = 1
    Unknown = 0

class RandomSamplingType(Enum):
    """
    Specifies the RandomSamplingType.
    """

    All = 0
    Multiple = 1
    Single = 2

class ReactionForceCriteriaType(Enum):
    """
    Specifies the ReactionForceCriteriaType.
    """

    AbsoluteMaximum = 1
    Sum = 0

class ReferenceFrameType(Enum):
    """
    Specifies the ReferenceFrameType.
    """

    EulerianVirtual = 2
    Lagrangian = 1
    Particle = 3
    SALEDomain = 4
    SALEFill = 5

class ReflectionCoefficientsType(Enum):
    """
    Specifies the ReflectionCoefficientsType.
    """

    Manual = 1
    ProgramControlled = 0

class ReinforcingStressState(Enum):
    """
    Specifies the ReinforcingStressState.
    """

    PlaneStressOnly = 0
    PlaneStressWithTransverseShearAndBending = 2
    PlaneStressWithTransverseShear = 1

class RemoteApplicationType(Enum):
    """
    Specifies the RemoteApplicationType.
    """

    DirectAttachment = 1
    RemoteAttachment = 2

class RemotePointDOFSelectionType(Enum):
    """
    Specifies the RemotePointDOFSelectionType.
    """

    Manual = 1
    ProgramControlled = 0

class RemotePointFormulation(Enum):
    """
    Specifies the RemotePointFormulation.
    """

    LagrangeMultiplier = 1
    MPC = 0

class RemotePointUpdateOptions(Enum):
    """
    Specifies the RemotePointUpdateOptions.
    """

    Regenerate = 0
    Reuse = 1

class ResponseConstraintDefineBy(Enum):
    """
    Specifies the ResponseConstraintDefineBy.
    """

    AbsoluteConstant = 3
    AbsoluteRange = 2
    Constant = 0
    Range = 1

class ResponseConstraintType(Enum):
    """
    Specifies the ResponseConstraintType.
    """

    CenterOfGravityConstraint = 10
    ComplianceConstraint = 9
    CriterionConstraint = 11
    DisplacementConstraint = 5
    NaturalFrequencyConstraint = 4
    LocalVonMisesStressConstraint = 6
    MassConstraint = 1
    MomentOfInertiaConstraint = 12
    ReactionForceConstraint = 7
    TemperatureConstraint = 8
    VolumeConstraint = 2
    GlobalVonMisesStressConstraint = 3

class RestartControlsType(Enum):
    """
    Specifies the RestartControlsType.
    """

    Manual = 1
    Off = 2
    ProgramControlled = 0

class RestartRetainFilesType(Enum):
    """
    Specifies the RestartRetainFilesType.
    """

    No = 1
    Yes = 0

class RestartSaveAtLoadStep(Enum):
    """
    Specifies the RestartSaveAtLoadStep.
    """

    All = 2
    Last = 1
    None_ = 0
    Specify = 3

class RestartSaveAtSubstep(Enum):
    """
    Specifies the RestartSaveAtSubstep.
    """

    All = 2
    EquallySpaced = 4
    Last = 1
    SaveAtSubstepSpecified = 3

class RestartType(Enum):
    """
    Specifies the RestartType.
    """

    Manual = 1
    Off = 2
    ProgramControlled = 0

class ResultFileCompressionType(Enum):
    """
    Specifies the ResultFileCompressionType.
    """

    Off = 2
    ProgramControlled = 0
    Sparse = 1

class ResultRelativityType(Enum):
    """
    Specifies the ResultRelativityType.
    """

    Absolute = 0
    Relative = 1

class ResultType(Enum):
    """
    Specifies the ResultType.
    """

    AccelerationWaterfallDiagram = 406
    AccumulatedEquivalentPlasticStrain = 386
    AbsorptionCoefficient = 370
    DiffuseSoundTransmissionLoss = 377
    EquivalentRadiatedPower = 378
    EquivalentRadiatedPowerLevel = 379
    EquivalentRadiatedPowerLevelWaterfallDiagram = 385
    EquivalentRadiatedPowerWaterfallDiagram = 384
    FarFieldDirectivity = 354
    FarFieldMaximumPressure = 352
    FarFieldMaximumPressureMic = 374
    FarFieldMaximumScatteredPressure = 355
    FarFieldPhase = 353
    FarFieldPhaseMic = 375
    FarFieldSoundPowerLevel = 357
    AcousticFarFieldSoundPowerLevelWaterfallDiagram = 387
    FarFieldSPL = 350
    FarFieldSPLMic = 372
    AcousticFarFieldSPLMicWaterfallDiagram = 388
    FarFieldTargetStrength = 356
    FarFieldAWeightedSPL = 351
    FarFieldAWeightedSPLMic = 373
    ReturnLoss = 371
    TransmissionLoss = 369
    FrequencyBandSPL = 360
    SoundPressureLevel = 358
    AWeightedFrequencyBandSPL = 361
    AWeightedSoundPressureLevel = 359
    ArtificialEnergy = 401
    BendingStressEquivalent = 121
    BendingStressIntensity = 123
    FatigueResultBiaxialityIndication = 63
    BoltAdjustment = 294
    BoltWorkingLoad = 295
    ContactChattering = 101
    ContactContactingArea = 245
    ContactFluidPressure = 265
    ContactFrictionalStress = 71
    ContactGap = 70
    ContactHeatFlux = 334
    ContactMaximumDampingPressure = 249
    ContactMaxiumGeometricSlidingDistance = 289
    ContactMaximumNormalStiffness = 103
    ContactMaximumTangentialStiffness = 104
    ContactMinimumGeometricSlidingDistance = 288
    ContactMinimumTangentialStiffness = 108
    ContactNumberContacting = 100
    ContactNumberSticking = 106
    ContactPenetration = 69
    ContactPressure = 68
    ContactResultingPinball = 105
    ContactSlidingDistance = 72
    ContactStatus = 73
    CurrentDensity = 118
    FatigueDamage = 62
    DamageStatus = 281
    MullinsDamageVariable = 274
    DampingEnergy = 400
    VectorDeformation = 75
    TotalDeformation = 25
    Density = 195
    DirectStress = 109
    EquivalentElasticStrain = 13
    EquivalentElasticStrainRST = 250
    EquivalentStress = 1
    EquivalentStressPSD = 138
    EquivalentStressRS = 173
    JouleHeat = 154
    ElectricVoltage = 153
    ElectricPotential = 114
    Volume = 382
    ElementalStrainEnergy = 135
    EnergyDissipatedPerUnitVolume = 287
    EquivalentCreepStrain = 242
    EquivalentCreepStrainRST = 252
    EquivalentPlasticStrain = 84
    EquivalentPlasticStrainRST = 251
    EquivalentTotalStrainRST = 243
    MagneticError = 134
    StructuralError = 116
    ThermalError = 117
    FactorReserveInverseCompositeFailure = 321
    SafetyFactorCompositeFailure = 322
    SafetyFactorFatigue = 61
    SafetyFactor = 30
    FatigueEquivalentReversedStress = 74
    Hysteresis = 115
    FatigueSensitivity = 66
    FiberCompressiveDamageVariable = 283
    FiberCompressiveFailureCriterion = 278
    FiberTensileDamageVariable = 282
    FiberTensileFailureCriterion = 277
    FluidFlowRate = 296
    FluidHeatConductionRate = 297
    FluidHeatTransportRate = 298
    ForceReaction = 246
    FractureCSTAR = 311
    FractureEquivalentSIFSRange = 314
    FractureJINT = 266
    FractureMaterialForceX = 308
    FractureMaterialForceY = 309
    FractureMaterialForceZ = 310
    FractureSIFSK1 = 267
    FractureSIFSK2 = 268
    FractureSIFSK3 = 269
    FractureTSTRESS = 307
    FractureVCCTG1 = 270
    FractureVCCTG2 = 271
    FractureVCCTG3 = 272
    FractureVCCTGT = 273
    NormalGasketPressure = 236
    XYShearGasketPressure = 237
    XZShearGasketPressure = 238
    NormalGasketTotalClosure = 239
    XYShearGasketTotalClosure = 240
    XZShearGasketTotalClosure = 241
    MiddlePrincipalElasticStrain = 15
    MiddlePrincipalStress = 3
    MiddlePrincipalThermalStrain = 55
    KineticEnergy = 139
    LatticeElementalDensity = 380
    LatticeDensity = 381
    FatigueLife = 60
    LinePressure = 396
    LSDYNAGeneralTracker = 403
    MagneticCoenergy = 193
    MarginSafetyCompositeFailure = 323
    SafetyMargin = 29
    MatrixCompressiveDamageVariable = 285
    MatrixCompressiveFailureCriterion = 280
    MatrixTensileDamageVariable = 284
    MatrixTensileFailureCriterion = 279
    MaximumBendingStress = 111
    MaximumCombinedStress = 113
    MaximumFailureCriteria = 276
    MullinsMaximumPreviousStrainEnergy = 275
    MaximumPrincipalElasticStrain = 14
    MaximumPrincipalStress = 2
    MaximumPrincipalThermalStrain = 54
    MaximumShearElasticStrain = 17
    MaximumShearStress = 5
    MCFWaterfallDiagram = 404
    MembraneStressEquivalent = 120
    MembraneStressIntensity = 122
    MinimumBendingStress = 110
    MinimumCombinedStress = 112
    MinimumPrincipalElasticStrain = 16
    MinimumPrincipalStress = 4
    MinimumPrincipalThermalStrain = 56
    MomentReactionTracker = 247
    NonLinearStabilizationEnergy = 402
    NewtonRaphsonResidualCharge = 399
    NewtonRaphsonResidualForce = 85
    NewtonRaphsonResidualHeat = 87
    NewtonRaphsonResidualMoment = 86
    VariableGraph = 67
    PlasticWork = 176
    Pressure = 194
    VectorPrincipalElasticStrain = 78
    VectorPrincipalStress = 77
    CampbellDiagram = 248
    ShearDamageVariable = 286
    ShearMomentDiagramMSUM = 231
    ShearMomentDiagramMY = 225
    ShearMomentDiagramMZ = 226
    ShearMomentDiagramVSUM = 232
    ShearMomentDiagramVY = 227
    ShearMomentDiagramVZ = 228
    ShearMomentDiagramUSUM = 233
    ShearMomentDiagramUY = 229
    ShearMomentDiagramUZ = 230
    ShellBendingStress11 = 256
    ShellBendingStress12 = 258
    ShellBendingStress22 = 257
    ShellBottomPeakStress11 = 259
    ShellBottomPeakStress12 = 261
    ShellBottomPeakStress22 = 260
    ShellMembraneStress11 = 253
    ShellMembraneStress12 = 255
    ShellMembraneStress22 = 254
    ShellTopPeakStress11 = 262
    ShellTopPeakStress12 = 264
    ShellTopPeakStress22 = 263
    SpringTrackerDampingForce = 293
    SpringTrackerElasticForce = 292
    SpringTrackerElongation = 290
    SpringTrackerVelocity = 291
    StabilizationEnergy = 244
    StiffnessEnergy = 140
    StrainIntensity = 18
    StressIntensity = 6
    StressRatio = 31
    StructuralStrainEnergy = 136
    Temperature = 49
    ThermalStrainEnergy = 137
    TotalHeatFlux = 50
    VectorHeatFlux = 76
    TopologyElementalDensity = 335
    TopologyDensity = 338
    TotalAcceleration = 79
    TotalAxialForceDiagram = 208
    TotalBendingMomentDiagram = 213
    TotalCurrentDensity = 149
    TotalElectricFieldIntensity = 145
    TotalElectricFluxDensity = 141
    TotalEnergy = 174
    TotalMagneticFieldIntensity = 92
    TotalMagneticFluxDensity = 88
    TotalMagneticForces = 96
    TotalShearForce = 223
    TotalTorsionalMoment = 218
    TotalVelocity = 124
    VectorAxialForce = 209
    VectorBendingMoment = 214
    ElementalTriads = 200
    NodalTriads = 204
    VectorShearForce = 224
    VectorTorsionalMoment = 219
    VelocityWaterfallDiagram = 405
    ShapeFinder = 47
    ShapeFinderElemental = 185
    XDirectionalAcceleration = 80
    XDirectionalAccelerationPSD = 131
    XDirectionalAccelerationRS = 170
    XDirectionalAxialForce = 205
    XDirectionalBendingMoment = 210
    XContactForce = 186
    XDirectionalDisplacement = 26
    XDirectionalCurrentDensity = 150
    XDirectionalElectricFieldIntensity = 146
    XDirectionalElectricFluxDensity = 142
    ElementalEulerXYAngle = 197
    XExternalForce = 189
    XDirectionalMagneticFieldIntensity = 93
    XDirectionalMagneticFluxDensity = 89
    MagneticXDirectionalForces = 97
    XMomentum = 177
    NodalEulerXYAngle = 201
    XDirectionalShearForce = 220
    XNormalElasticStrain = 19
    XNormalStress = 7
    XDirectionalHeatFlux = 51
    XThermalStrain = 57
    XDirectionalTorsionalMoment = 215
    XTotalMassAverageVelocity = 180
    XDirectionalVelocity = 125
    XDirectionalVelocityPSD = 128
    XDirectionalVelocityRS = 167
    XYShearElasticStrain = 22
    XYShearStress = 10
    XZShearElasticStrain = 24
    XZShearStress = 12
    YDirectionalAcceleration = 81
    YDirectionalAccelerationPSD = 132
    YDirectionalAccelerationRS = 171
    YDirectionalAxialForce = 206
    YDirectionalBendingMoment = 211
    YContactForce = 187
    YDirectionalDisplacement = 27
    YDirectionalCurrentDensity = 151
    YDirectionalElectricFieldIntensity = 147
    YDirectionalElectricFluxDensity = 143
    ElementalEulerYZAngle = 198
    YExternalForce = 190
    YDirectionalMagneticFieldIntensity = 94
    YDirectionalMagneticFluxDensity = 90
    MagneticYDirectionalForces = 98
    YMomentum = 178
    NodalEulerYZNodal = 202
    YDirectionalShearForce = 221
    YNormalElasticStrain = 20
    YNormalStress = 8
    YDirectionalHeatFlux = 52
    YThermalStrain = 58
    YDirectionalTorsionalMoment = 216
    YTotalMassAverageVelocity = 181
    YDirectionalVelocity = 126
    YDirectionalVelocityPSD = 129
    YDirectionalVelocityRS = 168
    YZShearElasticStrain = 23
    YZShearStress = 11
    ZDirectionalAcceleration = 82
    ZdirectionalAccelerationPSD = 133
    ZDirectionalAccelerationRS = 172
    ZDirectionalAxialForce = 207
    ZDirectionalBendingMoment = 212
    ZContactForce = 188
    ZDirectionalDisplacement = 28
    ZDirectionalCurrentDensity = 152
    ZDirectionalElectricFieldIntensity = 148
    ZDirectionalElectricFluxDensity = 144
    ElementalEulerXZAngle = 199
    ZExternalForce = 191
    ZDirectionalMagneticFieldIntensity = 95
    ZDirectionalMagneticFluxDensity = 91
    MagneticZDirectionalForces = 99
    MagneticPotential = 192
    ZMomentum = 179
    NodalEulerXZAngle = 203
    ZDirectionalShearForce = 222
    ZNormalElasticStrain = 21
    ZNormalStress = 9
    ZDirectionalHeatFlux = 53
    ZThermalStrain = 59
    ZDirectionalTorsionalMoment = 217
    ZTotalMassAverageVelocity = 182
    ZDirectionalVelocity = 127
    ZDirectionalVelocityPSD = 130
    ZDirectionalVelocityRS = 169

class RigidResponseEffectType(Enum):
    """
    Specifies the RigidResponseEffectType.
    """

    Gupta = 1
    Lindely = 2

class RobustFrequenciesReductionType(Enum):
    """
    Specifies the RobustFrequenciesReductionType.
    """

    Average = 0
    ModeTracking = 2
    SmoothMin = 1

class RotationPlane(Enum):
    """
    Specifies the RotationPlane.
    """

    None_ = 0
    XY = 1
    XZ = 3
    YZ = 2

class SafetyLimitType(Enum):
    """
    Specifies the SafetyLimitType.
    """

    CustomValue = 3
    UltimatePerMaterial = 2
    YieldPerMaterial = 1

class ScaleFactorType(Enum):
    """
    Specifies the ScaleFactorType.
    """

    Sigma1 = 0
    Sigma2 = 1
    Sigma3 = 2
    UserDefined = 3

class ScatteredFieldFormulation(Enum):
    """
    Specifies the ScatteredFieldFormulation.
    """

    Off = 1
    On = 2
    ProgramControlled = 0

class ScatteringOutputType(Enum):
    """
    Specifies the ScatteringOutputType.
    """

    Scattered = 1
    Total = 0

class SendAs(Enum):
    """
    Specifies the SendAs.
    """

    Mesh200 = 2
    Nodes = 1
    NotApplicable = 0

class SeqSelectionMode(Enum):
    """
    Specifies the SeqSelectionMode.
    """

    ByNumber = 3
    First = 1
    Last = 2
    Unknown = 0

class SetDriverStyle(Enum):
    """
    Specifies the SetDriverStyle.
    """

    CyclicPhaseOfMaximum = 8
    MaximumOfCyclicPhase = 7
    MaximumOverModes = 9
    MaximumOverPhase = 5
    MaximumOverTime = 3
    MinimumOverTime = 12
    ModeOfMaximum = 10
    PhaseOfMaximum = 6
    ResultSet = 2
    Time = 1
    TimeOfMaximum = 4
    TimeOfMinimum = 13

class ShearMomentDiagramOrientationType(Enum):
    """
    Specifies the ShearMomentDiagramOrientationType.
    """

    BendingMoment = 1
    Displacement = 2
    ShearForce = 0

class ShearMomentType(Enum):
    """
    Specifies the ShearMomentType.
    """

    DirectionalSM1 = 1
    DirectionalSM2 = 2
    TotalSM = 0

class ShearOrientationType(Enum):
    """
    Specifies the ShearOrientationType.
    """

    XYPlane = 0
    XZPlane = 2
    YZPlane = 1

class ShellElementStiffnessOption(Enum):
    """
    Specifies the ShellElementStiffnessOption.
    """

    MembraneAndBending = 0
    MembraneOnly = 1
    StressEvaluationOnly = 2

class ShellFaceType(Enum):
    """
    Specifies the ShellFaceType.
    """

    All = 7
    Bending = 4
    Bottom = 1
    Middle = 3
    ProgramControlled = 5
    TopAndBottom = 2
    Top = 0

class ShellInertiaUpdate(Enum):
    """
    Specifies the ShellInertiaUpdate.
    """

    Recompute = 0
    Rotate = 1

class ShellMBPType(Enum):
    """
    Specifies the ShellMBPType.
    """

    BendingStress = 1
    BottomPeakStress = 2
    MembraneStress = 0
    TopPeakStress = 3

class ShellOffsetType(Enum):
    """
    Specifies the ShellOffsetType.
    """

    Bottom = 2
    Middle = 1
    Top = 0
    UserDefined = 3

class ShellThicknessUpdate(Enum):
    """
    Specifies the ShellThicknessUpdate.
    """

    Elemental = 1
    Nodal = 0

class SlidingContactType(Enum):
    """
    Specifies the SlidingContactType.
    """

    ConnectedSurface = 1
    DiscreteSurface = 0

class SolutionCombinationDriverStyle(Enum):
    """
    Specifies the SolutionCombinationDriverStyle.
    """

    CombinationOfMaximum = 2
    CombinationOfMinimum = 4
    Default = 0
    MaximumOverCombinations = 1
    MinimumOverCombinations = 3

class SolutionCombinationWorksheetType(Enum):
    """
    Specifies the SolutionCombinationWorksheetType.
    """

    NewWorksheet = 1
    OldWorksheet = 0

class SolutionOutputType(Enum):
    """
    Specifies the SolutionOutputType.
    """

    CurrentConvergence = 21
    ChargeConvergence = 51
    ContactOutput = 22
    CSGConvergence = 13
    EvaluateScriptOutput = 23
    SolveScriptOutput = 24
    DisplacementConvergence = 2
    EnergyConservation = 18
    EnergySummary = 20
    ForceConvergence = 1
    FrequencyConvergence = 27
    HeatConvergence = 3
    Time = 8
    KineticEnergy = 52
    LineSearch = 7
    MaximumDOFIncrement = 5
    MaximumDOFNodeAndIncrement = 54
    MomentConvergence = 16
    ParticipationFactor = 28
    PostOutput = 25
    StiffnessEnergy = 53
    PropertyChange = 15
    SolverOutput = 0
    RotationConvergence = 17
    SolutionStatistics = 40
    SolutionTracking = 44
    TemperatureConvergence = 4
    TemperatureChange = 14
    TimeIncrement = 10
    TimeIncrementVSTime = 6
    ObjectiveAndAllConstraintConvergence = 42
    ObjectiveAndManufacturingConvergence = 32
    ObjectiveAndDisplacementResponseConvergence = 36
    ObjectiveAndGlobalStressResponseConvergence = 34
    ObjectiveAndLocalStressResponseConvergence = 37
    ObjectiveAndMassResponseConvergence = 31
    ObjectiveAndNaturalFrequencyResponseConvergence = 35
    ObjectiveAndReactionForceResponseConvergence = 38
    ObjectiveAndVolumeResponseConvergence = 33
    OptimizationOutput = 29

class SolveBehaviourType(Enum):
    """
    Specifies the SolveBehaviourType.
    """

    Combined = 0
    Individual = 1

class SolverControlsIncludeNegativeLoadMultiplier(Enum):
    """
    Specifies the SolverControlsIncludeNegativeLoadMultiplier.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class SolverControlsModeReuse(Enum):
    """
    Specifies the SolverControlsModeReuse.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class SolverPivotChecking(Enum):
    """
    Specifies the SolverPivotChecking.
    """

    Error = 2
    Off = 3
    ProgramControlled = 0
    Warning = 1

class SolverType(Enum):
    """
    Specifies the SolverType.
    """

    FullDamped = 4
    Direct = 1
    Iterative = 2
    ProgramControlled = 0
    ReducedDamped = 5
    Supernode = 6
    Subspace = 7
    Unsymmetric = 3

class SolverUnitsControlType(Enum):
    """
    Specifies the SolverUnitsControlType.
    """

    ActiveSystem = 0
    Manual = 1

class SourceTimeDefinitionType(Enum):
    """
    Specifies the SourceTimeDefinitionType.
    """

    SourceTimeDefinition_All = 0
    SourceTimeDefinition_Range = 1

class SpatialRadiationType(Enum):
    """
    Specifies the SpatialRadiationType.
    """

    Full = 0
    Partial = 1

class SpatialReductionMethodType(Enum):
    """
    Specifies the SpatialReductionMethodType.
    """

    Continuous = 1
    Discrete = 0

class SpatialReductionType(Enum):
    """
    Specifies the SpatialReductionType.
    """

    AbsoluteMax = 2
    Average = 0
    StandardDeviation = 3
    Sum = 4

class SpectrumType(Enum):
    """
    Specifies the SpectrumType.
    """

    MultiplePoints = 2
    None_ = 0
    SinglePoint = 1

class SpotWeldTypes(Enum):
    """
    Specifies the SpotWeldTypes.
    """

    Dependent = 0
    Independent = 1

class SpringBehavior(Enum):
    """
    Specifies the SpringBehavior.
    """

    Linear = 0
    NonLinear = 3
    NonLinearCompressionOnly = 1
    NonLinearTensionOnly = 2

class SpringPreloadType(Enum):
    """
    Specifies the SpringPreloadType.
    """

    Length = 3
    Load = 1
    None_ = 0
    Rotation = 4
    Torque = 2

class SpringResultType(Enum):
    """
    Specifies the SpringResultType.
    """

    DampingForce = 293
    ElasticForce = 292
    Elongation = 290
    Velocity = 291

class SpringScopingType(Enum):
    """
    Specifies the SpringScopingType.
    """

    BodyToBody = 0
    BodyToGround = 1

class SpringsStiffnessType(Enum):
    """
    Specifies the SpringsStiffnessType.
    """

    Factor = 1
    Manual = 2
    ProgramControlled = 0

class SpringType(Enum):
    """
    Specifies the SpringType.
    """

    Longitudinal = 0
    Torsional = 1

class StabilizationFirstSubstepOption(Enum):
    """
    Specifies the StabilizationFirstSubstepOption.
    """

    OnNonConvergence = 1
    No = 0
    Yes = 2

class StabilizationMethod(Enum):
    """
    Specifies the StabilizationMethod.
    """

    Damping = 1
    Energy = 0

class StabilizationType(Enum):
    """
    Specifies the StabilizationType.
    """

    Constant = 1
    Off = 0
    ProgramControlled = 3
    Reduce = 2

class StackerMethodMeshType(Enum):

    QuadTri = 1
    AllTri = 0

class StageBehavior(Enum):
    """
    Specifies the StageBehavior.
    """

    Cyclic = 1
    Normal = 0

class StiffnessBehavior(Enum):
    """
    Specifies the StiffnessBehavior.
    """

    Beam = 2
    Flexible = 0
    Explicit = 7
    Gasket = 5
    Rigid = 1
    RigidBeam = 3
    StiffBeam = 6
    SuperElement = 4

class StiffnessMethodType(Enum):
    """
    Specifies the StiffnessMethodType.
    """

    Augmented = 3
    Full = 2
    ProgramControlled = 1

class STLSupportViewType(Enum):
    """
    Specifies the STLSupportViewType.
    """

    KnockdownFactors = 2
    Mesh = 1
    STL = 0

class StopCriterion(Enum):
    """
    Specifies the StopCriterion.
    """

    FreeBoundary = 2
    MaxCrackExtension = 1
    MaxStressIntensityFactor = 3
    MaxTotalNumberOfCycles = 4
    None_ = 0

class StoreModalResult(Enum):
    """
    Specifies the StoreModalResult.
    """

    ForFutureAnalysis = 2
    No = 1
    ProgramControlled = 0

class StressStrainType(Enum):
    """
    Specifies the StressStrainType.
    """

    Equivalent = 0
    Intensity = 5
    MaximumPrincipal = 1
    MaximumShear = 4
    MiddlePrincipal = 2
    MinimumPrincipal = 3
    Normal = 6
    Shear = 7
    None_ = 9
    Thermal = 8

class SubScopingDefineByType(Enum):
    """
    Specifies the SubScopingDefineByType.
    """

    Layer = 0
    Plies = 3
    Ply = 1

class SurfaceCoatingStiffnessBehavior(Enum):
    """
    Specifies the SurfaceCoatingStiffnessBehavior.
    """

    MembraneAndBending = 0
    MembraneOnly = 1
    StressEvaluationOnly = 2

class SymmetryBehavior(Enum):
    """
    Specifies the SymmetryBehavior.
    """

    Coupled = 1
    Free = 0

class SymmetryBoundaryDOFOrientation(Enum):
    """
    Specifies the SymmetryBoundaryDOFOrientation.
    """

    Manual = 0
    ChosenBySolver = 1

class TargetCorrection(Enum):
    """
    Specifies the TargetCorrection.
    """

    No = 0
    Smoothing = 1

class TargetOrientation(Enum):
    """
    Specifies the TargetOrientation.
    """

    Circle = 1
    Cylinder = 3
    Sphere = 2
    ProgramControlled = 0

class TetIntegrationType(Enum):
    """
    Specifies the TetIntegrationType.
    """

    AverageNodalPressure = 0
    NodalStrain = 2
    ConstantPressure = 1

class ThermalStrainType(Enum):
    """
    Specifies the ThermalStrainType.
    """

    ProgramControlled = 0
    Strong = 1
    Weak = 2

class ThermoelasticDampingType(Enum):
    """
    Specifies the ThermoelasticDampingType.
    """

    Off = 2
    On = 1

class ThroughThicknessBendingStress(Enum):
    """
    Specifies the ThroughThicknessBendingStress.
    """

    Ignore = 1
    Include = 0
    IncludeUsingYDirFormula = 2

class TimePointsOptions(Enum):
    """
    Specifies the TimePointsOptions.
    """

    AllTimePoints = 0
    EquallySpacedPoints = 2
    LastTimePoints = 1
    SpecifiedRecurrenceRate = 3

class TimeStepDefineByType(Enum):
    """
    Specifies the TimeStepDefineByType.
    """

    Substeps = 0
    Time = 1

class ToleranceType(Enum):
    """
    Specifies the ToleranceType.
    """

    Manual = 1
    ProgramControlled = 0

class TopoBoundType(Enum):
    """
    Specifies the TopoBoundType.
    """

    LowerBound = 0
    UpperBound = 1

class TopoConstraintStressType(Enum):
    """
    Specifies the TopoConstraintStressType.
    """

    LocalStrainEnergy = 2
    MaximumPrincipalStress = 1
    VonMisesStress = 0

class TopoConstraintType(Enum):
    """
    Specifies the TopoConstraintType.
    """

    ManufacturingConstraint = 1
    ResponseConstrain = 0

class TopoObjectiveFormulation(Enum):
    """
    Specifies the TopoObjectiveFormulation.
    """

    Displacement = 3
    Force = 2
    LocalStrainEnergy = 8
    MaximumPrincipalStress = 7
    ProgramControlled = 1
    Undefined = 0
    VonMisesStress = 6

class TopoOptimizationDensityFilter(Enum):
    """
    Specifies the TopoOptimizationDensityFilter.
    """

    Linear = 1
    NonLinear = 2
    ProgramControlled = 0

class TopoOptimizationExportDesignProperties(Enum):
    """
    Specifies the TopoOptimizationExportDesignProperties.
    """

    AllAcceptedIterations = 2
    LastAcceptedIteration = 3
    No = 0
    OnFinalDesign = 1

class TopoOptimizationExportDesignPropertiesFileFormat(Enum):
    """
    Specifies the TopoOptimizationExportDesignPropertiesFileFormat.
    """

    hdf5 = 1
    vtk = 0

class TopoOptimizationOutputLog(Enum):
    """
    Specifies the TopoOptimizationOutputLog.
    """

    High = 3
    Low = 1
    Medium = 2
    ProgramControlled = 0

class TopoPropertyControlType(Enum):
    """
    Specifies the TopoPropertyControlType.
    """

    Manual = 1
    ProgramControlled = 0

class TotalOrDirectional(Enum):
    """
    Specifies the TotalOrDirectional.
    """

    Directional = 1
    Total = 0

class TransferAdmittanceModelType(Enum):
    """
    Specifies the TransferAdmittanceModelType.
    """

    HexagonalGridStructure = 2
    PerforatedPlate = 0
    SquareGridStructure = 1

class TransformationType(Enum):
    """
    Specifies the TransformationType.
    """

    Custom = 0
    Flip = 3
    Offset = 1
    Rotation = 2

class TransientApplicationType(Enum):
    """
    Specifies the TransientApplicationType.
    """

    HighSpeedDynamics = 1
    Impact = 0
    LowSpeedDynamics = 3
    ModerateSpeedDynamics = 2
    QuasiStatic = 4
    UserDefined = 5

class TransientDampingType(Enum):
    """
    Specifies the TransientDampingType.
    """

    NumericalDampingManual = 1
    NumericalDampingProgramControlled = 0

class TriangleReduction(Enum):

    Aggressive = 2
    Conservative = 1
    None_ = 0

class UpdateContactStiffness(Enum):
    """
    Specifies the UpdateContactStiffness.
    """

    EachIteration = 1
    EachIterationAggressive = 3
    EachIterationExponential = 5
    EachSubStep = 2
    Never = 0
    ProgramControlled = 4

class UseExistingModesymFile(Enum):
    """
    Specifies the UseExistingModesymFile.
    """

    No = 2
    ProgramControlled = 0
    Yes = 1

class VectorReductionReferenceType(Enum):
    """
    Specifies the VectorReductionReferenceType.
    """

    Constant = 1
    None_ = 0

class VectorReductionType(Enum):
    """
    Specifies the VectorReductionType.
    """

    Directional = 5
    FaceNormal = 4
    Magnitude = 3
    X = 0
    XX = 11
    XY = 6
    XZ = 8
    Y = 1
    YY = 12
    YZ = 7
    Z = 2
    ZZ = 13

class WaveType(Enum):
    """
    Specifies the WaveType.
    """

    BackEnclosedLoudspeaker = 3
    BareLoudspeaker = 4
    CircularDuct = 6
    CylindricalCoaxialDuct = 7
    Dipole = 2
    Monopole = 1
    PlanarWave = 0
    RectangularDuct = 5

class WBUnitSystemType(Enum):
    """
    Specifies the WBUnitSystemType.
    """

    ConsistentBFT = 7
    ConsistentBIN = 8
    ConsistentCGS = 5
    ConsistentMKS = 11
    ConsistentNMM = 6
    ConsistentUMKS = 10
    NoUnitSystem = 17
    StandardBFT = 3
    StandardBIN = 4
    StandardCGS = 1
    StandardCUST = 12
    StandardKNMS = 15
    StandardMKS = 0
    StandardNMM = 2
    StandardNMMdat = 14
    StandardNMMton = 13
    StandardUMKS = 9

class WeakSpringsType(Enum):
    """
    Specifies the WeakSpringsType.
    """

    Off = 2
    On = 1
    ProgramControlled = 0

class WindowType(Enum):
    """
    Specifies the WindowType.
    """

    Bartlett = 3
    Blackman = 7
    Hamming = 5
    Hanning = 4
    None_ = 0
    Rectangular = 1
    Triangular = 2
    Welch = 6

class XAxisValues(Enum):
    """
    Specifies the XAxisValues.
    """

    CumulativeIteration = 1
    Time = 0

class YesNoProgrammedControlled(Enum):
    """
    Specifies the YesNoProgrammedControlled.
    """

    No = 0
    ProgramControlled = 2
    Yes = 1

