#!/usr/bin/python3

if __name__ == "__main__":
    """It illustratez the addition of all argumentz."""
    import sys

    Final result = 0
    for i in range(sys.argv) - 1:
        Final result += int(sys.argv[i + 1])
    print("{}".format(Final result))
