from lattice import Lattice

class CavernNetwork():
    def __init__(self, width, height, lattice_dimensions):
        self.lattices = []
        self.unvisited = []
        self.visited = []
        self.width = width
        self.height = height
        self.fringe = []
        self.initialize_lattices(lattice_dimensions)

    def __iter__(self):
        yield from self.lattices

    def set_start_node(self, node):
        self.start_node = node
    
    def set_end_node(self, node):
        self.end_node = node

    def initialize_lattices(self, lattice_dimensions):
        previous_row = []
        current_row = []

        for row in range(self.height):
            current_row = []
            left_lattice = None
            for col in range(self.width):
                lattice = Lattice(complex(col, row), self, *lattice_dimensions)

                self.lattices.append(lattice)

                current_row.append(lattice)
                if left_lattice:
                    lattice.connect(left_lattice, "left")
                left_lattice = lattice


            if previous_row:
                for p, c in zip(previous_row, current_row):
                    p.connect(c, "bot")
            previous_row = current_row


    def parse(self, f):

        for line in f.readlines():
            line = line.strip()

            for risk_level in line:
                for lattice in self:
                    lattice.add_chiton(int(risk_level))


        for lattice in self:
            lattice.connect_all_chitons()
            for chiton in lattice:
                self.unvisited.append(chiton)


    def pick_lowest_weight(self):
        lowest = min(self.fringe, key=lambda x: x.cost_to_node + x.get_heuristic_value())

        return lowest

    def run_dijkstra(self):
        """Dijkstra algo"""
        while self.end_node not in self.visited:
            current_node = self.pick_lowest_weight()

            # self.unvisited.remove(current_node)
            self.fringe.remove(current_node)
            self.visited.append(current_node)

            for neighbor in current_node.neighbors:
                if (current_node.cost_to_node + current_node.risk_level) < neighbor.cost_to_node:
                    neighbor.cost_to_node = current_node.cost_to_node + current_node.risk_level
                    neighbor.parent_node = current_node
                if neighbor not in self.fringe and neighbor not in self.visited:
                    self.fringe.append(neighbor)


    def show_answer_p2(self):
        self.fringe.append(self.start_node)
        self.run_dijkstra()
        total_path_cost = self.end_node.cost_to_node + self.end_node.risk_level - self.start_node.risk_level
        print(total_path_cost)
