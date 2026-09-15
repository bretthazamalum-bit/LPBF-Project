"""Constants module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class Colors(object):
    """
    Color constants, in BGR bitfield layout.
    """

    @classmethod
    @property
    def Blue(cls) -> typing.Optional[int]:
        """
        Blue property.
        """
        return 16711680

    @classmethod
    @property
    def Cyan(cls) -> typing.Optional[int]:
        """
        Cyan property.
        """
        return 16776960

    @classmethod
    @property
    def Green(cls) -> typing.Optional[int]:
        """
        Green property.
        """
        return 65280

    @classmethod
    @property
    def Yellow(cls) -> typing.Optional[int]:
        """
        Yellow property.
        """
        return 65535

    @classmethod
    @property
    def Red(cls) -> typing.Optional[int]:
        """
        Red property.
        """
        return 255

    @classmethod
    @property
    def Gray(cls) -> typing.Optional[int]:
        """
        Gray property.
        """
        return 11053224

    @classmethod
    @property
    def White(cls) -> typing.Optional[int]:
        """
        White property.
        """
        return 16777215


