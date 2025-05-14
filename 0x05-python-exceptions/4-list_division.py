#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 in list

        Args:
            my_list_1: First list
            my_list_2: Second list
            list_length: Length of new list with divisors

        Return:
            New list with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            check_1 = isinstance(a, (int, float))
            check_2 = isinstance(b, (int, float))
            if not check_1 or not check_2:
                print("wrong type")
                new_list.append(0)
            else:
                new_list.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
