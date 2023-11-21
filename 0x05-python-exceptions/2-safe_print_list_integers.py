#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    firstCount = 0
    secondCount = 0
    for i in my_list:
        try:
            if (firstCount >= x):
                break
            print("{:d}".format(i), end="")
            firstCount += 1
        except (ValueError, TypeError):
            secondCount += 1
    if (firstCount + secondCount < x):
        raise IndexError("list index out of range")
    print("".format())
    return firstCount 
