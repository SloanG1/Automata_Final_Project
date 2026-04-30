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
        return True # Validates sudoku

    # This checks to see if the numbers in the column do not validate sudoku
    def column_check(self, column):
        check_array = []
        for rows in self.get_builder_sudoku():
            if rows[column] not in check_array:
                check_array.append(rows[column])
            else:
                return False  # Does not validate sudoku
        return True # Validates sudoku

    # This checks to see if the numbers in the subgrid do not validate sudoku
    def sub_grid_check(self, row, column):
        row_range = self.get_row_range(row)
        column_range = self.get_column_range(column)
        check_array = []
        for rows in row_range:
            for columns in column_range:
                if self.get_builder_sudoku()[rows][columns] not in check_array:
                    check_array.append(self.get_builder_sudoku()[rows][columns])
                else:
                    return False  # Does not validate sudoku
        return True  # Validates sudoku

    @staticmethod
    def get_row_range(row):
        if row <= 2:
            row_range = [0, 1, 2]
        elif row <= 5:
            row_range = [3, 4, 5]
        else:
            row_range = [6, 7, 8]
        return row_range

    @staticmethod
    def get_column_range(column):
        if column <= 2:
            column_range = [0, 1, 2]
        elif column <= 5:
            column_range = [3, 4, 5]
        else:
            column_range = [6, 7, 8]
        return column_range

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

print(test.sub_grid_check(2, 2))