"""AdditiveManufacturing module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class AMBuildSettings(object):
    """
    Defines a AMBuildSettings.
    """

    @property
    def LayerHeightType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMLayerHeightType]:
        """
        
            LayerHeightType - Get/Sets the layer height type.
            
        """
        return None

    @property
    def ThermalStrainMaterialModel(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMThermalStrainMaterialModel]:
        """
        Gets or sets the MachineLearningModel using the deprecated ThermalStrainMaterialModel methods.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMProcessSettingsAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Absorptivity(self) -> typing.Optional[float]:
        """
        Gets or sets the Absorptivity.
        """
        return None

    @property
    def ASCParallel(self) -> typing.Optional[float]:
        """
        Gets or sets the ASCParallel.
        """
        return None

    @property
    def ASCPerpendicular(self) -> typing.Optional[float]:
        """
        Gets or sets the ASCPerpendicular.
        """
        return None

    @property
    def ASCVertical(self) -> typing.Optional[float]:
        """
        Gets or sets the ASCVertical.
        """
        return None

    @property
    def BeamDiameter(self) -> typing.Optional[float]:
        """
        Gets or sets the BeamDiameter.
        """
        return None

    @property
    def BeamPower(self) -> typing.Optional[float]:
        """
        Gets or sets the BeamPower.
        """
        return None

    @property
    def PowderPropertyFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the PowderPropertyFactor.
        """
        return None

    @property
    def DwellTimeMultiple(self) -> typing.Optional[float]:
        """
        Gets or sets the DwellTimeMultiple.
        """
        return None

    @property
    def GeneratedLayerRotationAngle(self) -> typing.Optional[float]:
        """
        Gets or sets the GeneratedLayerRotationAngle.
        """
        return None

    @property
    def GeneratedStartLayerAngle(self) -> typing.Optional[float]:
        """
        Gets or sets the GeneratedStartLayerAngle.
        """
        return None

    @property
    def NumberOfHeatSources(self) -> typing.Optional[int]:
        """
        Gets or sets the NumberOfHeatSources.
        """
        return None

    @property
    def ScanPatternBuildFilePath(self) -> typing.Optional[str]:
        """
        Gets or sets the ScanPatternBuildFilePath.
        """
        return None

    @property
    def ScanStripeWidth(self) -> typing.Optional[float]:
        """
        Gets or sets the ScanStripeWidth.
        """
        return None

    @property
    def StrainScalingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the StrainScalingFactor.
        """
        return None

    @property
    def StrainScalingFactorX(self) -> typing.Optional[float]:
        """
        Gets or sets the StrainScalingFactorX.
        """
        return None

    @property
    def StrainScalingFactorY(self) -> typing.Optional[float]:
        """
        Gets or sets the StrainScalingFactorY.
        """
        return None

    @property
    def StrainScalingFactorZ(self) -> typing.Optional[float]:
        """
        Gets or sets the StrainScalingFactorZ.
        """
        return None

    @property
    def ThermalStrainScalingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalStrainScalingFactor.
        """
        return None

    @property
    def BuildGasConvectionCoefficient(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BuildGasConvectionCoefficient.
        """
        return None

    @property
    def BuildGasTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BuildGasTemperature.
        """
        return None

    @property
    def BuildPowderConvectionCoefficient(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BuildPowderConvectionCoefficient.
        """
        return None

    @property
    def BuildPowderTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the BuildPowderTemperature.
        """
        return None

    @property
    def CooldownGasConvectionCoefficient(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CooldownGasConvectionCoefficient.
        """
        return None

    @property
    def CooldownGasTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CooldownGasTemperature.
        """
        return None

    @property
    def CooldownPowderConvectionCoefficient(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CooldownPowderConvectionCoefficient.
        """
        return None

    @property
    def CooldownPowderTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the CooldownPowderTemperature.
        """
        return None

    @property
    def DepositionThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DepositionThickness.
        """
        return None

    @property
    def DwellTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DwellTime.
        """
        return None

    @property
    def HatchSpacing(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the HatchSpacing.
        """
        return None

    @property
    def LayerHeightValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the LayerHeightValue.
        """
        return None

    @property
    def PreheatTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the PreheatTemperature.
        """
        return None

    @property
    def RoomTemperature(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the RoomTemperature.
        """
        return None

    @property
    def ScanSpeed(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ScanSpeed.
        """
        return None

    @property
    def BuildGasOrPowderTemperatureType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMProcessSettingsType]:
        """
        Gets or sets the BuildGasOrPowderTemperatureType.
        """
        return None

    @property
    def BuildMachineType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMBuildMachineType]:
        """
        Gets or sets the BuildMachineType.
        """
        return None

    @property
    def CooldownGasOrPowderTemperatureType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMProcessSettingsType]:
        """
        Gets or sets the CooldownGasOrPowderTemperatureType.
        """
        return None

    @property
    def HeatingDuration(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMHeatingDurationType]:
        """
        Gets or sets the HeatingDuration.
        """
        return None

    @property
    def HeatingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMHeatingMethod]:
        """
        Gets or sets the HeatingMethod.
        """
        return None

    @property
    def InherentStrainDefinition(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMInherentStrainDefinition]:
        """
        Gets or sets the InherentStrainDefinition.
        """
        return None

    @property
    def MachineLearningModel(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMMachineLearningModel]:
        """
        Gets or sets the MachineLearningModel.
        """
        return None

    @property
    def AdditiveProcess(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMProcessType]:
        """
        Gets or sets the AdditiveProcess.
        """
        return None

    @property
    def ScanPatternDefinition(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMScanPatternDefinition]:
        """
        Gets or sets the ScanPatternDefinition.
        """
        return None

    @property
    def ThermalStrainMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMThermalStrainMethod]:
        """
        Gets or sets the ThermalStrainMethod.
        """
        return None

    @property
    def InherentStrain(self) -> typing.Optional[bool]:
        """
        Gets or sets the InherentStrain.
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

    def SaveBuildSettings(self, fName: str) -> None:
        """
        Run the SaveBuildSettings action.
        """
        pass

    def LoadBuildSettings(self, fName: str) -> None:
        """
        Run the LoadBuildSettings action.
        """
        pass

    def ResetToDefault(self) -> None:
        """
        ResetToDefault - Restores default values of all properties.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class IAMProcessStep(object):

    @property
    def ProcessStepType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMProcessStepType]:
        """
        ProcessStepType property.
        """
        return None


class SupportRemoval(object):

    pass

class BaseRemoval(object):

    pass

class BaseUnboltStep(object):

    pass

class UserStep(object):

    pass

class BuildStep(object):

    pass

class HeatTreatmentStep(object):

    pass

class CooldownStep(object):

    pass

class AMSupportRemovalSequence(object):

    @property
    def Count(self) -> typing.Optional[int]:
        """
        Count property.
        """
        return None

    def Add(self, item: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep) -> None:
        """
        
            Adds a support or base removal step.
            Throws a notSupportedException if the same step was already added.
            Usage:
             removalSequence.Add(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval())
             removalSequence.Add(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj))
            
        """
        pass

    def RemoveAt(self, index: int) -> None:
        """
        
            Remove AM step at index.
            Throws IndexOutOfRangeException if index is out of range
            Usage:
             removalSequence.RemoveAt(0)
            
        """
        pass

    def Swap(self, item1: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep, item2: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep) -> bool:
        """
        
            Swaps two steps in the Removal sequence.
            Returns true if successful and false if unsuccessful
            Usage:
            C#
             removalSequence.Swap(
                new Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval(),
                new Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj));
            Python
             removalSequence.Swap(
                Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval(),
                Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj))
            
        """
        pass

    def Swap(self, index1: int, index2: int) -> bool:
        """
        
            Swaps two steps in the Removal sequence by name.
            Returns true if successful and false if unsuccessful
            Usage:
             removalSequence.Swap("Base", "Generated Support 1")
            
        """
        pass

    def IndexOf(self, item: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep) -> int:
        """
        
            Returns index of removal object
            Returns -1 if removal object not found
            Usage:
            C#
                index1 = removalSequence.IndexOf(new Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval());
                index2 = removalSequence.IndexOf(new Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj));
            Python
                index1 = removalSequence.IndexOf(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval());
                index2 = removalSequence.IndexOf(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj));
            
        """
        pass

    def Insert(self, index: int, item: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep) -> None:
        """
        
            Inserts a given step at particular index(zero based)
            Throws an IndexOutOfRangeException if the step is being inserted out of range.
            Throws a NotSupportedException if the insertion is invalid
            Usage:
             Sequence.Insert(0,Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.UserStep())
            
        """
        pass

    def Contains(self, item: Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.IAMProcessStep) -> bool:
        """
        
            Returns true if the step exists in the sequencer. If not, returns false
            Usage:
                index1 = removalSequence.Contains(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.BaseRemoval());
                index2 = removalSequence.Contains(Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.SupportRemoval(supportObj));
            
        """
        pass


class AMProcess(object):
    """
    Defines a AMProcess.
    """

    @property
    def BuildGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the PartGeometry using the deprecated BuildGeometry method.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMProcessSimulationAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def SubsampleRate(self) -> typing.Optional[int]:
        """
        Gets or sets the SubsampleRate.
        """
        return None

    @property
    def ZLocationAtTopOfBase(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZLocationAtTopOfBase.
        """
        return None

    @property
    def ElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the ElementSize.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def LengthUnits(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the LengthUnits.
        """
        return None

    @property
    def NonlinearEffects(self) -> typing.Optional[bool]:
        """
        Gets or sets the NonlinearEffects.
        """
        return None

    @property
    def MeshUsingVoxelization(self) -> typing.Optional[bool]:
        """
        Gets or sets the MeshUsingVoxelization.
        """
        return None

    @property
    def BaseGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the BaseGeometry.
        """
        return None

    @property
    def PartGeometry(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the PartGeometry.
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

    def GetSequence(self, analysis: Ansys.ACT.Automation.Mechanical.Analysis) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.AMSupportRemovalSequence:
        """
        
            Gets the support removal sequence for a given environment.
            
        """
        pass

    def ResetAllSequences(self) -> None:
        """
        
            Resets the sequence for all analyses
            
        """
        pass

    def AddCartesianMesh(self) -> Ansys.ACT.Automation.Mechanical.MeshControls.AutomaticMethod:
        """
        AddCartesianMesh method.
        """
        pass

    def CreateBuildToBaseContact(self) -> Ansys.ACT.Automation.Mechanical.Connections.ContactRegion:
        """
        Run the CreateBuildToBaseContact action.
        """
        pass

    def CreateAMBondConnections(self) -> None:
        """
        Run the CreateAMBondConnections action.
        """
        pass

    def GenerateAMStrains(self) -> None:
        """
        Run the GenerateAMStrains action.
        """
        pass

    def CleanAMStrains(self) -> None:
        """
        Run the CleanAMStrains action.
        """
        pass

    def HasAMStrains(self) -> bool:
        """
        Get the HasAMStrains property.
        """
        pass

    def AddSupportGroup(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.AMSupportGroup:
        """
        Creates a new AMSupportGroup
        """
        pass

    def AddGeneratedAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.GeneratedAMSupport:
        """
        Creates a new GeneratedAMSupport
        """
        pass

    def AddPredefinedAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.PredefinedAMSupport:
        """
        Creates a new PredefinedAMSupport
        """
        pass

    def AddSTLAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.STLAMSupport:
        """
        Creates a new STLAMSupport
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class AMSupportGroup(object):
    """
    Defines a AMSupportGroup.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMSupportGroupAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def HangAngle(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the HangAngle.
        """
        return None

    @property
    def DetectAboveZLocation(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DetectAboveZLocation.
        """
        return None

    @property
    def OutputType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportGroupOutputType]:
        """
        Gets or sets the OutputType.
        """
        return None

    @property
    def GenerateOnRemesh(self) -> typing.Optional[bool]:
        """
        Gets or sets the GenerateOnRemesh.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
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

    def DetectSupportFaces(self) -> typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Runs the Detect Support Faces action.
        """
        pass

    def AddGeneratedAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.GeneratedAMSupport:
        """
        Creates a new GeneratedAMSupport
        """
        pass

    def AddPredefinedAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.PredefinedAMSupport:
        """
        Creates a new PredefinedAMSupport
        """
        pass

    def AddSTLAMSupport(self) -> Ansys.ACT.Automation.Mechanical.AdditiveManufacturing.STLAMSupport:
        """
        Creates a new GeneratedAMSupport
        """
        pass

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class GeneratedAMSupport(object):
    """
    Defines a GeneratedAMSupport.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMSupportAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Mode(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AutomaticOrManual]:
        """
        Gets or sets the Mode.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ThermalConductivityMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInX.
        """
        return None

    @property
    def ThermalConductivityMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInY.
        """
        return None

    @property
    def ThermalConductivityMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInZ.
        """
        return None

    @property
    def DensityMultiple(self) -> typing.Optional[float]:
        """
        Gets or sets the DensityMultiple.
        """
        return None

    @property
    def MaterialMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the MaterialMultiplier.
        """
        return None

    @property
    def ElasticModulusMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInX.
        """
        return None

    @property
    def ElasticModulusMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInY.
        """
        return None

    @property
    def ElasticModulusMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInZ.
        """
        return None

    @property
    def ShearModulusMultipleInXY(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXY.
        """
        return None

    @property
    def ShearModulusMultipleInXZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXZ.
        """
        return None

    @property
    def ShearModulusMultipleInYZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInYZ.
        """
        return None

    @property
    def WallSpacing(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallSpacing.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def Volume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Volume.
        """
        return None

    @property
    def MultiplierEntry(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMMultiplierEntryType]:
        """
        Gets or sets the MultiplierEntry.
        """
        return None

    @property
    def SupportType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportType]:
        """
        Gets or sets the SupportType.
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

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def GenerateSupportBodies(self, progress: Ansys.Mechanical.Application.Progress) -> None:
        """
        Generate Support Bodies.
        """
        pass

    def CreateNamedSelectionOfGeneratedElements(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def GetGeneratedBody(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        Returns the generated body object
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class STLAMSupport(object):
    """
    Defines a STLAMSupport.
    """

    @property
    def VoxelSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the VoxelSize.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMSupportAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Filename(self) -> typing.Optional[str]:
        """
        Gets or sets the Filename.
        """
        return None

    @property
    def SubsampleRate(self) -> typing.Optional[int]:
        """
        Gets or sets the SubsampleRate.
        """
        return None

    @property
    def ElementSize(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ElementSize.
        """
        return None

    @property
    def StlWallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the StlWallThickness.
        """
        return None

    @property
    def LengthUnits(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.WBUnitSystemType]:
        """
        Gets or sets the LengthUnits.
        """
        return None

    @property
    def STLSupportView(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.STLSupportViewType]:
        """
        Gets or sets the STLSupportView.
        """
        return None

    @property
    def Source(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMStlSource]:
        """
        Gets or sets the Source.
        """
        return None

    @property
    def STLSupportType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportSTLType]:
        """
        Gets or sets the STLSupportType.
        """
        return None

    @property
    def STL(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.STL]:
        """
        Gets or sets the STL.
        """
        return None

    @property
    def GeometrySelection(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometrySelection.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ThermalConductivityMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInX.
        """
        return None

    @property
    def ThermalConductivityMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInY.
        """
        return None

    @property
    def ThermalConductivityMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInZ.
        """
        return None

    @property
    def DensityMultiple(self) -> typing.Optional[float]:
        """
        Gets or sets the DensityMultiple.
        """
        return None

    @property
    def MaterialMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the MaterialMultiplier.
        """
        return None

    @property
    def ElasticModulusMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInX.
        """
        return None

    @property
    def ElasticModulusMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInY.
        """
        return None

    @property
    def ElasticModulusMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInZ.
        """
        return None

    @property
    def ShearModulusMultipleInXY(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXY.
        """
        return None

    @property
    def ShearModulusMultipleInXZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXZ.
        """
        return None

    @property
    def ShearModulusMultipleInYZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInYZ.
        """
        return None

    @property
    def WallSpacing(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallSpacing.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def Volume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Volume.
        """
        return None

    @property
    def MultiplierEntry(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMMultiplierEntryType]:
        """
        Gets or sets the MultiplierEntry.
        """
        return None

    @property
    def SupportType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportType]:
        """
        Gets or sets the SupportType.
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

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def GenerateSupportBodies(self, progress: Ansys.Mechanical.Application.Progress) -> None:
        """
        Generate Support Bodies.
        """
        pass

    def CreateNamedSelectionOfGeneratedElements(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Create a named selection of the generated elements.
        """
        pass

    def CreateNamedSelectionOfExternalElementFaces(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Create a named selection of the generated exterior element faces.
        """
        pass

    def ExportStl(self, filename: str, progress: Ansys.Mechanical.Application.Progress) -> None:
        """
        Export STL data.
        """
        pass

    def GetGeneratedBody(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        Returns the generated body object
        """
        pass

    def ImportSTL(self) -> None:
        """
        Run the ImportSTL action.
        """
        pass

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class AMSupport(object):
    """
    Defines a AMSupport.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMSupportAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ThermalConductivityMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInX.
        """
        return None

    @property
    def ThermalConductivityMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInY.
        """
        return None

    @property
    def ThermalConductivityMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInZ.
        """
        return None

    @property
    def DensityMultiple(self) -> typing.Optional[float]:
        """
        Gets or sets the DensityMultiple.
        """
        return None

    @property
    def MaterialMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the MaterialMultiplier.
        """
        return None

    @property
    def ElasticModulusMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInX.
        """
        return None

    @property
    def ElasticModulusMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInY.
        """
        return None

    @property
    def ElasticModulusMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInZ.
        """
        return None

    @property
    def ShearModulusMultipleInXY(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXY.
        """
        return None

    @property
    def ShearModulusMultipleInXZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXZ.
        """
        return None

    @property
    def ShearModulusMultipleInYZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInYZ.
        """
        return None

    @property
    def WallSpacing(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallSpacing.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def Volume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Volume.
        """
        return None

    @property
    def MultiplierEntry(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMMultiplierEntryType]:
        """
        Gets or sets the MultiplierEntry.
        """
        return None

    @property
    def SupportType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportType]:
        """
        Gets or sets the SupportType.
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

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


class PredefinedAMSupport(object):
    """
    Defines a PredefinedAMSupport.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSAMSupportAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ThermalConductivityMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInX.
        """
        return None

    @property
    def ThermalConductivityMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInY.
        """
        return None

    @property
    def ThermalConductivityMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ThermalConductivityMultipleInZ.
        """
        return None

    @property
    def DensityMultiple(self) -> typing.Optional[float]:
        """
        Gets or sets the DensityMultiple.
        """
        return None

    @property
    def MaterialMultiplier(self) -> typing.Optional[float]:
        """
        Gets or sets the MaterialMultiplier.
        """
        return None

    @property
    def ElasticModulusMultipleInX(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInX.
        """
        return None

    @property
    def ElasticModulusMultipleInY(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInY.
        """
        return None

    @property
    def ElasticModulusMultipleInZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ElasticModulusMultipleInZ.
        """
        return None

    @property
    def ShearModulusMultipleInXY(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXY.
        """
        return None

    @property
    def ShearModulusMultipleInXZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInXZ.
        """
        return None

    @property
    def ShearModulusMultipleInYZ(self) -> typing.Optional[float]:
        """
        Gets or sets the ShearModulusMultipleInYZ.
        """
        return None

    @property
    def WallSpacing(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallSpacing.
        """
        return None

    @property
    def WallThickness(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the WallThickness.
        """
        return None

    @property
    def Volume(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the Volume.
        """
        return None

    @property
    def MultiplierEntry(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMMultiplierEntryType]:
        """
        Gets or sets the MultiplierEntry.
        """
        return None

    @property
    def SupportType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.AMSupportType]:
        """
        Gets or sets the SupportType.
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

    def AddCommandSnippet(self) -> Ansys.ACT.Automation.Mechanical.CommandSnippet:
        """
        Creates a new CommandSnippet
        """
        pass

    def Delete(self) -> None:
        """
        Run the Delete action.
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


