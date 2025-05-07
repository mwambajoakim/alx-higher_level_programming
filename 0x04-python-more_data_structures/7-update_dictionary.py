#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Updates dictionary if key does not exist

        Args:
            a_dictionary: A dictioonary
            key: Key to check
            value: value of key

        Return:
            New dictionary
    """
    if key in a_dictionary or key not in a_dictionary:
        a_dictionary[key] = value
    return a_dictionary
