#!/usr/bin/python3
"""
This is the solution to LeetCode problem 54:

Given an m x n matrix, return all elements of 
the matrix in spiral order.

Runtime: O(n x n)
"""

class Solution:

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        res = []
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix) 

        while l < r and top < bottom:
            # get every i in the top row
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1
            # get every i in the rightmost column
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and top < bottom):
                break
            # get every i in the bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the leftmost column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))