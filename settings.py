import pygame
pygame.init()
pygame.font.init()

# capslock represent constants in python
#colors for the gane
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

#frame rate 
FPS = 250

WIDTH, HEIGHT = 500, 600  #Tool bar is extra 100 which will be at the bottom of the screen

ROWS = COLS = 50 #rows and columns for the pixel within the paint canvas

TOOLBAR_HEIGHT = HEIGHT- WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE #bg color of the canvas

DRAW_GRID_LINES = True #drawS grid lines

#for the font size 
def get_font(size):
    return pygame.font.SysFont("comicsans", size)