class Beam:
    """Beam class"""
    
    def __init__(self, length, young, width, height, supports, distributed_loads, punctual_loads):
        self.length = length
        self.young = young
        self.width = width
        self.height = height
        self.inertia = width*pow(height,3)/12 
        self.supports = supports
        self.distributed_loads = distributed_loads
        self.punctual_loads = punctual_loads
    
    def __str__(self):
        return f'''Beam
            length = {self.length}, Young Module = {self.young},
            width = {self.width}, height = {self.height},
            inertia = {self.inertia}
            supports = {self.supports}
            distributed_loads = {self.distributed_loads}
            punctual_loads = {self.punctual_loads}
            '''