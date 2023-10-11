#!/usr/bin/python3
from sys import argv


def main():
    res = 0
    for x in range(1, len(argv)):
        res += int(argv[x])
    print(res)


if __name__ == '__main__':
    main()
