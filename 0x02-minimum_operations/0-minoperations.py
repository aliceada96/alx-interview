#!usr/bin/python3
"""Function to find the no of operations"""


def minOperations(n):
    """Returns minimum number of operations required to obtain n characters."""
    if n <= 1:
        return 0

    div = 2
    operations = 0
    while n > 1:
        while n % div == 0:
            operations += div
            n = n // div
        div += 1
    return operations
