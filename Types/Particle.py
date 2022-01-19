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
        id, b = read_var_int(self.byte_array)
        self.id = id
        if id in PARTICLE_ID_DICT.keys():
            data = []
            decoding_scheme = PARTICLE_ID_DICT[id]
            for scheme in decoding_scheme:
                if scheme=='varint':
                    value, b = read_var_int(b)
                    data.append(value)
                elif scheme=='slot':
                    slot = Slot(b)
                    b = slot.decode()
                    data.append(slot)
                elif scheme=='position':
                    pos = Position(b)
                    b = pos.decode()
                    data.append(pos)
                elif scheme=='string':
                    length, b = read_var_int(b)
                    string_output = struct.unpack(f">{length}s", b[:length])[0]
                    data.append(string_output)
                else:
                    float_output = struct.unpack(f">{scheme}", b[:4])[0]
                    b = b[4:]
                    data.append(float_output)
        self.data = data
        return b


