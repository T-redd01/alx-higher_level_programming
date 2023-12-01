#!/usr/bin/python3
""" handling http errors """
from urllib import request
from urllib.error import HTTPError
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as e:
        print(f"Error code: {e.code}")
