#!/usr/bin/python3
"""Creates a square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """Defines a square that inherits from rectangle

        Args:
            size: Size of the square

        Return: 
            area: Area of the square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __repr__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
