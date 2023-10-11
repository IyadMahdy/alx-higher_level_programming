#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lamda row: list(map(lambda x: x**2, row)), matrix))
