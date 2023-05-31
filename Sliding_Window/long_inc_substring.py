#!/usr/bin/python3
"""
This code returns the longest increasing substring using the sliding window
approach.

Runtime = O(n)
Space = O(n) because a set was used to keep track of duplicates.
"""

class Solution:

    def longest_inc_substring(self, strs: str) -> int:

        char_set = set()
        l, longest = 0, 0 

        for r in range(len(strs)):
            if strs[r] in char_set:
                char_set.remove(strs[l])
                l += 1

            char_set.add(strs[r])
            longest = max(longest, r - l +1)

        return longest

# Driver code
if __name__ == '__main__':

    sol = Solution()
    s = 'abcabcbb'
    print(sol.longest_inc_substring(s))
