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
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
