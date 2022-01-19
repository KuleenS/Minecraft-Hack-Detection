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
        head_yaw = struct.unpack('>b', b)[0]
        self.head_yaw = head_yaw/256.0
    
    def __repr__(self) -> str:
        return f'Entity Head Look Packet has eid: {self.entity_id}, head_yaw: {self.head_yaw}'
