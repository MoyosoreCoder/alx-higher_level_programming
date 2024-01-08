#!/usr/bin/python3
""" function that list attribute and methods """
def lookup(obj):
        """Return a list of an object's available attributes."""
        return [attr for attr in dir(obj)]
