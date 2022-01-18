import struct
from utils.decode import read_var_int
from Packets.Packet import Packet

class EntityStatusPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.status = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        status = struct.unpack('b', b)
        cls.status = status
