import struct
from Packets.Packet import Packet
from utils.decode import read_var_int

class SpawnPlayerPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id:int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.uuid = None
        self.x = None
        self.y = None
        self.z = None
        self.yaw = None
        self.pitch = None 
        self.current_item = None

    @classmethod
    def decode(cls):
        eid, b = read_var_int(cls.byte_array)
        cls.entity_id = eid
        uuid, x, y, z, yaw, pitch, current_item = struct.unpack('>QQ>i>i>ibbh', b[:32])
        cls.uuid = uuid
        cls.x = x
        cls.y = y
        cls.z = z
        cls.yaw = yaw
        cls.pitch = pitch 
        cls.current_item = current_item
        
