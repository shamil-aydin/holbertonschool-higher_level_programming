#!/usr/bin/python3
"""Sends a request to a URL and handles HTTP error codes."""
import requests
import sys

if len(sys.argv) > 1:
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
