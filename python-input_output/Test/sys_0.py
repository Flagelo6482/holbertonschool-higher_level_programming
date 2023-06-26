#!/usr/bin/python3
#Funcion que pasamos un archivo de texto y lo imprime en la salida
import sys

my_txt = sys.argv[1]

with open(my_txt, mode="r") as file:
    lec = file.read()
print(lec)
