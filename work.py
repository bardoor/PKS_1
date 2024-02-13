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

