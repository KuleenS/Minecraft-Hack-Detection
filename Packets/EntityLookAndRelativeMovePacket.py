import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class EntityLookAndRelativeMovePacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.delta_x = None
        self.delta_y = None
        self.delta_z = None
        self.yaw = None
        self.pitch = None
        self.on_ground = None

    def decode(self):
        eid, b = read_var_int(self.byte_array)
        self.entity_id = eid
        delta_x, delta_y, delta_z, yaw, pitch, on_ground = struct.unpack('>bbbbb?', b)
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_z = delta_z
        self.yaw = yaw/256.0
        self.pitch = pitch/256.0
        self.on_ground = on_ground
