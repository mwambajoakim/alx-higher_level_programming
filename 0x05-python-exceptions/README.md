# <ins>Errors and Exceptions</ins>

## Introduction
Python offers a way to handle errors and help the user of your code not to panic when code breaks.
 By using the `try` and `except` cases, a programmer is able to tell the code, "Do this but in case you encounter an error while at it, do this other thing".
 ```
 try:
	<expression>
 except:
	<expression>
```

## 00 - This function that prints x elements of a list.
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements are printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try:` / `except:`
- No modules imported
- No use of `len()`

## 01 - This function that prints an integer with "{:d}".format().
- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if value has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False`
- Used `try:` / `except:`
- Used `"{:d}".format()` to print as integer
- No modules imported
- No use of `type()`