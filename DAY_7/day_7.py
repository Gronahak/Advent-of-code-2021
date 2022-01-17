
DEBUG_MODE = False
# DEBUG_MODE = True

class Crab_Conga_Line():
    def __init__(self, line):
        self.ipt = sorted([int(pos) for pos in line.split(',')])

    def compute_best_pos_p1(self):

        min_fuel = float("infinity")
        best_pos = -1

        for i, pos in enumerate(self.ipt[1:-1]):
            left, right = self.ipt[:i+1], self.ipt[i+2:]

            left_fuel, right_fuel = sum([pos - l for l in left]), sum([r - pos for r in right])

            total_fuel = left_fuel + right_fuel
            
            if total_fuel < min_fuel:
                best_pos = pos
                min_fuel = total_fuel

        print(min_fuel)
  
  
    def compute_best_pos_p2(self):

        min_fuel = float("infinity")
        best_pos = -1

        # for i, pos in enumerate(self.ipt[1:-1]):
        for pos in range(min(self.ipt), max(self.ipt)):
            left, right = [i for i in self.ipt if i < pos], [i for i in self.ipt if i > pos]

            left_fuel, right_fuel = sum([(pos - l)*(pos - l +1)/2 for l in left]), sum([(r - pos)*(r-pos+1)/2 for r in right])

            total_fuel = left_fuel + right_fuel
            
            if total_fuel < min_fuel:
                best_pos = pos
                min_fuel = total_fuel

        print(min_fuel)


def part_1():
    output = ''
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_7/input{debug}.txt'

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            ccl = Crab_Conga_Line(l.strip())

    ccl.compute_best_pos_p1()




def part_2():
    output = ''
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_7/input{debug}.txt'

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            ccl = Crab_Conga_Line(l.strip())

    ccl.compute_best_pos_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



