#!/usr/bin/python3
def uppercae(str):
    for i in string:
        char = ord(i)
        if char >= 97 and char <= 122:
            char = char - 32
        print('{:c}'.format(char), end='')
    print()
