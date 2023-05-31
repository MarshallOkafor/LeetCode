"""
This code returns an array answer such that 'answer[i]' is equal to 
the product of all the elements of the input array say 'nums[]'except
'nums[i]'

Runtime = O(n)
Space = O(1) excluding the result array.
"""

class Solution:
    """
    Class to instantiate solution object.
    """

    def product_except_self(self, nums: list):
        """
        This function loops through the array twice(forward and backward).
        Two variables prefix and postfix are used to compute the product 
        result of each answer[i].
        """

        result = [1] * len(nums) # Answer array with all indices intialized with value 1
        prefix = 1
        postfix = 1

        # Get the prefix results for each index and update the result array directly
        for i in range(len(nums)):
            result[i] *= prefix # Storing the prefix product result of index i
            prefix *= nums[i] # Updating the prefix value for the next index

        # Get the postfix results for each index and update the result array directly
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix 
            postfix *= nums[i]

        return result

# Driver code
if __name__ == '__main__':

    # Test values
    arr = [1, 2, 3, 4]

    # Solution object
    sol = Solution()

    # Function call
    print(sol.product_except_self(arr))
