#!/usr/bin/python3

"""
contains script takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter
"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    data = {}
    data["email"] = argv[2]
    data = urllib.parse.urlencode(data)
    data = data.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        r = response.read().encode("utf-8")
        print(r)
