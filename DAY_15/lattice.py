from chiton import Chiton

class Lattice():
    def __init__(self, pos: complex, network, width, height):
        self.network = network
        self.width = width
        self.height = height
        self.chitons = []
        for _ in range(self.height):
            new_row = []
            for _ in range(self.width):
                new_row.append(None)
            self.chitons.append(new_row)
        self.pos = pos
        self.next_chiton_pos = {
            "row": 0,
            "col": 0
        }
        self.interfaces = {
            "top": [],
            "bot": [],
            "left": [],
            "right": [],
        }

        self.neighbors = []
        self.directions = []

    def connect(self, other, direction):
        self.neighbors.append(other)
        self.directions.append(direction)
        # other.neighbors.append(self)

    def __repr__(self):
        out = ""
        for i, el in enumerate(self.chitons):
            out += str(el)
            if (i+1)%self.width == 0:
                out += "\n"
            else:
                out += ""

        return out

    def __iter__(self):
        for row in self.chitons:
            for chiton in row:
                yield chiton

    def add_chiton(self, base_value):
        r, c = self.next_chiton_pos.values()
        adjusted_value = (base_value + self.pos.imag +self.pos.real)%9



        if adjusted_value == 0:
            adjusted_value = 9
        chiton = Chiton(adjusted_value, self, r, c)
        if self.pos == 0 and r == c == 0:
            self.network.set_start_node(chiton)
        if self.pos == complex(self.network.width-1, self.network.height-1) and r == self.height-1 and c == self.width-1:
            self.network.set_end_node(chiton)
        self.chitons[r][c] = chiton

        if r == 0:
            self.interfaces["top"].append(chiton)
        if r == self.height-1:
            self.interfaces["bot"].append(chiton)
        if c == 0:
            self.interfaces["left"].append(chiton)
        if c == self.width-1:
            self.interfaces["right"].append(chiton)

        c += 1
        if c == c == self.width:
            c = 0
            r += 1

        self.next_chiton_pos["row"] = r
        self.next_chiton_pos["col"] = c

        # if r == 100:  # The last Chiton of the lattice has just been added
        #     self.connect_inner_chitons()

    def connect_inner_chitons(self):
        for line in self.chitons:
            for c1, c2 in zip(line[:-1], line[1:]):
                if c1 != c2:
                    c1.connect(c2)

        for l1, l2 in zip(self.chitons[:-1], self.chitons[1:]):
            for c1, c2 in zip(l1, l2):
                if c1 != c2:
                    c1.connect(c2)

    def connect_border_chitons(self, other, my_side):
        correspondance = {
            "left": "right",
            "right": "left",
            "top": "bot",
            "bot": "top",
        }
        other_side = correspondance[my_side]

        for c1, c2 in zip(self.interfaces[my_side], other.interfaces[other_side]):
            if c1 not in c2.neighbors:
                c1.connect(c2)

    def connect_all_chitons(self):
        self.connect_inner_chitons()
        for neighbor, direction in zip(self.neighbors, self.directions):
            self.connect_border_chitons(neighbor, direction)