from collections import defaultdict

DEBUG_MODE = False
# DEBUG_MODE = True

class PolymerParser():
    def __init__(self):
        self.polymer_string = ""
        self.rules = {}

    def parse(self, f):
        first = True
        for l in f.readlines():
            l = l.strip()
            
            if l == "":
                continue
            
            if first:
                first = False
                self.polymer_string = l

            else:
                left, right = l.split(" -> ")
                self.rules[left] = right

    def make_step(self):
        next_string = self.polymer_string[0]
        for a,b in zip(self.polymer_string[:-1], self.polymer_string[1:]):
            new_char = self.rules.get(a+b, "")
            next_string += new_char
            next_string += b

        self.polymer_string = next_string

    def initialize_pair_dict(self):
        self.pair_dict = defaultdict(int)
        for a,b in zip(self.polymer_string[:-1], self.polymer_string[1:]):
            self.pair_dict[a+b] += 1
    
    def initialize_char_dict(self):
        self.char_dict = defaultdict(int)
        for c in self.polymer_string:
            self.char_dict[c] += 1

    def make_step_p2(self):
        next_dict = defaultdict(int)
        for pair, n_occ in self.pair_dict.items():
            new_char = self.rules[pair]
            prefix, suffix = pair
            next_dict[prefix+new_char] += n_occ
            next_dict[new_char+suffix] += n_occ
            self.char_dict[new_char] += n_occ


        self.pair_dict = next_dict


    def show_answer_p1(self):
        counter = defaultdict(int)

        for _ in range(10):
            self.make_step()

        for l in self.polymer_string:
            counter[l] += 1

        print(max(counter.values()) - min(counter.values()))


    def show_answer_p2(self):
        
        self.initialize_pair_dict()
        self.initialize_char_dict()
        for _ in range(40):
            self.make_step_p2()

        print(max(self.char_dict.values()) - min(self.char_dict.values()))

        

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_14/input{debug}.txt'

    pp = PolymerParser()

    with open(path_to_file, 'r') as f:
        pp.parse(f)

    pp.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_14/input{debug}.txt'

    pp = PolymerParser()

    with open(path_to_file, 'r') as f:
        pp.parse(f)
        
    pp.show_answer_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



