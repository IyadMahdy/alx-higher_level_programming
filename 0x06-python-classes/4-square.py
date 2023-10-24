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
        Gets area
        """
        return self.__size ** 2
