#!/usr/bin/python3
"""
This is the solution to LeetCode problem 190:

Reverse bits of a given 32 bits unsigned integer.

Runtime: O(n)
"""

class Solution:

    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    n = 0b00000010100101000001111010011100
    sol = Solution()
    print(sol.reverseBits(n))