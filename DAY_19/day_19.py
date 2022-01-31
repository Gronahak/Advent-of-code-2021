from oceanmapper import OceanMapper

DEBUG_MODE = False
DEBUG_MODE = True



def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_19/input{debug}.txt'

    om = OceanMapper()

    with open(path_to_file, 'r') as f:
        om.parse(f)

    om.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_19/input{debug}.txt'

    om = OceanMapper()

    with open(path_to_file, 'r') as f:
        om.parse(f)
        
    om.show_answer_p2()



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



