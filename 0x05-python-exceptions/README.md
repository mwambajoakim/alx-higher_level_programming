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

## 00 - This function prints x elements of a list.
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements are printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try:` / `except:`
- No modules imported
- No use of `len()`

## 01 - This function prints an integer with "{:d}".format().
- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if value has been correctly printed (it means the `value` is an integer)
- Otherwise, returns `False`
- Used `try:` / `except:`
- Used `"{:d}".format()` to print as integer
- No modules imported
- No use of `type()`

## 02 - This function prints the first x elements of a list and only integers.
- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All integers are printed on the same line followed by a new line - other type of value in the list is skipped (in silence).
- `x` represents the number of elements to access in `my_list`
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- Used `try:` / `except:`
- Used `"{:d}".format()` to print an integer
- No imported modules
- No use of `len()`

## 03 - This function divides 2 integers and prints the result.
- Prototype: `def safe_print_division(a, b):`
- Assuming that `a` and `b` are integers
- The result of the division should print on the `finally:` section preceded by `Inside result:`
- Returns the value of the division, otherwise: `None`
- Used `try: / except: / finally:`
- Used `"{}".format()` to print the result
- No modules imported

## 04 - This function divides element by element 2 lists.
- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
- `list_length` can be bigger than the length of both lists
- Returns a new list (length = `list_length`) with all divisions
- If 2 elements can’t be divided, the division result should be equal to `0`
- If an element is not an integer or float:
	- print: `wrong type`
- If the division can’t be done (/0):
	- print: `division by 0`
- If my_list_1 or my_list_2 is too short
	- print: `out of range`
- You have to use `try: / except: / finally:`
- No imported modules_

## 05 - This function raises a type exception.
- Prototype: `def raise_exception():`
- No imported modules

## 06 - This unction raises a name exception with a message.
- Prototype: `def raise_exception_msg(message=""):`
- No imported modules

## 07 - This function prints an integer.
- Prototype: `def safe_print_integer_err(value):`
- `value` can be any type (integer, string, etc.)
- The integer is printed followed by a new line
- Returns `True` if value has been correctly printed (it means the value is an integer)
- Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
- Used `try:` / `except:`
- Used `"{:d}".format()` to print as integer
- No use of `type()`