import struct
from Packet import Packet
from utils.functions import read_var_int

class EntityTeleportPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(self, timestamp, length, byte_array, id)
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        x, y, z, yaw, pitch, on_ground = struct.unpack('>i>i>ibb?', b)
        cls.x = x
        cls.y = y
        cls.z = z
        cls.yaw = yaw/256.0
        cls.pitch = pitch/256.0
        cls.on_ground = on_ground