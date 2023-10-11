#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    f = 0
    s = 0
    for x, y in my_list:
        f += x * y
        s += y
    return f / s
