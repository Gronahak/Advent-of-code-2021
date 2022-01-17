
DEBUG_MODE = False
# DEBUG_MODE = True


class OctoGrid():
    def __init__(self):
        self.octopuses_list = []
        self.boundaries = {
            "top": 0,
            "bot": 0,
            "left": 0,
            "right": 0
        }

        self.to_flash = []
        self.flashed = []

        self.n_flashes = 0

        self.step = 0

    def __repr__(self):
        out = ""
        for i, o in enumerate(self.octopuses_list):
            out += str(o)
            if i % self.boundaries["right"] == 0:
                out += "\n"

        return out


    def add_octo(self, octo):
        self.octopuses_list.append(octo)
        if octo.ri > self.boundaries["bot"]:
            self.boundaries["bot"] = octo.ri
        
        if octo.ci > self.boundaries["right"]:
            self.boundaries["right"] = octo.ci

    def reset(self):
        self.to_flash = []
        self.flashed = []
        for o in self.octopuses_list:
            o.reset()


    def incoming_flash(self, octo):
        self.n_flashes += 1
        self.flashed.append(octo)

        for other in octo.get_neighbours():
            other.charge_up()


    def take_step(self):
        self.step += 1
        self.reset()
        
        for o in self.octopuses_list:
            o.charge_up()

        if len(self.flashed) == len(self.octopuses_list):
            print(self.step)
            raise StopIteration

    def show_answer(self):
        print(self.n_flashes)

    def end_of_input(self):
        self.width = self.boundaries["right"]+1
        self.height = self.boundaries["bot"]+1

    def get_octo_at(self, nx, ny):
        if any([
            nx < self.boundaries["left"],
            ny < self.boundaries["top"],
            nx > self.boundaries["right"],
            ny > self.boundaries["bot"],
        ]):
            return None

        return self.octopuses_list[nx + self.width * ny]


class Octopus():
    def __init__(self, ci, ri, nrj_lvl, grid):
        self.ci = ci
        self.ri = ri
        self.nrj_lvl = nrj_lvl
        self.grid = grid
        self.tired = False

    def __repr__(self):
        return str(self.nrj_lvl)

    def reset(self):
        if self.tired:
            self.tired = False
            self.nrj_lvl = 0

    def charge_up(self):
        if self.tired:
            return

        self.nrj_lvl += 1

        if self.nrj_lvl > 9:
            self.flash()

    def get_neighbours(self):
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]

        neighbours = []

        for x in dx:
            for y in dy:
                if x == y == 0:
                    continue
                nx, ny = self.ci + x, self.ri + y
                octo = self.grid.get_octo_at(nx, ny)
                if octo:
                    neighbours.append(octo)

        return neighbours

    def flash(self):
        self.tired = True
        self.grid.incoming_flash(self)

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_11/input{debug}.txt'

    octo_grid = OctoGrid()

    with open(path_to_file, 'r') as f:
        for ri, l in enumerate(f.readlines()):
            for ci, n in enumerate(l.strip()):
                octo = Octopus(ci, ri, int(n), octo_grid)

                octo_grid.add_octo(octo)

    octo_grid.end_of_input()

    while True:
        octo_grid.take_step()

    octo_grid.show_answer()

def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_11/input{debug}.txt'

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
        



RUN_PART = part_1


if __name__ == "__main__":
    RUN_PART()



