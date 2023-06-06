#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return
    else:
        indice = my_list[idx]
        return indice
