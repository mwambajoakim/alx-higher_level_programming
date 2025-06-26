#!/usr/bin/python3
"""Creates a class that defines a student"""


class Student:
    """Istantiates a student with first, last name and age

        Args:
            first_name: First name of student
            last_name: Last name of student
            age: Age of the student

        Return: 
            Dictionary representation of Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
