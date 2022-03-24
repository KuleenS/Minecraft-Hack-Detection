from Packets.Packet import Packet
from utils.decode import read_var_int


class EntityPacket(Packet):
    def __init__(self, timestamp: int, length: int, byte_array, id: int):
        super().__init__(timestamp, length, byte_array, id)
        self.entity_id = None

    def decode(self):
        eid = read_var_int(self.byte_array)
        self.entity_id = eid

    def get(self):
        return {
            'packet_type': 'entity',
            'timestamp': self.timestamp,
            'entity_id': self.entity_id
        }

    def __repr__(self) -> str:
        return f'Entity Packet has eid: {self.entity_id}'
