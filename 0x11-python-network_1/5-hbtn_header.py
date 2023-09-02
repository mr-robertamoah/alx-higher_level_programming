#!/usr/bin/python3

"""
contains script that takes in a URL,
sends a request to the URL and displays the value
of the variable X-Request-Id
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers["X-Request-Id"])
