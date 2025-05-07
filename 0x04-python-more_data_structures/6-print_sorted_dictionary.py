#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print keys and values of dictionary

        Args:
            a_dictionary: A dictionary

        Return:
            None
    """
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v), end='\n')
