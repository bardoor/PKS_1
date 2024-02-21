class Square:
	def __init__(self, side):
		self.side = side

	def sey_square(self):
		return f"Площадь квадрата >> {int(self.side) ** 2}"

	def sey_perimeter(self):
		return f"Периметр квадрата >> {int(self.side) * 4}"



def rectangle(a,b):
	print("Площадь >> ",a*b)
	print("Периметр >> ",a*2+b*2)
def circle(r):
	print("Площадь >> ",3.14*r**2)
	print("Периметр >> ",2 * 3,14 * r)