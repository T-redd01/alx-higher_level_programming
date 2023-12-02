#!/usr/bin/python3
""" accessig github api with requests """
import requests
import sys


if __name__ == "__main__":
    heads = {"Accept": "application/vnd.github+json",
             "Authorization": f"Bearer {sys.argv[2]}"}
    resp = requests.get(f"https://api.github.com/users/{sys.argv[1]}",
                        headers=heads)
    r_dict = resp.json()
    print(r_dict.get("id"))
