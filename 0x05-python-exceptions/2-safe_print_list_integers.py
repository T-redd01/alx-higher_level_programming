#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not isinstance(my_list, list):
        return 0

    els = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            els += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print("")
    return els
