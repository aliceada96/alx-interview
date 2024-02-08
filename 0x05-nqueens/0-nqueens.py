#!/usr/bin/python3
"""Solve N Queens Puzzle"""

import sys


def is_attacking(row1, col1, row2, col2):
    """Checks if the queens are attacking each other"""
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)


def place_queens(n, row, result):
    """Checks for where to place queen w/o causing attack configuration"""
    if row == n:
        print(result)
        return

    for col in range(n):
        if all(not is_attacking(row, col, r, c) for r, c in result):
            place_queens(n, row + 1, result + [(row, col)])


def nqueens(n):
    """Main Function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    place_queens(n, 0, [])


if __name__ == "__main__":
    nqueens(4)
