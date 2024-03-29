#!/usr/bin/python3
"""
Takes in a URL:
    sends a request to the URL
    displays the body of the response (decoded in utf-8)
    handles urllib.error.HTTPError exceptions
    prints the HTTP status code
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
