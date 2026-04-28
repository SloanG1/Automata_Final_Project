"""
This Program was written by Gavin Sloan
April 27th, 2026
This file is the window that all windows will reference
"""

#Import Files/Modules
import pygame
from source.interactors.config import *  # This lets all functions and variables be accessible

class Default_Window:
	# Data Attributes
	__window_width = -1
	__window_height = -1
	__background = (-1, -1, -1)
	__game_name = "Error"
	__font = "Error"

	# Init
	def __init__(self, window_width=WIDTH, window_height=HEIGHT, background=WHITE, game_name=GAME_NAME, font=FONT1):
		self.set_window_width(window_width)
		self.set_window_height(window_height)
		self.set_background(background)
		self.set_game_name(game_name)
		self.set_font(pygame.font.Font(font, 30))

	# Helpers
	def init_window(self):
		game_window = pygame.display.set_mode((self.get_window_width(), self.get_window_height()))  # Init window
		game_window.fill(self.get_background())  # Set background
		pygame.display.set_caption(self.get_game_name())
		pygame.display.update()
		return game_window  # Return game_window

	# Getters
	def get_window_width(self):
		return self.__window_width

	def get_window_height(self):
		return self.__window_height

	def get_background(self):
		return self.__background

	def get_game_name(self):
		return self.__game_name

	def get_font(self):
		return self.__font

	# Setters
	def set_window_width(self, window_width):
		self.__window_width = window_width

	def set_window_height(self, window_height):
		self.__window_height = window_height

	def set_background(self, background):
		self.__background = background

	def set_game_name(self, game_name):
		self.__game_name = game_name

	def set_font(self, font):
		self.__font = font

	# To String