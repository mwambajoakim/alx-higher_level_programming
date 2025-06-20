#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Creates a class whose area is not defined and validates an integer

        Args:
            name: Name of integer
            value: Value of integer

        Exceptions:
            ValueError: if value <= 0
            TypeError: if value is not an integer

    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
