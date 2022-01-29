from snailfishadder import SnailfishAdder

DEBUG_MODE = False
# DEBUG_MODE = True

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_18/input{debug}.txt'

    sfa = SnailfishAdder()

    with open(path_to_file, 'r') as f:
        sfa.parse(f)

    sfa.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_18/input{debug}.txt'

    sfa = SnailfishAdder()

    with open(path_to_file, 'r') as f:
        sfa.parse_p2(f)
        
    sfa.show_answer_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



