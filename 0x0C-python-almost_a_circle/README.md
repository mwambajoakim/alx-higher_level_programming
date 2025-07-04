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

## 01 - Wrote the first class Base:
- Created a folder named models with an empty file `__init__.py` inside - with this file, the folder will become a Python package
- Create a file named `models/base.py`:
- Class `Base`:
- private class attribute `__nb_objects = 0`
- class constructor: `def __init__(self, id=None):`:
	- if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume id is an integer and you don’t need to test the type of it
	- otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

## 02 - Wrote the class Rectangle that inherits from Base:
- In the file `models/rectangle.py`
- Class `Rectangle` inherits from `Base`
- Private instance attributes, each with its own public getter and setter:
	- `__width -> width`
	- `__height -> height`
	- `__x -> x`
	- `__y -> y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
	- Called the super class with `id` - this super call with use the logic of the `__init__` of the Base class
	- Assigned each argument `width`, `height`, `x` and `y` to the right attribute

## 03 - Updated the class Rectangle by adding validation of all setter methods and instantiation (id excluded):
- If the input is not an integer, raises the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
- If `width` or `height` is under or equals `0`, raises the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
- If `x` or `y` is under `0`, raises the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

## 04 - Updated the class Rectangle.
- Added the public method `def area(self):` 
- Returns the area value of the `Rectangle` instance.

## 05 - Update the class Rectangle
- Added the public method `def display(self):`
- Prints in stdout the `Rectangle` instance with the character `#` 
- Did not yet handle `x` and `y` here.

## 06 - Updated the class Rectangle
- Overrode the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

## 07 - Updated the class Rectangle
- Improved the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`

## 08 - Updated the class Rectangle
- Added the public method `def update(self, *args):` that assigns an argument to each attribute:
- 1st argument should be the `id` attribute
- 2nd argument should be the `width` attribute
- 3rd argument should be the `height` attribute
- 4th argument should be the `x` attribute
- 5th argument should be the `y` attribute

## 09 Updated the class Rectangle
- Updated the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:
- `**kwargs` can be thought of as a double pointer to a dictionary: key/value
	- As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance

## 10 - Wrote the class Square that inherits from Rectangle:
- In the file `models/square.py`
- Class S`quare` inherits from `Rectangle`
- Class constructor: `def __init__(self, size, x=0, y=0, id=None):`:
	- Called the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` must be assigned to the value of `size`
	- Created new attributes for this class, use all attributes of `Rectangle` - As reminder: a Square is a Rectangle with the same width and height
	- All `width`, `height`, `x` and `y` validation must inherit from Rectangle - same behavior in case of wrong data
- The overloading `__str__` method should returns `[Square] (<id>) <x>/<y> - <size>` - in our case, width or height

## 11 - Updated the class Square by adding the public getter and setter size
- The setter assigns (in this order) the `width` and the `height` - with the same value
- The setter has the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from width)

## 12 - Updated the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:
- `*args` is the list of arguments - no-keyworded arguments
	- 1st argument should be the `id` attribute
	- 2nd argument should be the `size` attribute
	- 3rd argument should be the `x` attribute
	- 4th argument should be the `y` attribute
- `**kwargs` is skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance