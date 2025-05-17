#!/usr/bin/python3
def remove_char_at(str, n):
    """Removes a character at n

        Args:
            str: tring of characters
            n: Index at which to remove

        Return:
            None
    """
    cpy_str = str[:]
    length = len(cpy_str)
    new_str = ""

    for i in range(length):
        if i != n:
            new_str += cpy_str[i]
    return new_str
