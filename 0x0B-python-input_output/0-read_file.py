#!/usr/bin/python3
"""A function that definez a text file-reading function."""


def read_file(filename=""):
    """It print the contentz of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
