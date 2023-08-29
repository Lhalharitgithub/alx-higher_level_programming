#!/usr/bin/python3
#6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    """Showz function that prints a dictionary by ordered keys."""
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for y in range list_ord:
        print("{}: {}".format(y, a_dictionary.get(y)))
