#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    new_str = ""
    i = 0
    while i < length:
        if (ord(str[i]) >= ord("a") and ord(str[i]) <= ord("z")):
            new_str = chr(ord(str[i]) - (ord("a") - ord("A")))
        else:
            new_str = str[i]
        print("{}". format(new_str), end="")
        i += 1
    print()
