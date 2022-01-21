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
            if format == 'f':
                value = struct.unpack('>f', buff[:4])[0]
                buff = buff[4:]
            elif format == 'h':
                value = struct.unpack('>h', buff[:2])[0]
                buff = buff[2:]
            elif format == 'i':
                value = struct.unpack('>i', buff[:4])[0]
                buff = buff[4:]
            elif format == 'b':
                value = struct.unpack('>b', buff[:1])[0]
                buff = buff[1:]
            elif format == 'string':
                length, buff = read_var_int(buff)
                value = struct.unpack(f'>{length}s', buff[:length])
                buff = buff[length:]
            elif format == 'slot':
                value = Slot(buff)
                buff = value.decode()
            data.append(value)
        self.data = data
        return buff

    def __repr__(self):
        if self.type == 0:
            return f'Metadata type: byte with data: {self.data}'
        elif self.type == 1:
            return f'Metadata type: short with data: {self.data}'
        elif self.type == 2:
            return f'Metadata type: int with data: {self.data}'
        elif self.type == 3:
            return f'Metadata type: string with data: {self.data}'
        elif self.type == 4:
            return f'Metadata type: string with data: {self.data}'
        elif self.type == 5:
            return f'Metadata type: Slot with data: {self.data}'
        elif self.type == 6:
            return f'Metadata type: x,y,z with data: {self.data}'
        elif self.type == 7:
            return f'Metadata type: pitch,yaw,roll with data: {self.data}'

    # An EntityMetadataPacket consists of an array of Metadata objects
