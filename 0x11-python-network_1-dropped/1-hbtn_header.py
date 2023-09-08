#!/usr/bin/python3

"""
contains script that fetches argv
"""

import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        r = response.info()
        print(r["X-Request-Id"])
