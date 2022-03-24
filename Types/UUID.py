import uuid

class UUID:
    def __init__(self, byte_array):
        self.byte_array = byte_array
        self.uuid = None
    
    def decode(self):
        decoded_uuid = uuid.UUID(bytes=self.byte_array.read(16))
        self.uuid = decoded_uuid