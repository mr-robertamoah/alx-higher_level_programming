#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    max_v = -1
    values = []
    for k, v in a_dictionary.items():
        values.append(v)
        if (max_v < v):
            max_v = v
    if values.count(max_v) == 1:
        for k, v in a_dictionary.items():
            if v == max_v:
                return k
    else:
        return None
