# <ins>Python Inheritance</ins>

## Introduction
In python, one can create a subclass from a class using inheritance. It basically means a child class (subclass) inherits a parent class (baseclass).

This means that whenever an instance of the child class is created, the parent class is inherited in that instance.

For example:
```
class Animal:
      def __init__(self, name):
      	  self.name = name

class Dog(Animal):
      def sound(self):
      	  super().__init__(self)
	  print("{} barks".format(self.name))
```
The `Dog` is a subclass of `Animal`. Any instance of `Dog` created will inherit from `Animal`.

## 00 - This function returns the list of available attributes and methods of an object:
- Prototype: `def lookup(obj):`
- Returns a list object
- No modules imported

## 01 - This class MyList inherits from list:
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type `int`
- No modules imported

## 02 - This function returns True if the object is exactly an instance of the specified class ; otherwise False.
- Prototype: `def is_same_class(obj, a_class):`
- No modules imported

## 03 - This function returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
- Prototype: `def is_kind_of_class(obj, a_class):`
- No modules imported


## 04 - This function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
- Prototype: `def inherits_from(obj, a_class):`
- No modules imported


## 05 - This is an empty class BaseGeometry.
- ` class BaseGeometry`
- No modules imported

## 06 - This is a class BaseGeometry (based on 5-base_geometry.py).
- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- No modules imported

## 07 - This class Rectangle inherits from BaseGeometry (7-base_geometry.py).
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
- `width` and `height` must be private. No getter or setter
- `width` and `height` must be positive integers, validated by `integer_validator`