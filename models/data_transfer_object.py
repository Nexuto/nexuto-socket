

from dataclasses import dataclass
from enums.status_enum import Status

@dataclass
class DataTransferObject():
    staus: Status
    