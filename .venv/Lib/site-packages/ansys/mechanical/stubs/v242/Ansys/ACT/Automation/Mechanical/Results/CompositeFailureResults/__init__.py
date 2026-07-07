"""CompositeFailureResults module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CompositeFailureCriteria(object):
    """
    Defines a CompositeFailureCriteria.
    """

    @property
    def MaximumStrain(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.MaximumStrainSettings]:
        """
        Gets the configuration of the maximum strain criterion for reinforced materials.
        """
        return None

    @property
    def MaximumStress(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.MaximumStressSettings]:
        """
        Gets the configuration of the maximum stress criterion for reinforced materials.
        """
        return None

    @property
    def TsaiWu(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.TsaiWuSettings]:
        """
        Gets the configuration of the Tsai-Wu failure criterion for reinforced materials.
        """
        return None

    @property
    def TsaiHill(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.TsaiHillSettings]:
        """
        Gets the configuration of the Tsai-Hill failure criterion for reinforced materials.
        """
        return None

    @property
    def Hoffman(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.HoffmanSettings]:
        """
        Gets the configuration of the Hoffman failure criterion for reinforced materials.
        """
        return None

    @property
    def Hashin(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.HashinSettings]:
        """
        Gets the configuration of the Hashin failure criterion for reinforced materials.
        """
        return None

    @property
    def Puck(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.PuckSettings]:
        """
        Gets the configuration of the Puck failure criterion for reinforced materials.
        """
        return None

    @property
    def LaRC(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.LaRCSettings]:
        """
        Gets the configuration of the LaRC (Langley Research Center) failure criterion for reinforced materials.
        """
        return None

    @property
    def Cuntze(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CuntzeSettings]:
        """
        Gets the configuration of the Cuntze failure criterion for reinforced materials.
        """
        return None

    @property
    def FaceSheetWrinkling(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.FaceSheetWrinklingSettings]:
        """
        Gets the configuration of the Face Sheet Wrinkling sandwich failure criterion.
        """
        return None

    @property
    def CoreFailure(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CoreFailureSettings]:
        """
        Gets the configuration of the Core Failure sandwich failure criterion
        """
        return None

    @property
    def ShearCrimping(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.ShearCrimpingSettings]:
        """
        Gets the configuration of the Shear Crimping sandwich failure criterion
        """
        return None

    @property
    def VonMises(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.VonMisesSettings]:
        """
        Gets the configuration of the Von Mises failure criterion for isotropic materials.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSCompositeFailureCriteriaAuto]:
        """
        Gets the internal object. For advanced usage only.
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


class CompositeFailureCriterionSettings(object):
    """
    Base class for settings objects which contain the configuration of a single failure criterion.
    """

    @property
    def Active(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class CompositeFailureTool(object):
    """
    Defines a CompositeFailureTool.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSCompositeFailureToolAuto]:
        """
        Gets the internal object. For advanced usage only.
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

    def AddInverseReserveFactor(self) -> Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CompositeFailureResult:
        """
        Creates a new InverseReserveFactor
        """
        pass

    def AddSafetyFactor(self) -> Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CompositeFailureResult:
        """
        Creates a new SafetyFactor
        """
        pass

    def AddSafetyMargin(self) -> Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CompositeFailureResult:
        """
        Creates a new SafetyMargin
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def AddGroupedScopedACPResults(self, resultType: Ansys.Mechanical.DataModel.Enums.ResultType, selectedPlies: typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]) -> None:
        """
        AddGroupedScopedACPResults method.
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


class CoreFailureSettings(object):
    """
    Defines the configuration for the Core failure criterion for sandwich structures.
    """

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the core failure criterion. The corresponding failure label
            is 'cf'.
        """
        return None

    @property
    def ConsiderInterlaminarNormalStresses(self) -> typing.Optional[bool]:
        """
        Gets or sets whether interlaminar normal stresses are included in the core failure evaluation.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class CuntzeSettings(object):
    """
    Defines the configuration for the Cuntze failure criterion for reinforced materials.
    """

    @property
    def FailureDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.FailureDimension]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def EvaluateFiberTensionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber tension failure is evaluated. The corresponding failure label is 'cft'
        """
        return None

    @property
    def FiberTensionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber tension failure (cft) evaluation.
        """
        return None

    @property
    def EvaluateFiberCompressionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber compression failure is evaluated. The corresponding failure label is 'cfc'
        """
        return None

    @property
    def FiberCompressionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber compression failure (cfc) evaluation.
        """
        return None

    @property
    def EvaluateMatrixTensionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix tension failure is evaluated. The corresponding failure label is 'cmA'
        """
        return None

    @property
    def MatrixTensionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix tension failure (cmA) evaluation.
        """
        return None

    @property
    def EvaluateMatrixCompressionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix compression failure is evaluated. The corresponding failure label is 'cmB'
        """
        return None

    @property
    def MatrixCompressionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix compression failure (cmB) evaluation.
        """
        return None

    @property
    def EvaluateMatrixWedgeShapeFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix wedge shape failure is evaluated. The corresponding failure label is 'cmC'
        """
        return None

    @property
    def MatrixWedgeShapeFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix wedge shape failure (cmC) evaluation.
        """
        return None

    @property
    def ModeInteractionCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the mode interaction coefficient.
        """
        return None

    @property
    def InPlaneShearFrictionCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the in-plane shear friction coefficient b21.
            The value must be greater than or equal to 0.
        """
        return None

    @property
    def OutOfPlaneShearFrictionCoefficient(self) -> typing.Optional[float]:
        """
        Gets the out-of-plane shear friction coefficient b32.
            Computed from the fracture plane angle theta.
        """
        return None

    @property
    def FracturePlaneAngle(self) -> typing.Optional[float]:
        """
        Gets or sets the fracture plane angle theta.
            The value must be in the range [45, 90).
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class FaceSheetWrinklingSettings(object):
    """
    Defines the configuration for the Face Sheet Wrinkling failure criterion for sandwich structures.
    """

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the face sheet wrinkling criterion. The corresponding failure
            label is 'wt' for wrinkling at the top face, 'wb' at the bottom face.
        """
        return None

    @property
    def HomogeneousCoreCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the wrinkling coefficient of homogeneous core materials.
        """
        return None

    @property
    def HoneycombCoreCoefficient(self) -> typing.Optional[float]:
        """
        Gets or sets the wrinkling coefficient of honeycomb core materials.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class HashinSettings(object):
    """
    Defines the configuration for the Hashin failure criterion for reinforced materials.
    """

    @property
    def FailureDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.FailureDimension]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def EvaluateFiberFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber failure is evaluated. The corresponding failure label is 'hf'
        """
        return None

    @property
    def FiberFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber failure evaluation.
        """
        return None

    @property
    def EvaluateMatrixFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix failure is evaluated. The corresponding failure label is 'hm'
        """
        return None

    @property
    def MatrixFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix failure evaluation.
        """
        return None

    @property
    def EvaluateDelamination(self) -> typing.Optional[bool]:
        """
        Gets or sets whether delamination is evaluated. Only applies when three-dimensional
            evaluation is selected. The corresponding failure label is 'hd'
        """
        return None

    @property
    def DelaminationWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the delamination evaluation.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class HoffmanSettings(object):
    """
    Defines the configuration for the Hoffman failure criterion for reinforced materials.
    """

    @property
    def FailureDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.FailureDimension]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion.
            The corresponding failure label is 'ho'.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class LaRCSettings(object):
    """
    Defines the configuration for the LaRC failure criterion for reinforced materials
    """

    @property
    def Formulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.LaRCFormulation]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def EvaluateFiberTensionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber tension failure is evaluated. The corresponding failure label is 'ltf3'.
        """
        return None

    @property
    def FiberTensionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber tension failure (ltf3) evaluation.
        """
        return None

    @property
    def EvaluateFiberCompressionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber compression failure is evaluated. The corresponding failure label is 'lfc4/6'.
        """
        return None

    @property
    def FiberCompressionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber compression failure (lfc4/6) evaluation.
        """
        return None

    @property
    def EvaluateMatrixTensionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix tension failure is evaluated. The corresponding failure label is 'lmt1'.
        """
        return None

    @property
    def MatrixTensionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix tension failure (lmt1) evaluation.
        """
        return None

    @property
    def EvaluateMatrixCompressionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix compression failure is evaluated. The corresponding failure label is 'lmc2/5'.
        """
        return None

    @property
    def MatrixCompressionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix compression failure (lmc2/5) evaluation.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class MaximumStrainSettings(object):
    """
    Defines the configuration for the Maximum Strain failure criterion for reinforced materials.
    """

    @property
    def EvaluateMaterialOneDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the material 1
            direction. The corresponding failure label is 'e1'.
        """
        return None

    @property
    def MaterialOneDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the material 1 direction. 
        """
        return None

    @property
    def EvaluateMaterialTwoDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the material 2
            direction. The corresponding failure label is 'e2'.
        """
        return None

    @property
    def MaterialTwoDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the material 2 direction. 
        """
        return None

    @property
    def EvaluateMaterialThreeDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the out-of-plane
            direction. The corresponding failure label is 'e3'.
        """
        return None

    @property
    def MaterialThreeDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the out-of-plane direction. 
        """
        return None

    @property
    def EvaluateShearOneTwoFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the in-plane shear e12. The corresponding failure
            label is 'e12'.
        """
        return None

    @property
    def ShearOneTwoFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to in-plane shear e12.
        """
        return None

    @property
    def EvaluateShearOneThreeFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the out-of-plane shear e13. The corresponding failure
            label is 'e13'.
        """
        return None

    @property
    def ShearOneThreeFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to out-of-plane shear e13.
        """
        return None

    @property
    def EvaluateShearTwoThreeFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the out-of-plane shear e23. The corresponding failure
            label is 'e23'.
        """
        return None

    @property
    def ShearTwoThreeFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to out-of-plane shear e23.
        """
        return None

    @property
    def OverrideMaterial(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the global strain limits are used, overriding material-specific limits.
        """
        return None

    @property
    def TensileLimitMaterialOneDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global tensile strain limit in the material 1 direction (eXt).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def CompressiveLimitMaterialOneDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global compressive strain limit in the material 1 direction (eXc).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def TensileLimitMaterialTwoDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global tensile strain limit in the material 2 direction (eYt).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def CompressiveLimitMaterialTwoDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global compressive strain limit in the material 2 direction (eYc).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def TensileLimitMaterialThreeDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global tensile strain limit in the out-of-plane direction (eZt).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def CompressiveLimitMaterialThreeDirection(self) -> typing.Optional[float]:
        """
        Gets or sets the global compressive strain limit in the out-of-plane direction (eZc).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def ShearLimitOneTwo(self) -> typing.Optional[float]:
        """
        Gets or sets the global in-plane shear strain limit (eSxy).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def ShearLimitOneThree(self) -> typing.Optional[float]:
        """
        Gets or sets the global out-of-plane shear strain limit (eSxz).
            Only used if OverrideMaterial is true.
        """
        return None

    @property
    def ShearLimitTwoThree(self) -> typing.Optional[float]:
        """
        Gets or sets the global out-of-plane shear strain limit (eSyz).
            Only used if OverrideMaterial is true.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class MaximumStressSettings(object):
    """
    Defines the configuration for the Maximum Stress failure criterion for reinforced materials.
    """

    @property
    def EvaluateMaterialOneDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the material 1 direction.
            The corresponding failure label is 's1'.
        """
        return None

    @property
    def MaterialOneDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the material 1 direction.
        """
        return None

    @property
    def EvaluateMaterialTwoDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the material 2 direction.
            The corresponding failure label is 's2'.
        """
        return None

    @property
    def MaterialTwoDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the material 2 direction.
        """
        return None

    @property
    def EvaluateMaterialThreeDirectionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the failure criterion is evaluated in the out-of-plane direction.
            The corresponding failure label is 's3'.
        """
        return None

    @property
    def MaterialThreeDirectionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion in the out-of-plane direction.
        """
        return None

    @property
    def EvaluateShearOneTwoFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the in-plane shear s12.
            The corresponding failure label is 's12'.
        """
        return None

    @property
    def ShearOneTwoFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to in-plane shear s12.
        """
        return None

    @property
    def EvaluateShearOneThreeFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the out-of-plane shear s13.
            The corresponding failure label is 's13'.
        """
        return None

    @property
    def ShearOneThreeFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to out-of-plane shear s13.
        """
        return None

    @property
    def EvaluateShearTwoThreeFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether failure is evaluated for the out-of-plane shear s23.
            The corresponding failure label is 's23'.
        """
        return None

    @property
    def ShearTwoThreeFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for failure due to out-of-plane shear s23.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class PuckSettings(object):
    """
    Defines the configuration for the Puck failure criterion for reinforced materials.
    """

    @property
    def Formulation(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.PuckFormulation]:
        """
        Gets or sets whether the simplified, 2D, or 3D Puck formulation is used.
        """
        return None

    @property
    def ConsiderInterFiberParallelStresses(self) -> typing.Optional[bool]:
        """
        Gets or sets whether inter-fiber failure will include the influence of the fiber parallel stresses.
        """
        return None

    @property
    def EvaluateFiberFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether fiber failure (pf) is evaluated. The corresponding failure label is 'pf'.
        """
        return None

    @property
    def FiberFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the fiber failure evaluation.
        """
        return None

    @property
    def EvaluateMatrixTensionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix tension failure is evaluated. The corresponding failure label is 'pmA'.
        """
        return None

    @property
    def MatrixTensionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix tension (pmA) failure evaluation.
        """
        return None

    @property
    def EvaluateMatrixCompressionFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix compression failure is evaluated. The corresponding failure label is 'pmB'.
        """
        return None

    @property
    def MatrixCompressionFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix compression (pmB) failure evaluation.
        """
        return None

    @property
    def EvaluateMatrixShearFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether matrix shear failure is evaluated. The corresponding failure label is 'pmC'.
        """
        return None

    @property
    def MatrixShearFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the matrix shear (pmC) failure evaluation.
        """
        return None

    @property
    def EvaluateDelamination(self) -> typing.Optional[bool]:
        """
        Gets or sets whether delamination is evaluated. Only applies when three-dimensional
            evaluation is selected. The corresponding failure label is 'pd'.
        """
        return None

    @property
    def DelaminationWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the delamination (pd) evaluation.
        """
        return None

    @property
    def OverrideMaterial(self) -> typing.Optional[bool]:
        """
        Gets or sets whether the global Puck constants are used overriding material-specific constants.
        """
        return None

    @property
    def InclinationFactorTwoOnePositive(self) -> typing.Optional[float]:
        """
        Gets or sets the p21(+) Puck constant.
        """
        return None

    @property
    def InclinationFactorTwoOneNegative(self) -> typing.Optional[float]:
        """
        Gets or sets the p21(-) Puck constant.
        """
        return None

    @property
    def InclinationFactorTwoTwoPositive(self) -> typing.Optional[float]:
        """
        Gets or sets the p22(+) Puck constant.
        """
        return None

    @property
    def InclinationFactorTwoTwoNegative(self) -> typing.Optional[float]:
        """
        Gets or sets the p22(-) Puck constant.
        """
        return None

    @property
    def DegradationInitiationFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the degradation initiation factor s (0 < s < 1).
        """
        return None

    @property
    def DegradationResidualStrengthFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the degradation residual strength factor M (0 < M < 1).
        """
        return None

    @property
    def InterfaceWeakeningFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the interface weakening factor.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class ShearCrimpingSettings(object):
    """
    Defines the configuration for the Face Sheet Crimping failure criterion for sandwich structures.
    """

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for shear crimping failure.
            The corresponding failure label is 'sc'.
        """
        return None

    @property
    def CoreWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor of core material of crimping allowable.
        """
        return None

    @property
    def FaceSheetWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor of face sheets of crimping allowable.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class TsaiHillSettings(object):
    """
    Defines the configuration for the Tsai-Hill failure criterion for reinforced materials.
    """

    @property
    def FailureDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.FailureDimension]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion.
            The corresponding failure label is 'th'.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class TsaiWuSettings(object):
    """
    Defines the configuration for the Tsai-Wu failure criterion for reinforced materials.
    """

    @property
    def FailureDimension(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.CompositeFailure.FailureDimension]:
        """
        Gets or sets whether the failure criterion is evaluated only in-plane (2D),
            or also in the out-of-plane direction (3D).
        """
        return None

    @property
    def WeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the failure criterion.
            The corresponding failure label is 'tw'.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class VonMisesSettings(object):
    """
    Defines the configuration for the Von Mises failure criterion for isotropic materials.
    """

    @property
    def EvaluateStrainFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether strain failure is evaluated. The corresponding failure label is 'vMe'.
        """
        return None

    @property
    def StrainFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the strain failure (vMe) evaluation.
        """
        return None

    @property
    def EvaluateStressFailure(self) -> typing.Optional[bool]:
        """
        Gets or sets whether stress failure is evaluated. The corresponding failure label is 'vMs'
        """
        return None

    @property
    def StressFailureWeightingFactor(self) -> typing.Optional[float]:
        """
        Gets or sets the weighting factor for the stress failure (vMs) evaluation.
        """
        return None

    @property
    def ConsiderInterlaminarNormalStresses(self) -> typing.Optional[bool]:
        """
        Gets or sets whether interlaminar normal stresses are evaluated.
        """
        return None

    def Reset(self) -> None:
        """
        Resets the settings to their default values.
        """
        pass


class CompositeFailureResult(object):

    @property
    def Ply(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.AnalysisPly]]:
        """
        Gets or sets the Ply selection.
        """
        return None

    @property
    def ShowOnReferenceSurface(self) -> typing.Optional[bool]:
        """
        Gets or sets the Show On Reference Surface property.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def PlotData(self) -> typing.Optional[Ansys.Mechanical.DataModel.Results.ResultDataTable]:
        """
        Gets the result table.
        """
        return None

    @property
    def Location(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the Location.
        """
        return None

    @property
    def TimeForMinimumOfMinimumValues(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Get the Time for the minimum of minimum values.
        """
        return None

    @property
    def TimeForMinimumOfMaximumValues(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Get the Time for the minimum of maximum values.
        """
        return None

    @property
    def LoadStepForMinimumOfMinimumValues(self) -> typing.Optional[int]:
        """
        Get the Load Step for the minimum of minimum values.
        """
        return None

    @property
    def LoadStepForMinimumOfMaximumValues(self) -> typing.Optional[int]:
        """
        Get the Load Step for the minimum of maximum values.
        """
        return None

    @property
    def TimeForMaximumOfMinimumValues(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Get the Time for the maximum of minimum values.
        """
        return None

    @property
    def TimeForMaximumOfMaximumValues(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Get the Time for the maximum of maximum values.
        """
        return None

    @property
    def LoadStepForMaximumOfMinimumValues(self) -> typing.Optional[int]:
        """
        Get the Load Step for the maximum of minimum values.
        """
        return None

    @property
    def LoadStepForMaximumOfMaximumValues(self) -> typing.Optional[int]:
        """
        Get the Load Step for the maximum of maximum values.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def CoordinateSystem(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        
            Gets or sets the Coordinate System. 
            Accepts/Returns None for Solution Coordinate System in the general case (if applicable). 
            Accepts/Returns None for Fiber Coordinate System for a result that is sub scoped by ply.
            
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GeometryDefineByType]:
        """
        Gets or sets the ScopingMethod.
        """
        return None

    @property
    def SetNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the Set Number.
        """
        return None

    @property
    def CombinationNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the Combination Number for a Solution Combination result.
        """
        return None

    @property
    def SolutionCombinationDriver(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SolutionCombinationDriverStyle]:
        """
        Gets or sets the SolutionCombinationDriver.
        """
        return None

    @property
    def Path(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Path]:
        """
        Path property.
        """
        return None

    @property
    def Surface(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Surface property.
        """
        return None

    @property
    def SurfaceCoating(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.SurfaceCoating]:
        """
        SurfaceCoating property.
        """
        return None

    @property
    def NamedSelections(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets or sets the NamedSelections.
        """
        return None

    @property
    def WaterfallShowTextOnMosaic(self) -> typing.Optional[bool]:
        """
        Gets or sets the Waterfall Mosaic Text Property.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def CrackFrontNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackFrontNumber.
        """
        return None

    @property
    def GlobalIDs(self) -> typing.Optional[str]:
        """
        Gets or sets the GlobalIDs.
        """
        return None

    @property
    def Identifier(self) -> typing.Optional[str]:
        """
        Gets or sets the Identifier.
        """
        return None

    @property
    def IterationNumber(self) -> typing.Optional[int]:
        """
        Gets the IterationNumber.
        """
        return None

    @property
    def LoadStep(self) -> typing.Optional[int]:
        """
        Gets the LoadStep.
        """
        return None

    @property
    def MaximumOccursOn(self) -> typing.Optional[str]:
        """
        Gets the MaximumOccursOn.
        """
        return None

    @property
    def MinimumOccursOn(self) -> typing.Optional[str]:
        """
        Gets the MinimumOccursOn.
        """
        return None

    @property
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def SolverComponentIDs(self) -> typing.Optional[str]:
        """
        Gets or sets the SolverComponentIDs.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def Average(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Average.
        """
        return None

    @property
    def Maximum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Maximum.
        """
        return None

    @property
    def MaximumOfMaximumOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumOfMaximumOverTime.
        """
        return None

    @property
    def MaximumOfMinimumOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumOfMinimumOverTime.
        """
        return None

    @property
    def Minimum(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Minimum.
        """
        return None

    @property
    def MinimumOfMaximumOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumOfMaximumOverTime.
        """
        return None

    @property
    def MinimumOfMinimumOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumOfMinimumOverTime.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def GraphControlsXAxis(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.GraphControlsXAxis]:
        """
        Gets or sets the GraphControlsXAxis.
        """
        return None

    @property
    def DisplayOption(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultAveragingType]:
        """
        Gets or sets the DisplayOption.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
        """
        return None

    @property
    def By(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.SetDriverStyle]:
        """
        Gets or sets the By.
        """
        return None

    @property
    def ItemType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ResultFileItemType]:
        """
        Gets or sets the ItemType.
        """
        return None

    @property
    def CalculateTimeHistory(self) -> typing.Optional[bool]:
        """
        Gets or sets the CalculateTimeHistory.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
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

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def FetchRemoteResults(self) -> None:
        """
        Run the FetchRemoteResult action.
        """
        pass

    def ExportToTextFile(self, filePath: str) -> None:
        """
        Run the ExportToTextFile action.
        """
        pass

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.Mechanical.DataModel.Interfaces.IDataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def CreateResultsAtAllSets(self) -> typing.List[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]:
        """
        Creates results at all sets for results under a solution.
        """
        pass

    def PromoteToNamedSelection(self) -> typing.Iterable[Ansys.ACT.Automation.Mechanical.NamedSelection]:
        """
        Run the PromoteToNamedSelection action.
        """
        pass

    def CreateParameter(self, propName: str) -> Ansys.ACT.Interfaces.Mechanical.IParameter:
        """
        CreateParameter method.
        """
        pass

    def AddAlert(self) -> Ansys.ACT.Automation.Mechanical.Results.Alert:
        """
        Creates a new Alert
        """
        pass

    def AddConvergence(self) -> Ansys.ACT.Automation.Mechanical.Results.Convergence:
        """
        Creates a new Convergence
        """
        pass

    def RenameBasedOnDefinition(self) -> None:
        """
        Run the RenameBasedOnDefinition action.
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


class CompositeSamplingPoint(object):
    """
    Defines a CompositeSamplingPoint.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSCompositeSamplingPointResultAuto]:
        """
        Gets the internal object. For advanced usage only.
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


class CompositeSamplingPointTool(object):
    """
    Defines a CompositeSamplingPointTool.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSCompositeFailureToolAuto]:
        """
        Gets the internal object. For advanced usage only.
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

    def AddCompositeSamplingPoint(self) -> Ansys.ACT.Automation.Mechanical.Results.CompositeFailureResults.CompositeSamplingPoint:
        """
        Creates a new CompositeSamplingPoint
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


