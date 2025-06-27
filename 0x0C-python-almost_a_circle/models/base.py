#!/usr/bin/python3
"""Manage id attribute"""


class Base:
    """This class defines the id attribute

        Args:
            id: Class id

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
