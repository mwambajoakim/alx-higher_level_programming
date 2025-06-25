#!/usr/bin/python3
"""Create object form JSON file"""
import json


def load_from_json_file(filename):
    """Load JSON from filename and deserialize

        Args:
            filename: File containing JSON

    """
    with open(filename, 'r') as from_JSON:
        return json.load(from_JSON)
