#!/usr/bin/python3
"""Writes JSON to a txt file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves writes my-obj content to filename

        Args:
            my_obj: JSON data to write
            filename: File name to write to
    """
    with open(filename, 'w', encoding="UTF-8") as write_JSON:
        write_JSON.write(json.dumps(my_obj))
