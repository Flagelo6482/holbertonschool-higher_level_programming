#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Last digit"""
    if number < 0:
        number = (abs(number) % 10)
    else:
        number = number % 10

    print(number, end="")
    return number
