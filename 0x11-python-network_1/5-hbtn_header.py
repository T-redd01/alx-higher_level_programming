#!/usr/bin/python3
""" get header content using requests """
import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    head = resp.headers
    print(head.get("X-Request-Id"))
