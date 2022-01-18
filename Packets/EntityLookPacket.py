import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class EntityLookPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        yaw, pitch, on_ground = struct.unpack('bb?', b)
        cls.yaw = yaw/256.0
        cls.pitch = pitch/256.0
        cls.on_ground = on_ground
