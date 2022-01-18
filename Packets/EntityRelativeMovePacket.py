import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class EntityRelativeMovePacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.delta_x = None
        self.delta_y = None
        self.delta_z = None
        self.on_ground = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        x,y,z, on_ground = struct.unpack('bbb?', b)
        cls.delta_x = x/32.0
        cls.delta_y = y/32.0
        cls.delta_z = z/32.0
        cls.on_ground = on_ground
