#!/usr/bin/python3

"""
contains script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    r = r.text
    print("Body response:")
    print("\t- type: ", end="")
    print(type(r))
    print("\t- content: ", end="")
    print(r)
