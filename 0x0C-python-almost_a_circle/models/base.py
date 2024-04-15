#!/usr/bin/python3
""" This is a python script with Base class """


class Base:
    """ Base class for monitoring id attributes """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
