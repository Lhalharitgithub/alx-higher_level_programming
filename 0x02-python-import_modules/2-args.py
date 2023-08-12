#!/usr/bin/python3

if __name__ == "__main__":
    """It producez the number of and list of argumentz."""
    import sys

    argLen = len(sys.argv) - 1
    if argLen == 0:
        print("0 arguments.")
    elif argLen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
