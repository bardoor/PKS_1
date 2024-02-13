import math



class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return f"площадь квадрата равна: {self.side ** 2}"
    
    def perimetr(self):
        return f"периметр квадрата равен: {self.side * 4}"
    
class Rectangle:
    def __init__(self,side1,side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return f"площадь прямоугольника равна: {self.side1 * self.side2}"
    
    def perimetr(self):
        return f"площадь прямоугольника равна: {self.side1 * 2 + self.side2 * 2}"
    
class Round:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f"площадь круга равна: {math.pi * (self.radius ** 2)}"
    
    def lenth(self):
        return f"длина круга равна: {2 * math.pi * self.radius}"

