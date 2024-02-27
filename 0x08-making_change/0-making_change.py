#!/usr/bin/python3
"""Function that determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Returns the minimum number of coins"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if it's possible to make change for the given total
    return dp[total] if dp[total] != float('inf') else -1
