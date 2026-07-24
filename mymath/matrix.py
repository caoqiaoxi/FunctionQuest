class Matrix:

	"""
	基础矩阵对象
	"""

	def __init__(self,data):
	
		self.data = data


	def __repr__(self):

		return f"Matrix({self.data})"


	def shape(self):

		rows = len(self.data)

		cols = len(self.data[0])

		return(rows,cols)


	def __add__(self,other):

		result = []

		for row_a,row_b in zip(
			self.data,
			other.data
		):

			row = []

			for a,b in zip(
				row_a,
				row_b
			):

				row.append(a+b)

			result.append(row)

		return Matrix(result)



	def __mul_(self,other):
	

		result=[]
	

		for i in range(len(self.data)):

			row =[]


			for j in range(len(other.data[0])):

				total = 0
				
				for k in range(len(other.data)):
				
					total += (

						self.data[i][k]

						*

						other.data[k][j]

	
					)


				row.append(total)

			result.append(row)

	
		return Matrix(result)

		
