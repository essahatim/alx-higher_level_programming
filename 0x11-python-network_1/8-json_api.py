#!/usr/bin/python3
"""
Takes in a letter:
    sends a POST request to http://0.0.0.0:5000/search_user
"""


import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=({'q': q}))
    try:
        json_resp = response.json()
        id, name = json_resp.get('id'), json_resp.get('name')
        if json_resp:
            print("[{}] {}".format(get('id'), get('name')))

        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
