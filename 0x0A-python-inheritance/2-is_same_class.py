#!/usr/bin/python3
"""Checks if object is instance o class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class

        Args:
            obj: Object
            a_class: Class

        Return:
            True if object is instance of class
            False if otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
