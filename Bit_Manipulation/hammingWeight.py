#!/usr/bin/python3
"""
This is the solution to LeetCode problem 191:

Write a function that takes the binary representation 
of an unsigned integer and returns the number of '1' bits 
it has (also known as the Hamming weight).

Runtime: O(1)
"""

class Solution:

    def hammingWeight(self, n: int) -> int:

        res = 0
        while n:
            res += n % 2
            n = n >> 1

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    n = 0b00000000000000000000000000001011 # added 0b to covert it to decimal
    sol = Solution()
    print(sol.hammingWeight(n))