#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve
"""


import requests
from sys import argv

if __name__ == '__main__':
    username = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], username)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
