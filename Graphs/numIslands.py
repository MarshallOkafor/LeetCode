#!/usr/bin/python3
"""
This is the solution to LeetCode problem 200:
Given an m x n 2D binary grid grid which represents a map 
of '1's (land) and '0's (water), return the number of 
islands.

Runtime: mxn => O(n^2)
"""

class Solution:

    def numIslands(self, grid):
        """
        :type grid: list[list[str]]
        :rtype: int
        """

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # BFS Helper function to visit the cells of the grid
        def bfs(r, c):
            
            import collections
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols)
                        and grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
    
# Driver code
if __name__ == '__main__':

    grid1 = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]

    sol = Solution()
    print(sol.numIslands(grid1))

    grid2 = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    print(sol.numIslands(grid2))