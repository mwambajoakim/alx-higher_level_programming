# Beginning of Python - Script-writing
## Introduction
Here in this project I go through the basics of Python. I also remind myself how to write scripts that help automate some tasks while developing products.

## 00 - This Shell script runs a Python script.
- The Python file name is saved in the environment variable `$PYFILE`

## 01 - This Shell script runs Python code.
- The Python code will be saved in the environment variable `$PYCODE`

## 02 - This Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
- Uses the function `print`

## 03 - This program prints the integer stored in the variable number, followed by Battery street, followed by a new line.
- The output of the script is:
	- the number, followed by Battery street,
	- followed by a new line
- The variable numberis not cast into a string
- Code is only 3 lines long
- Used f-strings for formatting

## 04 - This program prints the float stored in the variable number with a precision of 2 digits.
- The output of the program is:
	- `Float:`, followed by the float with only 2 digits
	- followed by a new line
- `number` is not cast to a string
- Used f-strings for formatting

## 05 - This program prints 3 times a string stored in the variable str, followed by its first 9 characters.
- The output of the program is:
	- 3 times the value of `str`
	- followed by a new line
	- followed by the 9 first characters of `str`
	- followed by a new line
- No loops or conditional statements
- Program has a maximum of 5 lines

## 06 - This program prints `Welcome to ALX`
- No loops or conditional statements used
- The variables `str1` and `str2` were used
- Program has exactly 5 lines 

## 07 - This program uses python string slicing to achieve the requirements
- No loops or conditionals used
- Program is exactly 8 lines long
- `word_first_3` contains the first 3 letters of the variable `word`
- `word_last_2` contains the last 2 letters of the variable `word`
- `middle_word` contains the value of the variable `word` without the first and last letters

## 08 - This program prints `object-oriented programming with Python`, followed by a new line.
- No loops or coditional statements used
- Program is exactle 5 lines
- No new variables were created
- No string literals were used

## 09 - This Python script prints “The Zen of Python”, by TimPeters, followed by a new line.
- The script has a maximum 98 characters long (checked with `wc -m 9-easter_egg.py`)

## 11 - This Python script prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
- Used the function `write` from the `sys` module
- No use of `print`
- Script prints to `stderr`
- Script exits with the status code 1

## 12 - This Python function `def magic_calculation(a, b):` does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
