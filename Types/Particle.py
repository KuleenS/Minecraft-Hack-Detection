from utils.decode import read_var_int
from utils.consts import PARTICLE_ID_DICT
from Types import Position, Slot
import struct

class Particle:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.id = None
        self.data = None

    def decode(self):
        id = read_var_int(self.byte_array)
        self.id = id
        if id in PARTICLE_ID_DICT.keys():
            data = []
            decoding_scheme = PARTICLE_ID_DICT[id]
            for scheme in decoding_scheme:
                if scheme=='varint':
                    value = read_var_int(self.byte_array)
                    data.append(value)
                elif scheme=='slot':
                    slot = Slot(self.byte_array)
                    slot.decode()
                    data.append(slot)
                elif scheme=='position':
                    pos = Position(self.byte_array)
                    pos.decode()
                    data.append(pos)
                elif scheme=='string':
                    length = read_var_int(self.byte_array)
                    string_output = struct.unpack(f">{length}s", self.byte_array.read(length))[0]
                    data.append(string_output)
                else:
                    float_output = struct.unpack(f">{scheme}", self.byte_array.read(4))[0]
                    data.append(float_output)
        self.data = data


