#!/usr/bin/python3
"""
This is the solution to LeetCode problem 33: 
Search in Rotated Sorted Array

Runtime: O(log n)
"""

class Solution:

    def search_item(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Best case
            if nums[mid] == target:
                return mid
            
            # Left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(sol.search_item(nums, target))