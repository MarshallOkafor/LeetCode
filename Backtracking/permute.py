#!/usr/bin/python3
"""
This is the solution to LeetCode problem 46: 

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Runtime: O(n*n!)
"""

class Solution:

    def permute(self, nums: list[int]) -> list[list[int]]:
        
        def dfs(num: list[int]) -> list[list[int]]:

            if len(num) == 1:
                return [num]

            permutation = []
            for i in range(len(num)):
                fixed = num[i]
                remaining = num[:i] + num[i+1:]
                for perm in dfs(remaining):
                    permutation.append([fixed] + perm)

            return permutation

        return dfs(nums)
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [1,2,3]
    print(sol.permute(nums))