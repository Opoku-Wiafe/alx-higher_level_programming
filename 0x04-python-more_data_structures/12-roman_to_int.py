#!/usr/bin/python3
def roman_to_int(roman_string):
    total = 0
    position = 0

    if roman_string is not None:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_characters = list(roman_numerals.keys()) 
        input_length = len(roman_string)  # Calculate the length of the input Roman numeral string.
        for char in roman_string:
            if char in roman_numerals:
                if char in 'IXC':
                    if position < input_length - 1:
                        next_char = roman_characters[position + 1]
                        if next_char in 'VXLCDM':
                            total += (roman_numerals[next_char] - roman_numerals[char])
                total += roman_numerals[char]

            position += 1  # Move to the next character in the input string.

    return total  # Return the calculated integer value.
