#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []

    for j in matrix:
        lista = []
        for i in j:
            lista.append(i ** 2)
        new_list.append(lista)
    return new_list
