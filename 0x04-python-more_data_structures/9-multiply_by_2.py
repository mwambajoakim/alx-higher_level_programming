#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return new dictionary with values multiplied
        by 2

        Args:
            a_dictionary: A dictionary

        Return:
            New dictionary
    """
    new_dictionary = {}

    for key, value in a_dictionary.items():
        value = value * 2
        new_dictionary[key] = value
    return new_dictionary
