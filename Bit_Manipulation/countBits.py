#!/usr/bin/python3
"""
This is the solution to LeetCode problem 338:

Given an integer n, return an array ans of length 
n + 1 such that for each i (0 <= i <= n), ans[i] 
is the number of 1's in the binary representation 
of i.

Runtime: O(n)
"""

class Solution:

    def countBits(self, n: int) -> list[int]:

        dp = [0] * (n + 1)
        offset = 1 # 2^0, 2^1,...

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    n = 5
    print(Solution().countBits(n))