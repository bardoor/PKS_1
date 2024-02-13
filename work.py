import math



class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return f"площадь квадрата равна: {self.side ** 2}"
    
    def perimetr(self):
        return f"периметр квадрата равен: {self.side * 4}"

