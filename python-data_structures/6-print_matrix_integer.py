#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Matrix!"""
    if len(matrix) == 1:
        return print()
    else:
        for i in range(len(matrix)):

            for q in range(len(matrix)):
                if isinstance(matrix[i][q], int):
                    if q == len(matrix) - 1:
                        print("{}".format(matrix[i][q]))
                        break
                    print("{:d}".format(matrix[i][q]), end=" ")
