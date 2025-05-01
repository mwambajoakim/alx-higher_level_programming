#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function that prints a list of integers

        Args:
            my_list: List of integers.
    """
    i = 0
    length = len(my_list)
    while (i < length):
        print("{:d}".format(my_list[i]))
        i += 1
