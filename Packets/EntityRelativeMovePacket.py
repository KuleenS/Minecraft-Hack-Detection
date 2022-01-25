import struct
from Packets.Packet import Packet
from utils.decode import read_var_int


class EntityRelativeMovePacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.delta_x = None
        self.delta_y = None
        self.delta_z = None
        self.on_ground = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        x, y, z, on_ground = struct.unpack('>bbb?', b)
        self.delta_x = x/32.0
        self.delta_y = y/32.0
        self.delta_z = z/32.0
        self.on_ground = on_ground

    def get(self):
        return {
            'packet_type': 'entity_relative_move',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            'delta_x': self.delta_x,
            'delta_y': self.delta_y,
            'delta_z': self.delta_z,
            'on_ground': self.on_ground
        }

    def __repr__(self) -> str:
        return f'Entity Relative Move Packet has eid: {self.entity_id}, delta_x: {self.delta_x}, delta_y: {self.delta_y}, delta_z: {self.delta_z}, on_ground: {self.on_ground}'
