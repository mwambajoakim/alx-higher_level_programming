#!/usr/bin/python3
"""Deserializes a JSON object to python"""
import json


def from_json_string(my_str):
    """Deserializes my_str to python data

        Args:
            my_str: JSON object to deserialize

        Return:
            Deserialized object
    """
    return json.loads(my_str)
