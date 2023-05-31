"""
Given an integer array nums representing the amount of money
of each house, return the maximum amount of money you can rob
without alerting the police.

Robbing an adjacent house will alert the police.

This is part of DP programming approach.

Runtime: O(n)
Space: O(1)
"""

class Solution:
    """
    Class to instantiate the solution object.
    """

    def rob(self, nums):
        """
        This function uses dynamic programming to solve the problem.
        """

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

# Driver code
if __name__ == '__main__':

    sol = Solution()
    arr = [1, 2, 3, 1]

    print(sol.rob(arr))