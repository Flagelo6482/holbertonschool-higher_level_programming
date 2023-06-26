#!/usr/bin/python3
#Funcion para leer los argumentos del pront
import sys

new_list = []
i = 0

while i < len(sys.argv):
    if i == 0:
        i += 1
        continue
    else:
        new_list.append(sys.argv[i])
        i += 1
print(new_list)
