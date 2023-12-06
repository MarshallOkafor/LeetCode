#!/usr/bin/python3
"""
This is the solution to LeetCode problem 131: 

Given an integer array nums of unique elements, return all possible 
subsets (the power set). The solution set must not contain duplicate 
subsets. Return the solution in any order.

Runtime: O(2^n)
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        subset = []
        def dfs(i):

            if i >= len(nums):
                res.append(list(subset))
                return

            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
      
        dfs(0)

        return res

# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [1,2,3]
    print(sol.subsets(nums))