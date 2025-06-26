# <ins>Python Input and Output</ins>

## Introduction
Reading and writing and appending text into files in python is quite straightforward. The open function takes care of this.
```
>>>open("filename", mode, encoding)
```
- _filename_ is the name of the file. open() creates a new file if the file does not exist.
- _mode_ is the way in which we want to view the file as. This can be:
	- 'r' for read
	- 'w' for write
	- 'a' for append
	- 'b' as bytes
	**if omitted, python automatically opens the file in read mode.**
-_ encoding_ the specific encoding of the operating system. For example UNIX systems use the UTF-8 encoding


## 00 - This function reads a text file (UTF8) and prints it to stdout:
- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- No modules imported

## 01 - This function writes a string to a text file (UTF8) and returns the number of characters written:
- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- No modules imported

## 02 - This function appends a string at the end of a text file (UTF8) and returns the number of characters added:
- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- No modules imported


## 03 - This function returns the JSON representation of an object (string):
- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.

## 04 - This function returns an object (Python data structure) represented by a JSON string:
- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

## 05 - This function writes an Object to a text file, using a JSON representation:
- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage `file permission` exceptions.

## 06 - This function creates an Object from a “JSON file”:
- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage `file permissions / exceptions`

## 07 - This script adds all arguments to a Python list, and then save them to a file:
- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a `JSON` representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage `file permissions / exceptions`.

## 08 - This function returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- No imported modules

## 09 - This is a class Student that defines a student by:
- Public instance attributes:
	- `first_name`
	- `last_name`
	- `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as 8-class_to_json.py)
- No modules imported