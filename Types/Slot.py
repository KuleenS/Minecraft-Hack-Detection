from re import I
import struct
from utils.decode import read_var_int
from Types import NBT

class Slot:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.item_id = None
        self.item_count = None
        self.nbt = None

    def decode(self):
        bool_output = struct.unpack(">?", self.byte_array[:1])[0]
        b = self.byte_array[1:]
        if not bool_output:
            return b
        else:
            id_output, b = read_var_int(b)
            self.item_id = id_output
            item_count = struct.unpack(">b", b[:1])[0]
            self.item_count = item_count
            b = b[1:]
            nbt = NBT(b)
            b = nbt.decode()
            self.nbt = nbt
            return b
