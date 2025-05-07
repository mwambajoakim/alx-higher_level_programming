#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns elements not similar in both sets

        Args:
            set_1: First set
            set_2: Second set

        Return:
            Unique elements
    """
    diff_elements = set_1 ^ set_2
    return diff_elements
