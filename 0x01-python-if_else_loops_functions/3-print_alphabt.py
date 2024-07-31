#!/usr/bin/python3
# A program that prints ASCII alphabet in lowercase

for char in range(97, 123):
    if char != 101 and char != 113:
        print("{}".format(chr(char)), end="")
