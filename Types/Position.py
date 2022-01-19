from utils.decode import read_var_int

class Position:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.x = None
        self.y = None
        self.z = None
    def decode(self):
        val, b = read_var_int(self.byte_array)
        self.x = val >> 38
        self.y = (val << 52 >> 52)
        self.z = (val << 26 >> 38)