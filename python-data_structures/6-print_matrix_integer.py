#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print()
    else:
        for i in range(len(matrix)):
            for q in range(len(matrix)):
                if q == len(matrix) - 1:
                    print("{}".format(matrix[i][q]))
                    break
                print("{:d}".format(matrix[i][q]), end=" ")
