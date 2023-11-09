#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, j in dict(sorted(a_dictionary.items())).items():
        print("{}: {}".format(i, j))
