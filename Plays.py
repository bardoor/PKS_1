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

class Wheel:
    __center_x: int
    __center_y: int
    __radius: int
    __color: int

    def __init__(self, center_x, center_y, radius: int, color: (int, int, int)):
        self.__center_x = center_x
        self.__center_y = center_y
        self.__radius = radius
        self.__color = color

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface=surface,
                           color=self.__color,
                           center=(self.__center_x, self.__center_y),
                           radius=self.__radius)

    def move(self, offset_x: int, offset_y: int):
        self.__center_x += offset_x
        self.__center_y += offset_y

class Body:
    __rect: pygame.Rect
    __color: (int, int, int)

    def __init__(self, left_top_x: int, left_top_y: int, width: int, height: int, color: (int, int, int)):
        self.__rect = pygame.Rect(left_top_x, left_top_y, width, height)
        self.__color = color

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, color=self.__color, rect=self.__rect)

    def move(self, offset_x: int, offset_y: int):
        # move_ip - move in place, то есть передвинуться в какое-либо место
        # В качестве параметров принимается смещение относительно текущего положения
        self.__rect.move_ip(offset_x, offset_y)
