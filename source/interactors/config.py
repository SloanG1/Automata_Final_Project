"""
Config file should only contain constant variables and should be accessible to all directories
"""

# Game Name
GAME_NAME = "Sudoku Life"

# Window Settings
WIDTH = 900
HEIGHT = 700

# Window Position Settings
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

# Grid Settings
SUB_GRID_SIZE = 20 # Set size of each subgrid
MID_GRID_SIZE = SUB_GRID_SIZE * 3 # Size of each group of grids
GRID_SIZE = MID_GRID_SIZE * 3 # Size of the entire grid

# Sprite Settings
SPRITE_WIDTH = SUB_GRID_SIZE
SPRITE_HEIGHT = SUB_GRID_SIZE

# Windows Settings
MAIN_MENU_WINDOW = "Main Menu"
SETTINGS_WINDOW = "Settings"
GAME_WINDOW = "Game Window"

# Color Types
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Add more colors later

# Blank Sudoku
BLANK_SUDOKU = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Font Types
FONT1 = 'freesansbold.ttf'

# Asset Settings
DEFAULT_IMAGE = 'source/assets/default.png'