#!/usr/bin/python3
"""Opens a file to append data"""


def append_write(filename="", text=""):
    """Open filename and append text to it
        Creates the file if it did not yet exist

        Args:
            filename: Name of the file
            text: Text to append

        Return: Number of characters appended
    """
    length = len(text)
    with open(filename, 'a', encoding="UTF-8") as append_text:
        append_text.write(text)
    return length
