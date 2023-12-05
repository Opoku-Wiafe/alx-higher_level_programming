#!/usr/bin/python3
""" This is the module of the code """


def add_attribute(obj, atr, value):
    """this function check new attribute to class """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
