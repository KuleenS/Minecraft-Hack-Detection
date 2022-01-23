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
        item_id = struct.unpack(">h", self.byte_array[:2])[0]
        b = self.byte_array[2:]
        self.item_id = item_id
        if item_id==-1:
            return b
        else:
            item_count, item_damage = struct.unpack(">bh", b[:3])
            self.item_count = item_count
            self.item_damange = item_damage
            b = b[3:]
            nbt_bool = struct.unpack(">b", b[:1])[0]
            if nbt_bool != 0:
                nbt = NBT.NBT(b)
                b = nbt.decode()
                self.nbt = nbt
            else:
                b = b[1:]
            return b
    
    def __repr__(self):
        return f"Item Slot with item id: {self.item_id}, count: {self.item_count}, damage {self.item_damange}, and NBT data {self.nbt}"
