#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        max_score = 0
        key = None

        for i in a_dictionary:
            if max_score < a_dictionary[i]:
                max_score = a_dictionary[i]
                key = i
        return key
