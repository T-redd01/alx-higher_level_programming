#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, v))
