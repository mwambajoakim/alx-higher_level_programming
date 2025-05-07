#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply members of lsit with number

        Args:
            my_list: List of elements
            number: number to multiply with

        Return:
            New list after multiplication
    """
    return list(map(lambda x: x * number, my_list))
