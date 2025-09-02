import random

class Sudoku():
    def __init__(self,population_number: int):
        self.population_number = population_number
        self.population = []
    def _init_sudoku_random_board(self):
        start_board = []
        '''Generates a starting board with randomly mixed numbers'''
        for i in range(9):
            sudoku_numbers = [i for i in range(1, 10)]
            random.shuffle(sudoku_numbers)
            start_board.append(sudoku_numbers)
        return start_board

    def print_board(self, board):
        '''Print sudoku board'''
        for index, row in enumerate(board,1):
            print(f"{index} : {row}")

    def generate_start_population(self):
        for i in range(self.population_number):
            sudoku_board = self._init_sudoku_random_board()
            self.population.append(sudoku_board)



sudoku = Sudoku(2)
sudoku.generate_start_population()
for i in range(2):
    sudoku.print_board(sudoku.population[i])
    print("-"*30)
