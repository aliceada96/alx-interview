#!/usr/bin/python3
"""Determines if a given data set is a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Checks whether the input string is encoded in UTF-8.

    Args:
    data (str): The string to be checked for UTF-8 compliance.
    Return: True if it is, False otherwise.
    """
    i = 0
    while i < len(data):
        if data[i] >> 7 == 0:  # 0xxxxxxx
            i += 1
        elif data[i] >> 5 == 0b110:  # 110xxxxx
            if i + 1 >= len(data) or data[i + 1] >> 6 != 0b10:
                return False
            i += 2
        elif data[i] >> 4 == 0b1110:  # 1110xxxx
            if i + 2 >= len(data) or data[i + 1] >> 6 != 0b10 or data[
                    i + 2] >> 6 != 0b10:
                return False
            i += 3
        elif data[i] >> 3 == 0b11110:  # 11110xxx
            if i + 3 >= len(data) or data[i + 1] >> 6 != 0b10 or data[
                    i + 2] >> 6 != 0b10 or data[i + 3] >> 6 != 0b10:
                return False
            i += 4
        else:
            return False

    return True
