#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    returns a matrix of integers which are the results
    of the division of another matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) != list or not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row]):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    else:
        if len(matrix) == 3:
            if len(matrix[0]) != len(matrix[2]):
                raise TypeError("Each row of the matrix must have the same size")
        new_matrix = []
        for i in range(len(matrix)):
            divided_int = list(map(lambda x: round(x / div, 2), matrix[i]))
            new_matrix.append(divided_int)
        return new_matrix
