#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    thous_dict = {"MMM": 3000, "MM": 2000, "M": 1000}
    hund_dict = {
        "CM": 900, "DCCC": 800, "DCC": 700, "DC": 600, "D": 500,
        "CD": 400, "CCC": 300, "CC": 200, "C": 100
    }
    tens_dict = {
        "XC": 90, "LXXX": 80, "LXX": 70, "LX": 60, "L": 50,
        "XL": 40, "XXX": 30, "XX": 20, "X": 10
    }
    ones_dict = {
        "IX": 9, "VIII": 8, "VII": 7, "VI": 6, "V": 5,
        "IV": 4, "III": 3, "II": 2, "I": 1
    }

    if roman_string in thous_dict:
        return thous_dict[roman_string]
    if roman_string in hund_dict:
        return hund_dict[roman_string]
    if roman_string in tens_dict:
        return tens_dict[roman_string]
    if roman_string in ones_dict:
        return ones_dict[roman_string]

    thous = 0
    hund = 0
    tens = 0
    ones = 0
    r_str = rem = c = ""
    for c in roman_string:
        r_str += c
        if r_str in thous_dict:
            thous = thous_dict[r_str]
            rem = r_str
    if rem:
        roman_string = roman_string[len(rem):]

    r_str = rem = c = ""
    for c in roman_string:
        r_str += c
        if r_str in hund_dict:
            hund = hund_dict[r_str]
            rem = r_str
    if rem:
        roman_string = roman_string[len(rem):]

    r_str = rem = c = ""
    for c in roman_string:
        r_str += c
        if r_str in tens_dict:
            tens = tens_dict[r_str]
            rem = r_str
    if rem:
        roman_string = roman_string[len(rem):]

    r_str = rem = c = ""
    for c in roman_string:
        r_str += c
        if r_str in ones_dict:
            ones = ones_dict[r_str]

    return thous + hund + tens + ones
