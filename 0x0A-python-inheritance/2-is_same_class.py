#!/usr/bin/python3
""" check exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """
    this method checkes if its the same
    """
    return type(obj) is a_class
