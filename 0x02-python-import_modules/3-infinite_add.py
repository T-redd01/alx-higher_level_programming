#!/usr/bin/python3
import sys

if __name__ == "__main__":
    x = 0
    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        x += int(v)
    print(x)
