# <ins> Test Driven Development</ins>

## Introduction

Test driven development or TDD is a way of coming up with solutions to problems in python by first testing then writing the code and taking care of the errors and fails from the testing.

There is interactive testing and OOP testing. In the former, the module `doctest1 is used to access submodules that help test the code for errors and breakage. It does this by scanning the python file and finding the symbol `>>>` and executing the code as if in interactive mode.

In the OOP approach, `unittests` are used to test for code. The different ways are used by different proogrammers. For instance, the unittest way is used to test code that is majorly in classes. That is why it is OOP oriented.

## 00 - This function  adds 2 integers.
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- No module was imported

## 01 - This function divides all elements of a matrix.
- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the matrix should be divided by `div`, rounded to 2 decimal places
- Returns a new matrix
- No modules were imported

## 02 - This function prints My name is <first name> <last name>
- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raises a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
- No modules were imported

## 03 - This function prints a square with the character #.
- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than `0`, raise a `TypeError` exception with the message `size must be an integer`
- No modules were imported

## 04 - This function prints a text with 2 new lines after each of these characters: ., ? and :
- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
- There should be no space at the beginning or at the end of each printed line
- No module was imported