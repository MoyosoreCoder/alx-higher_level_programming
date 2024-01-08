#!/usr/bin/python3
def lookup(obj):
    """ function that list attribute and methods """

    for attr in [dir(obj)]:
        """Return a list of an object's available attributes."""
        return (attr)
