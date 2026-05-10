#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header."""
import urllib.request
import sys

if len(sys.argv) > 1:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
