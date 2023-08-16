#!/usr/bin/python3
def roman_to_int(roman_string):
    check = lambda x, y: True if x not in y else False
    i = 0
    s = ""
    l = len(roman_string)
    while i < l:
        if roman_string[i] == 'M': # thousands
            while i < l and roman_string[i] not in "CDLXIV":
                s += roman_string[i]
                i += 1
            print(s)
        if i < l and roman_string[i] in "CDM": # hundreds
            s = ""
            while i < l and roman_string[i] not in "XLVI":
                s += roman_string[i]
                i += 1
            print(s)
        if i < l and roman_string[i] in "XLC": # tens
            s = ""
            while i < l and roman_string[i] not in "IV":
                s += roman_string[i]
                i += 1
            print(s)
        if i < l and roman_string[i] in "IV": # units
            s = ""
            while i < l:
                s += roman_string[i]
                i += 1
            print(s)
        i += 1


roman_to_int("X")
print("\n\n")

roman_to_int("DCCVII")
print("\n\n")

roman_to_int("D")
print("\n\n")


roman_to_int("LXXXVII")
print("\n\n")

roman_to_int("IX")
print("\n\n")

roman_to_int("VII")
