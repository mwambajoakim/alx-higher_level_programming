#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Searches for a character and replaces it

        Args:
            my_list: List of elements
            search: Element to search for
            replace: Element to replace with

        Return:
            new list with replace
    """
    if search is None:
        return my_list

    new_list = []
    for element in my_list:
        if element is search:
            del element
            element = replace
        new_list.append(element)
    return new_list
