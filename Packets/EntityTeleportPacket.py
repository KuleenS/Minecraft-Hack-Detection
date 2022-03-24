import struct
from Packets.Packet import Packet
from utils.decode import read_var_int


class EntityTeleportPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    def decode(self):
        eid = read_var_int(self.byte_array)
        self.entity_id = eid
        x, y, z, yaw, pitch, on_ground = struct.unpack('>iiibb?', self.byte_array.read(15))
        self.x = x/32.0
        self.y = y/32.0
        self.z = z/32.0
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.on_ground = on_ground

    def get(self):
        return {
            'packet_type': 'entity_teleport',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'yaw': self.yaw,
            'pitch': self.pitch,
            'on_ground': self.on_ground
        }

    def __repr__(self) -> str:
        return f'Entity Teleport Packet has eid: {self.entity_id}, x: {self.x}, y: {self.y}, z: {self.z}, yaw: {self.yaw}, pitch: {self.pitch}, on_ground: {self.on_ground}'
