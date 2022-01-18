import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class EntityTeleportPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        x, y, z, yaw, pitch, on_ground = struct.unpack('>iiibb?', b)
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.on_ground = on_ground