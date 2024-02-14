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


class Circle:  # Круг
    def __init__(self, radius: float):
        self.radius = radius

    def find_square(self) -> float:
        return math.pi * self.radius ** 2

    def find_perimeter(self) -> float:
        return 2 * math.pi * self.radius

class TimeInterval:
    seconds: int
    def __init__(self, seconds, minutes=0, hours = 0) -> None:
        self.seconds = seconds + minutes * 60 + hours * 3600
    
    def time_in_seconds(self) -> int:
        return self.seconds

    def time_in_minutes(self) -> float:
        return self.seconds / 60

    def time_in_hours(self) -> float:
        return self.seconds / 3600

    def __add__(self, other):
        return self.seconds + other.seconds

    def __sub__(self, other):
        return self.seconds - other.seconds

    def __eq__(self, other) -> bool:
        if self.seconds == other.seconds:
            return True
        return False

    def __ne__(self, other) -> bool:
        return not(__eq__(self))

    def __lt__(self, other) -> bool:
        if self.seconds < other.seconds:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.seconds > other.seconds:
            return True
        return False
