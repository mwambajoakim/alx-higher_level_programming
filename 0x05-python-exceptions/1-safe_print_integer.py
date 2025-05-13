#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with format specified

        Args:
            value: Vvalue to print

        Return:
            None
    """
    try:
        number = int(value)
        print("{:d}".format(number))
        return number
    except Exception:
        print("{}".format(value))
