#!/usr/bin/python3
import hidden_4


def main():
    for x in dir(hidden_4):
        if x[:2] != '__':
            print('{}'.format(x))


if __name__ == '__main__':
    main()
