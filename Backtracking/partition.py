#!/usr/bin/python3
"""
This is the solution to LeetCode problem 131: 

Given a string s, partition s such that every 
substring of the partition is a palindrome. Return 
all possible palindrome partitioning of s.

Runtime: O(n^2)
"""

class Solution:

    def partition(self, s: str) -> list[list[str]]:

        res, part = [], []

        # Helper dfs function
        def dfs(i):

            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        
        return res
    
    def isPali(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    s = 'aab'
    sol = Solution()
    print(sol.partition(s))