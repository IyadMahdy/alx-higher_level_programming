#!/usr/bin/python3
"""
Defines a Square
"""


class Square:
    """
    Square Class
    """
    def __init__(self, size=0):
        """
        Constructor
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter (size)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter (size)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Gets Area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square with dimensions (size)
        """
        if __size == 0:
            print()
        else:
            for i in range(__size):
                for j in range(__size):
                    print("#", end="")
                print()
