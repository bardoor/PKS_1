import math

class Square: # Квадрат
    def __init__(self, side_length):
        self.side_length = side_length

    def find_square(self):
        return self.side_length ** 2

    def find_perimeter(self):
        return self.side_length * 4


class Rectangle: # Прямоугольник
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def find_square(self):
        return self.width * self.height

    def find_perimeter(self):
        return self.width * 2 + self.height * 2
