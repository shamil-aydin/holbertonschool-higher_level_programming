#!/usr/bin/python3
"""Sends a POST request with email parameter to a URL."""
import requests
import sys

if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
