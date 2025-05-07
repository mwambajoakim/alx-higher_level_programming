#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns number of keys in dictionary

        Args:
            a_dictioanry: A dictionary

        Return:
            Number of keys
    """
    count = 0

    for elems in a_dictionary:
        count += 1
    return count
