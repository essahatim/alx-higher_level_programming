#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 arguments.")
    else:
        print("{:d} arguments:".format(size))
    for i in range(1, size + 1):
        print("{:d}: {:d}".format(i, sys.argv[i]))
