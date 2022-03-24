from pydoc import doc
import struct
from utils.consts import METADATA_TYPE_DICT
from Types import Slot
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
        value = None
        for format in decoding_format:
            if format == 'f':
                value = struct.unpack('>f', self.byte_array.read(4))[0]
            elif format == 'h':
                value = struct.unpack('>h', self.byte_array.read(2))[0]
            elif format == 'i':
                value = struct.unpack('>i', self.byte_array.read(4))[0]
            elif format == 'b':
                value = struct.unpack('>b', self.byte_array.read(1))[0]
            elif format == 'string':
                length = read_var_int(self.byte_array)
                value = struct.unpack(
                    f'>{length}s', self.byte_array.read(length))[0].decode('utf-8')
            elif format == 'slot':
                value = Slot.Slot(self.byte_array)
                value.decode()
            data.append(value)
        self.data = data

    def __repr__(self):
        if self.type == 0:
            return f'Metadata type: byte with data: {self.data}'
        elif self.type == 1:
            return f'Metadata type: short with data: {self.data}'
        elif self.type == 2:
            return f'Metadata type: int with data: {self.data}'
        elif self.type == 3:
            return f'Metadata type: float with data: {self.data}'
        elif self.type == 4:
            return f'Metadata type: string with data: {self.data}'
        elif self.type == 5:
            return f'Metadata type: Slot with data: {self.data}'
        elif self.type == 6:
            return f'Metadata type: x,y,z with data: {self.data}'
        elif self.type == 7:
            return f'Metadata type: pitch,yaw,roll with data: {self.data}'

    # An EntityMetadataPacket consists of an array of Metadata objects
