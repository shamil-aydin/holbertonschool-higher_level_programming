#!/usr/bin/python3
"""Sends a POST request with a letter and displays JSON result."""
import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""
response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

try:
    result = response.json()
    if result:
        print("[{}] {}".format(result.get('id'), result.get('name')))
    else:
        print("No result")
except Exception:
    print("Not a valid JSON")
