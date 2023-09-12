#!/usr/bin/python3
"""A function that definez an inherited list class MyList."""


class MyList(list):
    """Implementz sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
