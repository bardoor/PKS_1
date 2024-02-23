class Square:
    def __init__(self, side):
        self.side = side

    def sey_square(self):
        return self.side ** 2

    def sey_perimeter(self):
        return self.side * 4


class Rectangle:
	def __init__(self, side_a, side_b):
		self.a = side_a
		self.b = side_b

	def sey_square(self):
		return self.a * self.b
		
	def sey_perimeter(self):
		return (self.a + self.b) * 2

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def sey_square(self):
		return 3.14 * self.radius ** 2

	def sey_perimeter(self):
		return 2 * 3.14 * self.radius
