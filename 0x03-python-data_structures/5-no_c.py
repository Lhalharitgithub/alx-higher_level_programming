#!/usr/bin/python3
def no_c(my_string):
    """Deleting all elementz c and C from the string."""
    elementz = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(elementz))
