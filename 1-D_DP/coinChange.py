#!/usr/bin/python
"""
This is the solution to LeetCode problem 322:

You are given an integer array coins representing 
coins of different denominations and an integer amount 
representing a total amount of money. Return the fewest 
number of coins that you need to make up that amount..

This is part of DP programming approach.

Runtime: O(amount * coins)
"""

class Solution:

    def coinChange(self, coins, amount):
        """
        :type coins: list[int]
        :amount: int
        :rtype: int
        """

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # It takes 0 coin to change a 0 coin

        for a in range(1, (amount + 1)):
            for c in coins:
                if (a - c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function call
    coins = [1, 2, 5]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))