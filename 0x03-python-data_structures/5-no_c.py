#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for c_char in my_string:
        if c_char != 'c' and c_char != 'C':
            newStr += c_char
    return newStr
