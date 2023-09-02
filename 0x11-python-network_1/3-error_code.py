#!/usr/bin/python3

"""
contains script takes in a URL,
sends a request to the URL and displays
the body of the response
"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            r = response.read()
            print(r)
    except urllib.error.HTTPError as e:
        print("Error code: {}".formar(e.code))
