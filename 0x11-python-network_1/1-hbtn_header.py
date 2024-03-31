#!/usr/bin/python3
"""
Module documentation a Python script that takes in a URL
"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    reqes = urllib.request.Request(url)
    with urllib.request.urlopen(reqes) as response:
        request_id = response.getheader("X-Request-Id")
    print(request_id)
