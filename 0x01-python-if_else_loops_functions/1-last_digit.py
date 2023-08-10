#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = 0

if number < 0:
    dig = ((number * -1) % 10) * -1
else:
    dig = number % 10

print(f"Last digit of {number:d} is {dig:d}", end=' ')
if dig > 5:
    print("and is greater than 5")
elif dig < 6 and dig != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
