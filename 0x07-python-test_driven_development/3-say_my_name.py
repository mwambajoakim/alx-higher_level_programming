#!/usr/bin/python3
"""This module will print a name"""


def say_my_name(first_name, last_name=""):
    """Prints a name

        Args:
            first_name: First name
            last_name: Last name
    """
    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
