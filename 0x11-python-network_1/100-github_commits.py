#!/usr/bin/python3

"""
contains script takes 2 arguments in order tp
list 10 commits (from the most recent to oldest)
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/"
    url += argv[2] + "/" + argv[1] + "/commits"
    res = requests.get(url)
    r = res.json()
    for commit in r[:10]:
        print("{}: {}".format(
              commit.get("sha"),
              commit.get("commit").get("author").get("name")))
