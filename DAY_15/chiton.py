from enum import Enum, auto

class NodeStatus(Enum):
    START = auto()
    END = auto()
    MIDDLE = auto()

class Chiton:
    first_node = True
    def __init__(self, risk_level, lattice, row, col):
        self.row = row
        self.col = col
        self.lattice = lattice
        self.risk_level = risk_level
        self.neighbors = []
        self.cost_to_node = float("inf")
        self.parent_node = None
        if Chiton.first_node:
            self.status = NodeStatus.START
            self.cost_to_node = 0
            Chiton.first_node = False
        else:
            self.status = NodeStatus.MIDDLE

    def get_heuristic_value(self):
        network_width, network_height = self.lattice.network.width, self.lattice.network.height
        lattice_width, lattice_height = self.lattice.width, self.lattice.height

        goal_x, goal_y = network_width*lattice_width-1, network_height*lattice_height-1

        current_x, current_y = self.lattice.pos.real+self.col, self.lattice.pos.imag+self.row

        manhattan_distance_to_goal = (goal_x-current_x) + (goal_y-current_y)
        return manhattan_distance_to_goal
    
    
    def __repr__(self):
        return str(self.risk_level)

    def connect(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)