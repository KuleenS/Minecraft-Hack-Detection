import io
from nbt import nbt

class NBT:
    def __init__(self,byte_array):
        self.byte_array = byte_array
        self.NBT_data = None
    
    def decode(self):
        data = nbt.NBTFile(fileobj = io.BytesIO(self.byte_array))
        self.NBT_data = data
            