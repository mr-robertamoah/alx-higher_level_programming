#!/usr/bin/python3

"""
contains script takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    arg = (argv[1], argv[2])
    res = requests.get(url, auth=arg)
    print(res.json().get("id"))
