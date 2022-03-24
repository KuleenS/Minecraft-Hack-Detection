import struct
from utils.decode import read_var_int
from Packets.Packet import Packet


class EntityStatusPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None
        self.status = None

    def decode(self):
        eid, status = struct.unpack('>ib', self.byte_array.read(5))
        self.entity_id = eid
        self.status = status

    def get(self):
        return {
            'packet_type': 'entity_status',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id,
            'status': self.status
        }

    def __repr__(self) -> str:
        return f'Entity Status Packet has eid: {self.entity_id}, status: {self.status}'
