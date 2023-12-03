#!/usr/bin/python3
"""
This is the solution to LeetCode problem 42:
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining.

Runtime: O(n)
"""

class Solution:

    def trap(self, height: list[int]) -> int:

        res, l, r = 0, 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res 

# Driver code
if __name__ == '__main__':

    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))