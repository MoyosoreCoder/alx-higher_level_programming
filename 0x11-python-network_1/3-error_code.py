#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: {} <URL>".format(sys.argv[0]))
            sys.exit(1)

            url = sys.argv[1]
            try:
                with urllib.request.urlopen(url) as response:
                    print(response.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                print("Error code: {}".format(e.code))
            except urllib.error.URLError as e:
                print("Failed to reach the server:", e.reason)
