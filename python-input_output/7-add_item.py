#!/usr/bin/python3


"""Load, add, save"""


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
i = 1

try:
    new_list = load_from_json_file(file)
except BaseException:
    new_list = list()

#Agregamos todos los argumentos en una lista
while i < len(sys.argv):
    new_list.append(sys.argv[i])
    i += 1

save_to_json_file(new_list, file)
