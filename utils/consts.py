METADATA_TYPE_DICT = {
            0: ['b'],
            1: ['varint'],
            2: ['f'],
            3: ['string'],
            4: ['chat'],
            5: ['?', 'chat'],
            6: ['slot'],
            7: ['?'],
            8: ['f', 'f', 'f'],
            9: ['position'],
            10: ['?', 'position'], 
            11: ['varint'],
            12: ['?', 'uuid'],
            13: ['?', 'varint'],
            14: ['nbt'],
            15: ['particle'],
            16: ['varint', 'varint', 'varint'],
            17: ['?', 'varint'],
            18: ['pose']
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