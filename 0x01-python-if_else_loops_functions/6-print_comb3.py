#!/usr/bin/python3
for Numeric1 in range(0, 10):
    for Numeric2 in range(Numeric1 + 1, 10):
        if Numeric1 == 7 and Numeric2 == 9:
            print("{}{}".format(Numeric1, Numeric2), end=",")
        else:
            print("{}{}".format(Numeric1, Numeric2))
