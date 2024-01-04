#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ Represent a square """

    def __init__(self, size=0):
        """ initializes a new size

        Args:
        @self: custom builtin already made by python
        @size (int): size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ this method will get the area of size """

        return (self.__size * self.__size)
