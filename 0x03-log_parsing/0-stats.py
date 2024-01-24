#!/usr/bin/python3

import sys


def print_stats(status_codes, total_file_size):
    """
    This method logs the statistics
    Args: status_codes: dict of status codes
          total_file_size: total of the file
    Returns: Nothing
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
s_code = 0
counter = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # split input
        parsed_line = parsed_line[::-1]  # take only last 2 values

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                s_code = parsed_line[1]  # status code

                if (s_code in status_codes.keys()):
                    status_codes[s_code] += 1

            if (counter == 10):
                print_stats(status_codes, total_file_size)
                counter = 0

finally:
    print_stats(status_codes, total_file_size)
