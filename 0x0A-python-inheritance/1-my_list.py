#!/usr/bin/python3
"""Inherit a class which sorts a list"""


class MyList(list):
    """Receives a list and sorts it

        Args:
            list: Clas list

        Methods:
            print_sorted: Sorts a list

        Return:
            A sorted list
    """
    def print_sorted(self):
        print("{}".format(sorted(self)))
