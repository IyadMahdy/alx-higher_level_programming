#!/usr/bin/python3
def main():
    for x in dir(hidden_4):
        if x[:2] != '__':
            print(x)



if __name__ == '__main__':
    main()
