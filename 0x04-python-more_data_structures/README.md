# <ins>More Data tructures: Set, Dictionary</ins>

## Introduction
Besides lists and tuples, python has other data structures that help with data organizaion and manipulation. These are:
- Sets
- Dictionaries

- Sets are unordered and immutable data structures which can be formed by the `set()` function. The result willbe a data set that is inside curly braces. Eg.
```
>>>a = set("Joakim")
>>a
>>{'J', 'o', 'a', 'k', 'i', 'm'}
```
Besiedes being immutable, they do not hold **duplicate data**.

Dictionaries are also unordered and mutable. The data can be accessed through _keys_. Dictionaries have the form: _variable = {'key': value}_

## 00 - This function computes the square value of all integers of a matrix.
- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
	- Same size as `matrix`
	- Each value is the square of the value of the input
- Initial matrix is not modified
-No importeed modules
- Allowed use of regular loops, `map`, etc.

## 01 - This function replaces all occurrences of an element by another in a new list.
- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- No modules imported