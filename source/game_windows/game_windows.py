# Import Files/Modules
from source.interactors.button import Button
from source.interactors.config import *
from source.game_windows.default_window import Default_Window
from source.game_windows.sudoku_window import Sudoku_Window
import pygame

class Game_Windows:
    # Data Attributes
    __curr_window = None
    __def_window =  None

    # Init
    def __init__(self):
        self.set_curr_window(MAIN_MENU_WINDOW)
        self.set_def_window(Default_Window().init_window())

    # Helpers
    def draw_window(self):
        self.draw_main_menu()
        self.draw_settings()
        self.draw_game()


    def draw_main_menu(self):
        if self.get_curr_window() == MAIN_MENU_WINDOW:
            self.clear_window()
            self.create_play_button()
            self.create_settings_button()

    # Settings
    def draw_settings(self):
        if self.get_curr_window() == SETTINGS_WINDOW:
            self.clear_window()
            pygame.Surface.fill(self.get_def_window(), WHITE)
            self.create_main_menu_button()

    def draw_game(self):
        if self.get_curr_window() == GAME_WINDOW:
            self.clear_window()
            pygame.Surface.fill(self.get_def_window(), WHITE)
            self.create_main_menu_button()

    # Buttons
    def create_main_menu_button(self): # Image is a placeholder
        main_menu_button_img = pygame.image.load("../assets/buttons/play_game_button.png").convert_alpha()
        main_menu_button = Button(x_pos=CENTER_X, y_pos=CENTER_Y-300, image=main_menu_button_img)
        if main_menu_button.draw(self.get_def_window()):
            self.set_curr_window(MAIN_MENU_WINDOW)

    def create_play_button(self):
        play_button_img = pygame.image.load("../assets/buttons/play_game_button.png").convert_alpha()
        play_button = Button(x_pos=CENTER_X, y_pos=CENTER_Y-200, image=play_button_img)
        if play_button.draw(self.get_def_window()):
            self.set_curr_window(GAME_WINDOW)


    def create_settings_button(self): # Image is a placeholder
        settings_button_img = pygame.image.load("../assets/buttons/play_game_button.png").convert_alpha()
        settings_button = Button(x_pos=CENTER_X, y_pos=CENTER_Y, image=settings_button_img)
        if settings_button.draw(self.get_def_window()):
            self.set_curr_window(SETTINGS_WINDOW)

    # Call this function to clear the window
    def clear_window(self):
        pygame.Surface.fill(self.get_def_window(), WHITE)

    # Getters
    def get_curr_window(self):
        return self.__curr_window

    def get_def_window(self):
        return self.__def_window

    # Setters
    def set_curr_window(self, curr_window):
        self.__curr_window = curr_window

    def set_def_window(self, def_window):
        self.__def_window = def_window

    # To String