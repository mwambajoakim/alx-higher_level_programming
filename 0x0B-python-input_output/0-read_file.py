#!/usr/bin/python3
"""Opens a file for reading"""


def read_file(filename=""):
    """Opens a file for reading and prints to stdout

        Args:
            filename: Name of the file

        Return:
            None
    """
    with open(filename, 'r', encoding="UTF-8") as read_file:
        print("{}".format(read_file.read()), end="")
