from Packet import Packet

class EntityMetadataPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(self, timestamp, length, byte_array, id)

    @classmethod
    def decode(cls):
        pass
