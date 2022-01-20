from pydoc import doc
import struct
from utils.consts import METADATA_TYPE_DICT
from Types import Slot, Position, Pose, Particle, NBT, UUID, Chat
from utils.decode import read_var_int 

class Metadata:
    def __init__(self, index, type, byte_array):
        self.index = index
        self.type = type
        self.byte_array = byte_array
        self.data = None
    
    def decode(self):
        decoding_format = METADATA_TYPE_DICT[self.type]
        data = []
        buff = self.byte_array
        value = None
        for format in decoding_format:
            if format=='f':
                value = struct.unpack('>f', buff[:4])
                buff = buff[4:]
            elif format=='h':
                value = struct.unpack('>h', buff[:2])
                buff = buff[2:]
            elif format=='i':
                value = struct.unpack('>i', buff[:4])
                buff = buff[4:]
            elif format=='b':
                value = struct.unpack('>b', buff[:1])
                buff = buff[1:]
            elif format=='string':
                length, buff = read_var_int(buff)
                value = struct.unpack(f'>{length}s', buff[:length])
                buff = buff[length:]
            elif format=='slot':
                value = Slot(buff)
                buff = value.decode()
            data.append(value)
        self.data = data
        return buff

    #An EntityMetadataPacket consists of an array of Metadata objects