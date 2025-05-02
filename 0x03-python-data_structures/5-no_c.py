#!/usr/bin/python3
def no_c(my_string):
    """Removes the letters 'c' and 'C'

        Args:
            my_string: String

        Return:
            None
    """
    if my_string == "":
        return None
    new_string = ""
    for letter in my_string:
        if (letter != "c" and letter != "C"):
            new_string += letter
    return new_string
