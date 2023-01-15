#!/usr/bin/python3
"""
Given an integer array height of length n, this code returns the 
maximum amount of water a container can store.

Runtime: O(n)
"""
class Solution:

    def maxArea(self, height: list[int]) -> int:

        max_area = 0
        l, r = 0, len(height)-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
