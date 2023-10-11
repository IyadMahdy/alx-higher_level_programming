#!/usr/bin/python3
from sys import argv


def main():
    n = len(argv)
    print('{} '.format(n-1), end='')
    print('argument{}'.format('' if n-1 == 1 else 's'), end='')
    print('{}'.format('.' if n-1 == 0 else ':'))
    for i in range(1, n):
        print('{}: {}'.format(i, argv[i]))


if __name__ == '__main__':
    main()
