import struct
from utils.decode import read_var_int
from Packets.Packet import Packet

class EntityStatusPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.status = None

    def decode(self):
        eid, status = struct.unpack('>ib', self.byte_array)
        self.entity_id = eid
        self.status = status
