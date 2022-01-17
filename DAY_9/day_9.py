
DEBUG_MODE = False
# DEBUG_MODE = True


class SmokeBasin():
    def __init__(self):
        self.height_map = []

    def add_line(self, line):
        self.height_map.append(line)

    def end_of_input(self):
        self.height = len(self.height_map)
        self.width =  len(self.height_map[0])

        new_map = []
        for line in self.height_map:
            new_map.append([int(el) for el in line])

        self.height_map = new_map

    
    def get_neighbors_coord(self, ln, cn):
        neighbors = []
        y_deltas = [0, 0, -1, 1,]
        x_deltas = [-1, 1, 0, 0,]

        for dy, dx in zip(y_deltas, x_deltas):
            neighbour_coords = (cn + dx, ln + dy)

            if any([
                *[_ < 0 for _ in neighbour_coords],
                neighbour_coords[0] >= self.width,
                neighbour_coords[1] >= self.height,
                ]):
                continue
            else:
                neighbors.append((cn+dx, ln+dy))
        return neighbors

    def get_neighbors_val(self, ln, cn):
        neighbors = []
        y_deltas = [0, 0, -1, 1,]
        x_deltas = [-1, 1, 0, 0,]

        for dy, dx in zip(y_deltas, x_deltas):
            neighbour_coords = (cn + dx, ln + dy)

            if any([
                *[_ < 0 for _ in neighbour_coords],
                neighbour_coords[0] >= self.width,
                neighbour_coords[1] >= self.height,
                ]):
                continue
            else:
                neighbors.append(self.height_map[ln+dy][cn+dx])
        return neighbors

    def find_low_points(self):
        low_points = []
        for ln, line in enumerate(self.height_map):
            for cn, val in enumerate(line):
                neighbors = self.get_neighbors_val(ln, cn)
                if all([self.height_map[ln][cn] < _ for _ in neighbors]):
                    low_points.append((cn, ln))

        return low_points

    def show_answer(self):
        out = 0
        for cn, ln in self.find_low_points():
            out += self.height_map[ln][cn] + 1

        print(out)


class Part2Basin(SmokeBasin):
    def __init__(self):
        super().__init__()

    def end_of_input(self):
        super(Part2Basin, self).end_of_input()
        for l in self.height_map:
            l.insert(0, 9)
            l.append(9)

        line_of_nines = [9] * (self.width + 2)

        self.height_map.insert(0,line_of_nines)
        self.height_map.append(line_of_nines)

        self.height = len(self.height_map)
        self.width =  len(self.height_map[0])


    def get_cell(self, cn, ln):
        return self.height_map[ln][cn]
    
    def set_cell(self, cn, ln, val):
        self.height_map[ln][cn] = val

    def find_basin_area(self, cn, ln):
        if self.get_cell(cn, ln) == 9:
            return 0

        self.set_cell(cn, ln, 9)

        return 1 + sum([self.find_basin_area(cn_neigh, ln_neigh) for cn_neigh, ln_neigh in self.get_neighbors_coord(ln, cn)])


    def show_answer(self):
        coords =  self.find_low_points()


        # for cn, ln in coords:
        #     area = self.find_basin_area(cn, ln)
    
    
        basins_areas = sorted([self.find_basin_area(cn, ln) for cn, ln in coords])
        
        
        print(basins_areas[-3]*basins_areas[-2]*basins_areas[-1])


def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_9/input{debug}.txt'

    basin = SmokeBasin()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            basin.add_line(l)
        basin.end_of_input()

    basin.show_answer()
    # print(output)




def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_9/input{debug}.txt'

    basin = Part2Basin()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            basin.add_line(l)
        basin.end_of_input()

    basin.show_answer()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



