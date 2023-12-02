#!/usr/bin/python3
""" searching value and checking json with requests """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        search = ""
    else:
        search = sys.argv[1]
    args = {'q': search}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=args)
    r_dict = resp.json()
    if len(r_dict) == 0:
        print("No result")
    elif "application/json" not in resp.headers.get("content-type", ""):
        print("Not a valid JSON")
    else:
        print(f"[{r_dict.get('id')}] {r_dict.get('name')}")
