class Квадрат:
	def __init__(self, age):
		self.age = age

	def sey_площадь(self):
		return f"Площадь квадрата >> {int(self.age) ** 2}"

def rectangle(a,b):
	print("Площадь >> ",a*b)
	print("Периметр >> ",a*2+b*2)
def circle(r):
	print("Площадь >> ",3.14*r**2)
	print("Периметр >> ",2 * 3,14 * r)