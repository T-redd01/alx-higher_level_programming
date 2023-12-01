#!/usr/bin/python3
""" display url header content with urllib """
from urllib import request
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as resp:
        headers = resp.getheaders()
        for i in headers:
            if i[0] == "X-Request-Id":
                print(f"{i[1]}")
