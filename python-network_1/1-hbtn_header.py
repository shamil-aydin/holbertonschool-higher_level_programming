#!/usr/bin/python3
"""Script that takes a URL, sends a request and displays X-Request-Id header."""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
