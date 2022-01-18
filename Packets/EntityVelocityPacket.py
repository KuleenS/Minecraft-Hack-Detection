import struct
from utils.functions import read_var_int
from Packet import Packet


class EntityVelocityPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array:bytes, id:int):
        super().__init__(self, timestamp, length, byte_array, id)
        self.entity_id = None
        self.velocity_x = None
        self.velocity_y = None
        self.velocity_z = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        x,y,z = struct.unpack('bbb', b)
        cls.velocity_x = x/8000.0
        cls.velocity_y = y/8000.0
        cls.velocity_z = z/8000.0
