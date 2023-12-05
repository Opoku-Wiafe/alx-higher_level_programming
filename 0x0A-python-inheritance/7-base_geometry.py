#!/usr/bin/python3
""" this section modules geometry """


class BaseGeometry:
    """
    this section of the code modules geometry class
    """
    pass

    def area(self):
        """ this is the area of geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this vlaidates the geometry """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
