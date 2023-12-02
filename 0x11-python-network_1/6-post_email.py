#!/usr/bin/python3
""" spost request an email with requests """
import requests
import sys


if __name__ == "__main__":
    args = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data=args)
    print(resp.text)
