#!/usr/bin/python3
"""A class square"""


class Square:
	"""Creates a square and returns the area\
		prints it to stdout

		Args:
			size (int): ize of the square
			position (tuple): Position of square

		Return:
			area (int): Area of the square
	"""
	def __init__(self, size=0, position=(0,0)):
		self.__size = size
		self.__position = position

	@property
	def size(self):
		"""Gets the size of the square\
			Work with a setter to retrieve

			Args:
				value (int): Retrieved value for size

			Return:
				size (int): Size of the square
		"""
		return self.__size
	
	@size.setter
	def size(self, value):
		if not isinstance(value, int):
			raise TypeError("must be an integer")
		if value < 0:
			raise ValueError("must be >= 0")
		self.__size = value

	def area(self):
		"""Returns the area of a square

			Return:
				area (int): Area of a square
		"""
		return self.__size * self.__size
	
