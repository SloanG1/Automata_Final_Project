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
    def build_sudoku(self):
        self.generate_solved_sudoku()
        self.generate_unsolved_sudoku()

    def generate_random_number_list(self):
        random_num_list = list(range(1, 10))
        random.shuffle(random_num_list)
        return random_num_list

    def generate_solved_sudoku(self):
        empty_location = self.get_empty_location()

        if not empty_location:
            return True
        row, col = empty_location

        for num in self.generate_random_number_list():
            if self.check_validity(row, col, num):
                self.get_builder_sudoku()[row][col] = num

                if self.generate_solved_sudoku():
                    return True

                self.get_builder_sudoku()[row][col] = 0

        return False

    # Find an empty spot in the sudoku and return the row and col
    def get_empty_location(self):
        for row in range(9):
            for col in range(9):
                if self.get_builder_sudoku()[row][col] == 0:
                    return row, col
        return None

    def check_validity(self, row, col, num):
        row_valid = self.row_check(row, num)
        column_valid = self.column_check(col, num)
        sub_grid_valid = self.sub_grid_check(row, col, num)
        if row_valid and column_valid and sub_grid_valid:
            is_valid = True
        else:
            is_valid = False
        return is_valid

    def get_remove_numbers(self):
        removed_numbers = 0
        diff_dict = {"easy":20, "medium":30, "hard":40}
        removed_numbers = diff_dict.get(self.get_difficulty())
        return removed_numbers

    def generate_unsolved_sudoku(self):
        self.set_solved_sudoku_grid(self.get_builder_sudoku())
        for numbers in range(self.get_remove_numbers()):
            rand_row = Random().randrange(0, 9)
            rand_col = Random().randrange(0, 9)
            self.get_builder_sudoku()[rand_row][rand_col] = 0

        self.set_unsolved_sudoku_grid(self.get_builder_sudoku())

    # This checks to see if the numbers in the row do not validate sudoku
    def row_check(self, row, num):
        for numbers in range(9):
            if self.get_builder_sudoku()[row][numbers] == num:
                return False
        return True

    # This checks to see if the numbers in the column do not validate sudoku
    def column_check(self, col, num):
        for row in range(9):
            if self.get_builder_sudoku()[row][col] == num:
                return False
        return True

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
