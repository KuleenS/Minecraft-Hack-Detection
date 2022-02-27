from math import cos, sin, radians
"""
Packets Needed: Entity Head Look
"""
def process_head_yaw(packets: list[dict]) -> "tuple[list[int], list[float]]":
    timestamps = []
    head_yaws = []
    for packet in packets:
        timestamps.append(packet['timestamp'])
        head_yaw = packet['head_yaw']
        if head_yaw<0:
            head_yaw+=1
        head_yaws.append(head_yaw)
    return timestamps, head_yaws
"""
Packets Needed: Spawn Player, Entity Teleport, Entity Look and Relative Move, Entity Look, Entity
"""
def process_yaw_pitch(packets: list[dict]) -> "tuple[list[int], list[float], list[float], list[float]]":
    timestamps = []
    X = []
    Y = []
    Z = []
    for packet in packets:
        if packet['packet_type']=='entity' and len(X)!=0:
            X.append[X[-1]]
            Y.append[Y[-1]]
            Z.append[Z[-1]]
        else:
            print(packet['packet_type'],packet['pitch'], packet['yaw'])
            pitch = packet['pitch']
            yaw = packet['yaw']
            pitch = radians((packet['pitch']*256))
            yaw = radians((packet['yaw']*256))
            x = -cos(pitch) * sin(yaw) 
            y = -sin(pitch) 
            z =  cos(pitch) * cos(yaw)
            X.append(x)
            Y.append(y)
            Z.append(z)
        timestamps.append(packet['timestamp'])
    return timestamps, X, Y, Z
"""
Packets Needed: Entity Status
"""
def process_status(packets: list[dict]) -> "tuple[list[int], list[int]]":
    timestamps = []
    status = []
    for packet in packets:
        if packet['status']==2:
            status.append(1)
        else:
            status.append(0)
        timestamps.append(packet['timestamp'])
    return timestamps, status

"""
Packets Needed: Entity Metadata and Spawn Player
"""
def process_metadata(packets: list[dict]) -> "tuple[list[int], list[int], list[int], list[int], list[int], list[int]]":
    timestamps = []
    On_Fire = []
    Crouched = []
    Sprinting = []
    Eating_Drinking_Blocking = []
    Invisible = []
    for packet in packets:
        if packet['index']==0:
            data = packet['data']
            On_Fire.append(data & 0x01)
            Crouched.append(data & 0x02)
            Sprinting.append(data & 0x08)
            Eating_Drinking_Blocking.append(data & 0x10)
            Invisible.append(data & 0x20)
        else:
            On_Fire.append(0)
            Crouched.append(0)
            Sprinting.append(0)
            Eating_Drinking_Blocking.append(0)
            Invisible.append(0)
        timestamps.append(packet['timestamp'])
    return timestamps, On_Fire, Crouched, Sprinting, Eating_Drinking_Blocking, Invisible

"""
Packets Needed: Entity, Entity Look and Relative Move, Entity Teleport, Entity Velocity, Entity Relative Move, Spawn Player
"""
def process_xyz(packets: list[dict]) -> "tuple[list[int], list[float], list[float], list[float]]":
    timestamps = []
    X = []
    Y = []
    Z = []
    for i, packet in enumerate(packets):
        if packet['packet_type']=='entity' and len(X)!=0:
            X.append[X[-1]]
            Y.append[Y[-1]]
            Z.append[Z[-1]]
        elif packet['packet_type'] in ['spawn_player', 'entity_teleport']:
            X.append(packet['x'])
            Y.append(packet['y'])
            Z.append(packet['z'])
        elif packet['packet_type'] in ['entity_relative_move', 'entity_look_and_relative_move']:
            X.append(X[-1]+packet['x'])
            Y.append(Y[-1]+packet['y'])
            Z.append(Z[-1]+packet['z'])
        elif packet['type'] == 'entity_velocity' and len(X)!=0:
            velocity_x = (packet['velocity_x']*1000)/50
            velocity_y = (packet['velocity_y']*1000)/50
            velocity_z = (packet['velocity_z']*1000)/50
            delta_x = velocity_x * (packets[i+1]['timestamp'] - packet['timestamp'])
            delta_y = velocity_y * (packets[i+1]['timestamp'] - packet['timestamp'])
            delta_z = velocity_z * (packets[i+1]['timestamp'] - packet['timestamp'])
            X.append(X[-1]+delta_x)
            Y.append(Y[-1]+delta_y)
            Z.append(Z[-1]+delta_z)
        timestamps.append(packet['timestamp'])
    return timestamps, X, Y, Z
"""
Packets Needed: Entity Look, Entity Look and Relative Move, Entity Relative Move, Entity Teleport, Entity
"""
def process_on_ground(packets: list[dict]) -> "tuple[list[int], list[int]]":
    timestamps = []
    on_ground = []
    for packet in packets:
        on_ground.append(packet['on_ground'])
        timestamps.append(packet['timestamp'])
    return timestamps, on_ground