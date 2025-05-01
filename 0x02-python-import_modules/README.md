# <ins>Import and Modules</ins>

## Introduction
In this project, I go through the python Import and Modules.

Modules are like what we call libraries in C. They store different functions and packages that can be called and used in a file.

For one to call such modules and functions, they would need to use import in the file they are working on. For example to use the `pow` function in the math library,
```
import math

def main:
a = 2
b = 3
c = math.pow(a, b)

print("{}".format(c))

```

## 00 - This program imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

- Used print function with string format to display integers
- Assigned the value:
	- `1` to a variable called `a`
	- `2` to a variable called `b`
- and used those two variables as arguments when calling the functions `add` and `print`
- `a` and `b` are defined in 2 different lines: `a = 1` and another `b = 2`
- Program  prints: `<a value> + <b value> = <add(a, b) value> `followed with a new line
- Used the word` add_0` once in the code
- Neither used `*` or `*__import__` for importing 
- The code is not executed when imported - by using `__import__`

## 01 - This program imports functions from the file calculator_1.py, does some Maths, and prints the result.

- Did not use the function print (with string format to display integers) more than 4 times
- Defined the value:
	- `10` to a variable `a`
	- `5` to a variable `b`
- and used those two variables only, as arguments when calling functions (including `print`)
- `a` and `b` are defined in 2 different lines: `a = 10` and another `b = 5`
- The program calls each of the imported functions.
- The word `calculator_1` is used only once in the file
- Neither used `*` or `__import__` for importing 
- The code is not
 executed when imported

 ## 02 - This program prints the number of and the list of its arguments.
- The output is:
	- Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
	- `:` (or `.` if no arguments were passed) followed by
	- a new line, followed by (if at least one argument),
	- one line per argument:
		- the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
- The code is not executed when imported
The number of elements of `argv` is retrieved by using: `len(argv)`

## 03 - This program prints the result of the addition of all arguments
- The output is the result of the addition of all arguments, followed by a new line
- All arguments have been cast into integers by using `int() `(you can assume that all arguments can be casted into integers)
- The code is not executed when imported

# 05 - This program imports the variable a from the file variable_load_5.py and prints its value.
- Neither used `*` or `__import__` for importing 
- The code is not executed when imported