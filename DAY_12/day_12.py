
from enum import Enum, auto


DEBUG_MODE = False
# DEBUG_MODE = True

class CaveType(Enum):
    BIGCAVE = auto()
    SMALLCAVE = auto()

class Cell():

    def __init__(self, name):
        self.name = name
        if name.isupper():
            self.type = CaveType.BIGCAVE
        else:
            self.type = CaveType.SMALLCAVE

        self.neighbors = []

    def connect(self, other):
        self.neighbors.append(other)
        other.neighbors.append(self)

    def __repr__(self):
        return self.name




class Cave():
    def __init__(self):
        self.cells = {}
        self.paths = set()

    def parse(self, line):
        left, right = line.split("-")
        c1 = self.cells.get(left, Cell(name=left))
        c2 = self.cells.get(right, Cell(name=right))

        if left not in self.cells:
            self.cells[left] = c1
        
        if right not in self.cells:
            self.cells[right] = c2

        

        c1.connect(c2)
        pass

    def bfs_p1(self, current_node=None, end_node=None, path_so_far="start"):
        if current_node is None:
            current_node =  self.cells.get("start")
        if end_node is None:
            end_node = self.cells.get("end")

        if current_node == end_node:
            self.paths.add(path_so_far)
            return

        to_explore = []

        for n in current_node.neighbors:
            nodes_in_path = path_so_far.split(",")
            if n.type == CaveType.SMALLCAVE and str(n) in nodes_in_path:
                continue
            to_explore.append(n)

        for n in to_explore:
            self.bfs_p1(n, end_node, path_so_far+f',{str(n)}')


    def bfs_p2(self, current_node=None, end_node=None, path_so_far=None, can_revisit=True):
        if current_node is None:
            current_node =  self.cells.get("start")
        if end_node is None:
            end_node = self.cells.get("end")
        if path_so_far is None:
            path_so_far = [self.cells.get("start")]

        if current_node == end_node:
            self.paths.add( ",".join([str(n) for n in path_so_far]))
            return


        for n in current_node.neighbors:
            if n == self.cells.get("start"):
                continue
            if n.type == CaveType.SMALLCAVE and n in path_so_far:
                if not can_revisit:
                    continue
                else:
                    self.bfs_p2(n, end_node, path_so_far+[n], can_revisit=False)
            else:
                self.bfs_p2(n, end_node, path_so_far+[n], can_revisit)


    def bfs_old(self, current_node, end_node, path_so_far):
        for c in current_node.neighbors:
            if c == end_node:
                self.paths.add(','.join(cell.name for cell in path_so_far))
                return
            elif c.type == CaveType.SMALLCAVE:
                if c in path_so_far:
                    continue
            
            path_so_far.append(c)
            self.bfs_p1(c, end_node, path_so_far)


    def show_answer_p1(self):
        self.bfs_p1()
        print(len(self.paths))
    
    def show_answer_p2(self):
        self.bfs_p2()
        print(len(self.paths))


def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_12/input{debug}.txt'

    c = Cave()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            c.parse(l)

    c.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_12/input{debug}.txt'

    c = Cave()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            c.parse(l)

    c.show_answer_p2()




RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



