"""Dataset module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class Helpers(object):
    """
    
            A class that exposes helper methods/properties for a dataset object.
            
    """

    @classmethod
    def Import(cls, filename: str) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Imports dataset data from text a file.
            The import autodetects the file format from the supported options of tab delimited or LSPrePost export format for import.
            An InvalidOperationException is thrown if the import format in the input file is incompatible or if the data within the file is invalid.
            
        """
        pass

    @classmethod
    def GetMaximumCutOffFrequency(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Core.Units.Quantity:
        """
        
            Gets the maximum cutoff frequency limit of the dataset (useful for Filters like Butterworth and SAE).
            
        """
        pass


class Dataset2D(object):
    """
    
            A class to reference the dataset object.
            A dataset object is regarded as pure mathematical data containing X and Y values.
            
    """

    @property
    def XAxisVals(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.ChartVariable]:
        """
        
            Gets the X axis variable for the dataset.
            
        """
        return None

    @property
    def YAxisVals(self) -> typing.Optional[Ansys.Mechanical.DataModel.Utilities.Charts.ChartVariable]:
        """
        
            Gets the Y axis variable for the dataset.
            
        """
        return None


class Operations(object):
    """
    
            A class that provides methods to apply mathematical Operations (like Integration, Summation, Multiplication, etc.) to dataset object(s).
            All operations throw an InvalidOperationException when an invalid dataset is passed in as an input.
            An invalid dataset could be null dataset reference, dataset with either of the x or y values list empty or dataset with a mismatch in the size of its x and y values list.
            
    """

    @classmethod
    def Integration(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Performs integration using the trapezoidal rule on a dataset and returns the result as a new dataset.
            The resultant dataset will be Dimensionless. (See documentation for more details)
            An ArgumentException is thrown if the input dataset is either invalid or contains less than two values.
            
        """
        pass

    @classmethod
    def Differentiation(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Performs differentiation using the central difference method on a dataset and returns the result as a new dataset.
            The resultant dataset will be Dimensionless. (See documentation for more details)
            An ArgumentException is thrown if the input dataset is either invalid or is non-differentiable.
            
        """
        pass

    @classmethod
    def Addition(cls, dataset_1: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, dataset_2: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, extra_datasets: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        Addition method.
        """
        pass

    @classmethod
    def Subtraction(cls, minuend: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, subtrahend: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Performs a subtraction operation on the y-values of the subtrahend from the minuend and returns the result as a new dataset.
            The resultant dataset contains the intersection of x-values from all the input datasets and the subtraction of the corresponding y-values. (There is no interpolation done for any missing y-values.)
            If all the input datasets are of the same Quantity type, internal unit conversions are done if needed, and the resultant dataset will also be of the same Quantity type.
            If any of the input datasets have different Quantity types, no unit conversions are attempted, and the resultant dataset will be Dimensionless.
            An ArgumentException is thrown if either one of the datasets is invalid.
            An InvalidOperationException is thrown if there is no intersection between the x-values of the input datasets.
            
        """
        pass

    @classmethod
    def Multiplication(cls, dataset_1: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, dataset_2: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, extra_datasets: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        Multiplication method.
        """
        pass

    @classmethod
    def Division(cls, dividend: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, divisor: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Performs a division operation on the y-values of the dividend dataset by the divisor and returns the result as a new dataset.
            The resultant dataset contains the intersection of x-values from all the input datasets and the division of the corresponding y-values. (There is no interpolation done for any missing y-values.)
            If all the input datasets are of the same Quantity type, internal unit conversions are done if needed, but the resultant dataset will be Dimensionless. (See documentation for more details)
            If any of the input datasets have different Quantity types, no unit conversions are attempted, and the resultant dataset will be Dimensionless.
            An ArgumentException is thrown if either one of the datasets is invalid.
            An InvalidOperationException is thrown if there is no intersection between the x-values of the input datasets.
            
        """
        pass

    @classmethod
    def ScaleAxis(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, x_scale_factor: float, y_scale_factor: float) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Scales the dataset values by a factor provided in the input for each axis.
            The new resultant dataset is returned as the output.
            The resultant dataset will maintain the same Quantity and units as the input dataset.
            An ArgumentException is thrown if the input dataset is invalid.
            
        """
        pass

    @classmethod
    def ShiftAxis(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, x_shift_value: Ansys.Core.Units.Quantity, y_shift_value: Ansys.Core.Units.Quantity) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Shifts the dataset values by a value provided in the input for each axis.
            The new resultant dataset is returned as the output.
            The resultant dataset will maintain the same Quantity and units as the input dataset.
            An ArgumentException is thrown if the input dataset is invalid.
            
        """
        pass


class Filters(object):
    """
    
            A class that provides methods to apply mathematical Filters (like Butterworth and SAE filters) to a dataset object.
            All filters throw an InvalidOperationException when an invalid dataset is passed in as an input.
            An invalid dataset could be null dataset reference, dataset with either of the x or values list empty or dataset with a mismatch in the size of its x and y values list.
            
    """

    @classmethod
    def Butterworth(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, cutoff_frequency: Ansys.Core.Units.Quantity) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Applies Butterworth filter on the given dataset at the given cutoff frequency and returns the result as a new dataset.
            This is comparable to the native Butterworth filter for Solution Information tracker results.
            An InvalidOperationException is thrown if the inputs are incorrect.
            Invalid inputs comprise of an invalid dataset or a cutoff frequency out of valid range (negative or exceeding the maximum cutoff frequency possible for that dataset.
            The Maximum Cutoff Frequency for a particular dataset can be queried using the GetMaximumCutoffFrequency method in the Ansys.Mechanical.DataModel.Utilities.Dataset.Helpers namespace). 
            
        """
        pass

    @classmethod
    def ButterworthLSPP(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, cutoff_frequency: Ansys.Core.Units.Quantity) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Applies Butterworth filter on the given dataset at the given cutoff frequency and returns the result as a new dataset.
            This is comparable to the Butterworth filter provided by LSPrePost.
            An InvalidOperationException is thrown if the inputs are incorrect.
            Invalid inputs comprise of an invalid dataset or a cutoff frequency out of valid range (negative or exceeding the maximum cutoff frequency possible for that dataset.
            The Maximum Cutoff Frequency for a particular dataset can be queried using the GetMaximumCutoffFrequency method in the Ansys.Mechanical.DataModel.Utilities.Dataset.Helpers namespace). 
            
        """
        pass

    @classmethod
    def SAE(cls, dataset: Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D, cutoff_frequency: Ansys.Core.Units.Quantity) -> Ansys.Mechanical.DataModel.Utilities.Dataset.Dataset2D:
        """
        
            Applies SAE filter on the given dataset at the given cutoff frequency and returns the result as a new dataset.
            An InvalidOperationException is thrown if the inputs are incorrect.
            Invalid inputs comprise of an invalid dataset or a cutoff frequency out of valid range (negative or exceeding the maximum cutoff frequency possible for that dataset.
            The Maximum Cutoff Frequency for a particular dataset can be queried using the GetMaximumCutoffFrequency method in the Ansys.Mechanical.DataModel.Utilities.Dataset.Helpers namespace). 
            
        """
        pass


