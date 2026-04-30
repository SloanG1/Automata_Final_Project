# Import Files/Modules
from source.back_end.interactors.button import Button
from source.back_end.main_game.sudoku import Sudoku
from source.back_end.interactors.config import *
import pygame

class Sudoku_Window:
    # Data Attributes
    __curr_sub_grid = -1
    __note_checked = None  # This is to check to see if the user has selected to add notes to the board
    __def_window = None
    __game_board_array = []
    __new_game = False

    # Init
    def __init__(self, def_window=None):
        self.set_curr_sub_grid(-1)
        self.set_note_checked(False)
        self.set_def_window(def_window)
        self.set_game_board_array(BLANK_SUDOKU)
        self.set_new_game(True)
        self.create_grid()

    # Helpers

    # Combine all elements here
    def update_board(self):
        self.draw_grid()
        self.draw_check_numbers()

    # These are the numbers shown next to the sudoku board
    def draw_check_numbers(self):
        for key, y_pos in NUMBER_ARRAY.items():
            check_numbers_img = pygame.image.load(key).convert_alpha()
            check_squares = Button(width=50, height=50, x_pos = 30, y_pos=y_pos, image=check_numbers_img)
            check_squares.draw(self.get_def_window())

    # This will draw the note numbers on the main grid
    def get_grid_numbers(self):
        sudoku_grid = Sudoku()
        sudoku_grid.build_sudoku()
        sudoku_game = sudoku_grid.get_unsolved_sudoku_grid()
        return sudoku_game

    def get_number_images(self, numbers):
        num_dict = {1: NUMBER_ONE, 2: NUMBER_TWO, 3: NUMBER_THREE,
                    4: NUMBER_FOUR, 5: NUMBER_FIVE, 6: NUMBER_SIX,
                    7: NUMBER_SEVEN, 8: NUMBER_EIGHT, 9: NUMBER_NINE}
        return num_dict.get(numbers)


    # This will create the main grid
    def create_grid(self):
        sudoku_game = self.get_grid_numbers()

        for row in range(9):
            for col in range(9):
                number = sudoku_game[row][col]
                image = self.get_number_images(number)
                try:
                    grid_num_img = pygame.image.load(image).convert_alpha()

                    x_pos = 270 + (col * 40)
                    y_pos = 190 + (row * 40)

                    sub_grid_square = Button(width=42, height=42, x_pos=x_pos, y_pos=y_pos, image=grid_num_img)

                    sub_grid_square.draw(self.get_def_window())

                    self.get_game_board_array()[row][col] = sub_grid_square

                except TypeError:
                    pass

    # This will draw the main grid
    def draw_grid(self):
        for rows in range(len(self.get_game_board_array())):
            for cols in range(len(self.get_game_board_array()[rows])):
                sub_grid = self.get_game_board_array()[rows][cols]
                try:
                    if sub_grid.draw(self.get_def_window()):
                        self.calculate_current_sub_grid(rows, cols)
                except AttributeError:
                    pass

    def calculate_current_sub_grid(self, rows, cols):
        cols = cols + 1
        sub_grid = (rows * 9) + cols
        self.set_curr_sub_grid(sub_grid)


    # Getters
    def get_curr_sub_grid(self):
        return self.__curr_sub_grid

    def get_note_checked(self):
        return self.__note_checked

    def get_def_window(self):
        return self.__def_window

    def get_game_board_array(self):
        return self.__game_board_array

    def get_new_game(self):
        return self.__new_game

    # Setters
    def set_curr_sub_grid(self, curr_sub_grid):
        self.__curr_sub_grid = curr_sub_grid

    def set_note_checked(self, note_checked):
        self.__note_checked = note_checked

    def set_def_window(self, def_window):
        self.__def_window = def_window

    def set_game_board_array(self, game_board_array):
        self.__game_board_array = game_board_array

    def set_new_game(self, new_game):
        self.__new_game = new_game

    # To String