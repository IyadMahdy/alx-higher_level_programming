#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import *


def main():
    n = len(argv)
    ops = ['+', '-', '*', '/']
    func_list = [add, sub, mul, div]
    if n-1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    op = argv[2]
    if op not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print('{} {} {} = '.format(argv[1], argv[2], argv[3]), end='')
    print('{}'.format(func_list[ops.index(op)](int(argv[1]), int(argv[3]))))


if __name__ == '__main__':
    main()
