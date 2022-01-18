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