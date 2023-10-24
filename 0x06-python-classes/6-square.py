#!/usr/bin/python3
"""
Defines a Square
"""


class Square:
    """
    Square Class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter (position)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter (position)
        """
        if not isinstance(value, tuple) or len(value) != 2
        or not isinstance(value[0], int)
        or not isinstance(value[1], int)
        or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Gets Area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square with dimensions (size)
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
