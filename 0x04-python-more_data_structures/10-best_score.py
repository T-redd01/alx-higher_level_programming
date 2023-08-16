#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        m = 0
        k = None
        for i, v in a_dictionary.items():
            if v > m:
                print(v, m, i)
                m, k = v, i
        return k
