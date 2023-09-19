#!/usr/bin/python3
"""
This is the solution to LeetCode problem 695:
You are given an m x n binary matrix grid. An island 
is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges 
of the grid are surrounded by water.

The area of an island is the number of cells with a value
 1 in the island.

Return the maximum area of an island in grid. If there is 
no island, return 0.

Runtime: mxn => O(n^2)
"""

class Solution:

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visit = set()

        # dfs helper function
        def dfs(r, c):

            if r < 0 or r == rows or c < 0 or c == cols \
                or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))

            return 1 + dfs(r + 1, c) \
                     + dfs(r - 1, c) \
                     + dfs(r, c + 1) \
                     + dfs(r, c - 1)
        
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))

        return area
    
# Driver code
if __name__ == '__main__':

    # Variable, object and function call
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    sol = Solution()
    print(sol.maxAreaOfIsland(grid))