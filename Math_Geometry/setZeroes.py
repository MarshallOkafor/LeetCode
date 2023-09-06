#!/usr/bin/python3
"""
This is the solution to LeetCode problem 73:

Given an m x n integer matrix matrix, if an element 
is 0, set its entire row and column to 0's.

You must do it in place.

Runtime: O(n x n)
Memory: O(1)
"""

class Solution:

    def setZeroes(self, matrix: list[list[int]]) -> None:

        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0

        return matrix
    
# Driver code
if __name__  == '__main__':

    # Variable, object and function call
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol = Solution()
    print(sol.setZeroes(matrix))