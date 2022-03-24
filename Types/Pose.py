from utils.decode import read_var_int

class Pose:
    def __init__(self,byte_array):
        self.byte_array = byte_array
        self.pose = None

    def decode(self):
        pose = read_var_int(self.byte_array)
        self.pose = pose