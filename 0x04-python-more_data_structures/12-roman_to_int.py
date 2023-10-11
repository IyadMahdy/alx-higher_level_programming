#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    prev = 0

    for i in reversed(roman_string):
        val = values[i]

        if prev > val:
            res -= val
        else:
            res += val

        prev = val

    return res
