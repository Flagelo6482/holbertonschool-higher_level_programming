#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        longitud = len(sentence)
        char = sentence[0]

        return (longitud, char)
