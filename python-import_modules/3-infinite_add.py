#!/usr/bin/python3
# 3-infinite_add.py

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    else:
        resul = 0
        i = 1
        while i < len(sys.argv):
            resul += int(sys.argv[i])
            i += 1
        print(resul)
