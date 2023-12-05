#!/usr/bin/python3
"""checks if is instance that inherits from class"""


def inherits_from(obj, a_class):
    """
    this modules a method to check instance
    """
    return issubclass(type(obj), a_class)
