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
        print("    - type: ", end="")
        print(type(r))
        print("    - content: ", end="")
        print(r)
        print("    - utf8 content: ", end="")
        print(r.decode("utf-8"))
