class Circle:
	radius = 8
	Pi = 3.14
	
	def get_area(self):
		return self.radius**2 * self.Pi
	
	
my_first_circle = Circle()

print(my_first_circle.get_area()) 