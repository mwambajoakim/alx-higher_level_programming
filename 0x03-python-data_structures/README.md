# <ins>Python Data Structures</ins>

## Introduction

Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. - Python Docs

## 00 - This function prints all integers of a list.
- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line.
- No modules were imported
- Assuming that the list only contains integers
- No integers were cast to a string
- Used the `str.format()` to print integers

## 01 - This function retrieves an element from a list like in C.
- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function returns None
- If `idx` is out of range (> of number of element in `my_list`), the function returns None
- No modules were imported
- Did not use `try/except`

## 02- This function replaces an element of a list at a specific position (like in C).

- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function does not modify anything, and returns the original list
- If `idx` is out of range (> of number of element in my_list), the function does not modify anything, and returns the original list
- No modules were imported
- Did not use `try/except`

## 03 - This function prints all integers of a list, in reverse order.
- Prototype: `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line
- No module was imported
- Assuming that the list only contains integers
- No integers were cast to a string
- Used str.format() to print integers

## 04 - This function replaces an element in a list at a specific position without modifying the original list (like in C).
- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative, the function returns a copy of the original list
- If `idx` is out of range (> of number of element in my_list), the function  returns a copy of the original list
- No modules are imported
- No use of `try/except`

## 05 - This function removes all characters c and C from a string.
- Prototype: `def no_c(my_string):`
- The function returns the new string
- No modules are imported
- No use of `str.replace()`

## 06 - This function prints a matrix of integers.
- Prototype: `def print_matrix_integer(matrix=[[]]):`
- No modules are imported
- Assumption that the list only contains integers
- No integers cast into strings
- Used `str.format()` to print integers

## 07 - This function adds 2 tuples.
- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
- The first element is the addition of the first element of each argument
- The second element is the addition of the second element of each argument
- No modules are imported
- Assuming that the two tuples will contain integers
- If a tuple is smaller than 2, use the value `0` for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

## 08 - This function returns a tuple with the length of a string and its first character.
- Prototype: `def multiple_returns(sentence):`
- If the `sentence` is empty, the first character should be equal to `None`
- No imported modules

## 09 - This function finds the biggest integer of a list.
- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, returns `None`
- Assuming that the list only contains integers
- No imported modules
- No use of the builtin `max()`

## 10 - This function finds all multiples of 2 in a list.
- Prototype: `def divisible_by_2(my_list=[]):`
- Returns a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- No imported modules