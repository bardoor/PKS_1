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

class Cart:
    __body: Body
    __wheels: [Wheel]

    def __init__(self, left_top_x, left_top_y, width, height):
        self.__speed = 10
        body_height = 0.8 * height
        body_color = (90, 90, 90)  # Серый
        wheel_radius = 0.2 * height // 2
        wheel_color = (0, 50, 100)  # Желтый
        wheel_offset_x = 0.1 * width  # Смещение колеса относительно вертикальной границы вагонетки
        wheel_center_y = 0.9 * height  # Координата y центра колёс

        self.__body = Body(left_top_x, left_top_y, width, body_height, body_color)
        self.__wheels = [
            Wheel(wheel_offset_x, wheel_center_y, wheel_radius, wheel_color),
            Wheel(width - wheel_offset_x, wheel_center_y, wheel_radius, wheel_color)
        ]

    def draw(self, surface: pygame.Surface):
        self.__body.draw(surface)
        for wheel in self.__wheels:
            wheel.draw(surface)

    def move(self, direction: int):
        if direction == Direction.South:
            offset_x, offset_y = 0, -self.__speed
        elif direction == Direction.North:
            offset_x, offset_y = 0, self.__speed
        elif direction == Direction.East:
            offset_x, offset_y = self.__speed, 0
        elif direction == Direction.West:
            offset_x, offset_y = -self.__speed, 0
        self.__body.move(offset_x, offset_y)
        for wheel in self.__wheels:
            wheel.move(offset_x, offset_y)

class Game:
    __screen: pygame.Surface
    __background_color: (int, int, int)
    __frame_rate: int
    __clock: pygame.time.Clock
    __is_running: bool
    __cart: Cart

    def __init__(self, width: int, height: int, background_color: (int, int, int), frame_rate: int, caption: str):
        pygame.display.set_caption(caption)
        self.__screen = pygame.display.set_mode((width, height))
        self.__background_color = background_color
        self.__frame_rate = frame_rate
        self.__clock = pygame.time.Clock()
        self.__is_running = True
        self.__cart = Cart(0, 0, 200, 100)

    def __handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__is_running = False
            # Регистрируем нажатие на какую-либо клавишу
            elif event.type == pygame.KEYDOWN:
                # Если нажатая клавиша - стрелка вправо
                if event.key == pygame.K_RIGHT:
                    self.__cart.move(Direction.East)
                elif event.key == pygame.K_LEFT:
                    self.__cart.move(Direction.West)
                elif event.key == pygame.K_UP:
                    self.__cart.move(Direction.South)
                elif event.key == pygame.K_DOWN:
                    self.__cart.move(Direction.North)

    def __update(self):
        ...

    def __draw(self):
        self.__screen.fill(self.__background_color)
        self.__cart.draw(self.__screen)
        pygame.display.update()

    def run(self):
        while self.__is_running:
            self.__handle_events()
            self.__update()
            self.__draw()
            self.__clock.tick(self.__frame_rate)
