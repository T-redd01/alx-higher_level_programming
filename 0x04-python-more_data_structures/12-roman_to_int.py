#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0

    units = (("I", 1), ("II", 2), ("III", 3), ("IV", 4), ("V", 5),
             ("VI", 6), ("VII", 7), ("VIII", 8), ("IX", 9))
    tens = (("X", 10), ("XX", 20), ("XXX", 30), ("XL", 40), ("L", 50),
            ("LX", 60), ("LXX", 70), ("LXXX", 80), ("XC", 90))
    hundreds = (("C", 100), ("CC", 200), ("CCC", 300),  ("CD", 400),
                ("D", 500), ("DC", 600), ("DCC", 700),
                ("DCCC", 800), ("CM", 900))
    thousands = (("M", 1000), ("MM", 2000), ("MMM", 3000))
    i = 0
    s = ""
    ln = len(roman_string)
    num = 0
    while i < ln:
        if roman_string[i] == 'M':
            while i < ln and roman_string[i] not in "CDLXIV":
                s += roman_string[i]
                i += 1
            for r, n in thousands:
                if s == r:
                    num += n
        if i < ln and roman_string[i] in "CDM":
            s = ""
            while i < ln and roman_string[i] not in "XLVI":
                s += roman_string[i]
                i += 1
            for r, n in hundreds:
                if s == r:
                    num += n
        if i < ln and roman_string[i] in "XLC":
            s = ""
            while i < ln and roman_string[i] not in "IV":
                s += roman_string[i]
                i += 1
            for r, n in tens:
                if s == r:
                    num += n
        if i < ln and roman_string[i] in "IV":
            s = ""
            while i < ln:
                s += roman_string[i]
                i += 1
            for r, n in units:
                if s == r:
                    num += n
        i += 1
    return num
