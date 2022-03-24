import struct
from utils.decode import read_var_int
from Packets.Packet import Packet


class EntityVelocityPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array: bytes, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.velocity_x = None
        self.velocity_y = None
        self.velocity_z = None

    def decode(self):
        eid = read_var_int(self.byte_array)
        self.entity_id = eid
        x, y, z = struct.unpack('>hhh', self.byte_array.read(6))
        self.velocity_x = x/8000.0
        self.velocity_y = y/8000.0
        self.velocity_z = z/8000.0

    def get(self):
        return {
            'packet_type': 'entity_velocity',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            'velocity_x': self.velocity_x,
            'velocity_y': self.velocity_y,
            'velocity_z': self.velocity_z,
        }

    def __repr__(self) -> str:
        return f'Entity Velocity Packet has eid: {self.entity_id}, velocity_x: {self.velocity_x}, velocity_y: {self.velocity_y}, velocity_z: {self.velocity_z}'
