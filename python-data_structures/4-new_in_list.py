#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    lista = []

    for i in range(len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return my_list
        elif i == idx:
            lista.insert(i, element)
        else:
            lista.insert(i, my_list[i])

    return lista
