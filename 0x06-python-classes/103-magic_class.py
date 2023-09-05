#!/usr/bin/python3
"""The function definez a MagicClass matching exactly a bytecode
provided by Holberton."""

import math


class MagicClass:
    """The representation of a circle."""

    def __init__(self, radius=0):
        """The initialization of a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """The return of the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """It Returnz The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
