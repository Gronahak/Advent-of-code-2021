
from distutils.dir_util import copy_tree
import matplotlib.pyplot as plt

DEBUG_MODE = False
# DEBUG_MODE = True

class Origami():
    def __init__(self):
        self.dots = set()
        self.fold_instructions = []

    def parse(self, f):
        reading_dots = True
        for l in f.readlines():
            l = l.strip()
            if l == "":
                reading_dots = False
                continue
            if reading_dots:
                re, im = l.split(",")
                self.dots.add(complex(int(re),int(im)))
            else:
                self.fold_instructions.append(l.split(" ")[2])

    def do_fold(self, instruction):
        direction, distance = instruction.split("=")
        distance = int(distance)
        marked_for_removal = []
        marked_for_addition = []
        for n in self.dots:
            if direction == "y":
                to_check = n.imag
            if direction == "x":
                to_check = n.real

            if to_check > distance:
                if direction == "y":
                    new_x, new_y = n.real, n.imag - 2*(n.imag-distance)
                if direction == "x":
                    new_x, new_y = n.real - 2*(n.real-distance), n.imag
                
                symetric = complex(new_x, new_y)
                
                marked_for_addition.append(symetric)
                marked_for_removal.append(n)


        for n in marked_for_removal:
            self.dots.remove(n)

        for n in marked_for_addition:
            self.dots.add(n)


    def show_answer_p1(self):
        self.do_fold(self.fold_instructions[0])
        print(len(self.dots))

    def show_answer_p2(self):
        for i in self.fold_instructions:
            self.do_fold(i)

        # extract real part
        x = [ele.real for ele in self.dots]
        # extract imaginary part
        y = [-ele.imag for ele in self.dots]
        
        # plot the complex numbers
        plt.scatter(x, y)
        plt.ylabel('Imaginary')
        plt.xlabel('Real')
        plt.show()



def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_13/input{debug}.txt'

    origami = Origami()

    with open(path_to_file, 'r') as f:
        origami.parse(f)
        
    origami.show_answer_p1()


def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_13/input{debug}.txt'

    origami = Origami()

    with open(path_to_file, 'r') as f:
        origami.parse(f)
        
    origami.show_answer_p2()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



