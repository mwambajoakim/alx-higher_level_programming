#!/usr/bin/python3
"""Checks if object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of class a_class

        Args:
            obj: An object
            a_class: A class

        Return:
        True if obj is instance of a_class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
