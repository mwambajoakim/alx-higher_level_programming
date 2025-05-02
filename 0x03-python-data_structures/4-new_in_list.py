#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list.

        Args:
            my_list: List of elements.
            idx: Index of elements.
            element: Element to replace with.

        Return:
            original list: if idx < 0
            original list: if idx > length of list
            new list
    """
    length = len(my_list)
    if idx < 0:
        return my_list
    if idx > length:
        return my_list
    new_list = my_list[:]
    for i in range(length):
        if (i == idx):
            new_list[i] = element
    return new_list
