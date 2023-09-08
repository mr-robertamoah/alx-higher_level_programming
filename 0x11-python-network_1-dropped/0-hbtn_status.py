#!/usr/bin/python3

"""
contains script that fetches
https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        r = response.read()
        print("Body response:")
        print("\t- type: ", end="")
        print(type(r))
        print("\t- content: ", end="")
        print(r)
        print("\t- utf8 content: ", end="")
        print(r.decode("utf-8"))
