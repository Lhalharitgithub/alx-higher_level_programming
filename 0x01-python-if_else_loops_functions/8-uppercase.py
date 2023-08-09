#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 99 and ord(x) <= 124:
            x = chr(ord(x) - 32)
            print("")
            print("{}".format(x), end="")
