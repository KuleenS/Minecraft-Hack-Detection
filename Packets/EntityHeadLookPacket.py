import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class EntityHeadLookPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.head_yaw = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        head_yaw = struct.unpack('b', b)
        self.head_yaw = head_yaw/256.0
