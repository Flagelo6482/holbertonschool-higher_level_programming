#!/usr/bin/python3
# 2-args.py

import sys

i = 0

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n{}: {}".format(i+1, sys.argv[i+1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        while i < len(sys.argv):
            if i == 0:
                i += 1
                continue
            else:
                print("{}: {}".format(i, sys.argv[i]))
                i += 1
