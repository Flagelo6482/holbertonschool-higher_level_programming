#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for i in roman_string:
        current = roman[i]

        if current > prev_value:
            total += current - 2 * prev_value
        else:
            total += current
        prev_value = current
    return total
