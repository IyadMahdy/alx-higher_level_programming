#!/usr/bin/python3
"""Defining a Rectangle"""


class Rectangle:
    """
    Defines a Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        number_of_instances += 1

    def __str__(self):
        res = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height):
                for j in range(self.width):
                    res += '#'
                res += '\n' if i != self.height - 1 else ''
        return res

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 1
        return 2 * self.width + 2 * self.height
