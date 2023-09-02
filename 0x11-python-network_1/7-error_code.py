#!/usr/bin/python3

"""
contains script takes in a URL,
sends a request to the URL and displays
the body of the response
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
