#!/usr/bin/python3
"""Manage id attribute"""
import json


class Base:
    """This class defines the id attribute

        Args:
            id: Class id

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a list of JSON dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation into a file"""
        filename = f"{cls.__name__}.json"
        list_dictionaries = []
        with open(filename, 'w', encoding="UTF-8") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                for val in list_objs:
                    list_dictionaries.append(val.to_dictionary())
                json_str = cls.to_json_string(list_dictionaries)
                json_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)
