#!/usr/bin/python3
#100-weight_average.py


def weight_average(my_list=[]):
    """Printz a function that returns the weighted average of all integers tuple (<score>, <weight>)"""
    if not (my_list):
        return [0]
    num = [0]
    den = [0]
    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]
    return (num / den)
