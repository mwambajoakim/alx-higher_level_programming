#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary

        Args:
            a_dictionary: A dictionary
            key: Key in dictionary

        Return:
            new dictionary
    """
    if key not in a_dictionary:
        return a_dictionary

    del a_dictionary[key]
    return a_dictionary
