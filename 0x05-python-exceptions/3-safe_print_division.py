#!/usr/bin/python3
def safe_print_division(a, b):
    """This Write a function that dividez 2 integerz and printz the result."""
    
    try:
        div = a / b
    except (ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
