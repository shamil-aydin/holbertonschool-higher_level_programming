#!/usr/bin/python3
"""Sends a request to a URL and handles HTTP error codes."""
import urllib.request
import urllib.error
import sys

if len(sys.argv) > 1:
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
