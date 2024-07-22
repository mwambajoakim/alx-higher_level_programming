#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dgt = number % 10
ld = "Last digit of"

if l_dgt > 5:
    print("{} {} is {} and is greater than 5".format(ld, number, l_dgt))
elif l_dgt == 0:
    print("{} {} is {} and is 0".format(ld, number, l_dgt))
elif l_dgt < 6 and l_dgt != 0:
    print("{} {} is {} and is less than 6 and not 0".format(ld, number, l_dgt))
