import math

class box: # Квадрат
    def __init__(self, length_box):
        self.length_box = length_box

    def find_square(self):
        return (self.length_box ** 2)

    def find_perimeter(self):
        return (self.length_box * 4)


class rectangle: # Прямоугольник
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def find_square(self):
        return (self.width * self.length)

    def find_perimeter(self):
        return (self.width * 2 + self.length * 2)


class circle:  # Круг
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def find_square(self) -> float:
        return math.pi * (self.radius ** 2)

    def find_perimeter(self) -> float:
        return (2 * math.pi * self.radius)
