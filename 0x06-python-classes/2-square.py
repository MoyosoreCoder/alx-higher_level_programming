#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    def __init__(self, size=0):
        """built in method instantiated

        Args:
        @self: custom builtin already made by python
        @size (int): size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
