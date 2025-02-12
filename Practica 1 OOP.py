from math import pi


class Circle:
	def __init__(self, radius):
		self.pi = pi
		self.radius = radius 

	
	def get_area(self):
		return self.radius**2 * self.pi
	
	
my_first_circle = Circle(33)

print(my_first_circle.get_area()) 