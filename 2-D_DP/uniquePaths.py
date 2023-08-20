#!/usr/bin/python3
"""
This is the solution to LeetCode problem 62:

There is a robot on an m x n grid. Given the 
two integers m and n, return the number of possible 
unique paths that the robot can take to reach the 
bottom-right corner.

Runtime: O(m * n)
"""

class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function call
    m, n = 3, 7
    sol = Solution()
    print(sol.uniquePaths(m, n))