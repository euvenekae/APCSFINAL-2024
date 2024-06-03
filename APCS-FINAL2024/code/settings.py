import pygame 
from sys import exit
from os.path import join

CELL_SIZE = 80
ROWS = 8
COLS = 10
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

# colors 
LIGHT_GREEN = '#808080'
DARK_GREEN  = '#000000'

# start pos 
START_LENGTH = 3
START_ROW = ROWS // 2
START_COL = START_LENGTH + 2

# shadow 
SHADOW_SIZE = pygame.Vector2(4,4)
SHADOW_OPACITY = 50