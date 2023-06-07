#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        flag = 0
        for j in i:
            if flag == 0:
                flag = 1
            else:
                print(" ", end="")
            print("{:d}".format(j), end=" ")
        print("")
