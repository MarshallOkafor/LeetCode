"""
This code output the top K frequent elements in array of integers.

Runtime: O(n)
"""

class Solution:
    """
    Class to instantiate the solution object
    """

    def topKFrequent(self, nums: list, k: int):
        """
        A dictionary is used to count the number of occurrence of each number in the input array.
        An array is then used to store in the elements in increasing order of their frequency.
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = [] 

        # Collect the number of occurrence of each element
        # Key: element, Value: number of occurrnce
        for value in nums:
            count[value] = 1 + count.get(value, 0)

        # Update the frequency array
        for key, value in count.items():
            freq[value].append(key)

        # Get the top K elements
        for i in range(len(freq) - 1 , 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

# Driver code
if __name__ == '__main__':

    # Create solution object
    sol = Solution()

    # Test values
    arr = [1, 1, 1, 3, 2, 2]
    k = 2

    # Funtion code
    print(sol.topKFrequent(arr, k))