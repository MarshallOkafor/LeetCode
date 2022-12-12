"""
This code checks how many distinct ways you can climb a stairs to the top
if you can either climb 1 or 2 steps at a time.

This is part of DP programming approach.

Runtime: O(n)
Space: O(1)
"""

class Solution:
    """
    Class to instantiate the solution object
    """

    def climb_stairs(self, n: int) -> int:
        """
        This function iteratively keeps track of two variables which are basically 
        the decision you need to know how many ways you can climb to the top.
        """

        # Using a bottom up DP approach since the top requires just a step
        # And the step before the top requires only just a step too
        one, two = 1, 1 

        for i in range(n - 1): # Since the two last positions in n are known
            temp = one
            one = one + two
            two = temp

        return one

# Driver code
if __name__ == '__main__':

    sol = Solution()
    n = 5
    print(sol.climb_stairs(n))