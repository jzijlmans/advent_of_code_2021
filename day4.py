filename = "C:/Users/jeroe/PycharmProjects/advent_of_code_2021/input_files/day4.txt"

class Board:
    def __init__(self):
        self.unmarked_numbers = []
        self.number_pos = {}
        self.crossed_off_in_rows = [0,0,0,0,0]
        self.crossed_off_in_colums = [0,0,0,0,0]
        self.bingoed = False

    def add_number(self, number, i, j):
        self.number_pos[number] = (i,j)
        self.unmarked_numbers.append(int(number))

    def check_number(self,number):
        pos = self.number_pos.get(number)
        if pos:
            self.unmarked_numbers.remove(int(number))
            self.crossed_off_in_rows[pos[0]] += 1
            self.crossed_off_in_colums[pos[1]] += 1
            self.bingoed = self.crossed_off_in_rows[pos[0]]==5 or self.crossed_off_in_colums[pos[1]]==5
            return self.bingoed

def run_bingo_till_winner(trekkingen, boards):
    for called_num in trekkingen:
        for board in boards:
            bingo = board.check_number(called_num)
            if bingo:
                return board, called_num

def run_bingo_till_loser(trekkingen, boards):
    for called_num in trekkingen:
        for board in boards:
            board.check_number(called_num)
        if len(boards) > 1:
            boards = [board for board in boards if not board.bingoed]
        elif boards[0].bingoed:
            return boards[0], called_num

def read_input(filename):
    with open(filename) as f:
        trekkingen = f.readline().rstrip().split(',')

        boards=[]
        while True:
            next_line = f.readline()
            if next_line:
                board = Board()
                for i in range(5):
                    line = f.readline().rstrip()
                    line_list = line.split()
                    for j in range(5):
                        board.add_number(line_list[j],i,j)
                boards.append(board)
            else:
                break
    return trekkingen, boards

trekkingen, boards = read_input(filename)

board, called_num = run_bingo_till_winner(trekkingen, boards)
print('assignment1: ' + str(sum(board.unmarked_numbers) * int(called_num)))

trekkingen, boards = read_input(filename)
board, called_num = run_bingo_till_loser(trekkingen, boards)
print('assignment2: ' + str(sum(board.unmarked_numbers) * int(called_num)))