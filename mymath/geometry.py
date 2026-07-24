import math

class Vector:
	
	__slots__=("data",)


	def __init__(self,*args):

		self.data = tuple(args)


	def __getitem__(self,i):

		return self.data[i]



	@property
	def x(self):
		return self.data[0]


	@property
	def y(self):
		return self.data[1]


	#property
	def z(self):
		return self.data[2]



	def norm(self):

		return math.sqrt(
			sum(
				x * x
				for x in self.data
		)
	)
	


	def __add__(self,other):

		"""
		向量加法
		"""

		return Vector(
		*(
			a+b
			for a,b in zip(
			self.data,
			other.data
			)
		)
	)
	


	def __sub__(self,other):

		"""
		向量减法
		"""

		return Vector(
		*(
			a-b
			for a,b in zip(
			self.data,
			other.data
			)
		)
	)


	def __mul__(self,k):

		"""
		数乘缩放
		"""

		return Vector(
		*(
			k*x
			for x in self.data
		)
	)

	def dot(self,other):

		"""
		点积
		"""

		return sum(
			a*b
			for a,b in zip(
				self.data,
				other.data
			)
		)


	def normalize(self):
	
		"""
		单位向量
		"""

		n = self.norm()

		return Vector(
			*(
				x/n
				for x in self.data
			)
		)

	def angle(self,other):

		"""
		计算两个向量的夹角
		"""

		cos = self.dot(other)/(

			self.norm()*
			other.norm()
		)
	
		cos = max(-1,min(1,cos))

		return math.acos(cos)


	def cross(self,other):

		"""
		三维叉积
		"""

		x1,y1,z1 = self.data
		x2,y2,z2 = other.data

		return Vector(
		
			y1*z2-z1*y2,
			z1*x2-x1*z2,
			x1*y2-y1*x2		

		)


	def __repr__(self):
		return f"Vector{self.data}"

class Point(Vector):

	
	pass


