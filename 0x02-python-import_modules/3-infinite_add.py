#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    myargs = len(argv)
    if myargs == 1:
        print(0)
    elif myargs > 1:
        total = 0
        for i in range(1, myargs):
            total += int(argv[i])
        print("{:d}".format(total))

