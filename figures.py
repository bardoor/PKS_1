class Square:
    def __init__(self, side_lenght:float):
        self.side_lenght = side_lenght

    def lenght_perimeter(self):
        return(self.side_lenght * 4)

    def lenght_square(self):
        return(self.side_lenght * 2)


class Rectangle:
    def __init__(self , one_side_lenght:float , two_side_lenght:float):
        self.one_side_lenght = one_side_lenght
        self.two_side_lenght = two_side_lenght

    def lenght_perimeter(self):
        return((self.one_side_lenght + self.two_side_lenght) * 2)

    def lenght_square(self):
        return(self.one_side_lenght * self.two_side_lenght)


class Circle:
    def __init__(self , radius_circle: float):
        self.radius_circle = radius_circle

    def lenght_perimeter(self):
        p = 3.14
        return (p * 2 * self.radius_circle)

    def lenght_square(self):
        p = 3.14
        return ((self.radius_circle ** 2 )* p)
        
