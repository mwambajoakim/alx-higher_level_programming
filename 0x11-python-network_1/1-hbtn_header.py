#!/usr/bin/python3
"""
Script that takes a URL, sends a request to it,
and displays the value of the X-Request-Id header.
"""
from urllib import request
import sys

url = sys.argv[1]

with request.urlopen(url) as response:
    id_request = response.headers.get("X-Request-Id")
    print(id_request)
