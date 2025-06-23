#!/usr/bin/python3
"""Defines a rectangle inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle

        Args:
            width: Width of rectangle
            height: height of rectangle

        Return:
            area: Area of the rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __repr__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
