#!/usr/bin/python
"""
This is the solution to LeetCode problem 213:

All houses this place are arranged in a circle. 
That means the first house is the neighbor of the last one.

Robbing an adjacent house will alert the police.

This is part of DP programming approach.

Runtime: O(n)
Space: O(1)
"""

class Solution:

    def rob2(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """

        # We leverage Python array splicing and 
        # max in-built util.
        # Check if nums has only one element
        return max(nums[0], self.helper(nums[:-1]), 
                   self.helper(nums[1:]))
    
    def helper(self, nums: list[int]):
        """
        Rob1-type of aproach helper function
        """

        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    nums = [2, 3, 2]
    sol = Solution()
    print(sol.rob2(nums))