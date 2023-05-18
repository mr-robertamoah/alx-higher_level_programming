#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    thous_dict = {"MMM": 3000, "MM": 2000, "M": 1000}
    hund_dict = {"CM": 900, "DCCC": 800, "DCC": 700, "DC": 600, "D": 500, "CD": 400, "CCC": 300, "CC": 200, "C": 100}
    tens_dict = {"XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50, "XL": 40, "XXX": 30, "XX": 20, "X": 10}
    ones_dict = {"IX": 9, "VIII": 8, "VII": 7, "VI": 6, "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1}

    sum_r = 0
    for k, v in thous_dict.items():
        if k in roman_string:
            sum_r += v
            break
    for k, v in hund_dict.items():
        if k in roman_string:
            sum_r += v
            break
    for k, v in tens_dict.items():
        if k in roman_string:
            sum_r += v
            break
    for k, v in ones_dict.items():
        if k in roman_string:
            sum_r += v
            break

    return sum_r
