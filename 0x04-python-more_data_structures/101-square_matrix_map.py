#!/usr/bin/python3
#101-square_matrix_map.py


def square_matrix_map(matrix=[]):
    """The function that computes the square value of all integers of a matrix using map."""
    return (list(map(lambda x: list(map(lambda z: z**2, x)), matrix)))
