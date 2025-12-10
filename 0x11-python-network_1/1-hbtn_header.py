#!/usr/bin/python3
"""
Fetches url content X-Request-Id
"""
from urllib import request
import sys

url = sys.argv[1]

with request.urlopen(url) as response:
    id_request = response.headers.get("X-Request-Id")
    print(id_request)
