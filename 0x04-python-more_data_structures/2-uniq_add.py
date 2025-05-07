#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds unique elements of a list

        Args:
            my_list: List of elements

        Return:
            Sum of elements in list
    """
    last_num = set(my_list)
    sum = 0
    for nums in last_num:
        sum += nums
    return sum
