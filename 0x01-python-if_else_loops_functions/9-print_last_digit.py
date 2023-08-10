#!/usr/bin/python3
def print_last_digit(number):
    dig = 0
    if number < 0:
        dig = (number * -1) % 10
    else:
        dig = number % 10

    print(f"{dig:d}", end='')
    return dig
