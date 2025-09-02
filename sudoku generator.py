import random


class Sudoku():

    def __init__(self, population_number: int):
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
        for index, row in enumerate(board):
            print(f"{index} : {row}")

    def generate_start_population(self):
        '''Generate start population with sudoku boards'''
        for i in range(self.population_number):
            sudoku_board = self._init_sudoku_random_board()
            self.population.append(sudoku_board)

    def evaluate_sudoku_board(self, board):
        board_score = 0

        row_score = self._evaluate_row(board)
        column_score = self._evaluate_column(board)
        matrix_score = self._evaluate_matrix3x3(board)
        board_score = row_score + column_score + matrix_score

        return board_score

    def _evaluate_row(self, board):
        rows_score = 0
        for row in board:
            start_row_score = 45
            current_row_score = sum(row)
            start_row_score -= current_row_score
            rows_score += abs(start_row_score)
        return rows_score

    def _evaluate_column(self, board):
        columns_score = 0
        transpose_list = list(map(list, zip(*board)))
        for row in transpose_list:
            start_row_score = 45
            current_row_score = sum(row)
            start_row_score -= current_row_score
            columns_score += abs(start_row_score)
        return columns_score

    def _evaluate_matrix3x3(self, board):

        matrix_score = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                start_matrix_score = 45
                row1 = board[i][j: j + 3]
                row2 = board[i + 1][j: j + 3]
                row3 = board[i + 2][j: j + 3]
                current_matrix_score = sum(row1) + sum(row2) + sum(row3)
                start_matrix_score -= current_matrix_score
                matrix_score += abs(start_matrix_score)
                row1, row2, row3, start_matrix_score, current_matrix_score
        return matrix_score

    def selection(self):

        for i in range(self.population_number//2):
            board1 = self.population[i]
            board2 = self.population[i + self.population_number//2]
            board1_score = self.evaluate_sudoku_board(board1)
            board2_score = self.evaluate_sudoku_board(board2)
            print("="* 40)
            self.print_board(board1)
            print(board1_score)
            print("=" * 40)
            self.print_board(board2)
            print(board2_score)

            if board1_score > board2_score:
                self.population[i] = board2
            else:
                self.population[i] = board1

        random.shuffle(self.population)
        print("+"* 45)
        for board in self.population:
            print("")
            self.print_board(board)


sudoku = Sudoku(4)
sudoku.generate_start_population()
sudoku.selection()
# sudoku.evaluate_sudoku_board(sudoku.population[0])
# print('*' * 40)
# sudoku.evaluate_sudoku_board(sudoku.population[0])
# print('*' * 40)
# for i in range(2):
#     sudoku.print_board(sudoku.population[i])
#     print("-" * 30)
