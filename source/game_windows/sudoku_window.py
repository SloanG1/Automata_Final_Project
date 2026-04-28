# Import Files/Modules
from source.interactors.button import Button
from source.interactors.config import *
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

    # Helpers

    # Combine all elements here
    def draw_board(self):
        if self.get_new_game():
            self.create_grid()
            self.set_new_game(False)
        self.draw_grid()

    # These are the numbers shown near the bottom of a sudoku board
    def draw_check_numbers(self):
        pass

    # This will draw the numbers on the main grid
    def draw_main_numbers(self):
        pass

    # This will draw the note numbers on the main grid
    def draw_note_numbers(self):
        pass

    # This will create the main grid
    def create_grid(self):
        sub_grid_square_img = pygame.image.load("../assets/sub_grid_square.png").convert_alpha()
        for y_pos in range(190, 550, 40):
            # Set x_pos
            for x_pos in range(270, 630, 40):
                sub_grid_square = Button(width=42, height=42, x_pos=x_pos, y_pos=y_pos, image=sub_grid_square_img)
                self.get_game_board_array()[int((y_pos - 190) / 40)][int((x_pos - 270) / 40)] = sub_grid_square

    # This will draw the main ngrid
    def draw_grid(self):
        self.create_grid()
        for rows in range(len(self.get_game_board_array())):
            for cols in range(len(self.get_game_board_array()[rows])):
                sub_grid = self.get_game_board_array()[rows][cols]
                if sub_grid.draw(self.get_def_window()):
                    sub_grid_selected_square_img = pygame.image.load("../assets/buttons/play_game_button.png").convert_alpha()
                    sub_grid.set_image(sub_grid_selected_square_img)
                    self.calculate_current_sub_grid(rows, cols)

    def calculate_current_sub_grid(self, rows, cols):
        cols = cols + 1
        sub_grid = (rows * 9) + cols
        self.set_curr_sub_grid(sub_grid)
        print(self.get_curr_sub_grid())

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