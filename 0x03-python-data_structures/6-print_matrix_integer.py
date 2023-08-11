#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """print a 2 dimensional list of integers
    
        Args:
            matrix: 2d array of integers
    """
    for i in matrix:
        for j, v in enumerate(i):
            if j == 0:
                print("{:d}".format(v), end='')
            print(", {:d}".format(v), end='')
        print("")
