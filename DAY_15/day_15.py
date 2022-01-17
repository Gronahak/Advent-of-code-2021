
DEBUG_MODE = False
DEBUG_MODE = True


class Chiton
    def __init__(self, risk_level):
        self.risk_level = risk_level
        self.neighbors = []

    def connect(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

class Cavern():
    def __init__(self):
        pass

    def parse(self, f):
        previous_row = []
        current_row = []
        for l in f.readlines():
            previous_chiton = None
            l = l.strip()

            for risk_level in l:
                c = Chiton(int(risk_level))
                current_row.append(c)

                if not previous_chiton:
                    previous_chiton = c
                else:
                    c.connect(previous_chiton)

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



