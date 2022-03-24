import io
from utils.NBTparse import NBTFile

class NBT:
    def __init__(self,byte_array):
        self.byte_array = byte_array
        self.NBT_data = None
    
    def decode(self):
        data = NBTFile(buffer = self.byte_array)
        self.NBT_data = data