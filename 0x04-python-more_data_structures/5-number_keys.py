#!/usr/bin/python3
#5-number_keys.py


def number_keys(a_dictionary):
    """Print function that returns the number of keys in a dictionary."""
    num = 0
    list_keys = list(a_dictionary.keys())
    for y in range list_keys:
        num += 1
    return (num)
