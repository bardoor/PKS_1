class Circle:
    def __init__(self, radius_length: float) -> None:
        self.radius_length = radius_length
        self.radius_length = radius_length

    def find_S(self) -> float:
        π = 3.14
        return π * (self.radius_length ** 2)

    def find_P(self) -> float:
        π = 3.14
        return (2 * π * self.radius_length)


class Square:
    def __init__(self, length_side):
        self.length_side = length_side

    def find_S(self):
        return (self.length_side ** 2)

    def find_P(self):
        return (self.length_side * 4)


class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def find_S(self):
        return (self.width * self.length)

    def find_P(self):
        return (self.width * 2 + self.length * 2)



