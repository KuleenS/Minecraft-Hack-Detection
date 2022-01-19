from abc import ABC

class Packet(ABC):
    def __init__(self, timestamp: int, length: int, byte_array, id=None):
        self.timestamp = timestamp
        self.length = length
        self.byte_array = byte_array
        self.id = id

    def __repr__(self) -> str:
        pass

    def decode(self) -> None:
        pass
