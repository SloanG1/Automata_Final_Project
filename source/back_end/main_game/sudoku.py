# Add Files/Modules
from source.back_end.interactors.config import *
from random import Random

class Sudoku:
    # Data Attributes
    __current_cell = None
    __note_active = None
    __solved_sudoku_grid = []
    __unsolved_sudoku_grid = []
    __numbers_removed = -1
    __difficulty = None

    # Init
    def __init__(self):
        self.set_current_cell(None)
        self.set_note_active(False)
        self.set_solved_sudoku_grid([])
        self.set_unsolved_sudoku_grid([])
        self.set_difficulty("easy")

    # Helpers
    def generate_random_board(self):
        pass

    def generate_solved_puzzle(self):
        self.get_unsolved_sudoku_grid()

    def remove_numbers(self):
        pass

    # Getters
    def get_current_cell(self):
        return self.__current_cell

    def get_note_active(self):
        return self.__note_active

    def get_solved_sudoku_grid(self):
        return self.__solved_sudoku_grid

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

    def set_unsolved_sudoku_grid(self, unsolved_sudoku_grid):
        self.__unsolved_sudoku_grid = unsolved_sudoku_grid

    def set_numbers_removed(self, numbers_removed):
        self.__numbers_removed = numbers_removed

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    # To String