#!/usr/bin/python3
"""Creates Rectangle which inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle that inherits from BaseGeometry

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
