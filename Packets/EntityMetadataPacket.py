from Packets.Packet import Packet
import struct
from utils.decode import read_var_int
from Types import Metadata
import json


class EntityMetadataPacket(Packet):
    METADATA_TYPE_FILTER_OUT = [4, 5]

    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.metadata = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        metadata_entries = []
        while True:
            index_var = struct.unpack(">B", b[:1])[0]
            if index_var == 127:
                break
            else:
                b = b[1:]
                index = index_var & 0x1F
                type = index_var >> 5
                metadata_entry = Metadata(index, type, b)
                b = metadata_entry.decode()
                metadata_entries.append(metadata_entry)
        self.metadata = metadata_entries

    def get(self):
        return [{
            'packet_type': f'meta_{m.type}',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            m.type: m.data,
        } for m in self.metadata if m.type not in self.METADATA_TYPE_FILTER_OUT]

    def __repr__(self) -> str:
        return f'Entity Metadata Packet has eid: {self.entity_id}, metadata: {self.metadata}'
