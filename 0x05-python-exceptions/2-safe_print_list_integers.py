#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints x members of my_list only integers

        Args:
            my_list: List of elements
            x: Number of elements to print

        Return:
            Integer count
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
