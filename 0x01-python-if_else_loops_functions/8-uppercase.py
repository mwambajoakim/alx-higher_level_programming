#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    i = 0
    while i < length:
        if (ord(str[i]) >= ord("a") and ord(str[i]) <= ord("z")):
            print("{}".format(chr(ord(str[i]) - (ord("a") - ord("A")))),
                  end="")
        else:
            print("{}".format(str[i]), end="")
        i += 1
    print()
