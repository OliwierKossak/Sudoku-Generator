import random


# init_sudoku_board = [[0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0],
#                      [0,0,0,0,0,0,0,0,0]]

class Sudoku():
    def __init__(self):
        self.start_board = []

    def _init_sudoku_random_board(self):
        '''Generates a starting board with randomly mixed numbers'''
        for i in range(9):
            sudoku_numbers = [i for i in range(1, 10)]
            random.shuffle(sudoku_numbers)
            self.start_board.append(sudoku_numbers)


sudoku = Sudoku()
sudoku._init_sudoku_random_board()
print(sudoku.start_board)
