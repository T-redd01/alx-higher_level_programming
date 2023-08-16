#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = list(a_dictionary.items())
    for i, v in x:
        if v == value:
            del a_dictionary[i]
    return a_dictionary
