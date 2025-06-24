#!/usr/bin/python3
"""Opens file for writing"""


def write_file(filename="", text=""):
    """Opens file and writes to it.
        Creates a file if it does not exists and write to it
        Overwrites a file if it had content in it

        Args:
            filename: Name of the file
            text: Text to write to file

        Return:
            Number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as file_write:
        length = len(text)
        file_write.write(text)
        return length
