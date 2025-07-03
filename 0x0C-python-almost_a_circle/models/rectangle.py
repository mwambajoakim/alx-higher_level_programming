#!/usr/bin/python3
"""Instantiate a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle
        Args:
            width: Width of rectangle
            height: Height of rectangle
            x: horizontal justification
            y: vertical justification

        Return:
            area: Area of the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the rectangle with the symbol '#'"""
        if self.height == 0:
            print("")
            return

        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        return f"[Rectangle] ({a}) {b}/{c} - {d}/{e}"

    def update(self, *args):
        """Updates the class with new attributes

            Args:
                *args: New arguments to set attributes with
        """
        attr_names = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if i < len(attr_names):
                setattr(self, attr_names[i], arg)
