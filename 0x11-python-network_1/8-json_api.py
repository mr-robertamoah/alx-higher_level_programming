#!/usr/bin/python3

"""
contains script takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg = {"q": ""}
    if len(argv) > 1:
        arg["q"] = argv[1]
    res = requests.post(url, data=arg)
    if res.status_code == 204:
        print("No result")
    else:
        try:
            r = res.json()
            if len(r):
                print("[{}] {}".format(r["id"], r["name"]))
            else:
                print("No result")
        except Exception as e:
            print("Not a valid JSON")
