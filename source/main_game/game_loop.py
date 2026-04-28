"""
This Program was written by Gavin Sloan
April 27th, 2026
This file is where the game will run
"""

# Import Files/Modules
import pygame
from source.game_windows.game_windows import Game_Windows
pygame.init()

class Game_Loop:
    # Data Attributes
    __game_running = None
    __game_window = None

    # Init
    def __init__(self):
        self.set_game_running(True)
        self.set_game_window(Game_Windows())

    # Helpers

    def update_screen(self):
        self.get_game_window().draw_window()
        pygame.display.update()

    def run_game_loop(self):
        while self.get_game_running():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.set_game_running(False)

            self.update_screen()

        pygame.quit()


    # Getters
    def get_game_running(self):
        return self.__game_running

    def get_game_window(self):
        return self.__game_window

    # Setters
    def set_game_running(self, game_running):
        self.__game_running = game_running

    def set_game_window(self, game_window):
        self.__game_window = game_window

    # To String



