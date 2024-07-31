#!/usr/bin/python3
# A program that prints numbers from 0 to 99

for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{}, ".format(i), end="")
