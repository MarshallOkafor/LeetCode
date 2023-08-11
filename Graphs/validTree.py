#!/usr/bin/python3
"""
This is the solution to LeetCode problem 178:

Given a graph of n nodes and a list of undirected edges,
write a function to check whether these edges make up a 
valid tree.

Runtime: O(E + V)
"""

class Solution:

    def validTree(self, n: int, edges: list[list[int]]) -> bool:

        adjList = { i: [] for i in range(n) }

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = set()

        # Helper function to traverse the nodes of the graph
        def dfs(i, prev):

            if i in visited:
                return False
            
            visited.add(i)
            for j in adjList[i]:
                # Check if the immediate prev node is
                # returned. This is not a cycle
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
                
            return True
        
        return dfs(0, -1) and n == len(visited)
    
# Driver code
if __name__ == '__main__':

    # Variables, object and function call
    n = 5
    edges = [[0, 1], [0, 2], [3, 4]]

    sol = Solution()
    print(sol.validTree(n, edges))