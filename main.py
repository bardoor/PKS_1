class Square:
    def __init__(self, side_length: float) -> None:
        self.side_length = side_length

    def get_side_length(self) -> float:
        return self.side_length

    def find_area(self) -> float:
        return (self.side_length ** 2)
    
    def find_perimeter(self) -> float:
        return (self.side_length * 4)


class Rectangle:
    def __init__(self, first_side_length: float, second_side_length: float) -> None:
        self.first_side_length = first_side_length
        self.second_side_length = second_side_length

    def get_first_side_length(self) -> float:
        return self.first_side_length
    
    def get_second_side_length(self) -> float:
        return self.second_side_length

    def find_area(self) -> float:
        return (self.first_side_length * self.second_side_length)
    
    def find_perimeter(self) -> float:
        return (self.first_side_length + self.second_side_length) * 2


class Circle:
    def __init__(self, radius_length: float) -> None:
        self.radius_length = radius_length

    def find_area(self) -> float:
        π = 3.14
        return π * (self.radius_length ** 2)
    
    def find_perimeter(self) -> float:
        π = 3.14
        return (2 * π * self.radius_length)