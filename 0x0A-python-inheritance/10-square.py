#!/usr/bin/python3
"""  this section of the code modules rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ this is a class representation """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
