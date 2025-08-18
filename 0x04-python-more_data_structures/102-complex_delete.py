#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes a specific value in a dictionary.

       Args:
            a_dictionary: A dictionary.
            value: Value to delete.

       Return:
              Dictionary whose specified value has
              been deleted.
              Otherwise return the dictionary if the
              value does not exist.
    """
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
