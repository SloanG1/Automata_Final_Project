# Import Files/Modules
from source.interactors.button import Button
from source.interactors.config import *
from source.game_windows.default_window import Default_Window
import pygame

class Game_Windows:
    # Data Attributes
    __curr_window = "None"
    __def_window = "None"

    # Init
    def __init__(self):
        self.set_curr_window(MAIN_MENU_WINDOW)
        self.set_def_window(Default_Window().init_window())

    # Helpers
    def draw_window(self):
        self.draw_main_menu()


    def draw_main_menu(self):
        if self.get_curr_window() == "Main Menu":
            self.clear_window()
            self.create_play_button()
            self.create_settings_button()

    # Buttons
    def create_play_button(self):
        play_button_img = pygame.image.load("../assets/buttons/play_game_button.png").convert_alpha()
        play_button = Button(x_pos=CENTER_X, y_pos=CENTER_Y-200, image=play_button_img)
        if play_button.draw(self.get_def_window()):
            self.set_curr_window(GAME_WINDOW)

    def create_settings_button(self):
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