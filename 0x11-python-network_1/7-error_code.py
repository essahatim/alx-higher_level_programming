#!/usr/bin/python3
"""
Takes in a URL:
    sends a request to the URL
    isplays the body of the response
    If the HTTP status code is greater than or equal to 400:
        prints: Error code
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    r.s_c = response.status_code
    if r.s_c >= 400:
        print("Error code: {}".format(r.s_c))
    else:
        print(response.text)
