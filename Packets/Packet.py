from abc import ABC

class Packet(ABC):
    def __init__(self, timestamp: int, length: int, byte_array, id=None):
        self.timestamp = timestamp
        self.length = length
        self.byte_array = byte_array
        self.id = id

    def __repr__(self) -> str:
        return f'Packet with id {self.id} starting at {self.timestamp} with a byte_array {self.byte_array} of length {self.length}'

    @classmethod
    def decode(self):
        pass
