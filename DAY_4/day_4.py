import numpy as np

class BingoBoard():
    winner_number = 1

    def get_winner_number():
        BingoBoard.winner_number += 1
        return BingoBoard.winner_number-1
    def __init__(self):

        shape = (5, 5)
        self.board = -np.ones((shape))
        # self.ticks = np.random.rand(5,5)
        self.ticks = np.zeros((shape))
        self.board_filler = self.populate_line()
        next(self.board_filler)
        self.winner_number = 0

    def __str__(self):
        out = ""
        for l in self.board:
            out += str(l)+'\n'

        return out

    def populate_line(self):
        line_idx = 0
        while line_idx < 5:
            new_line_rcv = yield
            new_line_split = " ".join(new_line_rcv.split())
            self.board[line_idx] = np.array([int(n) for n in new_line_split.split(" ")])
            line_idx += 1
            if line_idx == 5:
                break

    def check_number(self, number):
        pos = np.argwhere(self.board == number)
        # pos = np.where(self.board == number)
        
        for x, y in pos:
            self.ticks[x,y] = 1
            

    def winning_board(self, last_number):
        if self.winner_number != 0:
            return False

        if any(sum(c) == 5 for c in self.ticks):
            self.winner_number = BingoBoard.get_winner_number()
        elif any(sum(c) == 5 for c in self.ticks.transpose()):
            self.winner_number = BingoBoard.get_winner_number()
        
        if self.winner_number == last_number:
            return True

    def display_info_part1(self, number):
        pos = np.argwhere(self.ticks == 0)
        # pos = np.where(self.board == number)
        
        unmarked_sum = 0
        for x, y in pos:
            unmarked_sum += self.board[x,y]

        print(unmarked_sum*number)

def debug_bingo_bong():
    b = BingoBoard()
    print(b)

    b.board_filler.send("1 1 1 1 1")
    print(b)
    print(b.winning_board())

    b.check_number(1)

    print(b)
    print(b.winning_board())
    for c in b.ticks:
        print(c)

def part_1():
    debug = '_debug' if DEBUG_MODE else ''
    path_to_file = f'DAY_4/input{debug}.txt'


    numbers_drawn = []
    bingo_boards = []

    board = BingoBoard()

    with open(path_to_file, 'r') as f:
        for l in f:
            # print(l)

            if not numbers_drawn:
                numbers_drawn = [int(n) for n in l.split(',')]
            else:
                if l == '\n':
                    continue
                try:
                    board.board_filler.send(l.strip())
                except StopIteration:
                    bingo_boards.append(board)
                    board = BingoBoard()

    try:
        for number in numbers_drawn:
            for b in bingo_boards:
                b.check_number(number)
                if b.winning_board():
                    b.display_info_part1(number)
                    raise StopIteration
    except StopIteration:
        pass





def part_2():
    debug = '_debug' if DEBUG_MODE else ''
    path_to_file = f'DAY_4/input{debug}.txt'


    numbers_drawn = []
    bingo_boards = []

    board = BingoBoard()

    with open(path_to_file, 'r') as f:
        for l in f:
            # print(l)

            if not numbers_drawn:
                numbers_drawn = [int(n) for n in l.split(',')]
            else:
                if l == '\n':
                    continue
                try:
                    board.board_filler.send(l.strip())
                except StopIteration:
                    bingo_boards.append(board)
                    board = BingoBoard()

    try:
        for number in numbers_drawn:
            for b in bingo_boards:
                b.check_number(number)
                if b.winning_board(len(bingo_boards)):
                    b.display_info_part1(number)
                    raise StopIteration
    except StopIteration:
        pass



DEBUG_MODE = False

RUN_PART = part_2




if __name__ == "__main__":
    RUN_PART()
    # debug_bingo_bong()



