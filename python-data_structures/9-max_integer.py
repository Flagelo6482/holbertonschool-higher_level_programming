#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_valor = my_list[0]
        for num in my_list:
            if num > max_valor:
                max_valor = num
        return max_valor
