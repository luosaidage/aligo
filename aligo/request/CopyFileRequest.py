"""..."""
from dataclasses import dataclass, field

from aligo.types import DataClass


@dataclass(unsafe_hash=True)
class CopyFileRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None
    to_drive_id: str = None
    to_parent_file_id: str = 'root'
    new_name: str = None
    auto_rename: bool = field(default=None, repr=False)
    overwrite: bool = field(default=None, repr=False)
