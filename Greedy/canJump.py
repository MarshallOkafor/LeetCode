#!/usr/bin/python3
"""
This is the solution to LeetCode problem 55:

You are given an integer array nums. You are initially 
positioned at the array's first index, and each element 
in the array represents your maximum jump length at that 
position. Return true if you can reach the last index, 
or false otherwise.

Runtime: O(n)
"""

class Solution:

    def canJump(self, nums: list[int]) -> bool:

        pos = len(nums) - 1

        # Make the length of the array shorter 
        # starting from the last index
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= pos:
                pos = i

        return True if pos == 0 else False
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.canJump(nums))