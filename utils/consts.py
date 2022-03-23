from .processfunctions import *

METADATA_TYPE_DICT = {
    0: ['b'],
    1: ['h'],
    2: ['i'],
    3: ['f'],
    4: ['string'],
    5: ['slot'],
    6: ['i', 'i', 'i'],
    7: ['f', 'f', 'f']
}

PARTICLE_ID_DICT = {
    2 : ['varint'],
    3 : ['varint'],
    14 : ['f', 'f', 'f', 'f'],
    15 : ['f', 'f', 'f', 'f', 'f', 'f', 'f'],
    24 : ['varint'],
    35 : ['slot'],
    36 : ['position', 'string', 'position', 'varint', 'varint']
}

ALL_PACKET_TYPES = [
    'entity_head_look',
    'spawn_player', 
    'entity_relative_move', 
    'entity_status', 
    'entity_velocity', 
    'entity_teleport', 
    'entity_metadata', 
    'entity_look_and_relative_move', 
    'entity_look', 
    'entity', 
    'meta_0', 
    'meta_1', 
    'meta_2', 
    'meta_3', 
    'meta_6', 
    'meta_7'
]

TIME_SERIES_PACKETS = {
    "on_ground" : (process_on_ground, ['entity_look', 'entity_look_and_relative_move', 'entity_relative_move', 'entity_teleport', 'entity']),
    "status" : (process_status, ['entity_status']),
    "metadata" : (process_metadata, ['entity_metadata', 'spawn_player']),
    "xyz" : (process_xyz, ['entity', 'entity_look_and_relative_move' , 'entity_teleport', 'entity_velocity', 'entity_relative_move', 'spawn_player']),
    "yaw_pitch" : (process_yaw_pitch, ['spawn_player','entity_teleport', 'entity_look_and_relative_move','entity_look' ,'entity']),
    "head_yaw" : (process_head_yaw, ['entity_head_look'])
}