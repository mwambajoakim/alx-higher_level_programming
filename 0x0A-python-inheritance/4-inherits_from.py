#!/usr/bin/python3
"""Checks if an object is a subclass"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a_class that inherited from a class

        Args:
            obj: An object
            a_class: A class

        Return:
        True if isinstance
        False otherwise
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
