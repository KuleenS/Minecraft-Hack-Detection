import struct
from Packets import Packet
from utils.decode import read_var_int
import uuid


class SpawnPlayerPacket(Packet):
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

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        decoded_uuid = uuid.UUID(bytes=b[:16])
        x, y, z, yaw, pitch, current_item = struct.unpack('>iiibbh', b[16:32])
        self.uuid = decoded_uuid
        self.x = x/32.0
        self.y = y/32.0
        self.z = z/32.0
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.current_item = current_item

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
            'current_item': self.current_item
        }

    def __repr__(self) -> str:
        return f'Spawn Player Packet has eid: {self.entity_id}, uuid: {self.uuid}, x: {self.x}, y: {self.y}, z: {self.z}, yaw: {self.yaw}, pitch: {self.pitch}, current_item {self.current_item}'
