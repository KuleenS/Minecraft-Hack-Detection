import io
import struct


def read_var_int(buff: bytes) -> "tuple[int, bytes]":
    buff = io.BytesIO(buff)
    total = 0
    shift = 0
    val = 0x80
    while val & 0x80:
        val = struct.unpack('>B', buff.read(1))[0]
        total |= ((val & 0x7F) << shift)
        shift += 7
    if total & (1 << 31):
        total = total - (1 << 32)
    return total, buff.read()


def read_metadata(buff: bytes) -> "tuple[int, bytes]":
    buff = io.BytesIO(buff)
    total = 0
    shift = 0
    val = 0xff
    while val & 0xff:
        val = struct.unpack('>B', buff.read(1))[0]
        total |= ((val & 0x7F) << shift)
        shift += 7
    if total & (1 << 31):
        total = total - (1 << 32)
    return total, buff.read()
