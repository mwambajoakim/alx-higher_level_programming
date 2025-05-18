#!/usr/bin/python3
for i in range(122, 64, -1):
    if i > 96 and i % 2 != 0:
        i = i - 32
    elif i >= 65 and i <= 96:
        continue
    print("{}".format(chr(i)), end="")
