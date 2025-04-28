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

## 00 - This program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

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