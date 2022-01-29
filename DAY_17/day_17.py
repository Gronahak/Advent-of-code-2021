from trickshot import TrickShot


DEBUG_MODE = False
# DEBUG_MODE = True



def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_17/input{debug}.txt'

    ts = TrickShot()

    with open(path_to_file, 'r') as f:
        ts.parse(f)

    ts.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_17/input{debug}.txt'

    ts = TrickShot()

    with open(path_to_file, 'r') as f:
        ts.parse(f)
        
    ts.show_answer_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



