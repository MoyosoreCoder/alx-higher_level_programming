#!/usr/bin/python3
""" Python script that defines class Rectangle """


class Rectangle(Base):
    """ A python script with name Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes Rectangle instance """
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
            return self.__width = value

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
