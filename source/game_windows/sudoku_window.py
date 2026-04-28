# Import Files/Modules
from source.interactors.button import Button
from source.interactors.config import *
import pygame

class Sudoku_Window:
    # Data Attributes
    __curr_sub_grid = -1
    __note_checked = None  # This is to check to see if the user has selected to add notes to the board
    __def_window = None

    # Init
    def __init__(self, def_window=None):
        self.set_curr_sub_grid(-1)
        self.set_note_checked(False)
        self.set_def_window(def_window)

    # Helpers

    # Combine all elements here
    def draw_board(self):
        pass

    # These are the numbers shown near the bottom of a sudoku board
    def draw_check_numbers(self):
        pass

    # This will draw the numbers on the main grid
    def draw_main_numbers(self):
        pass

    # This will draw the note numbers on the main grid
    def draw_note_numbers(self):
        pass

    # This will draw the main_grid
    def draw_grid(self):
        pass

    # Getters
    def get_curr_sub_grid(self):
        return self.__curr_sub_grid

    def get_note_checked(self):
        return self.__note_checked

    def get_def_window(self):
        return self.__def_window

    # Setters
    def set_curr_sub_grid(self, curr_sub_grid):
        self.__curr_sub_grid = curr_sub_grid

    def set_note_checked(self, note_checked):
        self.__note_checked = note_checked

    def set_def_window(self, def_window):
        self.__def_window = def_window

    # To String