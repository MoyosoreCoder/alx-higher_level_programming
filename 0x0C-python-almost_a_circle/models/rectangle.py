#!/usr/bin/python3
""" Python script that defines class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ A python script with name Rectangle

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes Rectangle instance
        Args:
            width(int): The width of the new Rectangle.
            height(int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
            """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ Getter for width """
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """ Getter for height """
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            """ Getter for x """
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            """ Getter for y """
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
