import struct
from Types import NBT

class Slot:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.item_id = None
        self.item_count = None
        self.item_damange = None
        self.nbt = None

    def decode(self):
        item_id = struct.unpack(">h", self.byte_array.read(2))[0]
        self.item_id = item_id
        if item_id==-1:
            return
        else:
            item_count, item_damage = struct.unpack(">bh", self.byte_array.read(3))
            self.item_count = item_count
            self.item_damange = item_damage
            nbt_bool = struct.unpack(">b", self.byte_array.read(1))[0]
            if nbt_bool != 0:
                nbt = NBT.NBT(self.byte_array)
                nbt.decode()
                self.nbt = nbt
    
    def __repr__(self):
        return f"Item Slot with item id: {self.item_id}, count: {self.item_count}, damage {self.item_damange}, and NBT data {self.nbt}"
