#!/usr/bin/python3
"""A function that definez a locked class."""


class LockedClass:
    """
    This prevent the user from instantiating new LockedClass attributez
    for anything but attributez called 'first_name'.
    """

    __slots__ = ["first_name"]
