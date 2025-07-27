#!/usr/bin/python3
"""Executes a function safely"""
import sys


def safe_function(fct, *args):
    """Uses try and except to handle a function

    Args:
        fct: Pointer to function
        args: Arguments that fct uses

    Return:
          True: If safely executed
          None: Otherwise
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
