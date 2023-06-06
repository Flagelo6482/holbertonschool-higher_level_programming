#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    else:
        for i in range(len(matrix)):
            for q in range(len(matrix)):
                if isinstance(matrix[i][q], int):
                    print("{}".format(matrix[i][q]), end=" ")
            print()
