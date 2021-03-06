import io
import struct

def read_var_int(buff) -> "int":
    total = 0
    shift = 0
    val = 0x80
    while val & 0x80:
        val = struct.unpack('>B', buff.read(1))[0]
        total |= ((val & 0x7F) << shift)
        shift += 7
    if total & (1 << 31):
        total = total - (1 << 32)
    return total
                    