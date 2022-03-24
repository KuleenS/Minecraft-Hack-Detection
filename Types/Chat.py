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
        length = read_var_int(self.byte_array)
        json_output, position_output = struct.unpack(f">{length}sb", self.byte_array.read(length))
        self.JSON_data = json_output
        self.position = position_output
        
        UUID_output = UUID(self.byte_array)
        UUID_output.decode()
        self.uuid = UUID_output

