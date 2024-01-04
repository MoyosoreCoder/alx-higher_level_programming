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
        self.size = size

    @property
    def size(self):
        """ retrieve the current size value """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ this method will get the area of size """

        return (self.__size * self.__size)
