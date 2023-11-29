#!/usr/bin/python3
"""
Addition of numbers using test
"""


def add_integer(num1, num2=98):
    """ This function adds two numbers """
    if type(num1) is float:
        num1 = int(num1)
    if type(num1) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(num2) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(num2) is float:
        num2 = int(num2)
    return num1 + num2
