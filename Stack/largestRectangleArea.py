#!/usr/bin/python3
"""
This is the solution to LeetCode problem 84: 

Given an array of integers heights representing the histogram's bar height where the width 
of each bar is 1, return the area of the largest rectangle in the histogram.

Runtime => O(n)
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        maxArea = 0

        """
        # Brute force solution

        for l in range(len(heights)):
            for r in range(l, len(heights)):
                minH = min(heights[l:r+1])
                area = minH * (r - l + 1)
                maxArea = max(maxArea, area)

        """

        # Optimal solution
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
        
# Driver code
if __name__ == '__main__':

    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))