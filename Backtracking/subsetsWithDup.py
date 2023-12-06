#!/usr/bin/python3
"""
This is the solution to LeetCode problem 90: 

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.

Runtime: O(2^n)
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res = []
        def dfs(i, subset):

            if i >= len(nums):
                res.append(list(subset))
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1, subset)
      
        dfs(0, [])

        return res
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [1,2,2]
    print(sol.subsetsWithDup(nums))