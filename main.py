import struct
import argparse
from os.path import exists
import io


from utils.classify import classify_packet
from utils.consts import ALL_PACKET_TYPES, TIME_SERIES_PACKETS
from utils.interpolate import interpolate
from utils.decode import read_var_int

def main(args):
    packets = []
    all_parsed = []
    final = []
    if not exists(args.file):
        raise ValueError('File does not exist')
    elif args.file.split('.')[-1] != "tmcpr":
        raise ValueError('File is in wrong format')
    with open(args.file, "rb") as f:
        while timestamp := f.read(4):
            timestamp = struct.unpack('>i', timestamp)[0]
            length = struct.unpack('>i', f.read(4))[0]
            byte_array = f.read(length)
            byte_array = io.BytesIO(byte_array)
            id = read_var_int(byte_array)
            length -= 1
            packet = classify_packet(timestamp, length, byte_array, id)
            packet and packets.append(packet)
    for packet in packets:
        packet.decode()
        parsed = packet.get()
        all_parsed.append(parsed)

    for parsed_packet in all_parsed:
        if type(parsed_packet) == list:
            for nested in parsed_packet:
                final.append(nested)
        else:
            final.append(parsed_packet)
    entity_ids = list(set([x['entity_id'] for x in final if 'uuid' in x]))
    print(final)
    player_time_series = {}
    biggest_timestamp = max([x['timestamp'] for x in final])
    smallest_timestamp = min([x['timestamp'] for x in final])
    for player in entity_ids:
        packets_for_player = [x for x in final if ('entity_id' in x) and (x['entity_id'] == player)]
        player_dict = {x: [] for x in ALL_PACKET_TYPES}
        for packet in packets_for_player:
            packet_type = packet['packet_type']
            player_dict[packet_type].append(packet)
        time_series_for_player = {}
        for time_series in TIME_SERIES_PACKETS:
            packets_to_process = []
            decode_config = TIME_SERIES_PACKETS[time_series]
            function_associated_with_time_series = decode_config[0]
            packets_associated_with_time_series = decode_config[1]
            for key in packets_associated_with_time_series:
                packets_to_process.extend(player_dict.get(key))
            packets_to_process = sorted(packets_to_process, key = lambda i: i['timestamp'])
            output_time_series = function_associated_with_time_series(packets_to_process)
            time_series_for_player[time_series] = interpolate(output_time_series, smallest_timestamp, biggest_timestamp)
        player_time_series[player] = time_series_for_player

        
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract position data from 1.8 mcpr files')
    parser.add_argument(
        '-f', '--file', help='file path to tmcpr file', required=True)
    args = parser.parse_args()
    main(args)
