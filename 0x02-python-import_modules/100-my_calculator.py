#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv
    if a[2] == '+':
        print(f"{a[1]} {a[2]} {a[3]} = {add(int(a[1]), int(a[3])):d}")
    elif a[2] == '-':
        print(f"{a[1]} {a[2]} {a[3]} = {sub(int(a[1]), int(a[3])):d}")
    elif a[2] == '/':
        print(f"{a[1]} {a[2]} {a[3]} = {div(int(a[1]), int(a[3])):d}")
    elif a[2] == '*':
        print(f"{a[1]} {a[2]} {a[3]} = {mul(int(a[1]), int(a[3])):d}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
