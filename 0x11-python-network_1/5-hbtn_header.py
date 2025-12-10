#!/usr/bin/python3
"""Script that fetches the X-Response-Id from
a url"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    response_id = response.headers.get("X-Response-Id")
    print(response_id)
