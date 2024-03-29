#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status:
    using requests package
"""


import requests

if __name__ : "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    body = requests.get(url).text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content: {}".format(body)
