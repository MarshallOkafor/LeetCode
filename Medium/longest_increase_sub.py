"""
Given an integer array nums, return the length of the longest
increasing subsequence.

This is part of DP programming approach.

Runtime: O(n)
Space: O(1)
"""

class Solution:
    """
    Class to instantiate the solution object.
    """

    def longest_increasing(self, arr: list[int]) -> int:
        """
        This function computes the longest subsequence using
        DP
        """

        LIS = [1] * len(arr)

        for i in range(len(arr) - 1, - 1, - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

# Driver code
if __name__ == '__main__':

    sol = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.longest_increasing(arr))