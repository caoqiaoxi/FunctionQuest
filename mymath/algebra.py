"""
Algebra Module
作者：Qiaoxi
Function Quest
"""


def square(x):
	"""
	返回 x^2
	"""
	return x * x


def cube(x):
	"""
	返回 x^3
	"""
	return x * x * x

def power(x,n):
	"""
	返回 x 的 n 次方

	参数：
	    x ：底数
	    n ：指数

	返回：
	    x^n
	"""
	
	result = 1
	
	for i in range(n):
		result = result * x

	return result

