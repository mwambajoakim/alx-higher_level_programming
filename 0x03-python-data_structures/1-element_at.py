#!/usr/bin/python3
def element_at(my_list, idx):
    """Prints element at specific index

    Args:
        my_list: List of elements.
        idx: Index of element.

    Return:
    None: If 0 > number > length of list
    Otherwise: Number at index
    """
    length = len(my_list)
    if idx < 0:
        return None
    if idx > length:
        return None
    for i in range(length):
        if (i == idx):
            return (my_list[i])
