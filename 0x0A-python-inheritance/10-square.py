#!/usr/bin/python3
"""Task 10"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Square Class that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
