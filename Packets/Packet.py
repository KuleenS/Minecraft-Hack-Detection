from abc import ABC
from typing import Any


class Packet(ABC):
    def __init__(self, timestamp: int, length: int, byte_array, id=None):
        self.timestamp = timestamp
        self.length = length
        self.byte_array = byte_array
        self.id = id

    def decode(self) -> None:
        pass

    def get(self) -> 'dict[str, any] | list[dict[str, Any]]':
        pass

    def __repr__(self) -> str:
        pass
