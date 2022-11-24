"""
This code checks if two strings are valid anagram. 
An anagram is a word, phrase, or name formed by rearranging the letters of another.

Runtime: O(n)
Space: O(n)
"""

class Solution:
    """
    A template class to create the solution object.
    """

    def is_anagram(self, str_1: str, str_2: str):
        """
        This function compares the two words using a hash map to check 
        if one is an anagram of the other.
        """

        # Base case, we check the length of the two strings
        if len(str_1) != len(str_2):
            return False

        # Create a dicitonary to store the counts of each letter
        # Each letter is a key, the value is the number of occurrence
        count_str_1, count_str_2 = {}, {}

        # Build the hash map/dictionary
        for i in range(len(str_1)):
            count_str_1[str_1[i]] = 1 + count_str_1.get(str_1[i], 0)
            count_str_2[str_2[i]] = 1 + count_str_2.get(str_2[i], 0)

        for key in count_str_1:
            if count_str_1[key] != count_str_2.get(key, 0):
                return False

        return True

# Driver code
if __name__ == '__main__':

    # Create an object
    sol = Solution()

    # Test strings
    str_1 = 'rat'
    str_2 = 'car'

    # Function call to check for valid anagram
    print(sol.is_anagram(str_1, str_2))