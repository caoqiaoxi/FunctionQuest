import math

class Point3D:
	
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def norm(self):
		return math.sqrt(
			self.x ** 2+
			self.y ** 2+
			self.z ** 2
		)

	def __repr__(self):
		return f"Point3D({self.x},{self.y},{self.z})"

class Point2D:

	def __init__(self,x,y):
		self.x = x
		self.y = y


	def norm(self):
		return math.sqrt(
			self.x ** 2+
			self.y ** 2
		)

	def __repr__(self):
		return f"Point2D({self.x},{self.y})"

