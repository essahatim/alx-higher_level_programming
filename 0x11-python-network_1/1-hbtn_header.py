#!/usr/bin/python3
"""
Takes in a URL
    sends a request to the URL
    displays the value of the X-Request-Id in the header of the response
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
