"""Results module."""
from __future__ import annotations
import typing
if typing.TYPE_CHECKING:
    import Ansys


class ResultDataTable(object):
    """
    Specifies the Result Table.
    """

    @property
    def Item(self) -> typing.Optional[typing.Iterable]:
        """
        Item property.
        """
        return None

    @property
    def Keys(self) -> typing.Optional[typing.Iterable[str]]:
        """
        Keys property.
        """
        return None

    @property
    def Values(self) -> typing.Optional[typing.Iterable[typing.Iterable]]:
        """
        Values property.
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        Count property.
        """
        return None

    def ContainsKey(self, key: str) -> bool:
        """
        ContainsKey method.
        """
        pass


class ResultVariable(object):
    """
    Specifies column data for the Result Table.
    """

    @property
    def Item(self) -> typing.Optional[float]:
        """
        Item property.
        """
        return None

    @property
    def Count(self) -> typing.Optional[int]:
        """
        Count property.
        """
        return None


