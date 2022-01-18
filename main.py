import json
import struct
import argparse
from utils.classify import classify_packet
from os.path import exists
import Packets

def main(args):
    #read the protocol for 1.8
    #Protocol 47 
    #JSON from https://github.com/PrismarineJS/minecraft-data/blob/master/data/pc/1.8/protocol.json
    protocol = json.load(open('./data/protocol.json', 'r'))

    #creates a mapping between id numbers and names of packets
    packet_json = protocol['play']['toClient']['types']
    #gets the mappings from the protocol
    packet_types = packet_json['packet'][1][0]['type'][1]['mappings']

    #adds packet_ in front of it to work with the keys of packet_json
    packet_types_values = ["packet_"+x for x in list(packet_types.values())]

    #converts the hex string ids to numbers
    packet_types_keys = [int(x, 16) for x in list(packet_types.keys())]

    #creates a dictionary of them
    packet_types = dict(zip(packet_types_keys, packet_types_values))

    packets = []
    if not exists(args.file):
        raise ValueError('File does not exist')
    elif args.file.split('.')[-1]!="tmcpr":
        raise ValueError('File is in wrong format')
    with open(args.file, "rb") as f:
        while timestamp := f.read(4):
            timestamp = struct.unpack('>i', timestamp)[0]
            length = struct.unpack('>i', f.read(4))[0]
            byte_array = f.read(length)
            id = byte_array[0]
            byte_array = byte_array[1:]
            length-=1
            packets.append(classify_packet(timestamp, length, byte_array, id))
    packets = [x for x in packets if x is not None]
    packets[0].decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract position data from 1.8 mcpr files')
    parser.add_argument('-f', '--file', help='file path to tmcpr file', required=True)
    args = parser.parse_args()
    main(args)