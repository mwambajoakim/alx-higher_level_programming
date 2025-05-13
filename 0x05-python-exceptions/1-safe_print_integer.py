#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with format specified

        Args:
            value: Vvalue to print

        Return:
            None
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
