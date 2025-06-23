#!/usr/bin/python3
"""Creates a square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square that inherits from Rectangle

        Args:
            size: Size of the square

        Return:
            area: Area of the square
    """
    def __init__(self, size):
        super().__init__("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
