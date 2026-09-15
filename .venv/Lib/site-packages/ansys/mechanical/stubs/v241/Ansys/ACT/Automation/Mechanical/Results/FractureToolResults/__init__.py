"""FractureToolResults module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class FractureTool(object):
    """
    Defines a FractureTool.
    """

    @property
    def MultipleCracksSelection(self) -> typing.Optional[typing.Iterable[Ansys.ACT.Automation.Mechanical.GenericCrack]]:
        """
        Get/Set multiple cracks to Fracture tool
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSFractureToolAuto]:
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
    def CrackSelectionMode(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.CrackSelectionModeType]:
        """
        Gets or sets the CrackSelectionMode.
        """
        return None

    @property
    def ScopingMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FractureToolScopeType]:
        """
        Gets or sets the ScopingMethod.
        """
        return None

    @property
    def Suppressed(self) -> typing.Optional[bool]:
        """
        Gets or sets the Suppressed.
        """
        return None

    @property
    def CrackSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.GenericCrack]:
        """
        Gets or sets the CrackSelection.
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

    def AddSIFSK1(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureSIFSK1
        """
        pass

    def AddSIFSK2(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureSIFSK2
        """
        pass

    def AddSIFSK3(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureSIFSK3
        """
        pass

    def AddJINT(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureJINT
        """
        pass

    def AddMaterialForceX(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureMaterialForceX
        """
        pass

    def AddMaterialForceY(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureMaterialForceY
        """
        pass

    def AddMaterialForceZ(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureMaterialForceZ
        """
        pass

    def AddTSTRESS(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureTSTRESS
        """
        pass

    def AddVCCTG1(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureVCCTG1
        """
        pass

    def AddVCCTG2(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureVCCTG2
        """
        pass

    def AddVCCTG3(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureVCCTG3
        """
        pass

    def AddVCCTGT(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureVCCTGT
        """
        pass

    def AddCStarIntegral(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureCSTAR
        """
        pass

    def AddEquivalentSIFSRange(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureToolResult:
        """
        Creates a new FractureEquivalentSIFSRange
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def AddCrackExtensionProbe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureCrackExtensionProbe:
        """
        Creates a new FractureCrackExtensionProbe
        """
        pass

    def AddEquivalentSIFSRangeProbe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureEquivalentSIFSRangeProbe:
        """
        Creates a new FractureEquivalentSIFSRangeProbe
        """
        pass

    def AddJINTProbe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureJINTProbe:
        """
        Creates a new FractureJINTProbe
        """
        pass

    def AddSIFSK1Probe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureSIFSProbe:
        """
        Creates a new FractureSIFSProbe
        """
        pass

    def AddSIFSK2Probe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureSIFSProbe:
        """
        Creates a new FractureSIFSProbe
        """
        pass

    def AddSIFSK3Probe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureSIFSProbe:
        """
        Creates a new FractureSIFSProbe
        """
        pass

    def AddNumberOfCyclesProbe(self) -> Ansys.ACT.Automation.Mechanical.Results.FractureToolResults.FractureTotalNumberOfCyclesProbe:
        """
        Creates a new FractureTotalNumberOfCyclesProbe
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


class FractureToolResult(object):
    """
    Defines a FractureToolResult.
    """

    @property
    def Mode(self) -> typing.Optional[int]:
        """
        Gets or sets the Mode.
        """
        return None

    @property
    def FractureResultType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FractureResultType]:
        """
        Gets or sets the FractureResultType.
        """
        return None

    @property
    def FractureResultSubType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FractureResultSubType]:
        """
        Gets or sets the FractureResultSubType.
        """
        return None

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def ActiveContourEnd(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContourEnd.
        """
        return None

    @property
    def ActiveContourStart(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContourStart.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
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
    def NamedSelections(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Interfaces.IDataModelObject]]:
        """
        Gets or sets the NamedSelections.
        """
        return None

    @property
    def WaterfallPanelShowTextOnMosaic(self) -> typing.Optional[bool]:
        """
        Gets or sets the Waterfall Panel Mosaic Text Property.
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


class FractureCrackExtensionProbe(object):
    """
    Defines a FractureCrackExtensionProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ResultProbeValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ResultProbeValue.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


class FractureEquivalentSIFSRangeProbe(object):
    """
    Defines a FractureEquivalentSIFSRangeProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ResultProbeValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ResultProbeValue.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


class FractureJINTProbe(object):
    """
    Defines a FractureJINTProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ResultProbeValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ResultProbeValue.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


class FractureSIFSProbe(object):
    """
    Defines a FractureSIFSProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ResultProbeValue(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ResultProbeValue.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def FractureProbeSubType(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.FractureSIFSProbeSubType]:
        """
        Gets or sets the FractureProbeSubType.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


class FractureToolProbe(object):
    """
    Defines a FractureToolProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


class FractureTotalNumberOfCyclesProbe(object):
    """
    Defines a FractureTotalNumberOfCyclesProbe.
    """

    @property
    def InternalObject(self) -> typing.Optional[Ansys.Common.Interop.DSObjectsAuto.IDSProbeResultAuto]:
        """
        Gets the internal object. For advanced usage only.
        """
        return None

    @property
    def ResultProbeValue(self) -> typing.Optional[int]:
        """
        Gets the ResultProbeValue.
        """
        return None

    @property
    def MaximumValueOverTime(self) -> typing.Optional[int]:
        """
        Gets the MaximumValueOverTime.
        """
        return None

    @property
    def MinimumValueOverTime(self) -> typing.Optional[int]:
        """
        Gets the MinimumValueOverTime.
        """
        return None

    @property
    def DataModelObjectCategory(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DataModelObjectCategory]:
        """
        Gets the current DataModelObject's category.
        """
        return None

    @property
    def ActiveContour(self) -> typing.Optional[int]:
        """
        Gets or sets the ActiveContour.
        """
        return None

    @property
    def CrackLengthPercentage(self) -> typing.Optional[int]:
        """
        Gets or sets the CrackLengthPercentage.
        """
        return None

    @property
    def SolverID(self) -> typing.Optional[int]:
        """
        Gets or sets the SolverID.
        """
        return None

    @property
    def Summation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MomentsAtSummationPointType]:
        """
        Gets or sets the Summation.
        """
        return None

    @property
    def LocationMethod(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LocationDefinitionMethod]:
        """
        Gets or sets the LocationMethod.
        """
        return None

    @property
    def GeometryLocation(self) -> typing.Optional[Ansys.ACT.Interfaces.Common.ISelectionInfo]:
        """
        Gets or sets the GeometryLocation.
        """
        return None

    @property
    def CoordinateSystemSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the CoordinateSystemSelection.
        """
        return None

    @property
    def BoundaryConditionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.DataModelObject]:
        """
        Gets or sets the BoundaryConditionSelection. In order to select the option 'WeakSprings', please use the property 'LocationMethod = LocationDefinitionMethod.WeakSprings'.
        """
        return None

    @property
    def ContactRegionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.ContactRegion]:
        """
        Gets or sets the ContactRegionSelection.
        """
        return None

    @property
    def RemotePointSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.RemotePoint]:
        """
        Gets or sets the RemotePointSelection.
        """
        return None

    @property
    def BeamSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Beam]:
        """
        Gets or sets the BeamSelection.
        """
        return None

    @property
    def MeshConnectionSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.MeshConnection]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SurfaceSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Surface]:
        """
        Gets or sets the MeshConnectionSelection.
        """
        return None

    @property
    def SpringSelection(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.Connections.Spring]:
        """
        Gets or sets the SpringSelection.
        """
        return None

    @property
    def IsSolved(self) -> typing.Optional[bool]:
        """
        Gets the IsSolved.
        """
        return None

    @property
    def Orientation(self) -> typing.Optional[Ansys.ACT.Automation.Mechanical.CoordinateSystem]:
        """
        Gets or sets the Orientation. Accepts/Returns None if it is the Solution Coordinate System.
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
    def LoadStepNumber(self) -> typing.Optional[int]:
        """
        Gets or sets the LoadStepNumber.
        """
        return None

    @property
    def Substep(self) -> typing.Optional[int]:
        """
        Gets the Substep.
        """
        return None

    @property
    def DisplayTime(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets or sets the DisplayTime.
        """
        return None

    @property
    def MaximumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumTotal.
        """
        return None

    @property
    def MaximumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumXAxis.
        """
        return None

    @property
    def MaximumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumYAxis.
        """
        return None

    @property
    def MaximumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MaximumZAxis.
        """
        return None

    @property
    def MinimumTotal(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumTotal.
        """
        return None

    @property
    def MinimumXAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumXAxis.
        """
        return None

    @property
    def MinimumYAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumYAxis.
        """
        return None

    @property
    def MinimumZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the MinimumZAxis.
        """
        return None

    @property
    def Time(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Time.
        """
        return None

    @property
    def Total(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the Total.
        """
        return None

    @property
    def XAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the XAxis.
        """
        return None

    @property
    def YAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the YAxis.
        """
        return None

    @property
    def ZAxis(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Gets the ZAxis.
        """
        return None

    @property
    def ResultSelection(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeDisplayFilter]:
        """
        Gets or sets the ResultSelection.
        """
        return None

    @property
    def SpatialResolution(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.MinimumOrMaximum]:
        """
        Gets or sets the SpatialResolution.
        """
        return None

    @property
    def Type(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.ProbeResultType]:
        """
        Gets the Type.
        """
        return None

    @property
    def DpfEvaluation(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.DpfEvaluationType]:
        """
        Gets or sets the DpfEvaluation.
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

    def ExportAnimation(self, filePath: str, format: Ansys.Mechanical.DataModel.Enums.GraphicsAnimationExportFormat, settings: Ansys.Mechanical.Graphics.AnimationExportSettings) -> None:
        """
        Run the ExportAnimation action.
        """
        pass

    def ClearGeneratedData(self) -> None:
        """
        Run the ClearGeneratedData action.
        """
        pass

    def DuplicateWithoutResults(self) -> Ansys.ACT.Automation.Mechanical.DataModelObject:
        """
        Run the DuplicateWithoutResults action.
        """
        pass

    def EvaluateAllResults(self) -> None:
        """
        Run the EvaluateAllResults action.
        """
        pass

    def SnapToMeshNodes(self) -> None:
        """
        Snap the coordinates of probe result to the mesh nodes.
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


