#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns elements divisible by 2

        Args:
            my_list: List of elements

        Return:
            True if element is divisible by 2
            False if otherwise
            New list
    """
    new = []

    for nums in my_list:
        new.append(nums % 2 == 0)
    return new
