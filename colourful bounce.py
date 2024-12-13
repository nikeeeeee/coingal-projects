import pygame 
import random
#initialize Pygame
pygame. init()
#Custom event Ids for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_EVENT_EVENT = pygame.USEREVENT + 2
#Define basic colors using pygame.Color
#Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
# Sprite colors
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):
    # Constructor method
def __init__(self, color, height, width):