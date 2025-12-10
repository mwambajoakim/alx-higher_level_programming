#!/usr/bin/python3
"""Script that requests a url and prints the response"""
import requests


if __name__ == "__main__":
    url = "https://www.google.com"
    req = requests.get(url)
    print("Body Response:")
    print(f"\t- type: ", type(req.text))
    print(f"\t- content: {req.text}")
