from enum import Enum, auto

DEBUG_MODE = False
DEBUG_MODE = True


class NodeStatus(Enum):
    START = auto()
    END = auto()
    MIDDLE = auto()

class Chiton
    first_node = True
    def __init__(self, risk_level):
        self.risk_level = risk_level
        self.neighbors = []
        if Chiton.first_node:
            self.status = NodeStatus.START
        else:
            self.status = NodeStatus.MIDDLE


    def connect(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

class Cavern():
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.nodes = []

self.nodes = []
    def parse(self, f):
        previous_row = []
        for l in f.readlines():
            previous_chiton = None
            current_row = []
            l = l.strip()

            for risk_level in l:
                c = Chiton(int(risk_level))
                current_row.append(c)

                if previous_chiton:
                    c.connect(previous_chiton)
                previous_chiton = c

            if previous_row:
                for above, below in zip(previous_row, current_row):
                    above.connect(below)
            
            previous_row = current_row
        c.status = NodeStatus.END

    def show_answer_p1(self):
        pass

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_15/input{debug}.txt'

    chiton = Cavern()

    with open(path_to_file, 'r') as f:
        chiton.parse(f)

    chiton.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_15/input{debug}.txt'

    chiton = Cavern()

    with open(path_to_file, 'r') as f:
        chiton.parse(f)
        
    chiton.show_answer_p2()



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



