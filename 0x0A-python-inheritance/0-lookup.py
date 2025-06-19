#!/usr/bin/python3
"""Module of a function that returns methods and
attributes of a class"""


def lookup(obj):
    """Returns list of available attributes and methods"""
    list = []
    list.append(dir(obj))
    return list
