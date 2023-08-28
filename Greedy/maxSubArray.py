#!/usr/bin/python3
"""
This is the solution to LeetCode problem 53:

Given an integer array nums, find the subarray 
with the largest sum, and return its sum.

Runtime: O(n)
"""

class Solution:

    def maxSubArray(self, nums: list[int]) -> int:

        maxSub = nums[0]
        curSum = 0

        # We iterate through the array in a sliding window
        # fashion.
        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums))