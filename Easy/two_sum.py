"""
This code checks and return the indices of two numbers that sum up to the target number.

Runtime: O(n)
Space: O(n)
"""

class Solution:
    """
    Class to instantiate the solution object.
    """

    def two_sum(self, nums: list, target: int):
        """
        This function uses a hash map to store and compare the values in the array.
        The values are the keys, and the indices are the values in the hash map.
        The hash map used is the Python dictionary data structure.
        """

        hash_map = {} # val : index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map[diff], index]
            hash_map[value] = index

        return 

# Driver code
if __name__ == '__main__':

    # Create a solution object
    sol = Solution()

    # Test array and target value
    arr = [2, 1, 7, 3, 6]
    target = 4

    # Function call
    print(sol.two_sum(arr, target))
