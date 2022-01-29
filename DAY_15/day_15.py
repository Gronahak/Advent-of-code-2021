from cavern_network import CavernNetwork
from cavern import Cavern

DEBUG_MODE = False
# DEBUG_MODE = True






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

    size = 100
    if DEBUG_MODE:
        size = 10

    cn = CavernNetwork(5,5,[size,size])

    with open(path_to_file, 'r') as f:
        cn.parse(f)
        
    cn.show_answer_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



