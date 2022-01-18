import struct
from Packet import Packet
from utils.functions import read_var_int

class EntityHeadLookPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(self, timestamp, length, byte_array, id)
        self.entity_id = None
        self.head_yaw = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        head_yaw = struct.unpack('b', b)
        cls.head_yaw = head_yaw/256.0
