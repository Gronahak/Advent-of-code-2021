
from calendar import c
import math


class SnailfishAdder():
    def __init__(self):
        self.lr = None
        self.numbers = []

    def parse(self, f):
        first = True

        for l in f.readlines():
            l = l.strip()
            if first:
                first = False
                self.lr = ListRepresentation().parse_from_string(l)

            else:
                self.lr += ListRepresentation().parse_from_string(l)

            self.lr.reduce()

        # self.lr = lr
    def parse_p2(self, f):
        for l in f.readlines():
            l = l.strip()
            self.numbers.append(ListRepresentation().parse_from_string(l))


    def show_answer_p1(self):
        print(self.lr.compute_amplitude())

    def show_answer_p2(self):
        max_amplitude = 0
        for n1 in self.numbers[:-1]:
            for n2 in self.numbers[1:]:
                left_plus_right = n1+n2
                left_plus_right.reduce()
                amplitude = left_plus_right.compute_amplitude()

                if amplitude > max_amplitude:
                    max_amplitude = amplitude
        
                right_plus_left = n2+n1
                right_plus_left.reduce()
                amplitude = right_plus_left.compute_amplitude()


                if amplitude > max_amplitude:
                    max_amplitude = amplitude

        print(max_amplitude)
    

class ListRepresentation():
    def __init__(self, numbers=None, nesting_level=None):
        self.numbers = []
        self.nesting_level = []
        if numbers:
            self.numbers = numbers.copy()
        if nesting_level:
            self.nesting_level = nesting_level.copy()

    def compute_amplitude(self):
        def do_step():
            for i in range(len(self.nesting_level[:-1])):
                if self.nesting_level[i] == self.nesting_level[i+1]:
                    self.numbers[i] = 3*self.numbers[i] + 2*self.numbers[i+1]
                    self.nesting_level[i] -= 1
                    self.numbers.pop(i+1)
                    self.nesting_level.pop(i+1)
                    break

        while len(self.numbers) > 1:
            do_step()
        return self.numbers[0]

    def parse_from_string(self, string):
        nesting_level = 0
        for char in string:
            if char == ',':
                continue
            elif char == '[':
                nesting_level += 1
            elif char == ']':
                nesting_level -= 1
            else:
                self.numbers.append(int(char))
                self.nesting_level.append(nesting_level)
        return self
    
    def reduce(self):
        result = self.reduce_step()

        while result is not None:
            result = self.reduce_step()

    def __str__(self):
        return ",".join([str(i) for i in self.numbers])


    # def __str__(self):
    #     out = ""
    #     stack = []
    #     last_level = -1
    #     coma = ","
    #     current_level = 0
    #     first = True

    #     for number, level in zip(self.numbers, self.nesting_level):
    #         if first:
    #             first = False
    #             out += "["*level
    #             last_level = level
    #         if level > last_level:
    #             out += coma
    #             out += "["*level

    #         if level == last_level:
    #             out += coma
    #             out += str(number)


    def reduce_step(self):
        cause = None
        for i, pair in enumerate(zip(self.numbers, self.nesting_level)):
            number, nesting_level = pair
            if nesting_level == 5:
                left_index, left_number = i, number
                right_index, right_number = i+1, self.numbers[i+1]
                cause = "explode"
                break
        if not cause:
            for i, pair in enumerate(zip(self.numbers, self.nesting_level)):
                if pair[0] >= 10:
                    number = pair[0]
                    cause = "split"
                    break

        if cause == "explode":
            if left_index > 0:
                self.numbers[left_index-1] += left_number
            if right_index < len(self.numbers)-1:
                self.numbers[right_index+1] += right_number

            self.numbers[left_index] = 0
            self.nesting_level[left_index] -= 1

            self.numbers.pop(right_index)
            self.nesting_level.pop(right_index)

        elif cause == "split":
            self.numbers[i] = number//2
            self.numbers.insert(i+1, math.ceil(number/2))

            self.nesting_level[i] += 1
            self.nesting_level.insert(i+1, self.nesting_level[i])

        return cause

    def to_snail_fish_number(self):
        return SnailfishNumber.parse_from_string(str(self))

    def __add__(self, other):
        return ListRepresentation(self.numbers+other.numbers, [i+1 for i in self.nesting_level+other.nesting_level])

class SnailfishNumber:
    def __init__(self, left, right):
        self.left = left
        self.right = right



    def parse_from_string(string):
        inner_string = string[1:-1]
        if string.count(",") == 1:
            return SnailfishNumber(*map(int, inner_string.split(",")))

        bracket_count = {
            "[": 0,
            "]": 0,
        }

        for pos, char in enumerate(inner_string):
            if char in bracket_count:
                bracket_count[char] += 1
            if char == "," and bracket_count["["] == bracket_count["]"]:
                return SnailfishNumber(inner_string[:pos], inner_string[pos+1:])

    def __repr__(self):
        return f"[{str(self.left)},{str(self.right)}]"

    def reduce(self):
        pass

    def __add__(self, other):
        return SnailfishNumber(self, other).reduce()

if __name__ == "__main__":
    l = "[1,2]"
    l = "[9,8]"
    l = "[[9,6],2]"
    l = "[5,[[[7,5],[4,5]],[0,2]]]"

    left = '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]'
    right = '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'

    lft = ListRepresentation().parse_from_string(left)
    rgt = ListRepresentation().parse_from_string(right)

    tot = lft + rgt
    tot.reduce()

    print(tot.numbers)