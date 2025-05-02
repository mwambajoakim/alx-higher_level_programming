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