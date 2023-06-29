#!/usr/bin/python3
"""
This is the solution to LeetCode problem 153: 
Find Minimum in Rotated Sorted Array

Runtime: O(log n)
"""

class Solution:

    def find_min(self, nums: list[int]) -> int:

        left, right = 0, len(nums) - 1
        min_item = nums[0] # just choosing an arbitrary pivot

        while left <= right:
            if nums[left] < nums[right]:
                min_item = min(min_item, nums[left])
                break
            
            # Since the array has been rotated
            mid = (left + right) // 2
            min_item = min(min_item, nums[mid])

            if nums[mid] > nums[left]:
                # Discard the left half
                left = mid + 1
            else:
                # Discard the right half
                right = mid - 1
        
        return min_item
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    print(sol.find_min(nums))