def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still float('inf'), it means the total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
