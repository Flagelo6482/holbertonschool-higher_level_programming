#!/usr/bin/python3

import json
import sys

args = sys.argv[1:]


with open("archivo_exitoso.txt", mode="a", encoding="utf-8") as file:
    file.write(json.dumps(args) + "\n")
