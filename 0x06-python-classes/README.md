# <ins>Classes and Objects</ins>

## Introduction
Classes are a way of grouping data together. It is a way to hold datat that is similar to different things. For example, we can have the class car that defines the type, the company, the model and so on. With the help of classes, we are able to create objects which are the different instances of the same class. Say for example, for our `class Car`, we can create an instance for the model Toyota.

In these classes we have attributes (characteristics) and we also have methods (actions). These are a way to help manipulate data for the different instances of a class.

Let's delve in.

## 00 - This empty class Square defines a square:
- No modules were imported

## 01 - This class Square defines a square by: (based on `0-square.py`)
- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- No modules imported

## 02 - This class Square defines a square by: (based on 1-square.py)
- Private instance attribute: `size`
- Instantiation with optional size: `def __init__(self, size=0):`
	- `size` must be an integer, otherwise raises a `TypeError` exception with the message `size must be an integer`
	- if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
- No imported modules