
DEBUG_MODE = False
DEBUG_MODE = True

class Foo():
    def __init__(self):
        pass

    def parse(self, f):
        for l in f.readlines():
            l = l.strip()

    def show_answer_p1(self):
        pass

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_15/input{debug}.txt'

    foo = Foo()

    with open(path_to_file, 'r') as f:
        foo.parse(f)

    foo.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_15/input{debug}.txt'

    foo = Foo()

    with open(path_to_file, 'r') as f:
        foo.parse(f)
        
    foo.show_answer_p2()



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



