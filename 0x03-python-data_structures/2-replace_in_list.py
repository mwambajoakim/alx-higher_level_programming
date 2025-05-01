#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element at given index

    Args:
        my_list: List of elemennts.
        idx: Index of element.
        element: Replacement.

    Return:
    my_list: if idx is negative.
    my_list: if idx > length of my_list.
    Otherwise: Return new list.
    """
    length = len(my_list)

    if idx < 0:
        return my_list
    if idx > length:
        return my_list

    for i in range(length):
        if i == idx:
            my_list[i] = element
    return my_list
