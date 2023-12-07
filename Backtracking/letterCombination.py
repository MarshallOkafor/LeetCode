#!/usr/bin/python3
"""
This is the solution to LeetCode problem 17: 

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
could represent. Return the answer in any order.

Runtime: O(4^n) at worst case
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        res = []
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, curStr):

            # Base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return 

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, '')
        
        return res
    
# Driver code
if __name__ == '__main__':

    sol = Solution()
    digits = '23'
    print(sol.letterCombinations(digits))