#!/usr/bin/python3
"""
This is the solution to LeetCode problem 22: 

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Runtime => O(2^2n)
"""

class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        # Add open parenthesis when open < n
        # Add close parenthesis when close < open
        # Add string to result list when open == close == n
        res, stack = [], []

        # Helper function
        def backtrack(openN: int, closeN: int) -> None:

            # Base case
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)

        return res
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))