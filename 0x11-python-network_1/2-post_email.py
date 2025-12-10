#!/usr/bin/python3
"""
Script that parses data and uses POST to send it
in a url
"""
from urllib import parse, request
import sys


if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    url = sys.argv[1]

    encoded_data = parse.urlencode(data).encode('ascii')

    request = request.Request(url, data=encoded_data, method='POST')

    with request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
