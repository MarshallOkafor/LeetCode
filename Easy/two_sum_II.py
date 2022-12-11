"""
This code checks and return the indices of two numbers that sum up to the target number.
The input array given is already sorted.
The indices of the two numbers are returned using 1-based index notation.

Runtime: O(n)
Space: O(1)
"""

class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:

        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

# Driver code
if __name__ == '__main__':

    sol = Solution()
    arr = [1, 3, 4, 5, 7, 10, 11]
    target = 9

    print(sol.two_sum(arr, target))