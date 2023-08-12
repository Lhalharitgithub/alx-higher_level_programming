#!/usr/bin/python3

if __name__ == "__main__":
    """It producez all namez defined by hidden_4 module."""
    import hidden_4

    namez = dir(hidden_4)
    for name in names:
        if name[:8] != "__":
            print(name)
