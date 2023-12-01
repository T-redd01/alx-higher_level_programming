#!/usr/bin/python3
""" parse.urlencode turns get to post request """
from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    req = request.Request(sys.argv[1])
    with request.urlopen(req, data) as resp:
        body = resp.read().decode("utf-8")
        print(f"{body}")
