
from typing import DefaultDict
from pprint import pprint

DEBUG_MODE = False
# DEBUG_MODE = True



class School_of_lanternfish():
    def __init__(self):
        self.count = DefaultDict(int)

        for n in range(9):
            self.count[n] = 0

    def __str__(self):
        return str(self.count)

    def read(self, line):
        for n in line.split(','):
            self.count[int(n)] += 1

    def iterate_1_day(self):
        next_days_count = DefaultDict(int)
        
        next_days_count[8] = self.count[0]

        for n in range(8):
            next_days_count[n] = self.count[n+1]


        next_days_count[6] += self.count[0]

        self.count = next_days_count

    def iterate_n_days(self, n_days):
        for n in range(n_days):
            self.iterate_1_day()


    def count_fishies(self):
        print(sum(self.count.values()))

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_6/input{debug}.txt'

    school = School_of_lanternfish()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            school.read(l.strip())


    n_days = 256
    school.iterate_n_days(n_days)
    school.count_fishies()
    # pprint(str(school))




def part_2():
    output = ''
    debug = '_debug_part2' if DEBUG_MODE else ''
    path_to_file = f'DAY_6/input{debug}.txt'

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            pass
        
    print(output)



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



