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
    [1, 2, 3, 0, 0, 0, 0, 0, 0],
    [4, 4, 6, 0, 0, 0, 0, 0, 0],
    [7, 8, 9, 0, 0, 0, 0, 0, 0],
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
PLAY_GAME_BUTTON = '../../front_end/assets/buttons/play_game_button.png'

# Add the number images
NUMBER_ONE = '../../front_end/assets/numbers/number_one.png'
NUMBER_TWO = '../../front_end/assets/numbers/number_two.png'
NUMBER_THREE = '../../front_end/assets/numbers/number_three.png'
NUMBER_FOUR = '../../front_end/assets/numbers/number_four.png'
NUMBER_FIVE = '../../front_end/assets/numbers/number_five.png'
NUMBER_SIX = '../../front_end/assets/numbers/number_six.png'
NUMBER_SEVEN = '../../front_end/assets/numbers/number_seven.png'
NUMBER_EIGHT = '../../front_end/assets/numbers/number_eight.png'
NUMBER_NINE = '../../front_end/assets/numbers/number_nine.png'

NUMBER_ARRAY = {NUMBER_ONE:100, NUMBER_TWO:150, NUMBER_THREE:200,
                NUMBER_FOUR:250, NUMBER_FIVE:300, NUMBER_SIX:350,
                NUMBER_SEVEN:400, NUMBER_EIGHT:450, NUMBER_NINE:500}
