"""Charts module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class LabelCollection(object):
    """
    
            A class to manage labels on the chart.
            
    """

    @property
    def Labels(self) -> typing.Optional[typing.Iterable[Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo]]:
        """
        
            Gets an IEnumerable of ILabelInfo objects, which contain information about the underlying label 
            
        """
        return None

    def CreateAndAddLabel(self, x_anchor: Ansys.Core.Units.Quantity, y_anchor: Ansys.Core.Units.Quantity, label_text: str) -> Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo:
        """
        
            Creates a new label and adds it to the chart at a specified position, where the label_text parameter is optional. 
            The default label text is: “x: <x_value>, y: <y_value>” (example: “x: 0.3497, y: 1.9821”).  
            An InvalidOperationException will be thrown when creating a Label at a location already assigned to another Label.
            
        """
        pass

    def DeleteLabel(self, label: Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo) -> None:
        """
        
            Deletes a label from a specific position in the chart. 
            An InvalidOperationException will be thrown when deleting a Label that does not exist.
            
        """
        pass

    def CreateLabelOnSegment(self, data_point_index: int, fractional_distance: float) -> Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo:
        """
        
            Create a label on the segment of the dataset starting from the data point at a specified distance along the segment. 
            Distance values are fractional going from 0 to 1 (first datapoint at 0) along the length of the segment
            An ArgumentException will be thrown when creating a Label at a location already assigned to another Label.
            
        """
        pass

    def CreateLabelsAtXCoordinate(self, x_anchor: Ansys.Core.Units.Quantity) -> typing.List[Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo]:
        """
        
            Creates label(s) on the dataset at a specified X coordinate. 
            This API may return multiple `LabelInfo` references in case the corresponding dataset has more than one Y-value for the given X-value (for eg. Spiral graphs). 
            Each `LabelInfo` reference corresponds to the multiple anchor positions thus obtained. 
            An ArgumentException will be thrown when creating a Label at a location already assigned to another Label.
            
        """
        pass

    def CreateLabelsAtYCoordinate(self, y_anchor: Ansys.Core.Units.Quantity) -> typing.List[Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection.LabelInfo]:
        """
        
            Creates label(s) on the dataset at a specified Y coordinate. 
            This API may return multiple `LabelInfo` references in case the corresponding dataset has more than one X-value for a given Y-value. 
            Each `LabelInfo` reference corresponds to the multiple anchor positions thus obtained. 
            An ArgumentException will be thrown when creating a Label at a location already assigned to another Label.
            
        """
        pass


class ReadOnlyChart(object):
    """
    
            ReadOnlyChart is used by objects to display data as a chart.
            The data itself is treated as read only and cannot be modified.
            Additional options are provided to customize the presentation of the data itself.
            
    """

    @property
    def Datasets(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D]]:
        """
        
            Retrieves all datasets of a chart.
            
        """
        return None

    @property
    def XAxisDisplayOptions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.AxisDisplayOptions]:
        """
        
            Returns a reference to the x-axis display options of a chart.
            
        """
        return None

    @property
    def YAxisDisplayOptions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.AxisDisplayOptions]:
        """
        
            Returns a reference to the y-axis display options of a chart.
            
        """
        return None

    @property
    def NormalizeYAxis(self) -> typing.Optional[bool]:
        """
        
            Allows a normalized display of y-axis values, usually for cases where the axis has mixed quantities.
            An InvalidOperationException will be thrown if attempting to set to False,
            when the Y axis datasets have incompatible Quantity types and the UseAutomaticLimits property is also set to False.
            
        """
        return None

    def GetDisplayOptionsForDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Charts.Dataset2DDisplayOptions:
        """
        
            Returns a reference to the dataset display options for a specific dataset.
            
        """
        pass

    def GetLabelCollectionForDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection:
        """
        
            Returns a reference to the label collection for a specific dataset.
            
        """
        pass


class Chart(object):
    """
    
            Chart is an object utilized by the Line Chart object to display charts and
            customize them with the flexibility to allow modification to the data of the chart
            to a certain extent. 
            
    """

    @property
    def Datasets(self) -> typing.Optional[typing.List[Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D]]:
        """
        
            Retrieves all datasets of a chart.
            
        """
        return None

    @property
    def XAxisDisplayOptions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.AxisDisplayOptions]:
        """
        
            Returns a reference to the x-axis display options of a chart.
            
        """
        return None

    @property
    def YAxisDisplayOptions(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.AxisDisplayOptions]:
        """
        
            Returns a reference to the y-axis display options of a chart.
            
        """
        return None

    @property
    def NormalizeYAxis(self) -> typing.Optional[bool]:
        """
        
            Allows a normalized display of y-axis values, usually for cases where the axis has mixed quantities.
            An InvalidOperationException will be thrown if attempting to set to False,
            when the Y axis datasets have incompatible Quantity types and the UseAutomaticLimits property is also set to False.
            
        """
        return None

    def AddDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, name: str) -> None:
        """
        
            Adds a dataset to a chart, provided the data is valid.
            Adding a name for the dataset is optional, the default name for the nth dataset added is “Series n”.
            An InvalidOperationException is thrown if the dataset is either invalid, already added to the chart,
            or contains non-positive values when the chart has IsLogarithmic enabled.
            
        """
        pass

    def RemoveDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> None:
        """
        
            Removes a dataset from the chart.
            
        """
        pass

    def GetDisplayOptionsForDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Charts.Dataset2DDisplayOptions:
        """
        
            Returns a reference to the dataset display options for a specific dataset.
            
        """
        pass

    def GetLabelCollectionForDataset(self, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Charts.LabelCollection:
        """
        
            Returns a reference to the label collection for a specific dataset.
            
        """
        pass


class AxisDisplayOptions(object):
    """
    
            A class that exposes methods/properties to customize the display of a chart axis. 
            
    """

    @property
    def AxisLabel(self) -> typing.Optional[str]:
        """
        
            Gets or sets the axis label.
            
        """
        return None

    @property
    def ShowGridLines(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the visibility of the axis gridlines.
            
        """
        return None

    @property
    def IsLogarithmic(self) -> typing.Optional[bool]:
        """
        
            Gets or sets whether the axis is logarithmic.
            A NotSupportedException is thrown if a dataset contains a non-positive value on the chosen axis.
            
        """
        return None

    @property
    def UseAutomaticLimits(self) -> typing.Optional[bool]:
        """
        
            Gets or sets whether axis limits are automatic or user-defined.
            When True, the MinimumLimit and MaximumLimit will be set to the LowerLimit and UpperLimit respectively.
            
        """
        return None

    @property
    def MinimumLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the Minimum limit used for the chart display.
            If UseAutomaticLimits is True, a NotSupportedException is thrown on the setter.
            
        """
        return None

    @property
    def MaximumLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets or sets the Maximum limit used for the chart display.
            If UseAutomaticLimits is True, a NotSupportedException is thrown on the setter.
            
        """
        return None

    @property
    def LowerLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets the default lower limit of the axis range.
            
        """
        return None

    @property
    def UpperLimit(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        
            Gets the default higher limit of the axis range.
            
        """
        return None

    def CopySettingsFrom(self, display_options_original: Ansys.Mechanical.DataModel.Utilities.Charts.AxisDisplayOptions) -> None:
        """
        
            Copies the settings used in the input AxisDisplayOptions reference to the AxisDisplayOptions calling this method.
            
        """
        pass


class Dataset2DDisplayOptions(object):
    """
    
            A class that exposes methods/properties to customize the display of a dataset on the chart.
            
    """

    @property
    def LineType(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Charts.Dataset2D.LineType]:
        """
        
            Gets or sets the Dataset2D Line display type 
            
        """
        return None

    @property
    def Color(self) -> typing.Optional[int]:
        """
        
            Gets or sets the Dataset2D Color 
            
        """
        return None

    @property
    def LineThickness(self) -> typing.Optional[float]:
        """
        
            Gets or sets the Dataset2D line thickness (in pixels) 
            
            An ArgumentException is thrown for values less than 1.
            
        """
        return None

    @property
    def MarkerShape(self) -> typing.Optional[Ansys.Mechanical.DataModel.MechanicalEnums.Charts.Dataset2D.MarkerShape]:
        """
        
            Gets or sets the Dataset2D marker shape 
            
        """
        return None

    @property
    def MarkerSize(self) -> typing.Optional[float]:
        """
        
            Gets or sets the Dataset2D marker size (in pixels)
            
        """
        return None

    @property
    def IsVisible(self) -> typing.Optional[bool]:
        """
        
            Gets or sets the visibility of the Dataset2D
            
        """
        return None

    @property
    def Name(self) -> typing.Optional[str]:
        """
        
            Gets or sets the Dataset2D name 
            
        """
        return None

    def CopySettingsFrom(self, input_display_options: Ansys.Mechanical.DataModel.Utilities.Charts.Dataset2DDisplayOptions) -> None:
        """
        
            Copies the settings of a Dataset2DDisplayOptions reference to this Dataset2DDisplayOptions . 
            
        """
        pass


class ChartVariable(object):
    """
    
            Chart Variable enables user to create a list of values that can be used to construct a dataset object.
            
    """

    pass

class LabelInfo(object):

    @property
    def X(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        X property.
        """
        return None

    @property
    def Y(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        Y property.
        """
        return None

    @property
    def XDisplay(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        XDisplay property.
        """
        return None

    @property
    def YDisplay(self) -> typing.Optional[Ansys.Core.Units.Quantity]:
        """
        YDisplay property.
        """
        return None

    @property
    def Text(self) -> typing.Optional[str]:
        """
        Text property.
        """
        return None

    @property
    def IsVisible(self) -> typing.Optional[bool]:
        """
        IsVisible property.
        """
        return None

    def Move(self, x_display: Ansys.Core.Units.Quantity, y_display: Ansys.Core.Units.Quantity) -> None:
        """
        
            Moves the label to the position on the X axis and the Y axis. An InvalidOperationException will be thrown when moving a Label that does not exist.
            
        """
        pass


