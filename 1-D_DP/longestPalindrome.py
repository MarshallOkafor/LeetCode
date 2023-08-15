#!/usr/bin/python
"""
This is the solution to LeetCode problem 5:

Given a string s, return the longest palindromic
substring in s.

This is part of DP programming approach.

Runtime: O(n^2)
"""

class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''
        resLen = 0

        for i in range(len(s)):
            # If the string is odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1

            # If the string is even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1

        return res
    
# Driver code
if __name__ == '__main__':

    s = 'cbbd'
    sol = Solution()
    print(sol.longestPalindrome(s))