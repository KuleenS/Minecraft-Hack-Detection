import struct
from utils.consts import METADATA_TYPE_DICT
from Types import Slot, Position, Pose, Particle, NBT, UUID, Chat
from utils.decode import read_var_int


class Metadata:
    def __init__(self, index, type, byte_array):
        self.index = index
        self.type = type
        self.byte_array = byte_array
        self.data = None

    def decode(self):
        decoding_format = METADATA_TYPE_DICT[self.type]
        data = []
        buff = self.byte_array
        for format in decoding_format:
            if format == 'varint':
                value, buff = read_var_int(buff)

            elif format == 'slot':
                value = Slot(buff)
                buff = value.decode()

            elif format == 'position':
                value = Position(buff)
                buff = value.decode()

            elif format == 'string':
                length, buff = read_var_int(buff)
                value = struct.unpack(f">{length}s", buff[:length])[0]
                buff = buff[length:]

            elif format == 'pose':
                value = Pose(buff)
                buff = value.decode()

            elif format == 'particle':
                value = Particle(buff)
                buff = value.decode()

            elif format == 'nbt':
                value = NBT(buff)
                buff = value.decode()

            elif format == 'uuid':
                value = UUID(buff)
                buff = value.decode()

            elif format == 'chat':
                value = Chat(buff)
                buff = value.decode()

            elif format == 'f':
                value = struct.unpack(f">{format}", buff[:4])[0]
                buff = buff[4:]

            elif format == '?':
                value = struct.unpack(f">{format}", buff[:1])[0]
                buff = buff[1:]
                if not value:
                    break
            data.append(value)
        self.data = data
        return buff

    # An EntityMetadataPacket consists of an array of Metadata objects
