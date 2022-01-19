from re import U
from utils.decode import read_var_int
import struct
from Types import UUID

class Chat:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.JSON_data = None
        self.position = None
        self.uuid = None

    def decode(self):
        length, b = read_var_int(self.byte_array)
        json_output, position_output = struct.unpack(f">{length}sb", b[:length+1])
        self.JSON_data = json_output
        self.position = position_output
        
        b = b[length+1:]
        UUID_output = UUID(b)
        b = UUID_output.decode()
        self.uuid = UUID_output
        return b


