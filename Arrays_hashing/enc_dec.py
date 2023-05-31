"""
This code is a basic implementation to encode and decode a list of strings and a string repectively.

Runtime: O(n)
space: O(n)
"""

class Solution:
    """
    Class to create an instance of the solution object
    """

    def encode(self, strs: list[str]) -> str:
        """
        This function encodes the list of strings in to one string.
        Complexity is O(n)
        """

        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        
        return result

    def decode(self, strs: str) -> list[str]:
        """
        This function decodes the string into a list of strings.
        Complexity is O(n)
        """

        result, i = [], 0

        while i < len(strs):
            j = i
            while strs[j] != '#':
                j += 1
            length = int(strs[i : j])
            result.append(strs[j+1 : j+1 + length])
            i = j+1 + length

        return result

# Driver code
if __name__ == '__main__':

    # Solution object
    sol = Solution()
    arr = ['lint', 'code', 'love', 'you']

    # Test function call
    print(sol.encode(arr))
    print(sol.decode(sol.encode(arr)))
