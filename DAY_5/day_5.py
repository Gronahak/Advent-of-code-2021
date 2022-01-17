class MineField:
    grid_size = 1000

    def __init__(self):
        self.grid  = [[0 for _ in range(MineField.grid_size)]  for _ in range(MineField.grid_size) ] 


    def iter_coords_part1(self, x1, y1, x2, y2):
        if x1 == x2:  # vertical line
            for l in range(min(y1, y2), max(y1, y2) + 1):
                yield (l, x1)
        
        elif y1 == y2:  # horizontal line
            for c in range(min(x1, x2), max(x1, x2) + 1):
                yield (y1, c)
        
        elif abs(y2-y1) == abs(x2-x1):  # diagonal
            if any([
                (x1 <= x2 and y1 <= y2),
                (x1 >= x2 and y1 >= y2),
            ]):   # f(x) = -x diagonal
                x0, y0 = min(x1, x2), min(y1, y2)
                for i in range(max(x1, x2) - min(x1, x2) + 1):
                    yield (y0 + i, x0 + i)

            else:
                x0, y0 = max(x1, x2), min(y1, y2)
                for i in range(max(x1, x2) - min(x1, x2) + 1):
                    yield (y0 + i, x0 - i)


        else:
            return


    def add_entry(self, *entry):
        x1, y1, x2, y2 = entry

        # input()
        generated = self.iter_coords_part1(x1, y1, x2, y2)
        try:
            for l, c in generated:
                self.grid[c][l] += 1
        except StopIteration:
            pass
        # input()


    def count_dangerous_spots(self):
        n = 0
        for l in range(MineField.grid_size):
            for c in range(MineField.grid_size):
                if self.grid[l][c] >= 2:
                    n += 1
        print(n)


    def __str__(self):
        return "\n".join(str(l) for l in self.grid)


def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_5/input{debug}.txt'

    mf = MineField()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():

            coord1, coord2 = l.strip().split(" -> ")
            x1, y1 = coord1.split(",")
            x2, y2 = coord2.split(",")
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            mf.add_entry(x1, y1, x2, y2)
    
    
    mf.count_dangerous_spots()




def part_2():
    output = ''
    debug = '_debug_part2' if DEBUG_MODE else ''
    path_to_file = f'DAY_5/input{debug}.txt'

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            pass
        
    print(output)



DEBUG_MODE = True
DEBUG_MODE = False


RUN_PART = part_1




if __name__ == "__main__":
    RUN_PART()



