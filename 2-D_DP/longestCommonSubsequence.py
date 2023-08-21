#!/usr/bin/python3
"""
This is the solution to LeetCode problem 1143:

Given two strings text1 and text2, return the length 
of their longest common subsequence. If there is no 
common subsequence, return 0

Runtime: O(m * n)
"""

class Solution:

    def lcs(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function call
    text1 = 'ezupkr'
    text2 = 'ubmrapg'
    sol = Solution()
    print(sol.lcs(text1, text2))