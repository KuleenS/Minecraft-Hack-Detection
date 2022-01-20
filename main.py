import struct
import argparse
from utils.classify import classify_packet
from os.path import exists


def main(args):
    packets = []
    if not exists(args.file):
        raise ValueError('File does not exist')
    elif args.file.split('.')[-1] != "tmcpr":
        raise ValueError('File is in wrong format')
    with open(args.file, "rb") as f:
        while timestamp := f.read(4):
            timestamp = struct.unpack('>i', timestamp)[0]
            length = struct.unpack('>i', f.read(4))[0]
            byte_array = f.read(length)
            id = byte_array[0]
            byte_array = byte_array[1:]
            length -= 1
            packet = classify_packet(timestamp, length, byte_array, id)
            packet and packets.append(packet)
    for packet in packets:
        packet.decode()
        print(packet.get())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract position data from 1.8 mcpr files')
    parser.add_argument(
        '-f', '--file', help='file path to tmcpr file', required=True)
    args = parser.parse_args()
    main(args)
