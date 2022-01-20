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

NBT_ID_DICT = {
    0 : 'TAG_End',
    1 : 'TAG_Byte',
    2: 'TAG_Short',
    3 : 'TAG_Int',
    4: 'TAG_Long',
    5 : 'TAG_Float',
    6 : 'TAG_Double',
    7 : 'TAG_Byte_Array',
    8 : 'TAG_String',
    9 : 'TAG_List',
    10 : 'TAG_Compound',
    11 : 'TAG_Int_Array',
    12 : 'TAG_Long_Array',
}