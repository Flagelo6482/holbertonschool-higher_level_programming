#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        resultado = a / b
    except:
        resultado = None
    finally:
        print("Inside result: {}".format(resultado))
        return resultado
