class Matrix:

	"""
	基础矩阵对象
	"""

	def __init__(self,data):
	
		self.data = data


	def __repr__(self):

		return f"Matrix({self.data})"

	@classmethod
	def identity(cls,n):
		data = []

		for i in range(n):

			row = []

			for j in range(n):

				if i == j:

					row.append(1)

				else:
		
					row.append(0)

			data.append(row)

		return cls(data)


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


	def __sub__(self,other):

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
		
				row.append(a-b)
		
			result.append(row)
	
		return Matrix(result)


	def __mul__(self,other):
	

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

		
	def transpose(self):
		
		rows = len(self.data)

		cols = len(self.data[0])

		result = []


		for j in range(cols):

			row = []

			for i in range(rows):

				row.append(self.data[i][j])

			result.append(row)


		return Matrix(result)


	def det(self):

		rows = len(self.data)

		cols = len(self.data[0])


		if rows != cols:

		
			raise ValueError(

				"Determinant requires square matrix"

			)

		if rows == 2:

			a = self.data[0][0]

			b = self.data[0][1]

			c = self.data[1][0]

			d = self.data[1][1]

		return a * d - b * c


	
	def inverse(self):

		det = self.det()

		if det == 0:

			raise ValueError(
				"Matrix is not invertible"
			)


		a = self.data[0][0]

		b = self.data[0][1]

		c = self.data[1][0]

		d = self.data[1][1]


		return Matrix(

			[

				[d/det,-b/det],
				[-c/det,a/det]

			]

		)
	def row_reduce(self):

		"""
		高斯-约旦消元
		返回简化行阶梯矩阵 RREF
		"""

		# 复制数据，避免修改原矩阵
		data = [
			row[:] 
			for row in self.data
		]


		rows = len(data)
		cols = len(data[0])


		pivot_row = 0


		for col in range(cols):

			# 所有行处理完成
			if pivot_row >= rows:
				break


			# =====================
			# 1. 寻找主元
			# =====================

			pivot_index = None


			for r in range(
				pivot_row,
				rows
			):

				if abs(data[r][col]) > 1e-10:

					pivot_index = r

					break



			# 当前列没有主元
			if pivot_index is None:

				continue



			# =====================
			# 2. 交换行
			# =====================

			data[pivot_row], data[pivot_index] = (
				data[pivot_index],
				data[pivot_row]
			)



			# =====================
			# 3. 主元归一化
			# =====================

			pivot_value = data[pivot_row][col]


			for j in range(cols):

				data[pivot_row][j] /= pivot_value



			# =====================
			# 4. 消除其他行
			# =====================

			for r in range(rows):

				if r == pivot_row:

					continue


				factor = data[r][col]


				for j in range(cols):

					data[r][j] -= (
						factor *
						data[pivot_row][j]
					)



			# 下一行主元

			pivot_row += 1



		return Matrix(data)
			
