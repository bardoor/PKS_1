import pygame
from enum import Enum

pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
BACKGROUND_COLOR = (255, 255, 255)
CAPTION = "Моя прекрасная вагонетка-самоходка"
FPS = 60


class Direction(Enum):
    South = 1
    North = 2
    West = 3
    East = 4
