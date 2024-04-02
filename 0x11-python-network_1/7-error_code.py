#!/usr/bin/python3
"""
Takes in a URL:
    sends a request to the URL
    displays the body of the response
    If the HTTP status code is greater than or equal to 400:
        prints: Error code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    status_code = response.status_code
    print(response.text) if status_code < 400 else print(
        "Error code: {}".format(status_code))
