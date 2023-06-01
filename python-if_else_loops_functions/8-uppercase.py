#!/usr/bin/python3
#8-uppercase.py

def uppercase(str):
    """Search uppercase"""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            str_up = str[i].swapcase()
            print("{}".format(str_up), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
