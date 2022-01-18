import struct
from Packet import Packet
from utils.functions import read_var_int

class EntityLookAndRelativeMovePacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(self, timestamp, length, byte_array, id)
        self.entity_id = None
        self.delta_x = None
        self.delta_y = None
        self.delta_z = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        delta_x, delta_y, delta_z, yaw, pitch, on_ground = struct.unpack('bbbbb?', b)
        cls.delta_x = delta_x
        cls.delta_y = delta_y
        cls.delta_z = delta_z
        cls.yaw = yaw/256.0
        cls.pitch = pitch/256.0
        cls.on_ground = on_ground
