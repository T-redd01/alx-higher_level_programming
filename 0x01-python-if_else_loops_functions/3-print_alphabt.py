#!/usr/bin/python3
for i in range(97, 122):
    if chr(i) in "qe":
        continue
    print("{:c}".format(i), end='')
