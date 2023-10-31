#!/usr/bin/python3
'''Task 1'''


def matrix_divided(matrix, div):
    if (
            not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(x, int) or isinstance(x, float)
                for row in matrix
                for x in row
            )
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists)"
                " of integers/floats"
                )
    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, float) and not isinstance(div, int)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return ([[round(float(x)/div, 2) for x in row] for row in matrix])

#    new_matrix = list()
#    for row in matrix:
#        new_row = list()
#        for element in row:
#            new_row.append(round(element / div, 2))
#        new_matrix.append(new_row)
#    return new_matrix
