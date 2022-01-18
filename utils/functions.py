import Packets

def read_var_int(b:bytes) -> tuple[int, bytes]:
    value = 0
    length = 0
    while True:
        currentByte = b[length]
        value |= (currentByte & 0x7F) << (length * 7)
        length += 1
        if ((value & 0x80) != 0x80):
            break
    return value, b[length:]

def classify_packet(timestamp: int, length: int, byte_array:bytes, id:int) -> Packets.Packet:
    """0x0C Spawn Player 12
    0x12 Entity Velocity 18
    0x14 Entity 20
    0x15 Entity Relative Move 21
    0x16 Entity Look 22
    0x17 Entity Look And Relative Move 23
    0x18 Entity Teleport 24
    0x19 Entity Head Look 25
    0x1A Entity Status 26
    0x1C Entity Metadata 28"""
    if id==12:
        packet = Packets.SpawnPlayerPacket(timestamp, length, byte_array, id)
    elif id==18:
        packet = Packets.EntityVelocityPacket(timestamp, length, byte_array, id)
    elif id==20:
        packet = Packets.EntityPacket(timestamp, length, byte_array, id)
    elif id==21:
        packet = Packets.EntityRelativeMovePacket(timestamp, length, byte_array, id)
    elif id==22:
        packet = Packets.EntityLookPacket(timestamp, length, byte_array, id)
    elif id==23:
        packet = Packets.EntityLookAndRelativeMovePacket(timestamp, length, byte_array, id)
    elif id==24:
        packet = Packets.EntityTeleportPacket(timestamp, length, byte_array, id)
    elif id==25:
        packet = Packets.EntityHeadLookPacket(timestamp, length, byte_array, id)
    elif id==26:
        packet = Packets.EntityStatusPacket(timestamp, length, byte_array, id)
    elif id==28:
        packet = Packets.EntityMetadataPacket(timestamp, length, byte_array, id)
    else:
        packet = None
    return packet

