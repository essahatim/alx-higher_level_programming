#!/usr/bin/python3
"""
Take GitHub API to display the user's id:
    using Basic Authentication with a personal access token
"""


import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    url = 'https://api.github.com/users/{}'.format(username)
    response = requests.get(url, auth=HTTPBasicAuth(username, sys.argv[2]))
    print(response.json().get('id'))
