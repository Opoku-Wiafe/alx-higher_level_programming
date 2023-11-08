#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elemen in matrix:
        for elemen2 in elemen:
            print("{:d}".format(elemen2),
                    end="" if elemen[len(elemen)-1] == elemen2 else " ")
        print("".format())
