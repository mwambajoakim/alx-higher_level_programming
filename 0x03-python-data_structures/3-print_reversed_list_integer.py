#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints the reverse of a list.

    Args:
        my_list: List of elements.

    Return:
        Nothing.
    """
    if my_list != None:
        length = len(my_list)
        i = length - 1
        if length > 0:
            while i >= 0:
                print("{:d}".format(my_list[i]))
                i -= 1
