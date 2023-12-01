#!/usr/bin/python3
""" requesting data from url with urllib """
from urllib import request


if __name__ == "__main__":
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as resp:
        body = resp.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
