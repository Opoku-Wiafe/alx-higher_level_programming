#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    myArg = len(argv)
    if myArg == 1:
        print("0 arguments.")
    elif myArg > 1:
        print("{:d} argument{:s}".format(myArg-1, "s:" if myArg > 2 else ":"))
        for i in range(1, myArg):
            print("{:d}: {:s}".format(i, argv[i]))
