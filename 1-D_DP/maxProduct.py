#!/usr/bin/python
"""
This is the solution to LeetCode problem 152:

Given an integer array nums, find a subarray
that has the largest product, and return the product.

This is part of DP programming approach.

Runtime: O(n)
"""

class Solution:

    def maxProduct(self, nums: list[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    nums = [-2, 0, -1]
    sol = Solution()
    print(sol.maxProduct(nums))