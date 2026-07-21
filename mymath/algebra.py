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


def absolute(x):
	"""
	返回 x 的绝对值

	参数：
	    x: int 或 float

	返回:
	    |x|

	"""

	if x >= 0:
		return x

	else:
		return -x


def factorial(n):
	"""
	返回 n 的阶乘

	参数：
	    n:非负整数

	返回:
	    n!

	"""

	result = 1

	for i in range(1,n+1):

		result = result * i

	return result


def sign(x):
	"""
	返回数字的符号

	参数：
	
	    x: int 或 float

	返回：

	    x > 0 返回1
	    x = 0 返回0
	    x < 0 返回-1

	"""

	if x > 0:
		return 1

	elif x == 0:
		return 0

	else:
		return -1


