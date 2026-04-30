# Add Files/Modules
from source.back_end.interactors.config import *
from random import Random

class Sudoku:
    # Data Attributes
    __current_cell = None
    __note_active = None
    __solved_sudoku_grid = []
    __builder_sudoku = []
    __unsolved_sudoku_grid = []
    __numbers_removed = -1
    __difficulty = None

    # Init
    def __init__(self):
        self.set_current_cell(None)
        self.set_note_active(False)
        self.set_solved_sudoku_grid([])
        self.set_builder_sudoku(BLANK_SUDOKU)
        self.set_unsolved_sudoku_grid([])
        self.set_numbers_removed(-1)
        self.set_difficulty("easy")

    # Helpers
    def generate_random_board(self):
        pass

    def generate_solved_puzzle(self):
        pass

    def remove_numbers(self):
        pass

    # This checks to see if the numbers in the row do not validate sudoku
    def row_check(self, row):
        check_array = []
        for numbers in self.get_builder_sudoku()[row]:
            if numbers not in check_array:
                check_array.append(numbers)
            else:
                return False # Does not validate sudoku
        return True

    # This checks to see if the numbers in the column do not validate sudoku
    def column_check(self, column):
        check_array = []
        for rows in self.get_builder_sudoku():
            if rows[column] not in check_array:
                check_array.append(rows[column])
            else:
                return False  # Does not validate sudoku
        return True

    # This checks to see if the numbers in the subgrid do not validate sudoku
    def sub_grid_check(self, row, column):
        pass

    # Getters
    def get_current_cell(self):
        return self.__current_cell

    def get_note_active(self):
        return self.__note_active

    def get_solved_sudoku_grid(self):
        return self.__solved_sudoku_grid

    def get_builder_sudoku(self):
        return self.__builder_sudoku

    def get_unsolved_sudoku_grid(self):
        return self.__unsolved_sudoku_grid

    def get_numbers_removed(self):
        return self.__numbers_removed

    def get_difficulty(self):
        return self.__difficulty

    # Setters
    def set_current_cell(self, current_cell):
        self.__current_cell = current_cell

    def set_note_active(self, note_active):
        self.__note_active = note_active

    def set_solved_sudoku_grid(self, solved_sudoku_grid):
        self.__solved_sudoku_grid = solved_sudoku_grid

    def set_builder_sudoku(self, builder_sudoku):
        self.__builder_sudoku = builder_sudoku

    def set_unsolved_sudoku_grid(self, unsolved_sudoku_grid):
        self.__unsolved_sudoku_grid = unsolved_sudoku_grid

    def set_numbers_removed(self, numbers_removed):
        self.__numbers_removed = numbers_removed

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    # To String

test = Sudoku()

print(test.column_check(3))