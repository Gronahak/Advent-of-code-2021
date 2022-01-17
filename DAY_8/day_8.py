from collections import defaultdict

DEBUG_MODE = False
# DEBUG_MODE = True


def compute_similarity(w1: str, w2: str) -> int:
    """Compute similarity between two alphavetically sorted strings
    
    """
    s = 0
    for l in w1:
        if l in w2:
            s += 1
    return s


CANONICAL_DIGITS = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}
compute_similarity(CANONICAL_DIGITS[5], CANONICAL_DIGITS[2])
compute_similarity(CANONICAL_DIGITS[5], CANONICAL_DIGITS[3])
compute_similarity(CANONICAL_DIGITS[3], CANONICAL_DIGITS[2])

class DigitsScanner():
    def __init__(self):
        self.count = 0
    def process_line_p1(self, line):
        _, right_side = line.split(" | ")
        words = right_side.split(" ")

        for w in words:
            if len(w) in [2, 4, 3, 7]:
                self.count += 1
  
    def process_line_p2(self, line):
        left_side, right_side = line.split(" | ")
        _input, _output = (side.split(" ") for side in [left_side, right_side])

        unk = defaultdict(list)  # dict of digits yet to be found key= len
        known = {}  # dict of digits already found   ex : "7" : "bce"

        correspondance = {}  # dict of corresponding segments ex: "A": "f"

        for w in _input:
            word_length = len(w)
            if word_length in [2, 4, 3, 7]:
                if word_length == 2:
                    known[1] = ''.join(sorted(w))
                if word_length == 4:
                    known[4] = ''.join(sorted(w))
                if word_length == 3:
                    known[7] = ''.join(sorted(w))
                if word_length == 7:
                    known[8] = ''.join(sorted(w))
            else:
                unk[word_length].append(w)


        # Find "A" segment:
        for l in known[7]:
            if l not in known[1]:
                correspondance["A"] = l

        # Identify words for 5 and 2:

        min_similarity = 8
        five_and_two = []
        for w1 in unk[5]:
            for w2 in unk[5]:
                if w2 <= w1:
                    continue

                s = compute_similarity(w1, w2)
                if s < min_similarity:
                    min_similarity = s
                    five_and_two = [w1, w2]

        # We then identify word for 3:
        for w in unk[5]:
            if w not in five_and_two:
                known[3] = ''.join(sorted(w))

        # Find "B" segment:
        for l in known[4]:
            if l not in known[3]:
                correspondance["B"] = l

        # Identify words for 5 and 2 for real:

        min_similarity = 8
        word_two = ""
        for w1 in five_and_two:
            s = compute_similarity(w1, known[4])
            if s < min_similarity:
                min_similarity = s
                word_two = w1

        known[2] = ''.join(sorted(word_two))
        five_and_two.remove(word_two)
        known[5] = ''.join(sorted(five_and_two[0]))


        # Find "C" segment:
        for l in known[4]:
            if l not in known[5]:
                correspondance["C"] = l

        # Identify word for 6:

        for w in unk[6]:
            if correspondance['C'] not in w:
                known[6] = ''.join(sorted(w))

        unk[6] = [''.join(sorted(w)) for w in unk[6]]

        unk[6].remove(known[6])


        # identify word for 0
        for w in unk[6]:
            for l in known[3]:
                if l not in w:
                    known[0] = ''.join(sorted(w))

        unk[6].remove(known[0])
        known[9] = ''.join(sorted(unk[6][0]))

        # Find "D" segment:
        
        for l in known[8]:
            if l not in known[0]:
                correspondance["D"] = l
    
        # Find "E" segment:
        
        for l in known[6]:
            if l not in known[5]:
                correspondance["E"] = l

        # Find "F" segment:
        
        for l in known[3]:
            if l not in known[2]:
                correspondance["F"] = l


        # Find "G" segment:

        last = list("abcdefg")
        for l in correspondance.values():
            last.remove(l)
        correspondance["G"] = last[0]

        reverse = {v: k for k, v in correspondance.items()}

        reverse_digits = {v: k for k, v in known.items()}

        line_output = ""
        for word in _output:
            sorted_w = ''.join(sorted(word))
            d = reverse_digits[sorted_w]
            line_output += str(d)
        
        self.count += int(line_output)

    def show_answer(self):
        print(self.count)


def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_8/input{debug}.txt'

    ds = DigitsScanner()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            ds.process_line_p1(l.strip())

    ds.show_answer()




def part_2():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_8/input{debug}.txt'

    ds = DigitsScanner()

    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            ds.process_line_p2(l.strip())

    ds.show_answer()

RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()

