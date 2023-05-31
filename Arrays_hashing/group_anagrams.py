"""
This code takes an input list of strings an return a group of anagrams.

Runtime: O(n)
Space: O(n)
"""

from collections import defaultdict

class Solution:
    """
    A class to instantiate the solution object.
    """

    def get_group_anagrams(self, list_of_strs: list):
        """
        This function uses a hash container (dictionary) to group the anagrams.
        """

        result = defaultdict(list) # Hash map to hold each grouping

        for strs in list_of_strs:
            count = [0] * 26 # list to hold character position from a...z
            for char in strs:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(strs)

        return result.values()

# Driver code
if __name__ == '__main__':

    sol = Solution()
    list_of_strs = ['eat', 'tea', 'nat', 'ate', 'tan', 'bat']

    # Function call
    print(sol.get_group_anagrams(list_of_strs))