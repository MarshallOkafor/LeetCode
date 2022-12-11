"""
This code output the longest consecutive sequence of elements that 
can be found in array of integers.

Runtime: O(n)
space: O(n)
"""

class Solution:
    """
    Class to instantiate the solution object
    """

    def longest_cons_seq(self, nums: list[int]) -> int:

        num_set = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

# Driver code
if __name__ == '__main__':

    sol = Solution()
     
    # test array
    arr = [100, 4, 200, 3, 7, 1, 2, 20, 5, 90, 6]

    # Function call
    print(sol.longest_cons_seq(arr))