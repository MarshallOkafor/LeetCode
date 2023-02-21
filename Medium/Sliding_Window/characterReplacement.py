#!/usr/bin/python3
"""
Descript: You are given a string s and an integer k. You can choose 
any character of the string and change it to any other uppercase English 
character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you 
can get after performing the above operations.

Runtime: O(n)
"""

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        
        # Assign variables to use
        count = {}
        maxFreq, longest, l = 0, 0, 0
        
        # Iterate throught the string
        # Count the charater with the highest number of occurence
        # Update the value of the longest using a valid relacement window
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            if ((r - l + 1) - maxFreq) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest

# Test code
sol = Solution()
s = 'AABBABA'
k = 2
print(sol.characterReplacement(s, k))

