#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """It Writez a function that printz an integer."""
    
    try:
        print("{:d}".format(value))
         else:
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
