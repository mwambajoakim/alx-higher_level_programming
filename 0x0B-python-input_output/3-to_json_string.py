#!/usr/bin/python3
"""Data to JSON representation"""
import json


def to_json_string(my_obj):
    """Takes data and turns into JSON object

        Args:
            my_obj: Data to change to JSON

        Return:
            JSON represantation of object
    """
    return json.dumps(my_obj)
