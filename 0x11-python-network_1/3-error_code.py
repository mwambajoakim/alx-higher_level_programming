#!/usr/bin/python3
"""Script that prints status code of url"""
from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        status_code = response.getcode()
        print(f"Error Code: {status_code}")
