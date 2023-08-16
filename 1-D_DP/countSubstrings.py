#!/usr/bin/python
"""
This is the solution to LeetCode problem 647:

Given a string s, return the number of palindromic
substring in s.

This is part of DP programming approach.

Runtime: O(n^2)
"""

class Solution:

    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):

             count += self.countPali(s, i, i)
             count += self.countPali(s, i, i+1)

        return count

    def countPali(self, s, l, r):

        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r +=1

        return count
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    s = 'aaa'
    sol = Solution()
    print(sol.countSubstrings(s))