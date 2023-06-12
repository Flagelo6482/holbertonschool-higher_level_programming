#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        formated = " ".join(["{:d}".format(num) for num in i])
        print(formated)
