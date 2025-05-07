#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns common elements in two sets

        Args:
            set_1: First set
            set_2: Second set

        Return:
            Common elements in both sets
    """
    common_elems = []

    for elem_1 in set_1:
        for elem_2 in set_2:
            if elem_1 == elem_2:
                common_elems.append(elem_1)
    return common_elems
