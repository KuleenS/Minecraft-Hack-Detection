import struct
from Packets import Packet
from utils.decode import read_var_int
import uuid
from Types import Metadata


class SpawnPlayerPacket(Packet):
    METADATA_TYPE_FILTER_OUT = [4, 5]

    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.uuid = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.current_item = None
        self.metadata = None

    def decode(self):
        eid = read_var_int(self.byte_array)
        self.entity_id = eid
        decoded_uuid = uuid.UUID(bytes=self.byte_array.read(16))
        x, y, z, yaw, pitch, current_item = struct.unpack('>iiibbh', self.byte_array.read(16))
        self.uuid = decoded_uuid
        self.x = x/32.0
        self.y = y/32.0
        self.z = z/32.0
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.current_item = current_item
        metadata_entries = []
        while True:
            index_var = struct.unpack(">B", self.byte_array.read(1))[0]
            if index_var == 127:
                break
            else:
                index = index_var & 0x1F
                type = index_var >> 5
                metadata_entry = Metadata(index, type, self.byte_array)
                metadata_entry.decode()
                metadata_entries.append(metadata_entry)
        self.metadata = metadata_entries

    def get(self):
        return {
            'packet_type': 'spawn_player',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            'uuid': self.uuid.hex,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'yaw': self.yaw,
            'pitch': self.pitch,
            'current_item': self.current_item,
            'metadata': [{
                'packet_type': f'meta_{m.type}',
                'index': m.index,
                'data': m.data,
                'type': m.type
            } for m in self.metadata if m.type not in self.METADATA_TYPE_FILTER_OUT]
        }

    def __repr__(self) -> str:
        return f'Spawn Player Packet has eid: {self.entity_id}, uuid: {self.uuid}, x: {self.x}, y: {self.y}, z: {self.z}, yaw: {self.yaw}, pitch: {self.pitch}, current_item {self.current_item}'