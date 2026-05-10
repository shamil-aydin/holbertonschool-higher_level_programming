#!/usr/bin/python3
"""Uses GitHub API with Basic Auth to display user id."""
import requests
import sys

if len(sys.argv) > 2:
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    print(response.json().get('id'))
