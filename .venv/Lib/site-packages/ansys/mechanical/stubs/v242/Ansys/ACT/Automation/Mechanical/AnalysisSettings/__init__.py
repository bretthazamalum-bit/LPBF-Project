"""AnalysisSettings module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class TopoOptAnalysisSettings(object):
    """
    Defines a TopoOptAnalysisSettings.
    """

    @property
    def ExportDesignProperties(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TopoOptimizationExportDesignProperties]:
        """
        Gets or sets the ExportDesignProperties.
        """
        return None

    @property
    def ExportDesignPropertiesFileFormat(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TopoOptimizationExportDesignPropertiesFileFormat]:
        """
        Gets or sets the ExportDesignPropertiesFileFormat.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAnalysisSettings]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ConvergenceAccuracy(self) -> typing.Optional[float]:
        """
        Gets or sets the ConvergenceAccuracy.
        """
        return None

    @property
    def TopoOptInitialDensity(self) -> typing.Optional[float]:
        """
        Gets or sets the TopoOptInitialDensity.
        """
        return None

    @property
    def MaxNumOfIntermediateFiles(self) -> typing.Optional[int]:
        """
        Gets or sets the MaxNumOfIntermediateFiles.
        """
        return None

    @property
    def MaximumNumberOfIterations(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumNumberOfIterations.
        """
        return None

    @property
    def MinimumNormalizedDensity(self) -> typing.Optional[float]:
        """
        Gets or sets the MinimumNormalizedDensity.
        """
        return None

    @property
    def StoreResultsAtValue(self) -> typing.Optional[int]:
        """
        Gets or sets the StoreResultsAtValue.
        """
        return None

    @property
    def PenaltyFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PenaltyFactor.
        """
        return None

    @property
    def Algorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AlgorithmType]:
        """
        Gets or sets the Algorithm.
        """
        return None

    @property
    def StoreResultsAt(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.IterationOptions]:
        """
        Gets or sets the StoreResultsAt.
        """
        return None

    @property
    def FutureAnalysis(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FutureIntentType]:
        """
        Gets or sets the FutureAnalysis.
        """
        return None

    @property
    def MultiOptimTypeStrategy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MultiOptimTypeStrategyType]:
        """
        Gets or sets the MultiOptimTypeStrategy.
        """
        return None

    @property
    def OptimizationOutputLog(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TopoOptimizationOutputLog]:
        """
        Gets or sets the OptimizationOutputLog.
        """
        return None

    @property
    def RegionOfAMOverhangConstraint(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExclusionParticipantType]:
        """
        Gets or sets the RegionOfAMOverhangConstraint.
        """
        return None

    @property
    def RegionOfManufacturingConstraint(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExclusionParticipantType]:
        """
        Gets or sets the RegionOfManufacturingConstraint.
        """
        return None

    @property
    def RegionOfMinMemberSize(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExclusionParticipantType]:
        """
        Gets or sets the RegionOfMinMemberSize.
        """
        return None

    @property
    def SolverUnitSystem(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the SolverUnitSystem.
        """
        return None

    @property
    def SolverType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.OptimizationSolverType]:
        """
        Gets or sets the SolverType.
        """
        return None

    @property
    def SolverUnits(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverUnitsControlType]:
        """
        Gets or sets the SolverUnits.
        """
        return None

    @property
    def Filter(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TopoOptimizationDensityFilter]:
        """
        Gets or sets the Filter.
        """
        return None

    @property
    def DeleteUnneededFiles(self) -> typing.Optional[bool]:
        """
        Gets or sets the DeleteUnneededFiles.
        """
        return None

    @property
    def ExportKnockdownFilePath(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExportKnockdownFilePath.
        """
        return None

    @property
    def SaveMAPDLDB(self) -> typing.Optional[bool]:
        """
        Gets or sets the SaveMAPDLDB.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Graph(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnalysisSettingsGraph]:
        """
        Graph property.
        """
        return None

    @property
    def ScratchSolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the ScratchSolverFilesDirectory.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the SolverFilesDirectory.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def DeleteAllRestartPoints(self) -> None:
        """
        DeleteAllRestartPoints method.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class AnalysisSettings(object):
    """
    Defines a AnalysisSettings.
    """

    @property
    def Graph(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnalysisSettingsGraph]:
        """
        Graph property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAnalysisSettings]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScratchSolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the ScratchSolverFilesDirectory.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the SolverFilesDirectory.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def DeleteAllRestartPoints(self) -> None:
        """
        DeleteAllRestartPoints method.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class ANSYSAnalysisSettings(object):
    """
    Defines a ANSYSAnalysisSettings.
    """

    @property
    def StepName(self) -> typing.Optional[str]:
        """
        Gets or sets the Step Name.
        """
        return None

    @property
    def AMStepType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMProcessStepType]:
        """
        Gets or sets the AM Process Step Type.
        """
        return None

    @property
    def AMSubstepsToApplyHeats(self) -> typing.Optional[int]:
        """
        Gets or sets the AM Substeps to Apply Heat.
        """
        return None

    @property
    def AMSubstepsBetweenHeating(self) -> typing.Optional[int]:
        """
        Gets or sets the AM Substeps Between Heating.
        """
        return None

    @property
    def AMCooldownNumberOfSubsteps(self) -> typing.Optional[int]:
        """
        Gets or sets the AM Cooldown Number of Substeps.
        """
        return None

    @property
    def CooldownTimeType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMCooldownTimeType]:
        """
        Gets or sets the AM Cooldown Time Type.
        """
        return None

    @property
    def CooldownTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the AM Cooldown Time.
        """
        return None

    @property
    def LayersToBuild(self) -> typing.Optional[int]:
        """
        Gets or sets the AM Layers to Build.
        """
        return None

    @property
    def ReferenceTemperatureType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMReferenceTemperatureType]:
        """
        Gets or sets the AM Reference Temperature Type.
        """
        return None

    @property
    def ReferenceTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the AM Reference Temperature.
        """
        return None

    @property
    def RelaxationTemperatureType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMRelaxationTemperatureType]:
        """
        Gets or sets the AM Relaxation Temperature Type.
        """
        return None

    @property
    def NumberOfRestartPoints(self) -> typing.Optional[int]:
        """
        Gets Number of Restart Points.
        """
        return None

    @property
    def CurrentRestartPoint(self) -> typing.Optional[int]:
        """
        Gets or sets the Current Restart Point.
        """
        return None

    @property
    def AggressiveRemeshing(self) -> typing.Optional[bool]:
        """
        Gets or sets the AggressiveRemeshing.
        """
        return None

    @property
    def SpinSoftening(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpinSofteningType]:
        """
        Gets or sets the SpinSoftening.
        """
        return None

    @property
    def UserDefinedFrequencySteps(self) -> typing.Optional[typing.List[Ansys.Core.Units.Quantity]]:
        """
        Gets or sets the UserDefinedFrequencySteps.
        """
        return None

    @property
    def OutputSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.OutputSelection]:
        """
        
            Gets or sets the Output Selection property in the Output Controls group of Analysis Settings.
            
        """
        return None

    @property
    def NamedSelection(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]]:
        """
        
            Gets or sets the objects of type NamedSelection to -- Named Selection property in the Output Controls group of Analysis Settings.
            If the OutputSelection != OutputSelection.NamedSelection,
            1. NamedSelection cannot be set. An exception will be thrown saying “Cannot modify ANSYSAnalysisSettings.NamedSelection if ANSYSAnalysisSettings.OutputSelection is not set to "OutputSelection.NamedSelection”.”
            2. Getting the NamedSelection value will return an empty list.
            
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAnalysisSettings]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def MassCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the MassCoefficient.
        """
        return None

    @property
    def StiffnessCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the StiffnessCoefficient.
        """
        return None

    @property
    def DampingRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the DampingRatio.
        """
        return None

    @property
    def ConstantDampingRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the ConstantDampingRatio.
        """
        return None

    @property
    def StructuralDampingCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the StructuralDampingCoefficient.
        """
        return None

    @property
    def ContactSplitMaxNum(self) -> typing.Optional[int]:
        """
        Gets or sets the ContactSplitMaxNum.
        """
        return None

    @property
    def ChargeConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the ChargeConvergenceTolerance.
        """
        return None

    @property
    def CurrentConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the CurrentConvergenceTolerance.
        """
        return None

    @property
    def EmagAMPSConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the EmagAMPSConvergenceTolerance.
        """
        return None

    @property
    def EmagCSGConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the EmagCSGConvergenceTolerance.
        """
        return None

    @property
    def EnergyConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the EnergyConvergenceTolerance.
        """
        return None

    @property
    def HeatConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the HeatConvergenceTolerance.
        """
        return None

    @property
    def TemperatureConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the TemperatureConvergenceTolerance.
        """
        return None

    @property
    def VoltageConvergenceTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the VoltageConvergenceTolerance.
        """
        return None

    @property
    def CreepLimitRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the CreepLimitRatio.
        """
        return None

    @property
    def CurrentStepNumberHarmonic(self) -> typing.Optional[int]:
        """
        Gets or sets the CurrentStepNumberHarmonic.
        """
        return None

    @property
    def CurrentStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the CurrentStepNumber.
        """
        return None

    @property
    def EngineOrderofExcitation(self) -> typing.Optional[int]:
        """
        Gets or sets the EngineOrderofExcitation.
        """
        return None

    @property
    def MaximumHarmonicIndex(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumHarmonicIndex.
        """
        return None

    @property
    def MinimumHarmonicIndex(self) -> typing.Optional[int]:
        """
        Gets or sets the MinimumHarmonicIndex.
        """
        return None

    @property
    def HarmonicIndexInterval(self) -> typing.Optional[int]:
        """
        Gets or sets the HarmonicIndexInterval.
        """
        return None

    @property
    def ClusterNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the ClusterNumber.
        """
        return None

    @property
    def SolutionIntervals(self) -> typing.Optional[int]:
        """
        Gets or sets the SolutionIntervals.
        """
        return None

    @property
    def KrylovSubspaceDimension(self) -> typing.Optional[int]:
        """
        Gets or sets the KrylovSubspaceDimension.
        """
        return None

    @property
    def KrylovResidualTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the KrylovResidualTolerance.
        """
        return None

    @property
    def HarmonicOrders(self) -> typing.Optional[str]:
        """
        Gets or sets the HarmonicOrders.
        """
        return None

    @property
    def InitialSubsteps(self) -> typing.Optional[int]:
        """
        Gets or sets the InitialSubsteps.
        """
        return None

    @property
    def InverseOptionEndStep(self) -> typing.Optional[int]:
        """
        Gets or sets the InverseOptionEndStep.
        """
        return None

    @property
    def MaximumSubsteps(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumSubsteps.
        """
        return None

    @property
    def MeshLoadStepValue(self) -> typing.Optional[int]:
        """
        Gets or sets the MeshLoadStepValue.
        """
        return None

    @property
    def MinimumSubsteps(self) -> typing.Optional[int]:
        """
        Gets or sets the MinimumSubsteps.
        """
        return None

    @property
    def ModalNumberOfPoints(self) -> typing.Optional[int]:
        """
        Gets or sets the ModalNumberOfPoints.
        """
        return None

    @property
    def ModeSignificanceLevel(self) -> typing.Optional[float]:
        """
        Gets or sets the ModeSignificanceLevel.
        """
        return None

    @property
    def GlobalSizeRatioQualityImprovement(self) -> typing.Optional[float]:
        """
        Gets or sets the GlobalSizeRatioQualityImprovement.
        """
        return None

    @property
    def GlobalSizeRatioQualityRefinement(self) -> typing.Optional[float]:
        """
        Gets or sets the GlobalSizeRatioQualityRefinement.
        """
        return None

    @property
    def NumberOfSculptedLayersQualityImprovement(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfSculptedLayersQualityImprovement.
        """
        return None

    @property
    def NumberOfSculptedLayersRefinement(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfSculptedLayersRefinement.
        """
        return None

    @property
    def RemeshingToleranceQualityImprovement(self) -> typing.Optional[float]:
        """
        Gets or sets the RemeshingToleranceQualityImprovement.
        """
        return None

    @property
    def RemeshingToleranceRefinement(self) -> typing.Optional[float]:
        """
        Gets or sets the RemeshingToleranceRefinement.
        """
        return None

    @property
    def StoreResulsAtValue(self) -> typing.Optional[int]:
        """
        Gets or sets the StoreResulsAtValue.
        """
        return None

    @property
    def NumberOfModesToUse(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfModesToUse.
        """
        return None

    @property
    def NumberOfRPMs(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfRPMs.
        """
        return None

    @property
    def NumberOfSteps(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfSteps.
        """
        return None

    @property
    def NumberOfSubSteps(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfSubSteps.
        """
        return None

    @property
    def NumericalDampingValue(self) -> typing.Optional[float]:
        """
        Gets or sets the NumericalDampingValue.
        """
        return None

    @property
    def NumLoadVectors(self) -> typing.Optional[int]:
        """
        Gets or sets the NumLoadVectors.
        """
        return None

    @property
    def MaximumModesToFind(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumModesToFind.
        """
        return None

    @property
    def NumberOfZones(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfZones.
        """
        return None

    @property
    def AxisymmetryDivisions(self) -> typing.Optional[int]:
        """
        Gets or sets the AxisymmetryDivisions.
        """
        return None

    @property
    def HemicubeResolution(self) -> typing.Optional[int]:
        """
        Gets or sets the HemicubeResolution.
        """
        return None

    @property
    def FluxConvergence(self) -> typing.Optional[float]:
        """
        Gets or sets the FluxConvergence.
        """
        return None

    @property
    def MaximumIteration(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumIteration.
        """
        return None

    @property
    def OverRelaxation(self) -> typing.Optional[float]:
        """
        Gets or sets the OverRelaxation.
        """
        return None

    @property
    def ReformulationTolerance(self) -> typing.Optional[float]:
        """
        Gets or sets the ReformulationTolerance.
        """
        return None

    @property
    def RestartAtLoadStep(self) -> typing.Optional[int]:
        """
        Gets the RestartAtLoadStep.
        """
        return None

    @property
    def RestartAtSubstep(self) -> typing.Optional[int]:
        """
        Gets the RestartAtSubstep.
        """
        return None

    @property
    def RestartAtTime(self) -> typing.Optional[float]:
        """
        Gets the RestartAtTime.
        """
        return None

    @property
    def RpmClusterNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the RpmClusterNumber.
        """
        return None

    @property
    def RpmSolutionIntervals(self) -> typing.Optional[int]:
        """
        Gets or sets the RpmSolutionIntervals.
        """
        return None

    @property
    def MaximumPointsToSavePerStep(self) -> typing.Optional[int]:
        """
        Gets or sets the MaximumPointsToSavePerStep.
        """
        return None

    @property
    def SaveSpecifiedLoadStep(self) -> typing.Optional[int]:
        """
        Gets or sets the SaveSpecifiedLoadStep.
        """
        return None

    @property
    def LoadStepValue(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepValue.
        """
        return None

    @property
    def SignificanceThreshold(self) -> typing.Optional[float]:
        """
        Gets or sets the SignificanceThreshold.
        """
        return None

    @property
    def StabilizationDampingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the StabilizationDampingFactor.
        """
        return None

    @property
    def StabilizationEnergyDissipationRatio(self) -> typing.Optional[float]:
        """
        Gets or sets the StabilizationEnergyDissipationRatio.
        """
        return None

    @property
    def StabilizationForceLimit(self) -> typing.Optional[float]:
        """
        Gets or sets the StabilizationForceLimit.
        """
        return None

    @property
    def TransientApplicationUserDefined(self) -> typing.Optional[float]:
        """
        Gets or sets the TransientApplicationUserDefined.
        """
        return None

    @property
    def SpringStiffnessFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the SpringStiffnessFactor.
        """
        return None

    @property
    def RelaxationTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RelaxationTemperature.
        """
        return None

    @property
    def Frequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Frequency.
        """
        return None

    @property
    def CentralFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CentralFrequency.
        """
        return None

    @property
    def ChargeConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ChargeConvergenceMinimumReference.
        """
        return None

    @property
    def ChargeConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ChargeConvergenceValue.
        """
        return None

    @property
    def CurrentConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CurrentConvergenceMinimumReference.
        """
        return None

    @property
    def CurrentConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CurrentConvergenceValue.
        """
        return None

    @property
    def DisplacementConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplacementConvergenceMinimumReference.
        """
        return None

    @property
    def DisplacementConvergenceTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplacementConvergenceTolerance.
        """
        return None

    @property
    def DisplacementConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplacementConvergenceValue.
        """
        return None

    @property
    def EmagAMPSConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EmagAMPSConvergenceMinimumReference.
        """
        return None

    @property
    def EmagAMPSConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EmagAMPSConvergenceValue.
        """
        return None

    @property
    def EmagCSGConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EmagCSGConvergenceMinimumReference.
        """
        return None

    @property
    def EmagCSGConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EmagCSGConvergenceValue.
        """
        return None

    @property
    def EnergyConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EnergyConvergenceMinimumReference.
        """
        return None

    @property
    def EnergyConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EnergyConvergenceValue.
        """
        return None

    @property
    def ForceConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ForceConvergenceMinimumReference.
        """
        return None

    @property
    def ForceConvergenceTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ForceConvergenceTolerance.
        """
        return None

    @property
    def ForceConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ForceConvergenceValue.
        """
        return None

    @property
    def HeatConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the HeatConvergenceMinimumReference.
        """
        return None

    @property
    def HeatConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the HeatConvergenceValue.
        """
        return None

    @property
    def MomentConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MomentConvergenceMinimumReference.
        """
        return None

    @property
    def MomentConvergenceTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MomentConvergenceTolerance.
        """
        return None

    @property
    def MomentConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MomentConvergenceValue.
        """
        return None

    @property
    def RotationConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RotationConvergenceMinimumReference.
        """
        return None

    @property
    def RotationConvergenceTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RotationConvergenceTolerance.
        """
        return None

    @property
    def TemperatureConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TemperatureConvergenceMinimumReference.
        """
        return None

    @property
    def TemperatureConvergenceInputValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TemperatureConvergenceInputValue.
        """
        return None

    @property
    def VoltageConvergenceMinimumReference(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the VoltageConvergenceMinimumReference.
        """
        return None

    @property
    def VoltageConvergenceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the VoltageConvergenceValue.
        """
        return None

    @property
    def RemovalDirection(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RemovalDirection.
        """
        return None

    @property
    def RemovalStepSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RemovalStepSize.
        """
        return None

    @property
    def StepEndTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the StepEndTime.
        """
        return None

    @property
    def MinimumElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Minimum Element Size property for Geometry Based Adaptivity.
        """
        return None

    @property
    def RangeMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Range Maximum property in Options group of Analysis Settings in Harmonic Analysis.
        """
        return None

    @property
    def RangeMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Range Minimum property in Options group of Analysis Settings in Harmonic Analysis.
        """
        return None

    @property
    def KrylovSubspaceFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the KrylovSubspaceFrequency.
        """
        return None

    @property
    def ModalRangeMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ModalRangeMaximum.
        """
        return None

    @property
    def ModalRangeMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ModalRangeMinimum.
        """
        return None

    @property
    def InitialTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the InitialTimeStep.
        """
        return None

    @property
    def SearchRangeMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Range Maximum property in Options group of Analysis Settings in Modal Analysis.
        """
        return None

    @property
    def MaximumTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MaximumTimeStep.
        """
        return None

    @property
    def SearchRangeMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Range Minimum property in Options group of Analysis Settings in Modal Analysis.
        """
        return None

    @property
    def MinimumTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the MinimumTimeStep.
        """
        return None

    @property
    def BoundaryAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BoundaryAngle.
        """
        return None

    @property
    def EdgeSplittingAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the EdgeSplittingAngle.
        """
        return None

    @property
    def SolverTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SolverTolerance.
        """
        return None

    @property
    def RpmValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RpmValue.
        """
        return None

    @property
    def RpmCentralFrequency(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RpmCentralFrequency.
        """
        return None

    @property
    def RpmRangeMaximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RpmRangeMaximum.
        """
        return None

    @property
    def RpmRangeMinimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RpmRangeMinimum.
        """
        return None

    @property
    def TimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the TimeStep.
        """
        return None

    @property
    def SpringStiffnessValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the SpringStiffnessValue.
        """
        return None

    @property
    def BaseRemovalType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMBaseRemovalType]:
        """
        Gets or sets the BaseRemovalType.
        """
        return None

    @property
    def StiffnessCoefficientDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DampingType]:
        """
        Gets or sets the StiffnessCoefficientDefineBy.
        """
        return None

    @property
    def CacheResultsInMemory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CacheResultsInMemory]:
        """
        Gets or sets the CacheResultsInMemory.
        """
        return None

    @property
    def ParticipationFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CalculateParticipationFactorResult]:
        """
        Gets or sets the ParticipationFactor.
        """
        return None

    @property
    def StoreResultsAt(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimePointsOptions]:
        """
        Gets or sets the StoreResultsAt.
        """
        return None

    @property
    def ConstantDamping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConstantDampingType]:
        """
        Gets or sets the ConstantDamping.
        """
        return None

    @property
    def ContactSplit(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactSplitType]:
        """
        Gets or sets the ContactSplit.
        """
        return None

    @property
    def ContactSummary(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ContactSummaryType]:
        """
        Gets or sets the ContactSummary.
        """
        return None

    @property
    def ChargeConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the ChargeConvergence.
        """
        return None

    @property
    def CurrentConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the CurrentConvergence.
        """
        return None

    @property
    def DisplacementConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the DisplacementConvergence.
        """
        return None

    @property
    def AMPSConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the AMPSConvergence.
        """
        return None

    @property
    def CSGConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the CSGConvergence.
        """
        return None

    @property
    def EnergyConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the EnergyConvergence.
        """
        return None

    @property
    def ForceConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the ForceConvergence.
        """
        return None

    @property
    def HeatConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the HeatConvergence.
        """
        return None

    @property
    def MomentConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the MomentConvergence.
        """
        return None

    @property
    def RotationConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the RotationConvergence.
        """
        return None

    @property
    def TemperatureConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the TemperatureConvergence.
        """
        return None

    @property
    def TemperatureConvergenceValue(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NonLinearValueType]:
        """
        Gets or sets the TemperatureConvergenceValue.
        """
        return None

    @property
    def VoltageConvergence(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType]:
        """
        Gets or sets the VoltageConvergence.
        """
        return None

    @property
    def CoriolisEffectApplied(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CoriolisEffectType]:
        """
        Gets or sets the CoriolisEffectApplied.
        """
        return None

    @property
    def CreepEffects(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.Creep]:
        """
        Gets or sets the CreepEffects.
        """
        return None

    @property
    def HarmonicIndexRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CyclicHarmonicIndex]:
        """
        Gets or sets the HarmonicIndexRange.
        """
        return None

    @property
    def DampingDefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DampingDefineBy]:
        """
        Gets or sets the DampingDefineBy.
        """
        return None

    @property
    def FarFieldRadiationSurface(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FarFieldRadiationSurfaceType]:
        """
        Gets or sets the FarFieldRadiationSurface.
        """
        return None

    @property
    def ExpandResultsFrom(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExpandResultFrom]:
        """
        Gets or sets the ExpandResultsFrom.
        """
        return None

    @property
    def FrequencySpacing(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FrequencySpacingType]:
        """
        Gets or sets the FrequencySpacing.
        """
        return None

    @property
    def FutureAnalysis(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FutureIntentType]:
        """
        Gets or sets the FutureAnalysis.
        """
        return None

    @property
    def GeneralMiscellaneousOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeneralMiscellaneousOptionType]:
        """
        Gets or sets the GeneralMiscellaneousOption.
        """
        return None

    @property
    def MultistepType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.HarmonicMultiStepType]:
        """
        Gets or sets the MultistepType.
        """
        return None

    @property
    def ModalFrequencyRange(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ModalFrequencyRangeType]:
        """
        Gets or sets the ModalFrequencyRange.
        """
        return None

    @property
    def StoreResultsAtAllFrequencies(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.HarmonicMSUPStorage]:
        """
        Gets or sets the StoreResultsAtAllFrequencies.
        """
        return None

    @property
    def SolutionMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.HarmonicMethod]:
        """
        Gets or sets the SolutionMethod.
        """
        return None

    @property
    def IncludeNegativeLoadMultiplier(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverControlsIncludeNegativeLoadMultiplier]:
        """
        Gets or sets the IncludeNegativeLoadMultiplier.
        """
        return None

    @property
    def LineSearch(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LineSearchType]:
        """
        Gets or sets the LineSearch.
        """
        return None

    @property
    def GenerateMeshRestartPoints(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshRestartControlsType]:
        """
        Gets or sets the GenerateMeshRestartPoints.
        """
        return None

    @property
    def MeshRetainFilesAfterFullSolve(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshRestartRetainFilesType]:
        """
        Gets or sets the MeshRetainFilesAfterFullSolve.
        """
        return None

    @property
    def MeshSaveAtLoadStep(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshRestartSaveAtLoadStep]:
        """
        Gets or sets the MeshSaveAtLoadStep.
        """
        return None

    @property
    def MeshSaveAtSubstep(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MeshRestartSaveAtSubstep]:
        """
        Gets or sets the MeshSaveAtSubstep.
        """
        return None

    @property
    def ModeReuse(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverControlsModeReuse]:
        """
        Gets or sets the ModeReuse.
        """
        return None

    @property
    def ModesCombinationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ModesCombinationType]:
        """
        Gets or sets the ModesCombinationType.
        """
        return None

    @property
    def ModeSelectionMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ModeSelectionMethod]:
        """
        Gets or sets the ModeSelectionMethod.
        """
        return None

    @property
    def OnDemandExpansionOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.OnDemandExpansionType]:
        """
        Gets or sets the OnDemandExpansionOption.
        """
        return None

    @property
    def NewtonRaphsonOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NewtonRaphsonType]:
        """
        Gets or sets the NewtonRaphsonOption.
        """
        return None

    @property
    def NodalForces(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.OutputControlsNodalForcesType]:
        """
        Gets or sets the NodalForces.
        """
        return None

    @property
    def ProjectToGeometry(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NLADControlProjectToGeometry]:
        """
        Gets or sets the ProjectToGeometry.
        """
        return None

    @property
    def RefinementAlgorithm(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NonlinearAdaptivityControlsRefinementAlgorithmType]:
        """
        Gets or sets the RefinementAlgorithm.
        """
        return None

    @property
    def RemeshingGradient(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NonlinearAdaptivityControlsRemeshingGradientType]:
        """
        Gets or sets the RemeshingGradient.
        """
        return None

    @property
    def NonLinearFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.NonLinearFormulationType]:
        """
        Gets or sets the NonLinearFormulation.
        """
        return None

    @property
    def NumericalDamping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TransientDampingType]:
        """
        Gets or sets the NumericalDamping.
        """
        return None

    @property
    def Expansion(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ExpandResultsSubType]:
        """
        Gets the Expansion.
        """
        return None

    @property
    def ViewFactorMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RadiosityViewFactorType]:
        """
        Gets or sets the ViewFactorMethod.
        """
        return None

    @property
    def RadiositySolver(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RadiositySolverType]:
        """
        Gets or sets the RadiositySolver.
        """
        return None

    @property
    def CombineRestartFiles(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CombineRestartFilesType]:
        """
        Gets or sets the CombineRestartFiles.
        """
        return None

    @property
    def GenerateRestartPoints(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RestartControlsType]:
        """
        Gets or sets the GenerateRestartPoints.
        """
        return None

    @property
    def RetainFilesAfterFullSolve(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RestartRetainFilesType]:
        """
        Gets or sets the RetainFilesAfterFullSolve.
        """
        return None

    @property
    def RestartType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RestartType]:
        """
        Gets or sets the RestartType.
        """
        return None

    @property
    def ResultFileCompression(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultFileCompressionType]:
        """
        Gets or sets the ResultFileCompression.
        """
        return None

    @property
    def RpmFrequencySpacing(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FrequencySpacingType]:
        """
        Gets or sets the RpmFrequencySpacing.
        """
        return None

    @property
    def SaveAtLoadStep(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RestartSaveAtLoadStep]:
        """
        Gets or sets the SaveAtLoadStep.
        """
        return None

    @property
    def SaveAtSubstep(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RestartSaveAtSubstep]:
        """
        Gets or sets the SaveAtSubstep.
        """
        return None

    @property
    def ScatteredFieldFormulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScatteredFieldFormulation]:
        """
        Gets or sets the ScatteredFieldFormulation.
        """
        return None

    @property
    def ScatteringOutputType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ScatteringOutputType]:
        """
        Gets or sets the ScatteringOutputType.
        """
        return None

    @property
    def SolverUnitSystem(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the SolverUnitSystem.
        """
        return None

    @property
    def SolverPivotChecking(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverPivotChecking]:
        """
        Gets or sets the SolverPivotChecking.
        """
        return None

    @property
    def SolverType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverType]:
        """
        Gets or sets the SolverType.
        """
        return None

    @property
    def SolverUnits(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolverUnitsControlType]:
        """
        Gets or sets the SolverUnits.
        """
        return None

    @property
    def SpectrumType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpectrumType]:
        """
        Gets or sets the SpectrumType.
        """
        return None

    @property
    def Stabilization(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StabilizationType]:
        """
        Gets or sets the Stabilization.
        """
        return None

    @property
    def StabilizationActivationForFirstSubstep(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StabilizationFirstSubstepOption]:
        """
        Gets or sets the StabilizationActivationForFirstSubstep.
        """
        return None

    @property
    def StabilizationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StabilizationMethod]:
        """
        Gets or sets the StabilizationMethod.
        """
        return None

    @property
    def StoreModalResults(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.StoreModalResult]:
        """
        Gets or sets the StoreModalResults.
        """
        return None

    @property
    def DefineBy(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TimeStepDefineByType]:
        """
        Gets or sets the DefineBy.
        """
        return None

    @property
    def TransientApplication(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.TransientApplicationType]:
        """
        Gets or sets the TransientApplication.
        """
        return None

    @property
    def UpdateViewFactor(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.UpdateViewFactor]:
        """
        Gets or sets the specification for updating the view factor.
        """
        return None

    @property
    def AutomaticTimeStepping(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticTimeStepping]:
        """
        Gets or sets the AutomaticTimeStepping.
        """
        return None

    @property
    def RetainModesymFileAfterSolve(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.UseExistingModesymFile]:
        """
        Gets or sets the RetainModesymFileAfterSolve.
        """
        return None

    @property
    def WeakSprings(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WeakSpringsType]:
        """
        Gets or sets the WeakSprings.
        """
        return None

    @property
    def SpringStiffness(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SpringsStiffnessType]:
        """
        Gets or sets the SpringStiffness.
        """
        return None

    @property
    def IgnoreAcousticDamping(self) -> typing.Optional[bool]:
        """
        Gets or sets the IgnoreAcousticDamping.
        """
        return None

    @property
    def CalculateAcceleration(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateAcceleration.
        """
        return None

    @property
    def BackStress(self) -> typing.Optional[bool]:
        """
        Gets or sets the BackStress.
        """
        return None

    @property
    def ContactMiscellaneous(self) -> typing.Optional[bool]:
        """
        Gets or sets the ContactMiscellaneous.
        """
        return None

    @property
    def CStarIntegral(self) -> typing.Optional[bool]:
        """
        Gets or sets the CStarIntegral.
        """
        return None

    @property
    def ElementCurrentDensity(self) -> typing.Optional[bool]:
        """
        Gets or sets the ElementCurrentDensity.
        """
        return None

    @property
    def FieldIntensityandFluxDensity(self) -> typing.Optional[bool]:
        """
        Gets or sets the FieldIntensityandFluxDensity.
        """
        return None

    @property
    def ElectromagneticNodalForces(self) -> typing.Optional[bool]:
        """
        Gets or sets the ElectromagneticNodalForces.
        """
        return None

    @property
    def ContactData(self) -> typing.Optional[bool]:
        """
        Gets or sets the ContactData.
        """
        return None

    @property
    def CalculateVolumeEnergy(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateVolumeEnergy.
        """
        return None

    @property
    def NonlinearData(self) -> typing.Optional[bool]:
        """
        Gets or sets the NonlinearData.
        """
        return None

    @property
    def CalculateEnergy(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateEnergy.
        """
        return None

    @property
    def CalculateEulerAngles(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateEulerAngles.
        """
        return None

    @property
    def HeatGenerationRate(self) -> typing.Optional[bool]:
        """
        Gets or sets the HeatGenerationRate.
        """
        return None

    @property
    def JIntegral(self) -> typing.Optional[bool]:
        """
        Gets or sets the JIntegral.
        """
        return None

    @property
    def MaterialForce(self) -> typing.Optional[bool]:
        """
        Gets or sets the MaterialForce.
        """
        return None

    @property
    def CalculateReactions(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateReactions.
        """
        return None

    @property
    def SIFS(self) -> typing.Optional[bool]:
        """
        Gets or sets the SIFS.
        """
        return None

    @property
    def Strain(self) -> typing.Optional[bool]:
        """
        Gets or sets the Strain.
        """
        return None

    @property
    def Stress(self) -> typing.Optional[bool]:
        """
        Gets or sets the Stress.
        """
        return None

    @property
    def CalculateThermalFlux(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateThermalFlux.
        """
        return None

    @property
    def TStress(self) -> typing.Optional[bool]:
        """
        Gets or sets the TStress.
        """
        return None

    @property
    def CalculateVelocity(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateVelocity.
        """
        return None

    @property
    def CalculateVelocityAndAcceleration(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateVelocityAndAcceleration.
        """
        return None

    @property
    def CampbellDiagram(self) -> typing.Optional[bool]:
        """
        Gets or sets the CampbellDiagram.
        """
        return None

    @property
    def CarryOverTimeStep(self) -> typing.Optional[bool]:
        """
        Gets or sets the CarryOverTimeStep.
        """
        return None

    @property
    def DeleteUnneededFiles(self) -> typing.Optional[bool]:
        """
        Gets or sets the DeleteUnneededFiles.
        """
        return None

    @property
    def CyclicModeSuperposition(self) -> typing.Optional[bool]:
        """
        Gets or sets the CyclicModeSuperposition.
        """
        return None

    @property
    def Damped(self) -> typing.Optional[bool]:
        """
        Gets or sets the Damped.
        """
        return None

    @property
    def EqvDampingRatioFromModal(self) -> typing.Optional[bool]:
        """
        Gets or sets the EqvDampingRatioFromModal.
        """
        return None

    @property
    def ExcludeInsignificantModes(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExcludeInsignificantModes.
        """
        return None

    @property
    def ExportHighStrains(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExportHighStrains.
        """
        return None

    @property
    def ExportLayerEndTemperature(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExportLayerEndTemperature.
        """
        return None

    @property
    def ExportRecoaterInterference(self) -> typing.Optional[bool]:
        """
        Gets or sets the ExportRecoaterInterference.
        """
        return None

    @property
    def FractureSolverControls(self) -> typing.Optional[bool]:
        """
        Gets or sets the FractureSolverControls.
        """
        return None

    @property
    def GeneralMiscellaneous(self) -> typing.Optional[bool]:
        """
        Gets or sets the GeneralMiscellaneous.
        """
        return None

    @property
    def ClusterResults(self) -> typing.Optional[bool]:
        """
        Gets or sets the ClusterResults.
        """
        return None

    @property
    def UserDefinedFrequencies(self) -> typing.Optional[bool]:
        """
        Gets or sets the UserDefinedFrequencies.
        """
        return None

    @property
    def Multistep(self) -> typing.Optional[bool]:
        """
        Gets or sets the Multistep.
        """
        return None

    @property
    def IncludeResidualVector(self) -> typing.Optional[bool]:
        """
        Gets or sets the IncludeResidualVector.
        """
        return None

    @property
    def InverseOption(self) -> typing.Optional[bool]:
        """
        Gets or sets the InverseOption.
        """
        return None

    @property
    def KeepModalResults(self) -> typing.Optional[bool]:
        """
        Gets or sets the KeepModalResults.
        """
        return None

    @property
    def KeepPreStressLoadPattern(self) -> typing.Optional[bool]:
        """
        Gets or sets the KeepPreStressLoadPattern.
        """
        return None

    @property
    def NonLinearSolution(self) -> typing.Optional[bool]:
        """
        Gets the NonLinearSolution.
        """
        return None

    @property
    def QuasiStaticSolution(self) -> typing.Optional[bool]:
        """
        Gets or sets the QuasiStaticSolution.
        """
        return None

    @property
    def LimitSearchToRange(self) -> typing.Optional[bool]:
        """
        Gets or sets the LimitSearchToRange.
        """
        return None

    @property
    def SaveMAPDLDB(self) -> typing.Optional[bool]:
        """
        Gets or sets the SaveMAPDLDB.
        """
        return None

    @property
    def StoreComplexSolution(self) -> typing.Optional[bool]:
        """
        Gets or sets the StoreComplexSolution.
        """
        return None

    @property
    def InertiaRelief(self) -> typing.Optional[bool]:
        """
        Gets or sets the InertiaRelief.
        """
        return None

    @property
    def LargeDeflection(self) -> typing.Optional[bool]:
        """
        Gets or sets the LargeDeflection.
        """
        return None

    @property
    def TimeIntegration(self) -> typing.Optional[bool]:
        """
        Gets or sets the TimeIntegration.
        """
        return None

    @property
    def ElectricOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ElectricOnly.
        """
        return None

    @property
    def StructuralOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the StructuralOnly.
        """
        return None

    @property
    def ThermalOnly(self) -> typing.Optional[bool]:
        """
        Gets or sets the ThermalOnly.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Graph(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnalysisSettingsGraph]:
        """
        Graph property.
        """
        return None

    @property
    def ScratchSolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the ScratchSolverFilesDirectory.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the SolverFilesDirectory.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def GetStepEndTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Step End Time at a given solution step.
            
        """
        pass

    def SetStepEndTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Step End Time for a given solution step.
            
        """
        pass

    def GetAutomaticTimeStepping(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.AutomaticTimeStepping:
        """
        
            Gets the Automatic Time Stepping at a given solution step.
            
        """
        pass

    def SetAutomaticTimeStepping(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.AutomaticTimeStepping) -> None:
        """
        
            Sets the Automatic Time Stepping for a given solution step.
            
        """
        pass

    def GetForceConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Force Convergence Tolerance Type at a given solution step.
            
        """
        pass

    def SetForceConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Force Convergence Tolerance Type for a given solution step.
            
        """
        pass

    def GetForceConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Force Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def SetForceConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Force Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def GetForceConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Force Convergence Value at a given solution step.
            
        """
        pass

    def SetForceConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Force Convergence Value for a given solution step.
            
        """
        pass

    def GetForceConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Force Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def SetForceConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Force Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def GetMomentConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Moment Convergence Tolerance type at a given solution step.
            
        """
        pass

    def SetMomentConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Moment Convergence Tolerance type for a given solution step.
            
        """
        pass

    def GetMomentConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Moment Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def SetMomentConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Moment Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def GetMomentConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Moment Convergence Value at a given solution step.
            
        """
        pass

    def SetMomentConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Moment Convergence Value for a given solution step.
            
        """
        pass

    def GetMomentConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Moment Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def SetMomentConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Moment Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def GetDisplacementConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Displacement Convergence Tolerance type at a given solution step.
            
        """
        pass

    def SetDisplacementConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Displacement Convergence Tolerance type for a given solution step.
            
        """
        pass

    def GetDisplacementConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Displacement Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def SetDisplacementConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Displacement Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def GetDisplacementConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Displacement Convergence Value at a given solution step.
            
        """
        pass

    def SetDisplacementConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Displacement Convergence Value for a given solution step.
            
        """
        pass

    def GetDisplacementConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Displacement Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def SetDisplacementConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Displacement Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def GetRotationConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Rotation Convergence Tolerance type at a given solution step.
            
        """
        pass

    def SetRotationConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Rotation Convergence Tolerance type for a given solution step.
            
        """
        pass

    def GetRotationConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Rotation Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def SetRotationConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Rotation Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def GetRotationConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Rotation Convergence Value at a given solution step.
            
        """
        pass

    def SetRotationConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Rotation Convergence Value for a given solution step.
            
        """
        pass

    def GetRotationConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Rotation Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def SetRotationConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Rotation Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetTemperatureConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Temperature Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetTemperatureConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Temperature Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetTemperatureConvergenceValue(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.NonLinearValueType) -> None:
        """
        
            Sets the Temperature Convergence Value for a given solution step.
            
        """
        pass

    def SetTemperatureConvergenceInputValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Temperature Convergence Input Value for a given solution step.
            
        """
        pass

    def SetTemperatureConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Temperature Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetHeatConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Heat Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetHeatConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Heat Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetHeatConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Heat Convergence Value for a given solution step.
            
        """
        pass

    def SetHeatConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Heat Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetVoltageConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Voltage Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetVoltageConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Voltage Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetVoltageConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Voltage Convergence Value for a given solution step.
            
        """
        pass

    def SetVoltageConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Voltage Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetChargeConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Charge Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetChargeConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Charge Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetChargeConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Charge Convergence Value for a given solution step.
            
        """
        pass

    def SetChargeConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Charge Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetEnergyConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Energy Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetEnergyConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Energy Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetEnergyConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Energy Convergence Value for a given solution step.
            
        """
        pass

    def SetEnergyConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Energy Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetCurrentConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the Current Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetCurrentConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Current Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetCurrentConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Current Convergence Value for a given solution step.
            
        """
        pass

    def SetCurrentConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Current Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetEmagAMPSConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the EmagAMPS Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetEmagAMPSConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the EmagAMPS Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetEmagAMPSConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the EmagAMPS Convergence Value for a given solution step.
            
        """
        pass

    def SetEmagAMPSConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the EmagAMPS Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def SetEmagCSGConvergenceType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType) -> None:
        """
        
            Sets the EmagCSG Convergence Tolerance type for a given solution step.
            
        """
        pass

    def SetEmagCSGConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the EmagCSG Convergence Tolerance as a percentage for a given solution step.
            For example if the user input is 5% then the "value" argument should be set to 5.
            
        """
        pass

    def SetEmagCSGConvergenceValue(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the EmagCSG Convergence Value for a given solution step.
            
        """
        pass

    def SetEmagCSGConvergenceMinimumReference(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the EmagCSG Convergence Minimum Reference for a given solution step.
            
        """
        pass

    def GetTemperatureConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Temperature Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetTemperatureConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Temperature Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetTemperatureConvergenceValue(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.NonLinearValueType:
        """
        
            Gets the Temperature Convergence Value at a given solution step.
            
        """
        pass

    def GetTemperatureConvergenceInputValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Temperature Convergence Input Value at a given solution step.
            
        """
        pass

    def GetTemperatureConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Temperature Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetHeatConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Heat Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetHeatConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Heat Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetHeatConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Heat Convergence Value at a given solution step.
            
        """
        pass

    def GetHeatConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Heat Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetVoltageConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Voltage Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetVoltageConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Voltage Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetVoltageConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Voltage Convergence Value at a given solution step.
            
        """
        pass

    def GetVoltageConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Voltage Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetCurrentConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Current Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetCurrentConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Current Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetCurrentConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Current Convergence Value at a given solution step.
            
        """
        pass

    def GetCurrentConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Current Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetEmagAMPSConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the EmagAMPS Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetEmagAMPSConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the EmagAMPS Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetEmagAMPSConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the EmagAMPS Convergence Value at a given solution step.
            
        """
        pass

    def GetEmagAMPSConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the EmagAMPS Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetEmagCSGConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the EmagCSG Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetEmagCSGConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the EmagCSG Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetEmagCSGConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the EmagCSG Convergence Value at a given solution step.
            
        """
        pass

    def GetEmagCSGConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the EmagCSG Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetEnergyConvergenceType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.ConvergenceToleranceType:
        """
        
            Gets the Energy Convergence Tolerance type at a given solution step.
            
        """
        pass

    def GetEnergyConvergenceTolerance(self, stepNumber: int) -> float:
        """
        
            Gets the Energy Convergence Tolerance as a percentage at a given solution step.
            
        """
        pass

    def GetEnergyConvergenceValue(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Energy Convergence Value at a given solution step.
            
        """
        pass

    def GetEnergyConvergenceMinimumReference(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Energy Convergence Minimum Reference at a given solution step.
            
        """
        pass

    def GetLineSearch(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.LineSearchType:
        """
        
            Gets the Line Search at a given solution step.
            
        """
        pass

    def SetLineSearch(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.LineSearchType) -> None:
        """
        
            Sets the Line Search for a given solution step.
            
        """
        pass

    def GetStabilization(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.StabilizationType:
        """
        
            Gets the Stabilization at a given solution step.
            
        """
        pass

    def SetStabilization(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.StabilizationType) -> None:
        """
        
            Sets the Stabilization for a given solution step.
            
        """
        pass

    def GetStabilizationMethod(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.StabilizationMethod:
        """
        
            Gets the Stabilization Method at a given solution step.
            
        """
        pass

    def SetStabilizationMethod(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.StabilizationMethod) -> None:
        """
        
            Sets the Stabilization Method for a given solution step.
            
        """
        pass

    def GetStabilizationEnergyDissipationRatio(self, stepNumber: int) -> float:
        """
        
            Gets the Stabilization Energy Dissipation Ratio at a given solution step.
            
        """
        pass

    def SetStabilizationEnergyDissipationRatio(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Stabilization Energy Dissipation Ratio for a given solution step.
            
        """
        pass

    def GetStabilizationDampingFactor(self, stepNumber: int) -> float:
        """
        
            Gets the Stabilization Damping Factor at a given solution step.
            
        """
        pass

    def SetStabilizationDampingFactor(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Stabilization Damping Factor for a given solution step.
            
        """
        pass

    def GetStabilizationFirstSubstepOption(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.StabilizationFirstSubstepOption:
        """
        
            Gets the Stabilization First Substep Option at a given solution step.
            
        """
        pass

    def SetStabilizationFirstSubstepOption(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.StabilizationFirstSubstepOption) -> None:
        """
        
            Sets the Stabilization First Substep Option for a given solution step.
            
        """
        pass

    def GetStabilizationForceLimit(self, stepNumber: int) -> float:
        """
        
            Gets the Stabilization Force Limit at a given solution step.
            
        """
        pass

    def SetStabilizationForceLimit(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Stabilization Force Limit for a given solution step.
            
        """
        pass

    def GetStoreResultsAt(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.TimePointsOptions:
        """
        
            Gets the Store Results At at a given solution step.
            
        """
        pass

    def SetStoreResultsAt(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.TimePointsOptions) -> None:
        """
        
            Sets the Store Results At for a given solution step.
            
        """
        pass

    def GetStoreResulsAtValue(self, stepNumber: int) -> int:
        """
        
            Gets the Store Results At Value at a given solution step.
            
        """
        pass

    def SetStoreResulsAtValue(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Store Results At Value for a given solution step.
            
        """
        pass

    def GetDefineBy(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.TimeStepDefineByType:
        """
        
            Gets the Define By at a given solution step.
            
        """
        pass

    def SetDefineBy(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.TimeStepDefineByType) -> None:
        """
        
            Sets the Define By for a given solution step.
            
        """
        pass

    def GetCarryOverTimeStep(self, stepNumber: int) -> bool:
        """
        
            Gets the Carry Over Time Step at a given solution step.
            
        """
        pass

    def SetCarryOverTimeStep(self, stepNumber: int, value: bool) -> None:
        """
        
            Sets the Carry Over Time Step for a given solution step.
            
        """
        pass

    def GetInitialTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Initial Time Step at a given solution step.
            
        """
        pass

    def SetInitialTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Initial Time Step for a given solution step.
            
        """
        pass

    def GetMinimumTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Minimum Time Step at a given solution step.
            
        """
        pass

    def SetMinimumTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Minimum Time Step for a given solution step.
            
        """
        pass

    def GetMaximumTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Maximum Time Step at a given solution step.
            
        """
        pass

    def SetMaximumTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Maximum Time Step for a given solution step.
            
        """
        pass

    def GetInitialSubsteps(self, stepNumber: int) -> int:
        """
        
            Gets the Initial Substeps at a given solution step.
            
        """
        pass

    def SetInitialSubsteps(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Initial Substeps for a given solution step.
            
        """
        pass

    def GetMinimumSubsteps(self, stepNumber: int) -> int:
        """
        
            Gets the Minimum Substeps at a given solution step.
            
        """
        pass

    def SetMinimumSubsteps(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Minimum Substeps for a given solution step.
            
        """
        pass

    def GetMaximumSubsteps(self, stepNumber: int) -> int:
        """
        
            Gets the Maximum Substeps at a given solution step.
            
        """
        pass

    def SetMaximumSubsteps(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Maximum Substeps for a given solution step.
            
        """
        pass

    def SetNumberOfSubSteps(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Number of Substeps for a given solution step.
            
        """
        pass

    def GetNumberOfSubSteps(self, stepNumber: int) -> int:
        """
        
            Gets the Number of Substeps for a given solution step.
            
        """
        pass

    def SetTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Time Step for a given solution step.
            
        """
        pass

    def GetTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Sets the Time Step for a given solution step.
            
        """
        pass

    def SetTimeIntegration(self, stepNumber: int, value: bool) -> None:
        """
        
            Sets the TimeIntegration for a given solution step.
            
        """
        pass

    def SetStructuralOnly(self, stepNumber: int, value: bool) -> None:
        """
        
            Sets the TimeIntegration Structural for a given solution step.
            
        """
        pass

    def SetThermalOnly(self, stepNumber: int, value: bool) -> None:
        """
        
            Sets the TimeIntegration Thermal for a given solution step.
            
        """
        pass

    def GetTimeIntegration(self, stepNumber: int) -> bool:
        """
        
            Gets the TimeIntegration for a given solution step.
            
        """
        pass

    def GetStructuralOnly(self, stepNumber: int) -> bool:
        """
        
            Gets the TimeIntegration Structural for a given solution step.
            
        """
        pass

    def GetThermalOnly(self, stepNumber: int) -> bool:
        """
        
            Sets the TimeIntegration Thermal for a given solution step.
            
        """
        pass

    def GetStepName(self, stepNumber: int) -> str:
        """
        Gets the Step name at a given step.
        """
        pass

    def SetStepName(self, stepNumber: int, value: str) -> None:
        """
        Sets the Step name at a given step.
        """
        pass

    def GetAMStepType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.AMProcessStepType:
        """
        Gets the AM Process Step Type at a given step.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        CopyTo method.
        """
        pass

    def SetCreepEffects(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.Creep) -> None:
        """
        
            Sets the Creep Effects for a given solution step.
            
        """
        pass

    def GetCreepEffects(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.Creep:
        """
        
            Gets the Creep Effects for a given solution step.
            
        """
        pass

    def SetCreepLimitRatio(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Creep Limit Ratio for a given solution step.
            
        """
        pass

    def GetCreepLimitRatio(self, stepNumber: int) -> float:
        """
        
            Gets the Creep Limit Ratio for a given solution step.
            
        """
        pass

    def DeleteAllRestartPoints(self) -> None:
        """
        DeleteAllRestartPoints method.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class EXDAnalysisSettings(object):
    """
    
            Defines Analysis Settings for Explicit Dynamics System.
            Note: Cycles in the UI are referred to as TimeSteps in API
            
    """

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        
            Gets the Internal Object. For advanced usage only.
            
        """
        return None

    @property
    def PreferenceType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDPreferenceType]:
        """
        
            Gets or sets the PreferenceType
            
        """
        return None

    @property
    def NumberOfSteps(self) -> typing.Optional[int]:
        """
        
            Gets or sets the NumberOfSteps.
            
        """
        return None

    @property
    def CurrentStepNumber(self) -> typing.Optional[int]:
        """
        
            Gets or sets the CurrentStepNumber.
            
        """
        return None

    @property
    def ResumeFromTimeStep(self) -> typing.Optional[int]:
        """
        
            Gets or sets the ResumeFromCycle.
             
        """
        return None

    @property
    def MaximumTimeSteps(self) -> typing.Optional[int]:
        """
        
            Gets or sets the MaximumNumberofCycles.
             
        """
        return None

    @property
    def MaximumEnergyError(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  MaximumEnergyError.
             
        """
        return None

    @property
    def ReferenceEnergyTimeStep(self) -> typing.Optional[int]:
        """
        
            Gets or sets the ReferenceEnergyCycle.
             
        """
        return None

    @property
    def InitialTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the InitialTimeStep.
             
        """
        return None

    @property
    def MinimumTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the MinimumTimeStep.
             
        """
        return None

    @property
    def MaximumTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the MaximumTimeStep.
             
        """
        return None

    @property
    def TimeStepSafetyFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  TimeStepSafetyFactor.
             
        """
        return None

    @property
    def CharZoneDimensionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDCharZoneDimensionType]:
        """
        
            Gets or sets the  CharZoneDimensionType.
             
        """
        return None

    @property
    def StepawareMassScalingType(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets the Step aware Mass Scaling Controls.
             
        """
        return None

    @property
    def AutomaticMassScalingType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the  AutomaticMassScaling.
             
        """
        return None

    @property
    def MassScalingMinTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  MassScalingMinTimeStep.
             
        """
        return None

    @property
    def MassScalingMaxElem(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  MassScalingMaxElem.
             
        """
        return None

    @property
    def MassScalingMaxPart(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  MassScalingMaxPart.
             
        """
        return None

    @property
    def MassScalingUpdateFreq(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  MassScalingUpdateFreq.
             
        """
        return None

    @property
    def SolverPrecisionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDSolverPrecisionType]:
        """
        
            Gets or sets the  SolverPrecisionType.
             
        """
        return None

    @property
    def SolveUnits(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDSolveUnitsType]:
        """
        
            Gets or sets the  SolveUnits.
             
        """
        return None

    @property
    def BeamSolutionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDBeamSolutionType]:
        """
        
            Gets or sets the  BeamSolutionType.
             
        """
        return None

    @property
    def BeamTimeStepSafetyFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  BeamTimeStepSafetyFactor.
             
        """
        return None

    @property
    def HexIntegrationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDHexIntegrationType]:
        """
        
            Gets or sets the  HexIntegrationType.
             
        """
        return None

    @property
    def ShellSublayers(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  ShellSublayers.
             
        """
        return None

    @property
    def ShellShearCorrectionFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  ShellShearCorrectionFactor.
             
        """
        return None

    @property
    def ShellWarpCorrection(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the  ShellWarpCorrection.
             
        """
        return None

    @property
    def ShellThicknessUpdateType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDShellThicknessUpdateType]:
        """
        
            Gets or sets the  ShellThicknessUpdateType.
             
        """
        return None

    @property
    def PusoCoefficient(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  PusoCoefficient.
             
        """
        return None

    @property
    def TetPressureIntegrationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDTetPressureIntegrationType]:
        """
        
            Gets or sets the  TetIntegrationType.
             
        """
        return None

    @property
    def ShellInertiaUpdateType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDShellInertiaUpdateType]:
        """
        
            Gets or sets the  ShellInertiaUpdateType.
             
        """
        return None

    @property
    def DensityUpdateType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDDensityUpdateType]:
        """
        
            Gets or sets the  DensityUpdateType.
             
        """
        return None

    @property
    def SphMinTimeStep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  Minimum Timestep for SPH.
             
        """
        return None

    @property
    def SPHMinDensityFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  Minimum Density Factor for SPH.
             
        """
        return None

    @property
    def SPHMaxDensityFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  Maximum Density Factor for SPH.
             
        """
        return None

    @property
    def SPHNodeDensityCutoffOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDSPHNodeDensityCutoffOption]:
        """
        
            Gets or sets the  SPHNodeDensityCutoffOption.
             
        """
        return None

    @property
    def DetonationBurnType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDDetonationBurnType]:
        """
        
            Gets or sets the  DetonationBurnType.
             
        """
        return None

    @property
    def MinimumVelocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  MinimumVelocity.
             
        """
        return None

    @property
    def MaximumVelocity(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  MaximumVelocity.
             
        """
        return None

    @property
    def RadiusCutoff(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  RadiusCutoff.
             
        """
        return None

    @property
    def MinimumStrainCutOff(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  MinimumStrainCutOff.
             
        """
        return None

    @property
    def EulerSizeDefType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerSizeDefType]:
        """
        
            Gets or sets the  EulerSizeDefType.
             
        """
        return None

    @property
    def EulerDomainType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerDomainType]:
        """
        
            Gets or sets the  EulerDomainType.
             
        """
        return None

    @property
    def EulerDisplayBox(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the  EulerDisplayBox.
             
        """
        return None

    @property
    def EulerDomScopeDefType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerDomScopeDefType]:
        """
        
            Gets or sets the  EulerDomScopeDefType.
             
        """
        return None

    @property
    def EulerXScaleFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  EulerXScaleFactor.
             
        """
        return None

    @property
    def EulerYScaleFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  EulerYScaleFactor.
             
        """
        return None

    @property
    def EulerZScaleFactor(self) -> typing.Optional[float]:
        """
        
            Gets or sets the  EulerZScaleFactor.
             
        """
        return None

    @property
    def EulerXOrigin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerXOrigin.
             
        """
        return None

    @property
    def EulerYOrigin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerYOrigin.
             
        """
        return None

    @property
    def EulerZOrigin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerZOrigin.
             
        """
        return None

    @property
    def EulerXDim(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerXDim.
             
        """
        return None

    @property
    def EulerYDim(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerYDim.
             
        """
        return None

    @property
    def EulerZDim(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerZDim.
             
        """
        return None

    @property
    def EulerResolutionDefType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerResolutionDefType]:
        """
        
            Gets or sets the  EulerResolutionDefType.
             
        """
        return None

    @property
    def EulerGradedDefinition(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerGradedDefinition]:
        """
        
            Gets or sets the  EulerGradedDefinition.
             
        """
        return None

    @property
    def EulerGradeIncrement(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerGradeIncrement.
             
        """
        return None

    @property
    def EulerGradeNumberOfTimes(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerGradeNumberOfTimes.
             
        """
        return None

    @property
    def EulerCellSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerCellSize.
             
        """
        return None

    @property
    def EulerTotalCells(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerTotalCells.
             
        """
        return None

    @property
    def EulerXZones(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerXZones.
             
        """
        return None

    @property
    def EulerYZones(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerYZones.
             
        """
        return None

    @property
    def EulerZZones(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerZZones.
             
        """
        return None

    @property
    def EulerBoundLowerX(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundLowerX.
             
        """
        return None

    @property
    def EulerBoundLowerY(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundLowerY.
             
        """
        return None

    @property
    def EulerBoundLowerZ(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundLowerZ.
             
        """
        return None

    @property
    def EulerBoundUpperX(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundUpperX.
             
        """
        return None

    @property
    def EulerBoundUpperY(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundUpperY.
             
        """
        return None

    @property
    def EulerBoundUpperZ(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerBoundaryDefType]:
        """
        
            Gets or sets the  EulerBoundUpperZ.
             
        """
        return None

    @property
    def EulerTrackType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDEulerTrackType]:
        """
        
            Gets the  EulerTrackType.
             
        """
        return None

    @property
    def EulerPropertyXmin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyXmin.
             
        """
        return None

    @property
    def EulerPropertyYmin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyYmin.
             
        """
        return None

    @property
    def EulerPropertyZmin(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyZmin.
             
        """
        return None

    @property
    def EulerPropertyXsize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyXsize.
             
        """
        return None

    @property
    def EulerPropertyYsize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyYsize.
             
        """
        return None

    @property
    def EulerPropertyZsize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the  EulerPropertyZsize.
             
        """
        return None

    @property
    def EulerPropertyXres(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerPropertyXres.
             
        """
        return None

    @property
    def EulerPropertyYres(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerPropertyYres.
             
        """
        return None

    @property
    def EulerPropertyZres(self) -> typing.Optional[int]:
        """
        
            Gets or sets the  EulerPropertyZres.
             
        """
        return None

    @property
    def EulerPropertyDisplayBox(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the  EulerPropertyDisplayBox.
             
        """
        return None

    @property
    def LinearArtificialViscosity(self) -> typing.Optional[float]:
        """
        
            Gets or sets the LinearArtificialViscosity.
            
        """
        return None

    @property
    def QuadraticArtificialViscosity(self) -> typing.Optional[float]:
        """
        
            Gets or sets the QuadraticArtificialViscosity.
            
        """
        return None

    @property
    def LinearViscosityExpansionType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the LinearViscosityExpansionType.
            
        """
        return None

    @property
    def ArtificialViscosityForShellsType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the ArtificialViscosityForShellsType.
            
        """
        return None

    @property
    def LinearViscositySPH(self) -> typing.Optional[float]:
        """
        
            Gets or sets the Linear Artificial Viscosity for SPH.
            
        """
        return None

    @property
    def QuadratricViscositySPH(self) -> typing.Optional[float]:
        """
        
            Gets or sets the Quadratic Artificial Viscosity for SPH.
            
        """
        return None

    @property
    def HourglassDampingType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDHourglassDampingType]:
        """
        
            Gets or sets the HourglassDampingType.
            
        """
        return None

    @property
    def StiffnessCoefficient(self) -> typing.Optional[float]:
        """
        
            Gets or sets the StiffnessCoefficient.
            
        """
        return None

    @property
    def ViscousCoefficient(self) -> typing.Optional[float]:
        """
        
            Gets or sets the ViscousCoefficient.
            
        """
        return None

    @property
    def ViscousCoefficientFB(self) -> typing.Optional[float]:
        """
        
            Gets or sets the ViscousCoefficientFB.
            
        """
        return None

    @property
    def ErosionOnGeomStrainType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the ErosionOnGeomStrainType.
            
        """
        return None

    @property
    def ErosionGeomStrainLimit(self) -> typing.Optional[float]:
        """
        
            Gets or sets the ErosionGeomStrainLimit
            
        """
        return None

    @property
    def ErosionOnMaterialFailureType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the ErosionOnMaterialFailureType
            
        """
        return None

    @property
    def ErosionOnMinElemTimestepType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the ErosionOnMinElemTimestepType
            
        """
        return None

    @property
    def ErosionMinElemTimestep(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the ErosionMinElemTimestep
            
        """
        return None

    @property
    def ErosionRetainIntertiaType(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the ErosionRetainIntertiaType
            
        """
        return None

    @property
    def StepawareOutputControlsType(self) -> typing.Optional[bool]:
        """
        
            Gets or Sets the Step aware Output Controls.
             
        """
        return None

    @property
    def OutputContactForcesOnType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDOutputContactForcesOnType]:
        """
        
            Gets or Sets OutputContactForces Increment Type.
             
        """
        return None

    @property
    def OutputContactForcesOnTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or Sets the Time increment for OutputContactForcesOnTime.
             
        """
        return None

    @property
    def OutputContactForcesOnTimeSteps(self) -> typing.Optional[int]:
        """
        
            Gets or Sets the Cycle increment for OutputContactForcesOnTimeSteps.
             
        """
        return None

    @property
    def OutputContactForcesOnPoints(self) -> typing.Optional[int]:
        """
        
            Gets or Sets the Points increment for OutputContactForcesOnPoints.
             
        """
        return None

    @property
    def SavePrintSummaryOnType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDSavePrintSummaryOnType]:
        """
        
            Gets or Sets SavePrintSummaryOnType.
             
        """
        return None

    @property
    def SavePrintSummaryOnTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or Sets the Time increment for SavePrintSummaryOnTime.
             
        """
        return None

    @property
    def SavePrintSummaryOnTimeSteps(self) -> typing.Optional[int]:
        """
        
            Gets or Sets Cycle increment for SavePrintSummaryOnTimeSteps.
             
        """
        return None

    @property
    def OutputRemapFile(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDOutputRemapFileOnType]:
        """
        
            Gets or Sets the Output Remap File Type.
             
        """
        return None

    @property
    def SaveUserEditOnType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.EXDSaveUserEditOnType]:
        """
        
            Gets or Sets SaveUserEditOnType.
             
        """
        return None

    @property
    def SaveUserEditOnTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or Sets Time increment for SaveUserEditOnTime.
             
        """
        return None

    @property
    def SaveUserEditOnTimeSteps(self) -> typing.Optional[int]:
        """
        
            Gets or Sets Cycle increment for SaveUserEditOnTimeSteps.
             
        """
        return None

    @property
    def Graph(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnalysisSettingsGraph]:
        """
        Graph property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAnalysisSettings]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScratchSolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the ScratchSolverFilesDirectory.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the SolverFilesDirectory.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def GetStepEndTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Step End Time at a given solution step.
            
        """
        pass

    def SetStepEndTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Step End Time for a given solution step.
            
        """
        pass

    def GetLoadStepType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.EXDLoadStepType:
        """
        
            Gets the  LoadStepType for a step.
             
        """
        pass

    def SetLoadStepType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDLoadStepType) -> None:
        """
        
            Sets the LoadStepType for a step.
             
        """
        pass

    def getADRConvergenceMethod(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.EXDADRConvergenceMethod:
        """
        
            Gets the Covergence Method for ADR loadstep.
             
        """
        pass

    def setADRConvergenceMethod(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDADRConvergenceMethod) -> None:
        """
        
            Sets the Covergence Method for ADR loadstep.
             
        """
        pass

    def getADRConvergenceTolerance(self, stepNumber: int) -> typing.Any:
        """
        
            Gets the Covergence Tolerance for ADR loadstep.
             
        """
        pass

    def setADRConvergenceTolerance(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the Covergence Tolerance for ADR loadstep.
             
        """
        pass

    def getADRMaximumIterations(self, stepNumber: int) -> typing.Any:
        """
        
            Gets the Maximum Iterations for ADR loadstep.
             
        """
        pass

    def setADRMaximumIterations(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Maximum Iterations for ADR loadstep.
             
        """
        pass

    def GetAutomaticMassScalingType(self, stepNumber: int) -> bool:
        """
        
            Gets the  AutomaticMassScalingType for a load step.
             
        """
        pass

    def SetAutomaticMassScalingType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDAutomaticMassScalingType) -> None:
        """
        
            Sets the  AutomaticMassScalingType for a load step.
             
        """
        pass

    def GetMassScalingMinTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the  MassScalingMinTimeStep for a load step.
             
        """
        pass

    def SetMassScalingMinTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the  MassScalingMinTimeStep for a load step.
             
        """
        pass

    def GetStaticDamping(self, stepNumber: int) -> typing.Any:
        """
        
            Gets the StaticDamping.
            
        """
        pass

    def SetStaticDamping(self, stepNumber: int, value: float) -> None:
        """
        
            Sets the StaticDamping.
            
        """
        pass

    def GetSaveResultsOnType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.EXDSaveResultsOnType:
        """
        
            Gets the  Save Results Type for a load step.
             
        """
        pass

    def SetSaveResultsOnType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDSaveResultsOnType) -> None:
        """
        
            Sets the  Save Results Type for a load step.
             
        """
        pass

    def GetSaveResultsOnTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Time increment for Save Results On for a load step.
             
        """
        pass

    def SetSaveResultsOnTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Set the Time increment for Save Results On for a load step.
             
        """
        pass

    def GetSaveResultsOnTimeSteps(self, stepNumber: int) -> int:
        """
        
            Gets the Cycle increment for Save Results On for a load step.
             
        """
        pass

    def SetSaveResultsOnTimeSteps(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the Cycle increment for Save Results On for a load step.
             
        """
        pass

    def GetSaveResultsOnPoints(self, stepNumber: int) -> int:
        """
        
            Gets the Points increment for Save Results On for a load step.
             
        """
        pass

    def SetSaveResultsOnPoints(self, stepNumber: int, value: int) -> None:
        """
        
            Set the Points increment for Save Results On for a load step.
             
        """
        pass

    def GetSaveRestartsOnType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.EXDSaveRestartsOnType:
        """
        
            Gets the  Save Restarts Type for a load step.
             
        """
        pass

    def SetSaveRestartsOnType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDSaveRestartsOnType) -> None:
        """
        
            Sets the  Save Restarts Type for a load step.
             
        """
        pass

    def GetSaveRestartsOnTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Time increment for Save Restarts On for a load step.
             
        """
        pass

    def SetSaveRestartsOnTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Set the Time increment for Save Restarts On for a load step.
             
        """
        pass

    def GetSaveRestartsOnTimeSteps(self, stepNumber: int) -> int:
        """
        
            Gets the Cycle increment for Save Restarts On for a load step.
             
        """
        pass

    def SetSaveRestartsOnTimeSteps(self, stepNumber: int, value: int) -> None:
        """
        
            Set the Cycle increment for Save Restarts On for a load step.
             
        """
        pass

    def GetSaveRestartsOnPoints(self, stepNumber: int) -> int:
        """
        
            Gets the Points increment for Save Restarts On Points for a load step.
             
        """
        pass

    def SetSaveRestartsOnPoints(self, stepNumber: int, value: int) -> None:
        """
        
            Set the Points increment for Save Restarts On for a load step.
             
        """
        pass

    def GetSaveProbeDataOnType(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.EXDSaveProbeDataOnType:
        """
        
            Gets the  Save ProbeData Type for a load step.
             
        """
        pass

    def SetSaveProbeDataOnType(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.EXDSaveProbeDataOnType) -> None:
        """
        
            Sets the  Save ProbeData Type for a load step.
             
        """
        pass

    def GetSaveProbeDataOnTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Time increment for Save ProbeData On for a load step.
             
        """
        pass

    def SetSaveProbeDataOnTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Set the Time increment for Save ProbeData On for a load step.
             
        """
        pass

    def GetSaveProbeDataOnTimeSteps(self, stepNumber: int) -> int:
        """
        
            Gets the Cycle increment for Save ProbeData On for a load step.
             
        """
        pass

    def SetSaveProbeDataOnTimeSteps(self, stepNumber: int, value: int) -> None:
        """
        
            Set the Cycle increment for Save ProbeData On for a load step.
             
        """
        pass

    def DeleteAllRestartPoints(self) -> None:
        """
        DeleteAllRestartPoints method.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


class RBDAnalysisSettings(object):

    @property
    def InternalObject(self) -> typing.Optional[typing.Any]:
        """
        InternalObject property.
        """
        return None

    @property
    def NumberOfSteps(self) -> typing.Optional[int]:
        """
        
            Gets or sets the NumberOfSteps.
            
        """
        return None

    @property
    def CurrentStepNumber(self) -> typing.Optional[int]:
        """
        
            Gets or sets the CurrentStepNumber.
            
        """
        return None

    @property
    def TimeIntegrationType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDTimeIntegrationType]:
        """
        
            Gets or sets the Integration Method.
            
        """
        return None

    @property
    def PositionCorrection(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the PositionCorrection.
            
        """
        return None

    @property
    def VelocityCorrection(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the VelocityCorrection.
            
        """
        return None

    @property
    def CorrectionType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDCorrectionType]:
        """
        
            Gets or sets the CorrectionType.
            
        """
        return None

    @property
    def AssemblyType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDCorrectionType]:
        """
        
            Gets or sets the AssemblyType.
            
        """
        return None

    @property
    def DropoffTolerance(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the DropoffTolerance.
            
        """
        return None

    @property
    def RelativeAssemblyTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the RelativeAssemblyTolerance activity.
            
        """
        return None

    @property
    def RelativeAssemblyToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the RelativeAssemblyToleranceValue.
            
        """
        return None

    @property
    def EnergyAccuracyTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the EnergyAccuracyTolerance activity.
            
        """
        return None

    @property
    def EnergyAccuracyToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the EnergyAccuracyToleranceValue.
            
        """
        return None

    @property
    def NumericalDampingTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the NumericalDamping activity.
            
        """
        return None

    @property
    def NumericalDampingValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the NumericalDampingValue.
            
        """
        return None

    @property
    def ForceResidualTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the ForceResidualTolerance activity.
            
        """
        return None

    @property
    def ForceResidualToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the ForceResidualToleranceValue.
            
        """
        return None

    @property
    def ConstraintEquationResidualTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the ConstraintEquationResidualTolerance activity.
            
        """
        return None

    @property
    def ConstraintEquationResidualToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the ConstraintEquationResidualToleranceValue.
            
        """
        return None

    @property
    def VelocityConstraintEquationResidualTolerance(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDProgramControlType]:
        """
        
            Gets or sets the VelocityConstraintEquationResidualTolerance activity.
            
        """
        return None

    @property
    def VelocityConstraintEquationResidualToleranceValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the ConstraintEquationResidualToleranceValue.
            
        """
        return None

    @property
    def PerformStaticAnalysis(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.RBDDoStaticAnalysisType]:
        """
        
            Gets or sets the .
            
        """
        return None

    @property
    def Graph(self) -> typing.Optional[Ansys.Mechanical.Graphics.AnalysisSettingsGraph]:
        """
        Graph property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAnalysisSettings]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ScratchSolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the ScratchSolverFilesDirectory.
        """
        return None

    @property
    def SolverFilesDirectory(self) -> typing.Optional[str]:
        """
        Gets the SolverFilesDirectory.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Children(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets the list of children.
        """
        return None

    @property
    def Comments(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Comment]]:
        """
        Gets the list of associated comments.
        """
        return None

    @property
    def Figures(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Figure]]:
        """
        Gets the list of associated figures.
        """
        return None

    @property
    def Images(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.Image]]:
        """
        Gets the list of associated images.
        """
        return None

    @property
    def Properties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties for this object.
            
        """
        return None

    @property
    def VisibleProperties(self) -> typing.Optional[tuple[Ansys.ACT.Automation.Mechanical.Property]]:
        """
        
            Gets the list of properties that are visible for this object.
            
        """
        return None

    def GetStepEndTime(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Step End Time at a given solution step.
            
        """
        pass

    def SetStepEndTime(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Step End Time for a given solution step.
            
        """
        pass

    def GetAutomaticTimeStepping(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.AutomaticTimeStepping:
        """
        
            Gets the Automatic Time Stepping at a given solution step.
            
        """
        pass

    def SetAutomaticTimeStepping(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.AutomaticTimeStepping) -> None:
        """
        
            Sets the Automatic Time Stepping for a given solution step.
            
        """
        pass

    def GetCarryOverTimeStep(self, stepNumber: int) -> bool:
        """
        
            Gets the Carry Over Time Step at a given solution step.
            
        """
        pass

    def SetCarryOverTimeStep(self, stepNumber: int, value: bool) -> None:
        """
        
            Sets the Carry Over Time Step for a given solution step.
            
        """
        pass

    def GetInitialTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Initial Time Step at a given solution step.
            
        """
        pass

    def SetInitialTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Initial Time Step for a given solution step.
            
        """
        pass

    def GetMinimumTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Minimum Time Step at a given solution step.
            
        """
        pass

    def SetMinimumTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Minimum Time Step for a given solution step.
            
        """
        pass

    def GetMaximumTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the Maximum Time Step at a given solution step.
            
        """
        pass

    def SetMaximumTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the Maximum Time Step for a given solution step.
            
        """
        pass

    def GetTimeStep(self, stepNumber: int) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the (fixed) Time Step at a given solution step.
            
        """
        pass

    def SetTimeStep(self, stepNumber: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        
            Sets the (fixed) Time Step for a given solution step.
            
        """
        pass

    def GetStoreResultAt(self, stepNumber: int) -> Ansys.Mechanical.DataModel.Enums.TimePointsOptions:
        """
        
            Gets the StoreResultAt setting at a given solution step.
            
        """
        pass

    def SetStoreResultAt(self, stepNumber: int, value: Ansys.Mechanical.DataModel.Enums.TimePointsOptions) -> None:
        """
        
            Sets the StoreResultAt setting for a given solution step.
            
        """
        pass

    def GetStoreResultAtValue(self, stepNumber: int) -> int:
        """
        
            Gets the StoreResultAtValue setting at a given solution step.
            
        """
        pass

    def SetStoreResultAtValue(self, stepNumber: int, value: int) -> None:
        """
        
            Sets the StoreResultAtValue setting for a given solution step.
            
        """
        pass

    def DeleteAllRestartPoints(self) -> None:
        """
        DeleteAllRestartPoints method.
        """
        pass

    def GetChildren(self, recurses: bool, children: typing.List[ChildrenType]) -> typing.List[ChildrenType]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def GetChildren(self, category: Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory, recurses: bool, children: typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Gets the list of children, filtered by type.
        """
        pass

    def AddComment(self) -> Ansys.ACT.Automation.Mechanical.Comment:
        """
        Creates a new child Comment.
        """
        pass

    def AddFigure(self) -> Ansys.ACT.Automation.Mechanical.Figure:
        """
        Creates a new child Figure.
        """
        pass

    def AddImage(self, filePath: str) -> Ansys.ACT.Automation.Mechanical.Image:
        """
        
            Creates a new child Image.
            If a filePath is provided, the image will be loaded from that file,
            if not, the image will be a screen capture of the Geometry window.
            
        """
        pass

    def Activate(self) -> None:
        """
        Activate the current object.
        """
        pass

    def CopyTo(self, other: Ansys.ACT.Automation.Mechanical.DataModelObject) -> None:
        """
        
            Copies all visible properties from this object to another.
            
        """
        pass

    def Duplicate(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        
            Creates a copy of the current DataModelObject.
            
        """
        pass

    def GroupAllSimilarChildren(self) -> None:
        """
        Run the GroupAllSimilarChildren action.
        """
        pass

    def GroupSimilarObjects(self) -> Ansys.ACT.Automation.Mechanical.TreeGroupingFolder:
        """
        Run the GroupSimilarObjects action.
        """
        pass

    def PropertyByName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its unique name.
            
        """
        pass

    def PropertyByAPIName(self, name: str) -> Ansys.ACT.Automation.Mechanical.Property:
        """
        
            Get a property by its API name.
            If multiple properties have the same API Name, only the first property with that name will be returned.
            
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Creates a new parameter for a Property.
            
        """
        pass

    def GetParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        
            Gets the parameter corresponding to the given property.
            
        """
        pass

    def RemoveParameter(self, propName: str) -> None:
        """
        
            Removes the parameter from the parameter set corresponding to the given property.
            
        """
        pass


