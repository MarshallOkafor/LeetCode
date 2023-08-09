#!/usr/bin/python3
"""
This is the solution to LeetCode problem 417:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
"""

class Solution:

    def pacificAtlantic(self, heights):
        """
        :type heights: list[list[int]]
        :rtype: list[list[int]]
        """

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        # Helper function
        def dfs(r, c, visited, prevHeight):
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or prevHeight > heights[r][c]):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append((r, c))

        return result
    
# Driver code
if __name__ == '__main__':

    # Variable, objects and function call
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    sol = Solution()
    print(sol.pacificAtlantic(heights))