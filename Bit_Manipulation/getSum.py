#!/usr/bin/python3
"""
This is the solution to LeetCode problem 371:

Given two integers a and b, return the sum of the 
two integers without using the operators + and -.

Runtime: O(n)
"""

class Solution:

    def getSum(self, a: int, b: int) -> int:

        # Limit the integer size to 32 bits
        MASK = 0xFFFFFFFF
        MASK_INT = 0x7FFFFFF

        # Use XOR and carry operations
        # The b variable is used for the carry
        while b != 0:
            a, b = ( a ^ b) & MASK, (( a & b ) << 1) & MASK

        # Check if the result is negative or positive
        if a > MASK_INT:
            return ~(a ^ MASK)
        else:
            return a
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    a, b = 1, 2
    print(Solution().getSum(a, b))