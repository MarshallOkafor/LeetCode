#!/usr/bin/python3
"""
This is the solution to LeetCode problem 704: 
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. If 
target exists, then return its index. Otherwise, return -1.

Runtime: O(log n)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            # For overflow
            # mid = (l + (r - l)) // 2
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [-1,0,3,5,9,12] 
    target = 9
    print(sol.search(nums, target))