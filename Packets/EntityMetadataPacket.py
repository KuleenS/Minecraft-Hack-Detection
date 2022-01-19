from Packets.Packet import Packet
import io
import struct
from utils.decode import read_var_int, read_metadata


class EntityMetadataPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.metadata = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid

    def __repr__(self) -> str:
        return f'Entity Metadata Packet has eid: {self.entity_id}, metadata: {self.metadata}'
