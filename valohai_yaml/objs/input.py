from enum import Enum
from typing import List, Optional, Union

from .base import Item


class KeepDirectories(Enum):
    """How to retain directories when using storage wildcards."""

    NONE = 'none'
    SUFFIX = 'suffix'
    FULL = 'full'

    @classmethod
    def cast(cls, value: Union[bool, str]) -> 'KeepDirectories':
        if not value:
            return KeepDirectories.NONE
        if value is True:
            return KeepDirectories.FULL
        return KeepDirectories(str(value).lower())


class Input(Item):
    """Represents an input definition within a step definition."""

    def __init__(
        self,
        *,
        name: str,
        default: Optional[Union[List[str], str]] = None,
        optional: bool = False,
        description: Optional[str] = None,
        keep_directories: bool = False,
        filename: Optional[str] = None
    ) -> None:
        self.name = name
        self.default = default  # may be None, a string or a list of strings
        self.optional = bool(optional)
        self.description = description
        self.keep_directories = KeepDirectories.cast(keep_directories)
        self.filename = filename

    def get_data(self) -> dict:
        data = super().get_data()
        if self.keep_directories is not KeepDirectories.NONE:
            data['keep_directories'] = data['keep_directories'].value
        else:
            data.pop('keep_directories', None)
        return data
