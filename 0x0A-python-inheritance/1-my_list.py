#!/usr/bin/python3
""" Defines a class type called MyList """


class MyList(list):
    """ method that prints the list, but sorted (ascending sort) """

    def print_sorted(self):
        """ print the output according to the test file list given """
        print(sorted(self))
