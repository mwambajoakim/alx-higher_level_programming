#!/usr/bin/python3
"""Creates a rectangle, its perimeter and area"""


class Rectangle:
    """Defines a rectangle Rectangle

        Args:
            width: Rectangle width
            height: Rectangle height

        Return:
            perimeter: Perimeter of the rectangle
            area: Area of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        per = 0
        if self.__width == 0 or self.__height == 0:
            per = 0
        else:
            per = 2 * (self.__width + self.__height)
        return per

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        return string.strip()

    def __repr__(self):
        return "Rectangle(" \
            "" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
