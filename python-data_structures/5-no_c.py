#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    tmp = my_string
    delete = "cC"

    tmp = ''.join(x for x in tmp if x not in delete)

    return tmp
