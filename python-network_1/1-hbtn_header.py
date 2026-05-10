#!/usr/bin/python3
"""Fetches X-Request-Id header from a URL."""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
