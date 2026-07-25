import math 

class Transform2D:

	def __init__(self,sx,sy):

		self.sx = sx

		self.sy = sy


	def scale(self,vector):

		x,y = vector

		new_x = self.sx * x

		new_y = self.sy * y

		
		return (new_x,new_y)

		
	def __reor__(self):

		return ( f"Transform2D ("f"sx = {self.sx} ," f"sy = {self.sy})")

			
	
