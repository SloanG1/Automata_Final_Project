# Add Files/Modules
from source.back_end.interactors.config import *
from random import Random
import random

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
    def generate_random_number(self):
        random_num = random.choice(SUDOKU_NUMBERS)
        return random_num

    def generate_solved_sudoku(self):
        is_valid = False
        while not is_valid:
            for rows in range(9):
                for columns in range(9):
                    self.get_builder_sudoku()[rows][columns] = self.generate_random_number()
            is_valid = self.check_validity()
            print(is_valid)

        return self.get_builder_sudoku()

    def check_validity(self, row, col, num):
        row_valid = self.row_check(row, num)
        column_valid = self.column_check(col, num)
        sub_grid_valid = self.sub_grid_check(row, col, num)
        if row_valid and column_valid and sub_grid_valid:
            is_valid = True
        else:
            is_valid = False
        return is_valid

    def generate_unsolved_sudoku(self):
        pass

    def remove_numbers(self):
        pass

    # This checks to see if the numbers in the row do not validate sudoku
    def row_check(self, row, num):
        for numbers in range(9):
            if self.get_builder_sudoku()[row][numbers] == num:
                return False

    # This checks to see if the numbers in the column do not validate sudoku
    def column_check(self, col, num):
        for numbers in range(9):
            if self.get_builder_sudoku()[col][numbers] == num:
                return False

    # This checks to see if the numbers in the subgrid do not validate sudoku
    def sub_grid_check(self, row, col, num):
        row = (row // 3) * 3
        col = (col // 3) * 3

        for row in range(row, row + 3):
            for column in range(col, col + 3):
                if self.get_builder_sudoku()[row][column] == num:
                    return False
        return True

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

print(test.generate_solved_sudoku())