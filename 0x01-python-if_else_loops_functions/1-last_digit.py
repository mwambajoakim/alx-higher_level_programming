#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
    last_digit = number % 10
    last_digit = -last_digit
    number = number * -1
    if last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number, number % 10))
    else:
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, last_digit))
else:
    if number % 10 > 5:
        print("Last digit of {} is {} and is greater than 5"
              .format(number, number % 10))
    elif ((number % 10 < 6) and (number % 10 != 0)):
        print("Last digit of {} is {} and is less than 6 and not 0"
              .format(number, number % 10))
    else:
        print("Last digit of {} is {} and is 0".format(number, number % 10))
