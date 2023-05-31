"""
This code detects if there are duplicates in a list.

It runs in O(n) time and takes O(n) space.
"""

class Solution:
    """
    Class to create the solution object.
    """

    def contain_duplicate(self, arr):
        """
        This function uses a hash set to check if there are duplicates in the list.
        """

        hash_set = set()        

        for item in arr:
            if item in hash_set:
                return True
            
            hash_set.add(item)

        return False
        

# Driver code
if __name__ == '__main__':

    # Create object of the class
    sol = Solution()

    # Test list of values
    arr = [1, 2, 3, 4, 1]

    # Function call to check for duplicates in the list
    print(sol.contain_duplicate(arr))