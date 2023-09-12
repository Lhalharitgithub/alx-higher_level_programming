#!/usr/bin/python3
"""A function that definez an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributez."""
    return (dir(obj))
