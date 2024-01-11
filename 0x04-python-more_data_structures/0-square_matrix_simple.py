#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        raised_to_power = list(map(lambda x: x**2, matrix[i]))
        new_matrix.append(raised_to_power)
    return new_matrix
