#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes an element at position idx

        Args:
        my_list: List of elements.
        idx: Position of element.

        Return:
        None
    """
    if idx < 0 or idx > len(my_list):
        return my_list
    length = len(my_list)
    i = 0
    while i < length:
        if i == idx:
            del my_list[i]
        i += 1
    return my_list
