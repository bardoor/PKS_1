class Square:
     def init(self, side_square:float):
        self.side_square = side_square

    def Square_perimeter(self):
        return(self.side_square * 4)

    def Square_square(self):
        return(self.side_square * 2)
class Rectangle:
    def init(self , one_side_rectangle:float , two_side_rectangle:float):
        self.one_side_rectangle = one_side_rectangle
        self.two_side_rectangle = two_side_rectangle

    def Rectangle_perimeter(self):
        return((self.one_side_rectangle + self.two_side_rectangle) * 2)

    def Rectangle_square(self):
        return(self.one_side_rectangle * self.two_side_rectangle)
class Circle:
     def init(self , radius_circle: float):
        self.radius_circle = radius_circle