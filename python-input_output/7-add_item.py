#!/usr/bin/python3


"""Load, add, save"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
Script that adds all arguments to a python list
and then save them to a file
"""
args = sys.argv[1:]

load_from_json_file("add_items.json")
save_to_json_file(args, "add_items.json")
