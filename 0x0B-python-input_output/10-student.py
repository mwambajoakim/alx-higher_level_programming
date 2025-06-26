#!/usr/bin/python3
"""Creates a class Student"""


class Student:
    """Instantiates class Student using first name, last name and age

        Args:
            first_name: First name of student
            last_name: Last name of student
            age: Age of student

        Return:
            Dictionary representation of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
