# <ins>Almost a Circle</ins>

## Introduction
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, I review everything about Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

Additionally,
- `args` and `kwargs`
- Serialization/Deserialization
- JSON

## 01 - Write the first class Base:
- Created a folder named models with an empty file `__init__.py` inside - with this file, the folder will become a Python package
- Create a file named `models/base.py`:
- Class `Base`:
- private class attribute `__nb_objects = 0`
- class constructor: `def __init__(self, id=None):`:
	- if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume id is an integer and you don’t need to test the type of it
	- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

