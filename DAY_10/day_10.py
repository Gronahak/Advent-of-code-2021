
DEBUG_MODE = False
# DEBUG_MODE = True

class InputChecker():
    def __init__(self):
        self.stack = []
        self.score = 0
        self.lines = {
            "ok": [],
            "corrupted": [],
            "incomplete": []
        }

    def closing_char(self, char):
        return char in ['>', ')', ']', '}']

    def matches_opener(self, opener, char):
        correspondance = {
            '(' : ')',
            '<' : '>',
            '[' : ']',
            '{' : '}',
        }
        return correspondance[opener] == char

    def get_score(self, c):
        score = {
            ')' : 3,
            ']' : 57,
            '}' : 1197,
            '>' : 25137,
        }
        return score[c]

    def check_line(self, line):
        self.stack = []
        for i, c in enumerate(line):
            if self.closing_char(c):
                if self.matches_opener(self.stack[-1], c):
                    self.stack.pop()
                else:
                    self.score += self.get_score(c)
                    self.lines["corrupted"].append(line[:i+1])
                    return
            
            else:
                self.stack.append(c)
        if len(self.stack) == 0:
            self.lines["ok"].append(line)
        else:
            self.lines["incomplete"].append("".join(self.stack))



        
    def show_answer(self):
        print(self.score)


    def get_part_2_answer(self):
        scores = []
        table = {
            "(": 1,
            "[": 2,
            "{": 3,
            "<": 4
        }
        for line in self.lines["incomplete"]:
            score = 0
            for ch in reversed(line):
                score *= 5
                score += table[ch]
            scores.append(score)

        print(sorted(scores)[len(scores)//2] )

def part_1():
    debug = '_debug_part1' if DEBUG_MODE else ''
    path_to_file = f'DAY_10/input{debug}.txt'


    ic = InputChecker()
    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            ic.check_line(l)


    ic.show_answer()



def part_2():
    # ans < 27719333539
    debug = '_debug_part2' if DEBUG_MODE else ''
    path_to_file = f'DAY_10/input{debug}.txt'


    ic = InputChecker()
    with open(path_to_file, 'r') as f:
        for l in f.readlines():
            l = l.strip()
            ic.check_line(l)


    ic.get_part_2_answer()



RUN_PART = part_2


if __name__ == "__main__":
    RUN_PART()



