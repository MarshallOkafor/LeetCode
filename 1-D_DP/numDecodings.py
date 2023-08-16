#!/usr/bin/python
"""
This is the solution to LeetCode problem 91:

Given a string s, return the number of palindromic
substring in s.

This is part of DP programming approach.

Runtime: O(n)
"""

class Solution:

    def numDecodings(self, s):

        dp = { len(s): 1 }

        for i in range(len(s) -1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == '1' or 
                s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]

        return dp[0]
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    s = '26'
    sol = Solution()
    print(sol.numDecodings(s))