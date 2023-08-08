#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print(ord(c))
        return True
    return False


print("H => {}".format("lower" if islower("H") else "upper"))

print("'4' => {}".format("lower" if islower("4") else "upper"))

print("'!' => {}".format("lower" if islower("!") else "upper"))
