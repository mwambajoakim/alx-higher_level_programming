#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and returns the result

        Args:
            a: First integer
            b: Second integer

        Return:
            If error return None
            else return result
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
