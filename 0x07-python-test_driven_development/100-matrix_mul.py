#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """multiply 2 matrices

    Args:
        m_a (list): a list of list with floats or ints
        m_b (list): a list of lists with floats or ints

    Returns:
        new matrix with multiplied values
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    if isinstance(m_a[0], list):
        l_len = len(m_a[0])
    for i in m_a:
        if i == []:
            raise ValueError("m_a can't be empty")
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) != l_len:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    
    if m_b == []:
        raise ValueError("m_b can't be empty")
    if isinstance(m_b[0], list):
        l_len = len(m_b[0])
    for i in m_b:
        if i == []:
            raise ValueError("m_b can't be empty")
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        if len(i) != l_len:
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = [[0 for i in range(len(m_b[0]))] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
