#!/usr/bin/python3
# 100-print_tebahpla.py

"""Smile the mirror!"""

for i in range(122, 96, -1):
    if i % 2 != 0:
        i -= 32
    print(chr(i), end="")
