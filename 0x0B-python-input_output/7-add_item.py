#!/usr/bin/python3
"""Script that adds all arguments to a Python list.
Saves them to a file"""

import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    filename = "add_item.json"

    if os.path.exists(filename):
        py_list = load_from_json_file(filename)
    else:
        py_list = []
    py_list.extend(sys.argv[1:])
    save_to_json_file(py_list, filename)
