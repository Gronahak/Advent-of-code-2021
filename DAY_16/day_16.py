
DEBUG_MODE = False
# DEBUG_MODE = True

from packet_parser import PacketParser

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_16/input{debug}.txt'

    pp = PacketParser()

    with open(path_to_file, 'r') as f:
        pp.parse(f)

    pp.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_16/input{debug}.txt'

    foo = PacketParser()

    with open(path_to_file, 'r') as f:
        foo.parse(f)
        
    foo.show_answer_p2()



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



