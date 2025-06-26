#!/usr/bin/python3
"""Return dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns a dictionary description of obj

        Args:
            obj: Object to serialize

        Return:
            Dictionary representation of the object
    """
    return obj.__dict__
