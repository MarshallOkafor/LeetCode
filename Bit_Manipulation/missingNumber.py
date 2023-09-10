#!/usr/bin/python3
"""
This is the solution to LeetCode problem 268:

Given an array nums containing n distinct numbers in 
the range [0, n], return the only number in the range 
that is missing from the array.

Runtime: O(n)
"""

class Solution:

    def missingNumber(self, nums: list[int]) -> int:

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res
            
# Driver code
if __name__ == '__main__':

    # Variable, object, and function call
    nums = [3,0,1]
    print(Solution().missingNumber(nums))