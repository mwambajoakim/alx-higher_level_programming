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