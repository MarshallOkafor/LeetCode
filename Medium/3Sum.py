#!/usr/bin/python3
"""
This code implements three sum of integers that sum up to zero 
without duplicates of the indices

Runtime: O(n^2)
"""
class Solution():

    def three_sum(self, nums: list[int]) -> list[int]:

        res = []
        nums.sort() # sort the input array

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                total = value + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.three_sum(nums))
