#!/usr/bin/python3
""" This is a python script with Base class """
import json


class Base:
    """ Base class for monitoring id attributes """
    Private Class Attributes:
        __nb_object(int): Number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
    """Method that initializes a new Base
    Args:
        id(int): The identity of the new Base.

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries
         Args:
            list_dictionaries (list): A list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
