#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        return [[j**2 for j in i] for i in matrix]
