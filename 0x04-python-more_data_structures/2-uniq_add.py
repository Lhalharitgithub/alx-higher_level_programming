#!/usr/bin/python3
#2-uniq_add.py


def uniq_add(my_list=[]):
    """Showz a function that adds all unique integers in a list (only once for each integer)."""
    uniq_list = set(my_list)
    num = 0
    for y in uniq_list:
        num += y
    return (num)
