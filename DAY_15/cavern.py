from chiton import Chiton

class Cavern:
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.unvisited = []
        self.visited = []

    def parse(self, f):
        previous_row = []
        for l in f.readlines():
            previous_chiton = None
            current_row = []
            l = l.strip()

            for risk_level in l:
                c = Chiton(int(risk_level), self)
                current_row.append(c)
                self.unvisited.append(c)

                if previous_chiton:
                    c.connect(previous_chiton)
                previous_chiton = c

            if previous_row:
                for above, below in zip(previous_row, current_row):
                    above.connect(below)
            
            previous_row = current_row
        c.status = NodeStatus.END
        self.end_node = c

    def pick_lowest_weight(self):
        lowest_weight = float("inf")
        lowest_node = None
        
        for node in self.unvisited:
            if node.cost_to_node < lowest_weight:
                lowest_weight = node.cost_to_node
                lowest_node = node

        return lowest_node

    def run_dijkstra(self):
        """Dijkstra algo"""
        while self.end_node not in self.visited:
            current_node = self.pick_lowest_weight()

            self.unvisited.remove(current_node)
            self.visited.append(current_node)

            for neighbor in current_node.neighbors:
                if (current_node.cost_to_node + current_node.risk_level) < neighbor.cost_to_node:
                    neighbor.cost_to_node = current_node.cost_to_node + current_node.risk_level
                    neighbor.parent_node = current_node


    def show_answer_p1(self):
        self.run_dijkstra()
        total_path_cost = self.end_node.cost_to_node + self.end_node.risk_level - self.start_node.risk_level
        print(total_path_cost)