#!/usr/bin/python3
#11-multiply_list_map.py


def multiply_list_map(my_list=[], number=0):
    """The function that returnz a list with all values multiplied by a number without using any loopz."""
    return (list(map((lambda y: y * number), my_list)))
