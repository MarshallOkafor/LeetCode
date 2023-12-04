#!/usr/bin/python3
"""
This is the solution to LeetCode problem 567:

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Runtime: O(26) => O(n)
"""

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Base case 
        if len(s1) > len(s2):
            return False
        
        # Use an array map to check matches
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0 # To slide the window from left => right
        for r in range(len(s1), len(s2)):
            # Best case
            if matches == 26: return True

            # Check for sub string
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Update the left character
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    s1 = 'ab'
    s2 = 'eidbaooo'
    print(sol.checkInclusion(s1, s2))