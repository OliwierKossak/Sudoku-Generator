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
        '''Generate start population with sudoku boards'''
        for i in range(self.population_number):
            sudoku_board = self._init_sudoku_random_board()
            self.population.append(sudoku_board)

    def evaluate_sudoku_board(self, board):
        board_score = 0
        print(self._evalute_row(board))
        print(self._evalute_column(board))

    def _evalute_row(self, board):
        rows_score = 0
        for row in board:
            start_row_score = 45
            current_row_score = sum(row)
            start_row_score -= current_row_score
            rows_score += abs(start_row_score)
        return rows_score

    def _evalute_column(self, board):
        columns_score = 0
        transpose_list = list(map(list,zip(*board)))
        for row in transpose_list:
            start_row_score = 45
            current_row_score = sum(row)
            start_row_score -= current_row_score
            columns_score += abs(start_row_score)
        return columns_score

sudoku = Sudoku(2)
sudoku.generate_start_population()
sudoku.evaluate_sudoku_board(sudoku.population[1])
for i in range(2):
    sudoku.print_board(sudoku.population[i])
    print("-"*30)
