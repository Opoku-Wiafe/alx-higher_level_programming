#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    nList = []
    for i in my_list:
        nList.append(True if i % 2 == 0 else False)
    return nList
