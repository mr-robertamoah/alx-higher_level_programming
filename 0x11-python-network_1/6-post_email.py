#!/usr/bin/python3

"""
contains script takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    data = {}
    data["email"] = argv[2]
    res = requests.post(url, data=data)
    print(res.text)
