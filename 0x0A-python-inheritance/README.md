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