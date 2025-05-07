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

## 02 - This function adds all unique integers in a list (only once for each integer).
- Prototype: `def uniqa_add(my_list=[]):`
- No imported modules

## 03 - This function returns a set of common elements in two sets.
- Prototype: `def common_elements(set_1, set_2):`
- No imported modules

## 04 - This function returns a set of all elements present in only one set.
- Prototype: `def only_diff_elements(set_1, set_2):`
- No imported module

## 05 - This function returns the number of keys in a dictionary.
- Prototype: `def number_keys(a_dictionary):`
- No imported module

## 06 - This function prints a dictionary by ordered keys.
- Prototype: `def print_sorted_dictionary(a_dictionary):`
- Assume that all keys are strings
- Keys will be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- No imported modules

## 07 - This function replaces or adds key/value in a dictionary.
- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- No imported modules