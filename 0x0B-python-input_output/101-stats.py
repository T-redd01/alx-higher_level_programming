#!/usr/bin/python3
"""trying to compute metrics"""
import sys

num = 0
counter = 0
my_l = []
try:
    for line in sys.stdin:
        num += len(line)
        counter += 1
        words = line.split(" ")
        new = [words[7], words[8]]
        my_l.append(new)
        my_l.sort()
        if counter == 10:
            counter = 0
            print(f"File size: {num:d}")
            for j in my_l:
                print(f"{j[0]}: {j[1]}")
except KeyboardInterrupt as e:
    print(f"File size: {num:d}")
    for i in my_l:
        print(f"{i[0]}: {i[1]}")
