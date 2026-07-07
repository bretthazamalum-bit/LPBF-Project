"""Tools module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class CurrentLegendSettings(object):
    """
    
             Represents a CurrentLegendSettings object. This object holds properties of the CurrentLegendSettings.
             
    """

    @property
    def NumberOfBands(self) -> typing.Optional[int]:
        """
        Number of bands on the legend (min:3, max:30). Bands are added/removed from the top of the legend.
        """
        return None

    @property
    def AllScientificNotation(self) -> typing.Optional[bool]:
        """
        Whether the result values are displayed in scientific notation.
        """
        return None

    @property
    def Digits(self) -> typing.Optional[int]:
        """
        Number of significant digits(min:2, max:8).
        """
        return None

    @property
    def ColorScheme(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendColorSchemeType]:
        """
        Color Scheme for the legend.
        """
        return None

    @property
    def SemiTransparency(self) -> typing.Optional[bool]:
        """
        Whether the legend is semi-transparent.
        """
        return None

    @property
    def LogarithmicScale(self) -> typing.Optional[bool]:
        """
        Whether the result values are distributed in a Logarithmic scale.
        """
        return None

    @property
    def HighFidelity(self) -> typing.Optional[bool]:
        """
        Whether to replot and improve the synchronization of the result values.
        """
        return None

    def GetBandColor(self, index: int) -> int:
        """
        Gets the color of the specified band.
        """
        pass

    def SetBandColor(self, index: int, ColorValue: int) -> None:
        """
        Sets the color of the specified band.
        """
        pass

    def GetLowerBound(self, index: int) -> Ansys.Core.Units.Quantity:
        """
        Gets lower bound value of the specified band.
        """
        pass

    def SetLowerBound(self, index: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        Sets lower bound value of the specified band.
        """
        pass

    def GetUpperBound(self, index: int) -> Ansys.Core.Units.Quantity:
        """
        Gets upper bound value of the specified band.
        """
        pass

    def SetUpperBound(self, index: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        Sets upper bound value of the specified band.
        """
        pass

    def GetBandColorAuto(self, index: int) -> bool:
        """
        Gets whether the specified band is set to Automatic or not.
        """
        pass

    def SetBandColorAuto(self, index: int, val: bool) -> None:
        """
        Sets the specified band to Automatic.
        """
        pass

    def GetUpperBandValueAuto(self, index: int) -> bool:
        """
        Gets whether the specified upper band value is set to Automatic or not.
        """
        pass

    def GetLowerBandValueAuto(self, index: int) -> bool:
        """
        Gets whether the specified lower band value is set to Automatic or not.
        """
        pass

    def ResetColors(self) -> None:
        """
        Resets all colors to default values.
        """
        pass

    def Reset(self) -> None:
        """
        Resets all legend customizations into default values.
        """
        pass

    def MakeCopy(self) -> Ansys.Mechanical.Graphics.Tools.LegendSettings:
        """
        Makes a copy of the CurrentLegendSettings object.
        """
        pass


class LegendSettings(object):
    """
    
            Represents a LegendSettings object. This object holds properties of the Standalone LegendSettings.
            
    """

    @property
    def NumberOfBands(self) -> typing.Optional[int]:
        """
        Number of bands on the legend (min:3, max:30). Bands are added/removed from the top of the legend.
        """
        return None

    @property
    def AllScientificNotation(self) -> typing.Optional[bool]:
        """
        Whether the result values are displayed in scientific notation.
        """
        return None

    @property
    def Digits(self) -> typing.Optional[int]:
        """
        Number of significant digits (min:2 , max:8).
        """
        return None

    @property
    def ColorScheme(self) -> typing.Optional[Ansys.Mechanical.DataModel.Enums.LegendColorSchemeType]:
        """
        Color Scheme for the legend.
        """
        return None

    @property
    def SemiTransparency(self) -> typing.Optional[bool]:
        """
        Whether the legend is semi-transparent.
        """
        return None

    @property
    def LogarithmicScale(self) -> typing.Optional[bool]:
        """
        Whether the result values are distributed in a Logarithmic scale.
        """
        return None

    @property
    def HighFidelity(self) -> typing.Optional[bool]:
        """
        Whether to replot and improve the synchronization of the result values.
        """
        return None

    @property
    def Unit(self) -> typing.Optional[str]:
        """
        The unit for the legend.
        """
        return None

    def GetLowerBound(self, index: int) -> Ansys.Core.Units.Quantity:
        """
        Gets lower bound value of the specified band.
        """
        pass

    def SetLowerBound(self, index: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        Sets lower bound value of the specified band.
        """
        pass

    def GetUpperBound(self, index: int) -> Ansys.Core.Units.Quantity:
        """
        Gets upper bound value of the specified band.
        """
        pass

    def SetUpperBound(self, index: int, value: Ansys.Core.Units.Quantity) -> None:
        """
        Sets upper bound value of the specified band.
        """
        pass

    def GetBandColor(self, index: int) -> int:
        """
        Gets the color of the specified band.
        """
        pass

    def SetBandColor(self, index: int, colorValue: int) -> None:
        """
        Sets the color of the specified band.
        """
        pass

    def GetBandColorAuto(self, index: int) -> bool:
        """
        Gets whether the specified band is set to Automatic or not.
        """
        pass

    def SetBandColorAuto(self, index: int, val: bool) -> None:
        """
        Sets the specified band to Automatic.
        """
        pass

    def GetUpperBandValueAuto(self, index: int) -> bool:
        """
        Gets whether the specified upper band value is set to Automatic or not.
        """
        pass

    def GetLowerBandValueAuto(self, index: int) -> bool:
        """
        Gets whether the lower specified band value is set to Automatic or not.
        """
        pass

    def ResetColors(self) -> None:
        """
        Resets all colors to default values.
        """
        pass

    def Reset(self) -> None:
        """
        Resets all legend customizations into default values.
        """
        pass


