#!/usr/bin/python3

def magic_calculation(a, b):
    for i in range(1, 3):
        if i > a:
            raise Exception("Too far")
        result += a ** b / i
    return result + b
