#!/usr/bin/python3
def print_last_digit(number):
    ans = abs(number) % 10
    print(f'{ans:d}', end='')
    return ans
