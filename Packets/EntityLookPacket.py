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

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        yaw, pitch, on_ground = struct.unpack('bb?', b)
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.on_ground = on_ground
