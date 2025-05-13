#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x number of elements in my_list

        Args:
            my_list: List of elements
            x: Number of elements to print

        Return:
            New list of elements
    """
    try:
        i = 0
        count = 0
        while i < x:
            print("{}".format(my_list[i]), end="")
            count += 1
            i += 1
        print()
        return count
    except Exception:
        print()
        return count
