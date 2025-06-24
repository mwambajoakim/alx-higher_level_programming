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