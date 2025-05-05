#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns largest integer.

        Args:
            my_list: List of integers

        Return:
            None if my_list is empty
            Largest number otherwise
    """
    if my_list == []:
        return None
    largest = my_list[0]
    for number in my_list:
        if number > largest:
            largest = number
    return largest
