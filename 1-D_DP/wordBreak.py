#!/usr/bin/python
"""
This is the solution to LeetCode problem 139:

Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused 
multiple times in the segmentation.

Runtime: O(n * m)
"""

class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i+len(w)] == w:
                    dp[i]  = dp[i + len(w)]
                if dp[i]:
                    break
            
        return dp[0]
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function call
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))