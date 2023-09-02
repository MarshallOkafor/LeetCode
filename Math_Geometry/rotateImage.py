#!/usr/bin/python3
"""
This is the solution to LeetCode problem 48:

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise)

Runtime: O(n x n)
"""

class Solution:

    def rotate(self, matrix: list[list[int]]) -> None:

        l, r = 0, len(matrix)-1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # Copy out top left
                topLeft = matrix[top][l + i]
                # Move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # Move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # Move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # Move top left to top right
                matrix[top + i][r] = topLeft

            l += 1
            r -= 1

        return matrix

# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol = Solution()
    print(sol.rotate(matrix))