from Packets.Packet import Packet
import struct
from utils.decode import read_var_int
from Types import Metadata


class EntityMetadataPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.metadata = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        metadata_entries = []
        while True:
            index = struct.unpack(">B", buff[:1])
            if index == 255:
                break
            else:
                buff = buff[1:]
                type_output, buff = read_var_int(buff)
                metadata_entry = Metadata(index, type_output, buff)
                buff = metadata_entry.decode()
                metadata_entries.append(metadata_entry)
        
        self.metadata = metadata_entries

    def __repr__(self) -> str:
        return f'Entity Metadata Packet has eid: {self.entity_id}, metadata: {self.metadata}'
