import struct

class Metadata:
    def __init__(self):
        self.index = None
        self.type = None
        self.value = None

    #An EntityMetadataPacket consists of an array of Metadata objects